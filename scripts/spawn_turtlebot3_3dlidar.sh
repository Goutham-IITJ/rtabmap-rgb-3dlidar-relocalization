#!/bin/bash
set -e

source /opt/ros/humble/setup.bash

X=${1:-0.0}
Y=${2:-0.0}
Z=${3:-0.01}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

MODEL="$REPO_DIR/models/turtlebot3_waffle_3dlidar/model.sdf"

if [ ! -f "$MODEL" ]; then
  echo "Local model not found:"
  echo "$MODEL"
  echo ""
  echo "Fallback expected path:"
  echo "$HOME/.gazebo/models/turtlebot3_waffle_3dlidar/model.sdf"
  MODEL="$HOME/.gazebo/models/turtlebot3_waffle_3dlidar/model.sdf"
fi

if [ ! -f "$MODEL" ]; then
  echo "3D LiDAR TurtleBot3 model not found."
  exit 1
fi

ros2 run gazebo_ros spawn_entity.py \
  -entity turtlebot3_waffle_3dlidar \
  -file "$MODEL" \
  -x "$X" \
  -y "$Y" \
  -z "$Z"
