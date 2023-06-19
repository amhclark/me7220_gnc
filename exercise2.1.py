#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class RobotController:

    def __init__(self):
        rospy.init_node('robot_controller_node', anonymous=True)
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.cmd = Twist()
    
    def move_fwd(self, linear_speed):
        self.cmd.linear.x = linear_speed
        self.cmd_vel_pub()
    
    def stop(self):
        self.cmd.linear.x = 0.0
    
    def cmd_vel_pub(self):
        self.vel_publisher.publish(self.cmd)
    

if __name__ == '__main__':
    robot_control = RobotController()

    try:
        while not rospy.is_shutdown():
            robot_control.move_fwd(0.5)
            rospy.sleep(1)
            robot_control.stop()
            rospy.sleep(1)
    except rospy.ROSInterruptException:
        pass

