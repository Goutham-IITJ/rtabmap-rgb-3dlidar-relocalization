# Offline Phase Summary - RGB + 3D LiDAR RTAB-Map

## Objective
Develop and validate a real-robot global relocalization / kidnapped robot recovery pipeline using RGB camera, 3D LiDAR, odometry, and TF.

## Final Pipeline
Inputs:
- /camera/image_raw
- /camera/camera_info
- /livox/lidar
- /odom
- /tf and /tf_static

RTAB-Map outputs:
- map
- localization_pose
- map -> odom correction
- RTAB-Map database graph

## Main Result
The RGB + 3D LiDAR RTAB-Map pipeline was validated in simulation and on the real robot.

Real robot arena map:
- DB size: 177 MB
- Nodes: 671
- Global loop closure links: 136
- Proximity links: 602
- Integrity: OK

## Kidnap Recovery Validation
Recovery was validated using:
- localization_pose
- map -> odom TF
- odom -> base_footprint TF
- loop_closure_id / proximity_detection_id
- videos and screenshots

Key observation:
During manual relocation, odom -> base_footprint translation stayed locally bounded, while map -> odom changed after RTAB-Map relocalization. This indicates recovery through global relocalization, not odometry teleportation.
