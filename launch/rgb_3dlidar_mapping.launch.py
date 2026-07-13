from launch import LaunchDescription
from launch_ros.actions import Node
import os


def generate_launch_description():
    home = os.path.expanduser("~")

    params_file = os.path.join(
        home,
        "rtabmap_rgb_3dlidar_ws/config/rtabmap_rgb_3dlidar_params.yaml"
    )

    database_file = os.path.join(
        home,
        ".ros/rtabmap_rgb_3dlidar.db"
    )

    common_params = {
        "use_sim_time": True,
        "frame_id": "base_footprint",

        # Inputs: RGB + 3D LiDAR cloud + odom
        "subscribe_rgb": True,
        "subscribe_depth": False,
        "subscribe_scan": False,
        "subscribe_scan_cloud": True,
        "subscribe_stereo": False,
        "subscribe_rgbd": False,

        "approx_sync": True,
        "sync_queue_size": 50,
        "topic_queue_size": 50,
        "wait_for_transform": 2.0,

        "Reg/Force3DoF": "true",
        "Reg/Strategy": "1",

        "Vis/EstimationType": "2",
        "RGBD/LoopClosureReextractFeatures": "true",
        "RGBD/ProximityBySpace": "true",

        "Grid/FromDepth": "false",

        "Kp/MaxFeatures": "2000",
        "Vis/MaxFeatures": "2000",
        "Vis/MinInliers": "6",
        "Vis/InlierDistance": "0.15",

        "Icp/PointToPlane": "true",
        "Icp/VoxelSize": "0.10",
        "Icp/MaxCorrespondenceDistance": "0.50",
        "Icp/CorrespondenceRatio": "0.1",
        "Icp/MaxTranslation": "1.5",
        "Icp/MaxRotation": "3.14",

        "RGBD/OptimizeMaxError": "10.0",
        "Rtabmap/DetectionRate": "1.0",
        "Vis/EpipolarGeometryVar": "1.0",
    }

    common_remaps = [
        ("rgb/image", "/camera/image_raw"),
        ("rgb/camera_info", "/camera/camera_info"),
        ("scan_cloud", "/lidar_3d/points"),
        ("odom", "/odom"),
    ]

    return LaunchDescription([
        Node(
            package="rtabmap_slam",
            executable="rtabmap",
            namespace="rtabmap_rgb_3dlidar",
            name="rtabmap",
            output="screen",
            parameters=[
                params_file,
                common_params,
                {
                    "database_path": database_file,
                    "Mem/IncrementalMemory": "true",
                    "Mem/InitWMWithAllNodes": "false",
                },
            ],
            remappings=common_remaps,
            arguments=["-d"],
        )
    ])
