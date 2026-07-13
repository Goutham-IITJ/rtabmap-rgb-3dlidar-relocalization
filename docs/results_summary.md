
Results Summary
RGB + 2D LiDAR

The RGB + 2D LiDAR pipeline was verified to be correctly connected, but loop closures were not reliable enough for kidnapped robot recovery.

Main conclusion:

RGB + 2D LiDAR can generate a map, but was weak for reliable global relocalization in this setup.
RGB + 3D LiDAR

The RGB + 3D LiDAR pipeline was tested with:

RGB image
CameraInfo
3D LiDAR PointCloud2
Odometry
TF

The mapping database contained:

1207 nodes
189 global closure links
2224 local-space / proximity links

After tuning monocular visual verification parameters, localization produced multiple loop closures and corrected scan-map misalignment.

Kidnapped Robot Test

The robot was manually moved in Gazebo while odometry did not jump, confirming a valid kidnapped robot test.

Recovery was observed through:

non-zero proximity detections
non-zero loop closures
map -> odom correction
scan-map realignment

Main conclusion:

RGB + 3D LiDAR RTAB-Map localization successfully recovered from a kidnapped pose in simulation.

