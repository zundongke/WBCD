
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyrealsense2 as rs
from xarm_cotroller import xArm6Controller
from collect_data.msg import PosCmd
from collect_data.msg import JointInformation
class save_data():
    def __init__(self):
        rospy.init_node('saving_node', anonymous=True)
        self.bridge = CvBridge()
        self.episode=[]
        self.img=None
        self.state=None
        self.action=None
        self.rate=rospy.Rate(30)
        self.temp_dict={}
        self.img_subscriber=rospy.Subscriber('realsense_img', Image,self.img_callback)
        self.propriception_subscriber=rospy.Subscriber('xarm_msg',JointInformation, self.pro_callback)
        self.control_subscriber=rospy.Subscriber('action',PosCmd,self.control_callback)
    def img_callback(self,msg):
        self.img=self.bridge.imgmsg_to_cv2(msg)
        self.temp_dict['img']=self.img
    def pro_callback(self,msg):
        self.temp_dict['state/pos']=msg.joint_pos
        self.temp_dict['state/vel']=msg.joint_vel
        self.temp_dict['state/cur']=msg.joint_cur
    def control_callback(self,msg):
        action=dict()
        action['x']=msg.x
        action['y']=msg.y
        action['z']=msg.z
        action['roll']=msg.roll
        action['pitch']=msg.pitch
        action['yaw']=msg.yaw
        action['gripper']=msg.gripper
        self.temp_dict['action']=action
    def run(self):
        while not rospy.is_shutdown():
            # 将当前时间步的数据添加到 episode 列表中
            self.episode.append(self.temp_dict.copy())
            # 清空临时字典，为下一个时间步做准备
            self.temp_dict.clear()
            # 等待下一个时间步
            self.rate.sleep()
if __name__ == '__main__':
    node  = save_data()
    node.run()
    # rospy.spin()