# RTAB-Map RGB + 3D LiDAR Global Relocalization
### Kidnapped Robot Recovery using Monocular RGB + 3D LiDAR + RTAB-Map

<p align="center">
  <img src="docs/Screenshot from 2026-07-13 13-22-46.png" width="750"/>
</p>

> Internship Project – ugo Inc., Tokyo, Japan  
> Goutham A S

---

# Overview

This repository contains the complete workspace used to investigate **global relocalization (Kidnapped Robot Recovery)** using **RTAB-Map** with a **Monocular RGB Camera and 3D LiDAR**.

Unlike conventional localization systems that assume a continuous pose estimate, this project focuses on recovering the robot after it has been **physically displaced to an unknown location**, where odometry alone is no longer valid.

The project contains both

- Simulation pipeline (ROS2 Humble + Gazebo Classic)
- Real robot launch configuration
- Mapping pipeline
- Localization pipeline
- Evaluation utilities
- Experimental documentation

---

# Motivation

Global relocalization is a critical capability for autonomous mobile robots operating in warehouses, hospitals, offices and service environments.

A robot may become "kidnapped" when

- Human intervention moves the robot
- Wheel odometry becomes invalid
- Localization completely fails
- Robot is restarted in an unknown pose

Instead of relying purely on odometry, the robot should recover by recognizing previously visited locations and correcting its global pose.

---

# Project Goal

Develop and evaluate an RTAB-Map based localization framework capable of

- Building maps using RGB + 3D LiDAR
- Localizing against previously built maps
- Recovering after kidnapped robot scenarios
- Quantifying recovery behaviour through repeated experiments

---

# Repository Structure

```
rtabmap_rgb_3dlidar_ws
│
├── config/
│   └── rtabmap_rgb_3dlidar_params.yaml
│
├── launch/
│   ├── rgb_3dlidar_mapping.launch.py
│   ├── rgb_3dlidar_localization.launch.py
│   ├── rgb_3dlidar_localization_lite.launch.py
│   ├── rgb_3dlidar_hardware_mapping.launch.py
│   └── rgb_3dlidar_hardware_localization.launch.py
│
├── models/
│   └── turtlebot3_waffle_3dlidar/
│
├── scripts/
│   ├── launch_aws_world.sh
│   ├── spawn_turtlebot3_3dlidar.sh
│   ├── start_robot_state_publisher.sh
│   ├── setup_sim_dependencies.sh
│   └── analyze_rtabmap_db.sh
│
├── docs/
│   ├── hardware_requirements.md
│   ├── simulation_run_order.md
│   ├── offline_phase_summary.md
│   └── results_summary.md
│
└── README.md
```

---

# System Pipeline

```
                 RGB Camera
                      │
                      │
                CameraInfo
                      │
                      ▼

3D LiDAR ─────► PointCloud2

                      │
                      │

Wheel Odometry + TF
          │
          ▼

      RTAB-Map
          │
          │
 ┌────────┴────────┐
 │                 │
 ▼                 ▼

 Mapping      Localization

 │                 │
 ▼                 ▼

Database       Loop Closure

                    │
                    ▼

            map → odom correction

                    │

                    ▼

          Global Pose Recovery
```

---

# Software Requirements

- Ubuntu 22.04
- ROS2 Humble
- Gazebo Classic
- RTAB-Map ROS
- TurtleBot3 packages
- PCL
- OpenCV

---

# Sensors Used

Simulation

- Monocular RGB Camera
- Velodyne-style 3D LiDAR
- Wheel Odometry
- TF

Hardware

- RGB Camera
- 3D LiDAR
- Robot Odometry

---

# Mapping Pipeline

The mapping launch subscribes to

- RGB Image
- CameraInfo
- PointCloud2
- Odometry
- TF

RTAB-Map incrementally constructs

- Visual graph
- Occupancy map
- Point cloud map
- Loop closures
- Database (.db)

Launch

```bash
ros2 launch launch/rgb_3dlidar_mapping.launch.py
```

---

# Localization Pipeline

Localization uses

- Previously created RTAB-Map database
- RGB Camera
- PointCloud2
- Odometry
- TF

RTAB-Map performs

- Place recognition
- Loop closure detection
- Pose graph optimization
- map→odom correction

Launch

```bash
ros2 launch launch/rgb_3dlidar_localization.launch.py
```

---

# Kidnapped Robot Experiment

Evaluation procedure

1. Start localization.
2. Allow robot to localize normally.
3. Physically move (kidnap) the robot to an unknown position.
4. Continue publishing odometry.
5. Observe localization behaviour.
6. Record

- localization_pose
- map→odom transform
- odom→base_footprint transform
- loop closures
- recovery time

Expected behaviour

Before recovery

- odom→base remains locally continuous
- localization pose becomes inconsistent
- map→odom remains unchanged

After successful loop closure

- localization pose jumps to correct global pose
- map→odom updates
- odom→base remains continuous

This confirms recovery occurred through **global relocalization rather than odometry reset.**

---

# Experimental Results

The RGB + 3D LiDAR pipeline successfully demonstrated

- Stable mapping
- Reliable localization
- Multiple successful kidnapped robot recovery events
- Recovery through loop closure and pose graph optimization
- Continuous odometry during physical displacement

RTAB-Map database generated

- ~1200 nodes
- ~190 global loop closures
- ~2200 proximity detections

---

# Running Simulation

Refer to

```
docs/simulation_run_order.md
```

for the complete multi-terminal launch sequence.

---

# Hardware Launch

Mapping

```bash
ros2 launch launch/rgb_3dlidar_hardware_mapping.launch.py
```

Localization

```bash
ros2 launch launch/rgb_3dlidar_hardware_localization.launch.py
```

---

# Documentation

Additional documentation

- hardware_requirements.md
- simulation_run_order.md
- offline_phase_summary.md
- results_summary.md

---

# Future Work

- Automated kidnapped robot benchmarking
- Recovery time statistics
- Comparison with AMCL
- Comparison with EMCL2
- Descriptor-based global localization
- Multi-session mapping
- Outdoor evaluation

---

# Author

**Goutham A. S.**

B.Tech Electrical Engineering

Indian Institute of Technology Jodhpur

Robotics Society IIT Jodhpur

Intern — ugo Inc., Tokyo, Japan

---

# Acknowledgements

- ugo Inc.
- IIT Jodhpur
- Open Robotics
- RTAB-Map
- TurtleBot3
