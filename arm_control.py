import asyncio
import websockets
import json
import numpy as np
from datetime import datetime
from scipy.spatial.transform import Rotation
from xarm_controller import xArm6Controller  

VR_POS_SCALE = 1000 
ROTATION_SCALE = 1.0 
XARM_IP = "192.168.2.202" 
xarm = xArm6Controller(ip=XARM_IP)
xarm.reset()  

class MessageProcessor:
    previous_pos = None
    previous_rot = None
    @staticmethod
    async def process_pose(data):
        position = data.get("position", [])
        rotation = data.get("rotation", [])
        
        if len(position) == 3 and len(rotation) == 4:
            print(f"[{datetime.now()}] Pose - Pos: {position}, Rot: {rotation}")

            converted_pos, euler = convert_vr_to_robot_frame(position, rotation)
            delta_pos_mm = converted_pos * VR_POS_SCALE  
            delta_rot_deg = euler * ROTATION_SCALE  
            
            if MessageProcessor.previous_pos is not None and MessageProcessor.previous_rot is not None:
                delta_pos = delta_pos_mm - MessageProcessor.previous_pos
                R1 = Rotation.from_euler("xyz", euler, degrees=True)
                R2 = Rotation.from_euler("xyz", MessageProcessor.previous_rot, degrees=True)
                delta_rot = R2.inv()*R1
                delta_rot=delta_rot.as_euler('xyz',degrees=True)
                delta_pose = np.concatenate([delta_pos, delta_rot])
                xarm.set_delta_eef_pose(delta_pose)
                print(f"[{datetime.now()}] Moving arm to: {delta_pos}, Rotation: {delta_rot}")
            else:
                print(f"[{datetime.now()}] First pose received. Skipping movement.")

            MessageProcessor.previous_pos = delta_pos_mm
            MessageProcessor.previous_rot = delta_rot_deg

    @staticmethod
    async def process_gripper(data):
        action = data.get("action", "")
        if action in ("grab", "release"):
            print(f"[{datetime.now()}] Gripper - Action: {action}")
            if action == "grab":
                xarm.set_gripper_position(300)  
            elif action == "release":
                xarm.set_gripper_position(800)  

def convert_vr_to_robot_frame(pos, delta_rot):
    converted_pos = np.array([
        -pos[2],   # Unity Z -> arm X
        pos[0],  # Unity X -> arm（-X）
        pos[1]    # Unity Y -> arm Z
    ])

    r = Rotation.from_quat(np.array([delta_rot[0],delta_rot[3],delta_rot[1],delta_rot[2]]))
    rot_euler = r.as_euler('xyz',degrees=True)
    rot_euler=np.array([-rot_euler[0],rot_euler[2],-rot_euler[1]])
    # convert_matrix = np.array([
    #     [0, 0, -1],  
    #     [0, 1, 0], 
    #     [1, 0, 0]
    # ])
    # rot_matrix = convert_matrix @ rot_matrix @ convert_matrix.T

    r_converted = Rotation.from_euler('xyz',rot_euler,degrees=True)
    euler = r_converted.as_euler('xyz', degrees=True)

    return converted_pos, euler

async def handler(websocket, path):
    print(f"Client connected from {websocket.remote_address}")
    
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                msg_type = data.get("messageType")
                
                if not msg_type:
                    print(f"Invalid message: {message}")
                    continue
                
                if msg_type == "pose":
                    await MessageProcessor.process_pose(data)
                elif msg_type == "gripper":
                    await MessageProcessor.process_gripper(data)
                else:
                    print(f"Unknown message type: {msg_type}")
                    
            except json.JSONDecodeError:
                print(f"Non-JSON message: {message}")
            except Exception as e:
                print(f"Processing error: {str(e)}")
                
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Handler error: {str(e)}")

async def main():
    server = await websockets.serve(
        handler,
        "0.0.0.0",  
        8765,
        ping_interval=20,
        ping_timeout=60,
        close_timeout=1
    )
    
    print("WebSocket server started at ws://0.0.0.0:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())


# import asyncio
# import websockets
# import json
# from datetime import datetime

# class MessageProcessor:
#     @staticmethod
#     async def process_pose(data):
#         position = data.get("position", [])
#         rotation = data.get("rotation", [])
#         if len(position) == 3 and len(rotation) == 4:
#             print(f"[{datetime.now()}] Pose - Pos: {position}, Rot: {rotation}")

#     @staticmethod
#     async def process_gripper(data):
#         action = data.get("action", "")
#         if action in ("grab", "release"):
#             print(f"[{datetime.now()}] Gripper - Action: {action}")

# async def handler(websocket, path):
#     print(f"Client connected from {websocket.remote_address}")
    
#     try:
#         async for message in websocket:
#             try:
#                 data = json.loads(message)
#                 msg_type = data.get("messageType")
                
#                 if not msg_type:
#                     print(f"Invalid message: {message}")
#                     continue
                
#                 if msg_type == "pose":
#                     await MessageProcessor.process_pose(data)
#                 elif msg_type == "gripper":
#                     await MessageProcessor.process_gripper(data)
#                 else:
#                     print(f"Unknown message type: {msg_type}")
                    
#             except json.JSONDecodeError:
#                 print(f"Non-JSON message: {message}")
#             except Exception as e:
#                 print(f"Processing error: {str(e)}")
                
#     except websockets.exceptions.ConnectionClosed:
#         print("Client disconnected")
#     except Exception as e:
#         print(f"Handler error: {str(e)}")

# async def main():
#     server = await websockets.serve(
#         handler,
#         "0.0.0.0",
#         8765,
#         ping_interval=20,
#         ping_timeout=60,
#         close_timeout=1
#     )
    
#     print("WebSocket server started at ws://0.0.0.0:8765")
#     await server.wait_closed()

# if __name__ == "__main__":
#     asyncio.run(main())