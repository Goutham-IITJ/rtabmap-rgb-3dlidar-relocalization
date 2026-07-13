#!/bin/bash

source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=waffle

ros2 launch turtlebot3_gazebo robot_state_publisher.launch.py
