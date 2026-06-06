#!/bin/bash
# Setup script for ROS 2 Aroma Diffuser Robot Project
# This script installs ROS 2 Jazzy and builds the project

set -e

echo "=========================================="
echo "ROS 2 Aroma Diffuser Robot - Setup Script"
echo "=========================================="
echo ""

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "Cannot detect OS"
    exit 1
fi

echo "Detected OS: $OS"

# Check if running Ubuntu 24.04
if [[ "$VERSION_ID" != "24.04" ]]; then
    echo "WARNING: This project requires Ubuntu 24.04 for ROS 2 Jazzy"
    echo "Current version: $VERSION_ID"
fi

echo ""
echo "Step 1: Setting up ROS 2 Jazzy repository..."
sudo curl -sSL https://repo.ros2.org/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu noble main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

echo "Step 2: Updating package lists..."
sudo apt update

echo "Step 3: Installing ROS 2 Jazzy..."
sudo apt install -y ros-jazzy-desktop

echo "Step 4: Installing build tools..."
sudo apt install -y python3-colcon-common-extensions python3-rosdep

echo "Step 5: Initializing rosdep..."
sudo rosdep init || true
rosdep update

echo "Step 6: Sourcing ROS 2 setup..."
source /opt/ros/jazzy/setup.bash

echo "Step 7: Building project..."
cd "$(dirname "$0")"
rosdep install --from-paths src --ignore-src -r -y || true
colcon build --symlink-install

echo ""
echo "=========================================="
echo "Build completed successfully!"
echo "=========================================="
echo ""
echo "To use the project, source the setup in your current shell:"
echo "  source install/setup.bash"
echo ""
echo "To run Lab 1 (ROS 2 Basics):"
echo "  ros2 launch lab01_ros2_basics basics_launch.py"
echo ""
echo "To run Lab 2 Mission Control:"
echo "  ros2 launch lab02_nav2_slam_mission_control mission_launch.py"
echo ""
echo "To run Lab 3 Aroma Diffuser:"
echo "  ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py"
echo ""
