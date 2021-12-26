#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

rospy.init_node('note_and_avoid')


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)


def callback(msg):
    
    print(msg.ranges[360], " : ", type(msg.ranges[360]))

    
    
    if msg.ranges[360] == float('inf'):
        speed = Twist()
        speed.linear.x = 0.2
        speed.angular.z = 0.3        
    elif msg.ranges[360] > 1:
        speed = Twist()
        speed.linear.x = 0.5
        speed.angular.z = 0.0
    elif msg.ranges[360] < 1: 
        speed = Twist()
        speed.linear.x = 0.0
        speed.angular.z = 0.5
     
        

    pub.publish(speed)


lasersub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()
