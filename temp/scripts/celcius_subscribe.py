#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32, Float32

def callback(data):
    rospy.loginfo('Celcius is ', data.data)


def listener():
    rospy.init_node('celcius_subscribe', anonymous=True)
    rospy.Subscriber('celcius', Float32,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()