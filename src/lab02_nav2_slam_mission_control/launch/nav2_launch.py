#!/usr/bin/env python3
"""
Lab 2: Nav2 Launch File
Launches Navigation 2 stack
"""

from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_dir = get_package_share_directory('lab02_nav2_slam_mission_control')
    nav2_config = os.path.join(pkg_dir, 'config', 'nav2_params.yaml')
    rviz_config = os.path.join(pkg_dir, 'rviz', 'nav2_default_view.rviz')
    
    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'yaml_filename': os.path.join(pkg_dir, 'maps', 'map.yaml')}],
        ),
        
        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[nav2_config],
        ),
        
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[nav2_config],
        ),
        
        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[nav2_config],
        ),
        
        Node(
            package='nav2_behaviortree_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[nav2_config],
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
        ),
    ])
