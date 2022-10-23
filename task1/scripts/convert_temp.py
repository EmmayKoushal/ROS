#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32, Float32

def callback(data):
    c = (data.data - 32) * (5/9)

    pub = rospy.Publisher('celcius', Float32, queue_size=10)
    rospy.loginfo('Celcius: ', c)
    pub.publish(c)


def listener():
    rospy.init_node('convert_temp', anonymous=True)
    rospy.Subscriber('farenhite', Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
