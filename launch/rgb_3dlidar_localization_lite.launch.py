from launch import LaunchDescription
from launch_ros.actions import Node
import os


def generate_launch_description():
    home = os.path.expanduser("~")

    database_file = os.path.join(
        home,
        ".ros/rtabmap_rgb_3dlidar_LOCALIZATION_TEST.db"
    )

    params = {
        "use_sim_time": True,
        "frame_id": "base_footprint",
        "database_path": database_file,

        # Localization mode
        "Mem/IncrementalMemory": "false",

        # Lighter than loading all 1207 nodes into working memory
        "Mem/InitWMWithAllNodes": "false",

        # Inputs: RGB + 3D LiDAR + odom
        "subscribe_rgb": True,
        "subscribe_depth": False,
        "subscribe_scan": False,
        "subscribe_scan_cloud": True,
        "subscribe_stereo": False,
        "subscribe_rgbd": False,

        "approx_sync": True,
        "sync_queue_size": 10,
        "topic_queue_size": 10,
        "wait_for_transform": 2.0,

        "Vis/EpipolarGeometryVar": "1.0",

        # Registration
        "Reg/Force3DoF": "true",
        "Reg/Strategy": "1",

        # Monocular visual verification
        "Vis/EstimationType": "2",
        "RGBD/LoopClosureReextractFeatures": "true",
        "RGBD/ProximityBySpace": "true",

        # No depth-camera grid
        "Grid/FromDepth": "false",

        # Reduce CPU load
        "Kp/MaxFeatures": "2000",
        "Vis/MaxFeatures": "2000",
        "Vis/MinInliers": "6",
        "Vis/InlierDistance": "0.15",

        # Reduce 3D cloud computation
        "scan_cloud_max_points": 2500,
        "Icp/PointToPlane": "true",
        "Icp/VoxelSize": "0.20",
        "Icp/MaxCorrespondenceDistance": "0.60",
        "Icp/CorrespondenceRatio": "0.1",
        "Icp/MaxTranslation": "1.5",
        "Icp/MaxRotation": "3.14",

        "RGBD/OptimizeMaxError": "10.0",

        # Process one frame every ~2 seconds
        "Rtabmap/DetectionRate": "0.5",
    }

    remaps = [
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
            parameters=[params],
            remappings=remaps,
        )
    ])
