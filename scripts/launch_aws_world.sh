#!/bin/bash

source /opt/ros/humble/setup.bash

AWS_WORLD_DIR=/home/goutham/ros2_ws/src/aws-robomaker-small-house-world

if [ ! -d "$AWS_WORLD_DIR" ]; then
  echo "AWS world directory not found:"
  echo "$AWS_WORLD_DIR"
  echo "Clone aws-robomaker-small-house-world into ~/ros2_ws/src first."
  exit 1
fi

export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$AWS_WORLD_DIR/models

ros2 launch gazebo_ros gazebo.launch.py \
  world:=$AWS_WORLD_DIR/worlds/small_house.world \
  verbose:=true
