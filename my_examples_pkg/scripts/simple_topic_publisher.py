#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
# count = Int32()
# count.data = 0

twistmessage = Twist()

twistmessage.linear.x = 0
twistmessage.linear.y = 0.5
twistmessage.angular.x = 0.5

while not rospy.is_shutdown(): 
  pub.publish(twistmessage)
  rate.sleep()