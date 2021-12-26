#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist


def move_bb8(request):
    print("move_bb8_in_circle has been called")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(2)
    # count = Int32()
    # count.data = 0

    twistmessage = Twist()

    twistmessage.linear.x = 0.5
    twistmessage.angular.z = 0.3

    pub.publish(twistmessage)
    return EmptyResponse()
    #return MyServiceResponse(len(request.words.split())) 


rospy.init_node('move_bb8_in_circle')
my_service = rospy.Service('/move_bb8_in_circle', Empty, move_bb8) 
rospy.spin()