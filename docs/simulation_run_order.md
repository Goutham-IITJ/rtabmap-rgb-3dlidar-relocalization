
Simulation Run Order

This simulation was tested on ROS 2 Humble + Gazebo Classic.

Terminal 1: Launch AWS Small House World

source /opt/ros/humble/setup.bash
cd ~/rtabmap_rgb_3dlidar_ws
bash scripts/launch_aws_world.sh

Terminal 2: Spawn TurtleBot3 with 3D LiDAR

source /opt/ros/humble/setup.bash
cd ~/rtabmap_rgb_3dlidar_ws
bash scripts/spawn_turtlebot3_3dlidar.sh

Terminal 3: Start Robot State Publisher

source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=waffle
cd ~/rtabmap_rgb_3dlidar_ws
bash scripts/start_robot_state_publisher.sh

Terminal 4: Static TF for 3D LiDAR

source /opt/ros/humble/setup.bash
ros2 run tf2_ros static_transform_publisher 0 0 0.22 0 0 0 base_link lidar_3d_link

Terminal 5: Mapping

source /opt/ros/humble/setup.bash
ros2 launch ~/rtabmap_rgb_3dlidar_ws/launch/rgb_3dlidar_mapping.launch.py

Terminal 6: Localization

source /opt/ros/humble/setup.bash
ros2 launch ~/rtabmap_rgb_3dlidar_ws/launch/rgb_3dlidar_localization.launch.py

