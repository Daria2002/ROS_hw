#!/usr/bin/env python
import numpy
import rospy
from geometry_msgs.msg import Twist

def commander(vel, ang_vel, msgPublisher):
    msg=Twist()
    msg.linear.x = vel
    msg.angular.z = ang_vel
    msgPublisher.publish(msg)
    rospy.sleep(1)

if __name__ == '__main__':
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('publisher')
    v = 2
    try:
        while not rospy.is_shutdown():
            w=numpy.random.random_integers(-5, 5)
            commander(v, w, pub)
    except rospy.ROSInterruptException:
        pass
