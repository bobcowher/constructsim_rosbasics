#! /usr/bin/env python

import rospy
import sys
from std_srvs.srv import Empty

rospy.init_node('move_bb8_client')

rospy.wait_for_service('/move_bb8_in_circle')

service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

result = service()

print(result)