import asyncio
import socket
import struct
import serial
import json
import os
import time
from typing import Optional

SERVER_IP = "10.20.239.20"
SERVER_PORT = 5000
FRAME_SIZE = 94
SERIAL_READ_SIZE = 200
HEARTBEAT_INTERVAL = 5
RECONNECT_DELAY = 0.5
MAX_RECONNECT_ATTEMPTS = 10

class VRClient:
    def __init__(self):
        self.socket_client: Optional[socket.socket] = None
        self.ser: Optional[serial.Serial] = None
        self.running = True
        self.reconnect_attempts = 0

    def find_serial_device(self) -> Optional[str]:
        dev_dir = "/dev/serial/by-id/"
        keyword = "USB_Single_Serial"
        if not os.path.exists(dev_dir):
            return None
        for filename in os.listdir(dev_dir):
            if keyword in filename:
                return os.path.realpath(os.path.join(dev_dir, filename))
        return None

    def parse_frame(self, data: bytes) -> Optional[dict]:
        if len(data) < FRAME_SIZE:
            return None
        try:
            unpacked = struct.unpack('<2B B 3i 3i i B 3i 3i i B 3i 2i i 2B i 3B', data[:FRAME_SIZE])
            (
                h1, h2, l_head, lx, ly, lz, lr, lp, lyaw, lgrip,
                r_head, rx, ry, rz, rr, rp, ryaw, rgrip,
                c_head, chx, chy, chz, hpit, hyaw, height, m1, m2,
                t, e1, e2, e3
            ) = unpacked
            if h1 != 0x55 or h2 != 0xAA or e1 != 0x0A or e2 != 0x0D or e3 != 0xEE:
                return None
            return {
                "msgvrright": {
                    "x": rx/1e5, "y": ry/1e5, "z": rz/1e5,
                    "roll": rr/1e5, "pitch": rp/1e5, "yaw": ryaw/1e5,
                    "gripper": rgrip/1e5
                },
                "msgvrleft": {
                    "x": lx/1e5, "y": ly/1e5, "z": lz/1e5,
                    "roll": lr/1e5, "pitch": lp/1e5, "yaw": lyaw/1e5,
                    "gripper": lgrip/1e5,
                    "chx": chx/1e5, "chy": chy/1e5, "chz": chz/1e5,
                    "height": height/1e5,
                    "head_pit": hpit/1e5, "head_yaw": hyaw/1e5,
                    "mode1": m1, "mode2": m2
                }
            }
        except Exception as e:
            print(f"[解析错误] {e}")
            return None

    async def connect_socket(self) -> bool:
        try:
            if self.socket_client:
                self.socket_client.close()
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_client.setblocking(False)
            await asyncio.get_event_loop().sock_connect(self.socket_client, (SERVER_IP, SERVER_PORT))
            print(f"[Socket] 已连接到 {SERVER_IP}:{SERVER_PORT}")
            return True
        except Exception as e:
            print(f"[连接失败] {e}")
            return False

    async def connect_serial(self) -> bool:
        port = self.find_serial_device()
        if not port:
            print("[串口] 未找到设备")
            return False
        try:
            self.ser = serial.Serial(port, baudrate=921600, timeout=0.1)
            print(f"[串口] 已连接 {port}")
            return True
        except Exception as e:
            print(f"[串口打开失败] {e}")
            return False

    async def send_heartbeat(self):
        while self.running:
            try:
                await asyncio.get_event_loop().sock_sendall(
                    self.socket_client,
                    json.dumps({"heartbeat": True}).encode()
                )
                print("[心跳] 已发送")
                await asyncio.sleep(HEARTBEAT_INTERVAL)
            except Exception as e:
                print(f"[心跳失败] {e}")
                break

    async def process_serial_data(self):
        buffer = bytearray()
        while self.running:
            buffer += self.ser.read(SERIAL_READ_SIZE)
            while len(buffer) >= FRAME_SIZE:
                if buffer[0] == 0x55 and buffer[1] == 0xAA:
                    frame = buffer[:FRAME_SIZE]
                    parsed = self.parse_frame(frame)
                    if parsed:
                        message = json.dumps(parsed).encode()
                        try:
                            await asyncio.get_event_loop().sock_sendall(self.socket_client, message)
                            print(f"[发送] {message}")
                        except Exception as e:
                            print(f"[发送失败] {e}")
                            return
                    buffer = buffer[FRAME_SIZE:]
                else:
                    buffer.pop(0)
            await asyncio.sleep(0.001)

    async def run(self):
        while self.running:
            if not await self.connect_socket():
                self.reconnect_attempts += 1
                if self.reconnect_attempts >= MAX_RECONNECT_ATTEMPTS:
                    print("[错误] 重连失败过多，退出")
                    break
                await asyncio.sleep(RECONNECT_DELAY)
                continue

            if not await self.connect_serial():
                await asyncio.sleep(RECONNECT_DELAY)
                continue

            heartbeat_task = asyncio.create_task(self.send_heartbeat())

            try:
                await self.process_serial_data()
            finally:
                heartbeat_task.cancel()
                if self.ser:
                    self.ser.close()
                if self.socket_client:
                    self.socket_client.close()
                print("[断开连接] 即将重连...")
                await asyncio.sleep(RECONNECT_DELAY)

    async def shutdown(self):
        self.running = False
        if self.ser:
            self.ser.close()
        if self.socket_client:
            self.socket_client.close()

async def main():
    client = VRClient()
    try:
        await client.run()
    except KeyboardInterrupt:
        print("用户中断")
    finally:
        await client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
