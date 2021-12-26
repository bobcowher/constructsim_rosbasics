#! /usr/bin/env python

import rospy
import sys
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

rospy.init_node('move_bb8_client')

rospy.wait_for_service('/move_bb8_in_circle_custom')

service = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

result = service(duration=12)

print(result)