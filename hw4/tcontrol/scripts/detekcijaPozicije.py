#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def detekcija(data):
    if(data.x<5.5 and data.x>4.5 and data.y<5.5 and data.y>4.5):
        rospy.loginfo("Turtle in the middle!")

if __name__ == '__main__':
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("pose", Pose, detekcija)
    rospy.spin()

