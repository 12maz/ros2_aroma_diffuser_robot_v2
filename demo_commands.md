# Demo Commands - Step by Step Demonstration

This document provides exact commands for live demonstration of the ROS 2 Aroma Diffuser Robot project.

## Preparation (Before Demo)

```bash
# Open a terminal and navigate to project
cd /path/to/ros2_aroma_diffuser_robot_v2

# Source ROS 2 environment
source /opt/ros/jazzy/setup.bash

# Ensure project is built
colcon build --symlink-install

# Source project setup
source install/setup.bash
```

## Phase 1: Build Verification (5 minutes)

### Step 1.1: Show project structure
```bash
# Show directory layout
tree -L 3 src/

# Or with find
find src -type f -name "*.py" | head -20
```

**Expected**: Show all three packages organized under src/

### Step 1.2: Verify packages are discovered
```bash
ros2 pkg list | grep lab
```

**Expected output:**
```
lab01_ros2_basics
lab02_nav2_slam_mission_control
lab03_aroma_diffuser_robot_mission
```

### Step 1.3: Show all executables
```bash
ros2 pkg executables | grep lab
```

**Expected output:**
```
lab01_ros2_basics publisher_node
lab01_ros2_basics subscriber_node
lab02_nav2_slam_mission_control mission_controller_node
lab02_nav2_slam_mission_control robot_location_monitor_node
lab03_aroma_diffuser_robot_mission aroma_diffuser_node
lab03_aroma_diffuser_robot_mission aroma_mission_node
```

### Step 1.4: Show available launch files
```bash
ros2 launch lab01_ros2_basics --help
ros2 launch lab02_nav2_slam_mission_control --help
ros2 launch lab03_aroma_diffuser_robot_mission --help
```

## Phase 2: Lab 1 - ROS 2 Basics (8 minutes)

### Step 2.1: Launch both nodes together (Recommended for demo)

**Open one terminal:**
```bash
ros2 launch lab01_ros2_basics basics_launch.py
```

**Expected output:**
```
[INFO] [launch]: All log files can be found below /home/user/.ros/log/...
[INFO] [publisher_node-1]: process started with PID 12345
[subscriber_node-1]: process started with PID 12346
[publisher_node-1]: Publisher started
[subscriber_node-1]: Subscriber started
[publisher_node-1]: Publishing message: Robot Status #1 - System OK
[subscriber_node-1]: Received message: Publishing message: Robot Status #1 - System OK
[subscriber_node-1]: Communication successful
[publisher_node-1]: Publishing message: Robot Status #2 - System OK
[subscriber_node-1]: Received message: Publishing message: Robot Status #2 - System OK
[subscriber_node-1]: Communication successful
```

Let it run for 5-10 seconds showing message exchange, then press Ctrl+C.

### Alternative 2.1.1: Run nodes separately to show communication

**Terminal 1:**
```bash
ros2 run lab01_ros2_basics publisher_node
```

**Terminal 2 (new):**
```bash
ros2 run lab01_ros2_basics subscriber_node
```

**Terminal 3 (new) - Optional: Monitor the topic**
```bash
ros2 topic echo /aroma_robot/status
```

### Step 2.2: Show topic information

**Terminal 3 (if available):**
```bash
ros2 topic list
ros2 topic info /aroma_robot/status
ros2 topic bw /aroma_robot/status
```

**Expected:**
- Topic exists and has 1 publisher, 1 subscriber
- Message type is `std_msgs/String`
- Shows bandwidth usage

### Step 2.3: Explain the architecture
- Show publisher_node.py source code (brief)
- Show subscriber_node.py source code (brief)
- Show basics_launch.py to explain node orchestration

---

## Phase 3: Lab 2 - Mission Control & Navigation (5 minutes)

### Step 3.1: Launch mission controller

**Terminal 1:**
```bash
ros2 launch lab02_nav2_slam_mission_control mission_launch.py
```

**Expected output:**
```
[mission_controller_node-1]: Goal Sent
[mission_controller_node-1]: Obstacle avoidance enabled
[robot_location_monitor_node-1]: Robot location monitor started
[robot_location_monitor_node-1]: Robot location update: Robot at X=0.00, Y=2.00, Theta=0.50
[mission_controller_node-1]: Goal Accepted
[mission_controller_node-1]: Goal Reached
[mission_controller_node-1]: Robot location update: X=2.0, Y=2.0
[mission_controller_node-1]: Navigating to next waypoint...
[mission_controller_node-1]: Mission Completed
```

Let it run for 10-15 seconds showing mission progression, then press Ctrl+C.

### Step 3.2: Monitor mission topics

**Terminal 2:**
```bash
ros2 topic echo /mission_status
```

**Terminal 3 (optional):**
```bash
ros2 topic echo /robot_location
```

### Step 3.3: Explain the mission

The mission demonstrates:
- Goal setting and acceptance
- Obstacle avoidance
- Robot location monitoring
- Mission completion
- Multi-waypoint path

This provides the foundation for autonomous navigation.

---

## Phase 4: Lab 3 - Aroma Diffuser Mission (7 minutes)

