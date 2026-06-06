#!/usr/bin/env python3
"""
Lab 2: Simulation Launch File
Launches TurtleBot3 in Gazebo with indoor world
"""

from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_dir = get_package_share_directory('lab02_nav2_slam_mission_control')
    world_file = os.path.join(pkg_dir, 'worlds', 'indoor_world.world')
    
    return LaunchDescription([
        DeclareLaunchArgument('world', default_value=world_file),
        
        # Gazebo server
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '-s', 'libgazebo_ros_factory.so',
                '-s', 'libgazebo_ros_init.so',
                LaunchConfiguration('world')
            ],
            output='screen',
            on_exit=None,
        ),
        
        # Gazebo client (commented for headless environment)
        # ExecuteProcess(
        #     cmd=['gzclient'],
        #     output='screen',
        # ),
        
        # TurtleBot3 spawn (requires turtlebot3 package)
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'gazebo_ros', 'spawn_entity.py',
                '-entity', 'turtlebot3_burger',
                '-topic', '/robot_description',
                '-x', '0', '-y', '0', '-z', '0'
            ],
            output='screen',
            on_exit=None,
        ),
    ])
