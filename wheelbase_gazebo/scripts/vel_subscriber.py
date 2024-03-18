#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import Twist

_DIST_BETWEEN_WHEELS = 312

def callback(data):
    # rospy.loginfo("Received linear velocity: %s", data.linear.x)
    # rospy.loginfo("Received angular velocity: %s", data.angular.z)
    
    v = data.linear.x			# as float data is published to the topic, we need not to concatenate again.
    w = data.angular.z
    
    right_vel =  v + (_DIST_BETWEEN_WHEELS * w)/4
    left_vel =  v - (_DIST_BETWEEN_WHEELS * w)/4

    right_rpm = right_vel * 60 / (_DIST_BETWEEN_WHEELS * 2 * 3.14)      # revolutions per minute
    left_rpm = left_vel * 60 / (_DIST_BETWEEN_WHEELS * 2 * 3.14)

    rospy.loginfo("Right rpm should be : \n%s", right_rpm)
    rospy.loginfo("Left rpm should be : \n%s", left_rpm)

def listener():
    rospy.init_node('vel_subscriber', anonymous = True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    # print("heard it! ")
  
