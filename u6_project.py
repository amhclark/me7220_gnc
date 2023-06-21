#!/usr/bin/env python

from robot_control_class_2 import RobotControl

class WallFollower():

    def __init__(self):
        self.robot = RobotControl()
        self.wall_distance_threshold = 1.0  # Distance threshold for detecting a wall
        self.angular_speed = 0.5  # Angular speed for turning
        self.linear_speed = 0.2  # Linear speed for forward motion

    def stop_robot(self):
        self.robot.stop_robot()

    def move_forward(self):
        self.robot.move_straight()

    def turn(self, clockwise):
        if clockwise:
            self.robot.turn("clockwise", self.angular_speed, 1)  # Adjust the turn duration as needed
        else:
            self.robot.turn("counterclockwise", self.angular_speed, 1)  # Adjust the turn duration as needed

    def follow_wall(self):
        while True:
            if self.robot.get_front_laser() < self.wall_distance_threshold:
                self.stop_robot()
                self.turn(clockwise=True)
            else:
                self.move_forward()

if __name__ == '__main__':
    wallfollower_object = WallFollower()
    try:
        wallfollower_object.follow_wall()
    except rospy.ROSInterruptException:
        pass
