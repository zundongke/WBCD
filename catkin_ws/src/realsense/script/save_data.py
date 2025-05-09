
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
        self.img_subscriber=rospy.Subscriber('realsense_img', Image,self.img_callback)
        self.propriception_subscriber=rospy.Subscriber('xarm_msg',propriception, self.pro_callback)
        self.control_subscriber=rospy.Subscriber('action',action,self.control_callback)
        self.episdoe=[]
        self.img=None
        self.state=None
        self.action=None
        self.rate=rospy.Rate(10)
        
    def img_callback(self,msg):
        current_time = rospy.Time.now()
        self.img=msg
    def pro_callback(self,msg):
        current_time = rospy.Time.now()
    def control_callback(self,msg):
        current_time = rospy.Time.now()
        self.action=msg

if __name__ == '__main__':
    listener = Listener()
    rospy.spin()