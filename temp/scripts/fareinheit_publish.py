#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import random

def sender():
    pub = rospy.Publisher('farenhite', Int32, queue_size=10)
    rospy.init_node('farenhite_publish', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        temp = random.randint(0, 100)
        #rospy.loginfo('The Farenhite published is: ', temp)
        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass