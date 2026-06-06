from setuptools import setup
from glob import glob
import os

package_name = 'lab02_nav2_slam_mission_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'maps'), glob('maps/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ROS2 Student',
    maintainer_email='student@example.com',
    description='lab02_nav2_slam_mission_control package for ROS 2 Jazzy project.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'mission_controller_node = lab02_nav2_slam_mission_control.mission_controller_node:main',
            'robot_location_monitor_node = lab02_nav2_slam_mission_control.robot_location_monitor_node:main',
        ],
    },
)
