
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyrealsense2 as rs
from xarm_cotroller import xArm6Controller
from realsense.msg import action
from realsense.msg import propriception
class save_data():
    def __init__(self):
        rospy.init_node('saving_node', anonymous=True)
        self.bridge = CvBridge()
        self.episode=[]
        self.img=None
        self.state=None
        self.action=None
        self.rate=rospy.Rate(10)
        self.temp_dict={}
        self.img_subscriber=rospy.Subscriber('realsense_img', Image,self.img_callback)
        self.propriception_subscriber=rospy.Subscriber('xarm_msg',propriception, self.pro_callback)
        self.control_subscriber=rospy.Subscriber('action',action,self.control_callback)
    def img_callback(self,msg):
        self.img=self.bridge.imgmsg_to_cv2(msg)
        self.temp_dict['img']=self.img
    def pro_callback(self,msg):
        self.temp_dict['state/qpos']=msg.qpos
        self.temp_dict['state/qvel']=msg.qvel
        self.temp_dict['state/qeff']=msg.qeff
    def control_callback(self,msg):
        self.action=msg
        self.temp_dict['action']=msg
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