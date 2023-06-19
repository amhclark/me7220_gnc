#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
rate = rospy.Rate(2)
vel_message = Twist()

vel_message.linear.x = 0.5

while not rospy.is_shutdown():
    pub.publish(vel_message)

rate.sleep()
