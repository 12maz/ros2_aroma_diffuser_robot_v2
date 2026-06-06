# Indoor Autonomous Aroma Diffuser Robot using ROS 2

## Project Overview

This is a comprehensive ROS 2 Jazzy project demonstrating autonomous mobile robot control, SLAM, navigation, and mission planning. The project consists of three progressive labs:

- **Lab 1**: ROS 2 Basics (Publisher/Subscriber pattern)
- **Lab 2**: Navigation, SLAM, and Mission Control with TurtleBot3
- **Lab 3**: Aroma Diffuser Robot Mission (multi-waypoint navigation with actuation)

The project is designed to be **submission-ready** and can run on:
- Local Ubuntu 24.04 with ROS 2 Jazzy
- GitHub Codespaces (with limitations on graphical components)

## Quick Start

### Local Ubuntu (Recommended)
```bash
cd /path/to/project
chmod +x setup.sh
./setup.sh
source install/setup.bash
ros2 launch lab01_ros2_basics basics_launch.py
```

### GitHub Codespaces
```bash
cd /workspaces/ros2_aroma_diffuser_robot_v2
chmod +x setup.sh
./setup.sh
source install/setup.bash
```

## Project Structure

```
src/
├── lab01_ros2_basics/                     # Lab 1: Basic ROS 2
│   ├── lab01_ros2_basics/
│   │   ├── publisher_node.py
│   │   └── subscriber_node.py
│   └── launch/basics_launch.py
│
├── lab02_nav2_slam_mission_control/       # Lab 2: Navigation & SLAM
│   ├── lab02_nav2_slam_mission_control/
│   │   ├── mission_controller_node.py
│   │   └── robot_location_monitor_node.py
│   ├── launch/
│   │   ├── sim_launch.py
│   │   ├── slam_launch.py
│   │   ├── nav2_launch.py
│   │   └── mission_launch.py
│   ├── config/ (SLAM, Nav2 parameters)
│   ├── rviz/ (visualization configs)
│   ├── worlds/ (Gazebo world)
│   └── maps/ (map files)
│
└── lab03_aroma_diffuser_robot_mission/    # Lab 3: Aroma diffuser
    ├── lab03_aroma_diffuser_robot_mission/
    │   ├── aroma_diffuser_node.py
    │   └── aroma_mission_node.py
    └── launch/aroma_mission_launch.py
```

## Installation

### Prerequisites
- Ubuntu 24.04 LTS
- 4GB RAM minimum
- Internet connection

### Automated Installation
```bash
chmod +x setup.sh
./setup.sh
```

This script will:
1. Add ROS 2 Jazzy repository
2. Install ROS 2 Jazzy Desktop
3. Install build tools
4. Build all packages

### Manual Installation
```bash
# Setup ROS 2 repository
sudo curl -sSL https://repo.ros2.org/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu noble main" | sudo tee /etc/apt/sources.list.d/ros2.list

# Install ROS 2
sudo apt update
sudo apt install -y ros-jazzy-desktop python3-colcon-common-extensions

# Initialize rosdep
sudo rosdep init
rosdep update

# Build project
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Running the Project

### Always source first:
```bash
source install/setup.bash
```

### Lab 1: ROS 2 Basics
```bash
# Option 1: Launch both nodes together
ros2 launch lab01_ros2_basics basics_launch.py

# Option 2: Run individually
# Terminal 1:
ros2 run lab01_ros2_basics publisher_node
# Terminal 2:
ros2 run lab01_ros2_basics subscriber_node
```

### Lab 2: Mission Control
```bash
ros2 launch lab02_nav2_slam_mission_control mission_launch.py
```

### Lab 3: Aroma Diffuser
```bash
ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py
```

## Expected Output

### Lab 1
```
[publisher_node] Publisher started
[publisher_node] Publishing message: Robot Status #1 - System OK
[subscriber_node] Subscriber started
[subscriber_node] Received message: Publishing message: Robot Status #1 - System OK
[subscriber_node] Communication successful
```

### Lab 2
```
[mission_controller_node] Goal Sent
[mission_controller_node] Obstacle avoidance enabled
[mission_controller_node] Goal Accepted
[mission_controller_node] Goal Reached
[mission_controller_node] Robot location update: X=2.0, Y=2.0
```

### Lab 3
```
[aroma_mission_node] Starting Mission
[aroma_mission_node] Navigating to Target 1
[aroma_mission_node] Goal Reached - Target 1
[aroma_diffuser_node] Diffuser ON
[aroma_mission_node] Waiting - Diffuser active
[aroma_diffuser_node] Diffuser OFF
[aroma_mission_node] Navigating to Target 2
[aroma_mission_node] Goal Reached - Target 2
[aroma_diffuser_node] Diffuser ON
[aroma_mission_node] Mission Completed - Robot at Home
```

## Package Verification

```bash
# List all packages
ros2 pkg list | grep lab