### Step 4.1: Launch aroma mission

**Terminal 1:**
```bash
ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py
```

**Expected output (scrolling over ~12 seconds):**
```
[aroma_diffuser_node-1]: Aroma Diffuser Node started
[aroma_mission_node-1]: Starting Mission
[aroma_mission_node-1]: At Home - Mission initialized
[aroma_mission_node-1]: Navigating to Target 1
[aroma_mission_node-1]: Goal Reached - Target 1
[aroma_diffuser_node-1]: Diffuser ON
[aroma_mission_node-1]: Waiting - Diffuser active
[aroma_diffuser_node-1]: Diffuser OFF
[aroma_mission_node-1]: Navigating to Target 2
[aroma_mission_node-1]: Goal Reached - Target 2
[aroma_diffuser_node-1]: Diffuser ON
[aroma_mission_node-1]: Waiting - Diffuser active
[aroma_diffuser_node-1]: Diffuser OFF
[aroma_mission_node-1]: Navigating back to Home
[aroma_mission_node-1]: Mission Completed - Robot at Home
```

### Step 4.2: Monitor mission topics

**Terminal 2:**
```bash
ros2 topic echo /aroma/mission_status
```

**Terminal 3:**
```bash
ros2 topic echo /aroma/diffuser_state
```

### Step 4.3: Show message flow

Demonstrate:
- Mission status updates
- Diffuser commands and state
- Topic coordination between nodes
- Timed state transitions

---

## Phase 5: Summary and Q&A (5 minutes)

### Quick Summary Commands

**List all packages again:**
```bash
ros2 pkg list | grep lab
```

**Show build directory:**
```bash
ls -la build/
ls -la install/
```

**Show colcon build output:**
```bash
cat build.log | tail -50
```

### Key Points to Highlight

1. **Lab 1**: Basic ROS 2 communication patterns (pub/sub)
2. **Lab 2**: Navigation and mission control foundation
3. **Lab 3**: Complete mission with multi-step sequence and actuator control

### Possible Questions and Answers

**Q: How do the nodes communicate?**
A: Through ROS 2 topics using pub/sub pattern. Each node publishes messages that other nodes can subscribe to.

**Q: Can nodes run on different machines?**
A: Yes! ROS 2 supports distributed systems. Nodes can run on any machine on the network with proper ROS 2 setup.

**Q: How does the mission proceed through states?**
A: Timer callbacks check elapsed time and transition to next state when conditions are met.

**Q: What about the TurtleBot3 simulation?**
A: Lab 2 includes launch files for full Gazebo simulation. In headless environments (Codespaces), we run mission control without graphics.

---

## Alternative Demo Scenarios

### Quick 5-Minute Demo (Minimum)

1. Show project structure (1 min)
2. List packages and executables (1 min)
3. Run Lab 1 with launch file (2 min)
4. Run Lab 3 mission (1 min)

### Comprehensive 30-Minute Demo

1. Build phase walkthrough (5 min)
2. Lab 1 detailed with topic monitoring (8 min)
3. Lab 2 mission control explanation (5 min)
4. Lab 3 full mission (7 min)
5. Code walkthrough and Q&A (5 min)

### GUI Demo (with Desktop Ubuntu)

For systems with display:
```bash
# Add to above commands:
ros2 launch lab02_nav2_slam_mission_control sim_launch.py    # Gazebo
ros2 launch lab02_nav2_slam_mission_control nav2_launch.py   # RViz + Nav2
```

---

## Troubleshooting During Demo

### Node doesn't start
```bash
# Check if package is installed
ros2 pkg list | grep lab01

# Rebuild if needed
colcon build --symlink-install
source install/setup.bash
```

### Topic doesn't appear
```bash
# List active topics
ros2 topic list

# Check node is running
ros2 node list

# Show node info
ros2 node info /publisher_node
```

### Strange output or errors
```bash
# Check environment is properly sourced
echo $ROS_PACKAGE_PATH

# Verify ROS 2 is working
ros2 topic list
ros2 node list
```

### Clean rebuild if issues persist
```bash
rm -rf build/ install/ log/
colcon build --symlink-install
source install/setup.bash
```

---

## Time Breakdown

| Phase | Time | Activity |
|-------|------|----------|
| 1 | 5 min | Build verification |
| 2 | 8 min | Lab 1 demo |
| 3 | 5 min | Lab 2 demo |
| 4 | 7 min | Lab 3 demo |
| 5 | 5 min | Summary |
| **Total** | **30 min** | **Full demo** |

---

## Recording Tips

If recording the demo for later:

1. **Terminal setup**: Use large font (size 18+) for visibility
2. **Speed**: Run demos at normal speed, don't rush
3. **Narration**: Explain what's happening as it runs
4. **Zoom**: Zoom into terminal or code when showing details
5. **Multiple videos**: Consider separate videos for each lab

### Recording Commands

```bash
# Record terminal to file (text)
script demo_output.txt

# Then run all demo commands
# Exit with 'exit' command

# View recording
cat demo_output.txt
```

---

This demo script ensures a smooth, professional presentation of the ROS 2 Aroma Diffuser Robot project.
