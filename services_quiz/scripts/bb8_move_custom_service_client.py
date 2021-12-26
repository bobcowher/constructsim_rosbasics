#! /usr/bin/env python

import rospy
import sys
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

rospy.init_node('move_bb8_client')

rospy.wait_for_service('/move_bb8_in_square_custom')

service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

result = service(side=5, repetitions=2)
result = service(side=10, repetitions=1)

print(result)