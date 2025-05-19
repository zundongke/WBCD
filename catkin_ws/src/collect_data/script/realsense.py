#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pyrealsense2 as rs

class RealSenseNode:
    def __init__(self,device_ids):
        rospy.init_node('realsense_processor', anonymous=True)
        self.pipelines = []
        self.configs = []
        self.bridge = CvBridge()
        for i, device_id in enumerate(device_ids):
            self.pipeline = rs.pipeline()
            self.config = rs.config()
            self.config.enable_device(device_id.get_info(rs.camera_info.serial_number))
            self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
            self.pipeline.start(self.config)
            self.pipelines.append(self.pipeline)
            self.configs.append(self.config)
            topic_name = f'realsense_img_{i}'
            setattr(self, f'img_pub_{i}', rospy.Publisher(topic_name, Image, queue_size=10))
        self.rate=rospy.Rate(20)
        rospy.loginfo("RealSense processing node initialized")
    def run(self):
        while not rospy.is_shutdown():
            for i, pipeline in enumerate(self.pipelines):
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                if not color_frame:
                    return None

                color_image = np.array(color_frame.get_data())
                ros_image=self.bridge.cv2_to_imgmsg(color_image)
                publisher = getattr(self, f'img_pub_{i}')
                publisher.publish(ros_image)
                rospy.loginfo('publishing ros_img')
            self.rate.sleep()

if __name__ == '__main__':
    ctx = rs.context()
    devices = ctx.query_devices()
    node = RealSenseNode(devices)
    node.run()
 