#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)          # ''/"" doesnt matter for a string.
    rospy.init_node('vel_publisher', anonymous=True)                       # Initialize the ROS node

    rate = rospy.Rate(10)                       # 10hz
    
    while not rospy.is_shutdown():
        vel_msg = Twist()

        vel_msg.linear.x = float(input("Set your linear velocity:"))
        # speed = vel_msg.linear.x
        vel_msg.angular.z = float(input("Set your angular velocity:"))
        # angular_speed = vel_msg.angular.z

        # Publish the message
    ##### rospy.loginfo("Publishing: \n%s", vel_msg)
        # rospy.loginfo("Publishing linear velocity: %s, angular velocity: %s", speed, angular_speed)
        pub.publish(vel_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
        # print("helloooo")
    except rospy.ROSInterruptException:
        pass
      
