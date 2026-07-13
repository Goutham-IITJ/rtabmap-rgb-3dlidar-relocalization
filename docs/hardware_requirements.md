# Hardware Requirements for RGB + 3D LiDAR RTAB-Map

For real robot testing, the required ROS 2 topics are:

## Required Topics

- RGB image topic: `sensor_msgs/msg/Image`
- CameraInfo topic: `sensor_msgs/msg/CameraInfo`
- 3D LiDAR cloud topic: `sensor_msgs/msg/PointCloud2`
- Odometry topic: `nav_msgs/msg/Odometry`
- `/tf`
- `/tf_static`

## PointCloud2 Requirement

The 3D LiDAR cloud should be published as:

```text
sensor_msgs/msg/PointCloud2

Minimum required fields:

x
y
z

Optional but useful fields:

intensity
ring
time

The cloud should have a valid:

header.stamp
header.frame_id

The header.frame_id should correspond to the LiDAR frame.

Required TF Chain

RTAB-Map should be able to transform between:

odom -> base_link / base_footprint
base_link / base_footprint -> camera frame
base_link / base_footprint -> LiDAR frame
Real Robot Changes

For real robot use:

use_sim_time = false

The topic remaps in the launch file should be changed from simulation topics to the real robot topics.
