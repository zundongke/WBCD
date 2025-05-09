import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyrealsense2 as rs
from xarm_cotroller import xArm6Controller
from realsense.msg import action
class xarm_control:
    def __init__(self,ip):
        rospy.init_node('control_node', anonymous=True)
        self.controller=xArm6Controller(ip)
        self.pub=rospy.Publisher('action', action,queue_size=10)
        self.rate=rospy.Rate(20)
    def run(self):
        while not rospy.is_shutdown():
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                return None

            color_image = np.array(color_frame.get_data())
            ros_image=self.bridge.cv2_to_imgmsg(color_image)
            self.img_pub.publish(ros_image)
            rospy.loginfo('controlling xarm')
            self.rate.sleep()
    