#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    print msg.ranges[360]
    move.angular.z = 0
    move.linear.x = -0.2
    for i in range(310,420):
        if msg.ranges[i] < 0.6:
            move.linear.x = 0
            move.angular.z = 2.2
           
        
        pub.publish(move)
            
            
    
        
        
    
rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/hokuyo_laser', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 20)
move  = Twist()
rospy.spin()