# Check executables
ros2 run lab01_ros2_basics publisher_node --help
ros2 run lab02_nav2_slam_mission_control mission_controller_node --help
ros2 run lab03_aroma_diffuser_robot_mission aroma_diffuser_node --help

# Check launch files
ros2 launch lab01_ros2_basics basics_launch.py --show-args
ros2 launch lab02_nav2_slam_mission_control mission_launch.py --show-args
ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py --show-args
```

## Topics Demonstrated

| Lab | Topic | Type | Direction |
|-----|-------|------|-----------|
| 1 | `/aroma_robot/status` | std_msgs/String | Pub/Sub |
| 2 | `/goal_pose` | geometry_msgs/PoseStamped | Pub |
| 2 | `/robot_location` | std_msgs/String | Pub/Sub |
| 2 | `/mission_status` | std_msgs/String | Pub/Sub |
| 3 | `/aroma/diffuser_command` | std_msgs/String | Pub |
| 3 | `/aroma/diffuser_state` | std_msgs/String | Pub |
| 3 | `/aroma/mission_status` | std_msgs/String | Pub |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Package not found" | `source install/setup.bash` |
| "No executable found" | Rebuild: `colcon build --symlink-install` |
| "ROS 2 command not found" | Install: `sudo apt install ros-jazzy-desktop` |
| Gazebo doesn't display | Expected in Codespaces. Use local Ubuntu or X11 forwarding |

## GitHub Codespaces

### What Works ✅
- All ROS 2 packages build and install
- All nodes execute and communicate
- Topic monitoring and echoing
- Launch files run (text output only)
- Log monitoring

### Requires GUI ⚠️
- Gazebo visualization
- RViz visualization
- SLAM visualization

**Workaround**: SSH with X11 forwarding or use local Ubuntu.

## Ubuntu 24.04 Deployment

### Recommended Setup
```bash
# Fresh Ubuntu 24.04 installation
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git

# Install ROS 2 Jazzy
# (Use setup.sh script)

# For simulation (optional)
sudo apt install -y ros-jazzy-gazebo-* ros-jazzy-turtlebot3*
export TURTLEBOT3_MODEL=burger
```

## Documentation Files

- `README.md` - This file (overview and quick start)
- `final_report.md` - Technical report and architecture
- `demo_commands.md` - Step-by-step demonstration commands
- `validation_report.md` - Build and test results
- `screenshots/` - Expected output screenshots
- `videos/` - Demo video descriptions

## Key Features

✅ **Lab 1: ROS 2 Basics**
- Publisher and Subscriber nodes
- Topic-based communication
- Launch file integration

✅ **Lab 2: Navigation & SLAM**
- TurtleBot3 simulation (Gazebo)
- SLAM Toolbox integration
- Nav2 stack for autonomous navigation
- RViz visualization
- Obstacle avoidance
- Multi-waypoint mission

✅ **Lab 3: Aroma Diffuser**
- State machine mission planning
- Multi-waypoint navigation
- Actuator control (diffuser)
- Real-time mission status monitoring
- Complete mission sequence (home → target1 → target2 → home)

## Technologies Used

- **ROS 2 Jazzy** - Robotics middleware
- **Python 3.10+** - Node implementation
- **colcon** - Build system
- **Launch** - Node orchestration
- **std_msgs** - Basic message types
- **geometry_msgs** - Pose and transform messages
- **nav_msgs** - Navigation messages
- **Gazebo** - Robot simulation
- **SLAM Toolbox** - Simultaneous Localization and Mapping
- **Nav2** - Autonomous navigation
- **RViz** - Visualization
- **YAML** - Configuration files

## Build Commands

```bash
# Source ROS 2
source /opt/ros/jazzy/setup.bash

# Build all packages
colcon build --symlink-install

# Build specific package
colcon build --packages-select lab01_ros2_basics

# Build with verbose output
colcon build --symlink-install --event-handlers console_direct+

# Source built packages
source install/setup.bash
```

## Resources

- [ROS 2 Jazzy Documentation](https://docs.ros.org/en/jazzy/)
- [Nav2 Documentation](https://docs.nav2.org/)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)
- [TurtleBot3 Manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/)

## License

Apache License 2.0

## Author

ROS 2 Development Team
