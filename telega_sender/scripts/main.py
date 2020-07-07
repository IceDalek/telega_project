#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
rospy.init_node('joy_to_cmd_vel', anonymous=True)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)


def callback(data):
    vel = Twist()
    vel.linear.x = data.axes[3]
    vel.angular.z = -data.axes[0]
    pub.publish(vel)
    print("published axes from joy")


rospy.Subscriber("joy", Joy, callback) 

   
def listener():
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rate.sleep()
        rospy.spin()

if __name__ == '__main__':
    listener()
