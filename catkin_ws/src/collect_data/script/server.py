import asyncio
import json
import logging
from typing import Dict, Optional
import rospy
from collect_data.msg import PosCmd
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class VRServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 5000):
        rospy.init_node('vr_server')
        self.host = host
        self.port = port
        self.clients: Dict[asyncio.StreamWriter, Dict] = {}
        self.heartbeat_interval = 5
        self.server: Optional[asyncio.Server] = None
        self.vr_right=rospy.Publisher('/ARX_VR_R', PosCmd,queue_size=10)
        self.vr_left=rospy.Publisher('/ARX_VR_L', PosCmd,queue_size=10)
        self.rate=rospy.Rate(30)
    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """处理单个客户端连接"""
        client_addr = writer.get_extra_info('peername')
        self.clients[writer] = {"addr": client_addr, "last_heartbeat": time.time()}
        logging.info(f"New client connected: {client_addr}")
        try:
            while True:
                data = await reader.read(4096)
                if not data:
                    break
                try:
                    message = json.loads(data.decode())
                        # 处理其他业务消息（示例：打印VR数据）
                    logging.info(f"VR Data from {client_addr}: {message}")
                    right_msg=message['msgvrright']
                    left_msg=message['msgvrleft']
                    self.vr_right.publish(right_msg)
                    self.vr_left.publish(left_msg)
                    self.rate.sleep()
                except json.JSONDecodeError:
                    logging.warning(f"Invalid JSON from {client_addr}")
                    await self.send_error(writer, "Invalid JSON format")

        except ConnectionError:
            logging.warning(f"Client {client_addr} disconnected abruptly")
        finally:
            del self.clients[writer]
            writer.close()
            await writer.wait_closed()
            logging.info(f"Client {client_addr} disconnected")

    async def start(self):
        """启动服务器"""
        self.server = await asyncio.start_server(
            self.handle_client,
            self.host,
            self.port
        )
        logging.info(f"Server started on {self.host}:{self.port}")

        # 启动心跳检测任务
        # asyncio.create_task(self.check_heartbeats())

        async with self.server:
            await self.server.serve_forever()

    async def shutdown(self):
        """关闭服务器"""
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            logging.info("Server stopped")

async def main():
    server = VRServer(host="0.0.0.0", port=5000)
    try:
        await server.start()
    except KeyboardInterrupt:
        logging.info("Shutting down server...")
    finally:
        await server.shutdown()

if __name__ == "__main__":
    import time
    asyncio.run(main())