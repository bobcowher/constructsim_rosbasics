#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
import time


def callback(msg):
    print (msg)
    time.sleep(5)


rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('/counter', Int32, callback)

sub = rospy.Subscriber('/odom',Odometry, callback)
rospy.spin()