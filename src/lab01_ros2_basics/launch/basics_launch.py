#!/usr/bin/env python3
"""
Lab 1: Basic Launch File
Launches publisher and subscriber nodes
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab01_ros2_basics',
            executable='publisher_node',
            name='publisher',
            output='screen'
        ),
        Node(
            package='lab01_ros2_basics',
            executable='subscriber_node',
            name='subscriber',
            output='screen'
        ),
    ])
