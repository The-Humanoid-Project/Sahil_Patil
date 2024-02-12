#!/usr/bin/env python

import rospy
import sys
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo("Received linear velocity: %s", data.linear.x)
    rospy.loginfo("Received angular velocity: %s", data.angular.z)

def listener():
    rospy.init_node('pysub1', anonymous = True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    # print("heard it! ")