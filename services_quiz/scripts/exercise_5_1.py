#! /usr/bin/env python

import rospy
# from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest
from iri_wam_reproduce_trajectory.srv import ExecTraj

import sys

import rospkg
rospack = rospkg.RosPack()

rospy.init_node('service_client')

rospy.wait_for_service('/execute_trajectory')

traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

traj_by_name_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)

result = traj_by_name_service(traj)

print(result)