#!/bin/bash
set -e

echo "This script sets up simulation dependencies for ROS 2 Humble + Gazebo Classic."

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

if [ ! -d "aws-robomaker-small-house-world" ]; then
  git clone https://github.com/aws-robotics/aws-robomaker-small-house-world.git
else
  echo "AWS small house world already exists."
fi

echo ""
echo "Done."
echo "Expected world path:"
echo "$HOME/ros2_ws/src/aws-robomaker-small-house-world/worlds/small_house.world"
