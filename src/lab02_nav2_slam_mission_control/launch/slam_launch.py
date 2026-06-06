#!/usr/bin/env python3
"""
Lab 2: SLAM Launch File
Launches SLAM Toolbox
"""

from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_dir = get_package_share_directory('lab02_nav2_slam_mission_control')
    slam_config = os.path.join(pkg_dir, 'config', 'slam_params.yaml')
    
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[slam_config],
            remappings=[
                ('/scan', '/scan'),
                ('/tf', '/tf'),
                ('/tf_static', '/tf_static'),
            ]
        ),
    ])
