#!/usr/bin/env python3
"""
Lab 2: Mission Launch File
Launches mission controller and robot location monitor
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab02_nav2_slam_mission_control',
            executable='mission_controller_node',
            name='mission_controller',
            output='screen'
        ),
        
        Node(
            package='lab02_nav2_slam_mission_control',
            executable='robot_location_monitor_node',
            name='robot_location_monitor',
            output='screen'
        ),
    ])
