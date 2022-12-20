#!/usr/bin/env python3

import rospy
import time
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2

def publish_video(video_publisher):
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        raw_image = bridge.cv2_to_imgmsg(frame, 'bgr8')
        video_publisher.publish(raw_image)


if __name__ == '__main__':
    rospy.init_node('video_publisher_node', anonymous=True)
    video_publisher = rospy.Publisher('usb_cam/image_raw', Image, queue_size=10)
    publish_video(video_publisher)