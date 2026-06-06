# Screenshots Directory

This directory should contain the following screenshots for demonstration purposes.

## Required Screenshots

### 1. Build Success
- **Filename**: `01_build_success.png`
- **Command**: `colcon build --symlink-install`
- **Content**: Terminal showing successful colcon build output with "Packages: 3, Built: 3" message

### 2. Package Discovery
- **Filename**: `02_package_list.png`
- **Command**: `ros2 pkg list | grep lab`
- **Content**: List of all three packages:
  - lab01_ros2_basics
  - lab02_nav2_slam_mission_control
  - lab03_aroma_diffuser_robot_mission

### 3. Lab 1 Publisher Output
- **Filename**: `03_lab1_publisher_output.png`
- **Command**: `ros2 run lab01_ros2_basics publisher_node`
- **Content**: Terminal showing:
  - "Publisher started"
  - Publishing messages with incrementing counter
  - Example: "Publishing message: Robot Status #1 - System OK"

### 4. Lab 1 Subscriber Output
- **Filename**: `04_lab1_subscriber_output.png`
- **Command**: `ros2 run lab01_ros2_basics subscriber_node`
- **Content**: Terminal showing:
  - "Subscriber started"
  - Received messages matching publisher output
  - "Communication successful" messages

### 5. Lab 1 Launch File
- **Filename**: `05_lab1_launch_output.png`
- **Command**: `ros2 launch lab01_ros2_basics basics_launch.py`
- **Content**: Combined output showing both publisher and subscriber working together

### 6. Lab 2 Mission Control Output
- **Filename**: `06_lab2_mission_output.png`
- **Command**: `ros2 launch lab02_nav2_slam_mission_control mission_launch.py`
- **Content**: Terminal showing:
  - "Goal Sent"
  - "Goal Accepted"
  - "Goal Reached"
  - "Mission Completed"
  - Robot location updates

### 7. Lab 2 Location Monitoring
- **Filename**: `07_lab2_location_updates.png`
- **Command**: `ros2 topic echo /robot_location`
- **Content**: Stream of robot location updates showing X, Y, Theta values

### 8. Lab 3 Aroma Mission Complete
- **Filename**: `08_lab3_aroma_mission.png`
- **Command**: `ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py`
- **Content**: Terminal showing complete mission sequence:
  - Starting Mission
  - Navigating to targets
  - Diffuser ON/OFF commands
  - Mission Completed

### 9. Lab 3 Diffuser State
- **Filename**: `09_lab3_diffuser_state.png`
- **Command**: Split screen with: `ros2 topic echo /aroma/diffuser_state` and `ros2 topic echo /aroma/mission_status`
- **Content**: State changes as mission progresses

### 10. Repository Structure
- **Filename**: `10_repo_structure.png`
- **Command**: `tree -L 3 src/`
- **Content**: Directory tree showing all packages, files, and structure

## Additional Screenshots (Optional)

### Gazebo Simulation
- **Filename**: `gazebo_simulation.png`
- **Content**: Gazebo window showing TurtleBot3 in indoor world
- **Note**: Requires display or VNC forwarding

### RViz Visualization
- **Filename**: `rviz_visualization.png`
- **Content**: RViz window showing:
  - Map
  - Robot position
  - Navigation goal
  - Costmap
  - Planned path

### SLAM Visualization
- **Filename**: `slam_visualization.png`
- **Content**: SLAM Toolbox output showing map being built

### Nav2 Visualization
- **Filename**: `nav2_visualization.png`
- **Content**: Nav2 stack showing autonomous navigation in progress

## How to Create Screenshots

### On Local Ubuntu with Desktop

1. **Build Success**:
   ```bash
   colcon build --symlink-install 2>&1 | tee build_output.txt
   # Screenshot the final lines showing successful build
   ```

2. **Package List**:
   ```bash
   ros2 pkg list | grep lab
   # Screenshot the output
   ```

3. **Running Nodes**:
   ```bash
   # In separate terminals, run each node and screenshot
   ros2 run lab01_ros2_basics publisher_node
   ros2 run lab01_ros2_basics subscriber_node
   ```

4. **Gazebo and RViz**:
   ```bash
   # Run launch files and take screenshots
   ros2 launch lab02_nav2_slam_mission_control sim_launch.py
   ros2 launch lab02_nav2_slam_mission_control nav2_launch.py
   ```

### On GitHub Codespaces

For headless environment, screenshots would be:
- Terminal output only (text-based)
- No graphical windows (Gazebo, RViz)
- Focused on console output and topic echoing

Alternative: Use VNC/X11 forwarding to get GUI screenshots.

## Screenshot Organization

```
screenshots/
├── README.md (this file)
├── 01_build_success.png
├── 02_package_list.png
├── 03_lab1_publisher_output.png
├── 04_lab1_subscriber_output.png
├── 05_lab1_launch_output.png
├── 06_lab2_mission_output.png
├── 07_lab2_location_updates.png
├── 08_lab3_aroma_mission.png
├── 09_lab3_diffuser_state.png
├── 10_repo_structure.png
├── gazebo_simulation.png (optional)
├── rviz_visualization.png (optional)
├── slam_visualization.png (optional)
└── nav2_visualization.png (optional)
```

## Notes for Submission

- All text in screenshots should be clearly readable (font size 12+)
- Include date/timestamp if possible
- Crop to relevant content only
- Use PNG format for quality
- Consider adding annotations if helpful

## Automated Capture Script

To capture screenshots programmatically:

```bash
#!/bin/bash
# capture_screenshots.sh

mkdir -p screenshots

# Build success
echo "Capturing build output..."
colcon build --symlink-install 2>&1 | tail -20 > /tmp/build_output.txt

# Package list
echo "Capturing package list..."
ros2 pkg list | grep lab > /tmp/package_list.txt

# Run commands and capture output (requires separate terminals)
# This would need to be done manually or with tmux/screen

echo "Screenshots captured to /tmp/"
```

---

**Note**: Screenshots should be added after successful project execution in a proper ROS 2 environment with display support.
