#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse, BB8CustomServiceMessage, BB8CustomServiceMessageResponse
import time
from geometry_msgs.msg import Twist


def circlemove(duration):
    count = 0

    while count <= duration:
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rate = rospy.Rate(2)
        # count = Int32()
        # count.data = 0

        twistmessage = Twist()

        twistmessage.linear.x = 0.5
        twistmessage.angular.z = 0.3

        pub.publish(twistmessage)

        print("Running {0} out of {1} seconds".format(count, duration))

        count += 1
        time.sleep(1)

def circlestop():
        print("Stopping BB8...")
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rate = rospy.Rate(2)
        # count = Int32()
        # count.data = 0

        twistmessage = Twist()

        twistmessage.linear.x = 0.0
        twistmessage.angular.z = 0.0

        pub.publish(twistmessage)

def rightturn():
    print("Turning right")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(2)

    twistmessage = Twist()

    #Stop for a turn. 
    twistmessage.linear.x = 0.0
    twistmessage.angular.z = 0.0
    pub.publish(twistmessage)
    
    #Turn. 
    twistmessage.linear.x = 0.0
    twistmessage.angular.z = 0.5
    pub.publish(twistmessage)
    time.sleep(3)

    #Stop turning
    twistmessage.linear.x = 0.0
    twistmessage.angular.z = 0.0
    pub.publish(twistmessage)

def straight_line(distance):
    print("Turning right")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(2)
    twistmessage = Twist()

    for x in range(int(distance)):
        twistmessage.linear.x = 0.5
        twistmessage.angular.z = 0.0
        pub.publish(twistmessage)
        time.sleep(1)

    twistmessage.linear.x = 0.0
    twistmessage.angular.z = 0.0
    pub.publish(twistmessage)

def square(request):
    for x in range(int(request.repetitions) * 4):
        straight_line(request.side)
        rightturn()
    
    my_response = BB8CustomServiceMessageResponse()

    #Generate a response. 
    if request.side > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse
    


def my_callback(request):
    
    print("Request Data==> duration="+str(request.duration))
    my_response = MyCustomServiceMessageResponse()
    
    #Move the robot. 
    circlemove(request.duration)
    circlestop()

    #Generate a response. 
    if request.duration > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    return  my_response # the service Response class, in this case MyCustomServiceMessageResponse

rospy.init_node('service_client') 
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback

bb8_square_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , square) # create the Service called my_service with the defined callback




rospy.spin() # maintain the service open.