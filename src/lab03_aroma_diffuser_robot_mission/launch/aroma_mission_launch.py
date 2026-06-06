#!/usr/bin/env python3
"""
Lab 3: Aroma Mission Launch File
Launches aroma diffuser and aroma mission nodes
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab03_aroma_diffuser_robot_mission',
            executable='aroma_diffuser_node',
            name='aroma_diffuser',
            output='screen'
        ),
        
        Node(
            package='lab03_aroma_diffuser_robot_mission',
            executable='aroma_mission_node',
            name='aroma_mission',
            output='screen'
        ),
    ])
