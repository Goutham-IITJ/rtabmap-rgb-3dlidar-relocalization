from launch import LaunchDescription
from launch_ros.actions import Node
import os


def generate_launch_description():
    home = os.path.expanduser("~")

    database_file = os.path.join(
        home,
        ".ros/rtabmap_rgb_3dlidar_hardware_LOCALIZATION_TEST.db"
    )

    params = {
        "use_sim_time": False,
        "frame_id": "base_footprint",
        "database_path": database_file,

        "Mem/IncrementalMemory": "false",
        "Mem/InitWMWithAllNodes": "false",

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
        "Vis/EpipolarGeometryVar": "1.0",

        "RGBD/LoopClosureReextractFeatures": "true",
        "RGBD/ProximityBySpace": "true",

        "Grid/FromDepth": "false",

        "Kp/MaxFeatures": "2000",
        "Vis/MaxFeatures": "2000",
        "Vis/MinInliers": "6",
        "Vis/InlierDistance": "0.15",

        "scan_cloud_max_points": 5000,

        "Icp/PointToPlane": "true",
        "Icp/VoxelSize": "0.15",
        "Icp/MaxCorrespondenceDistance": "0.60",
        "Icp/CorrespondenceRatio": "0.1",
        "Icp/MaxTranslation": "1.5",
        "Icp/MaxRotation": "3.14",

        "RGBD/OptimizeMaxError": "10.0",
        "Rtabmap/DetectionRate": "0.5",
    }

    remaps = [
        ("rgb/image", "/camera/image_raw"),
        ("rgb/camera_info", "/camera/camera_info"),
        ("scan_cloud", "/livox/lidar"),
        ("odom", "/odom"),
    ]

    return LaunchDescription([
        Node(
            package="rtabmap_slam",
            executable="rtabmap",
            namespace="rtabmap_rgb_3dlidar",
            name="rtabmap",
            output="screen",
            parameters=[params],
            remappings=remaps,
        )
    ])
