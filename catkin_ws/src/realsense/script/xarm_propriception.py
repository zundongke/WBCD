import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyrealsense2 as rs
from xarm_cotroller import xArm6Controller
from realsense.msg import propriception
class xarm_node():
    def __init__(self,ip) -> None:
        rospy.init_node('propriception_pub', anonymous=True)
        self.xarm_controller=xArm6Controller(ip)
        self.pub=rospy.Publisher('xarm_msg',propriception,queue_size=10)
        self.rate=rospy.Rate(20)
    def run(self):
        while not rospy.is_shutdown():
            data=self.xarm_controller.get_proprio_state()
            msg=propriception()
            msg.qpos=data['qpos']
            msg.qvel=data['qvel']
            msg.qeff=data['qeff']
            self.pub.publish(msg)
            rospy.loginfo('publishing ros_img')
            self.rate.sleep()

if __name__ == '__main__':
    node = xarm_node()
    node.run()