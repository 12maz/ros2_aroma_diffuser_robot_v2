# Videos Directory

This directory should contain demonstration videos of the ROS 2 Aroma Diffuser Robot project.

## Required Video Clips

### 1. Complete Project Demo
- **Filename**: `01_complete_demo.mp4`
- **Duration**: 30 minutes
- **Content**:
  - Project structure walkthrough (2 min)
  - Build process and verification (5 min)
  - Lab 1: ROS 2 Basics demonstration (8 min)
  - Lab 2: Mission Control demo (5 min)
  - Lab 3: Aroma Diffuser Mission (7 min)
  - Summary and Q&A (3 min)

### 2. Lab 1: ROS 2 Basics
- **Filename**: `02_lab1_ros2_basics.mp4`
- **Duration**: 8 minutes
- **Content**:
  - Show publisher_node.py code (2 min)
  - Show subscriber_node.py code (2 min)
  - Run both nodes together (2 min)
  - Explain topic communication (2 min)

### 3. Lab 2: Mission Control
- **Filename**: `03_lab2_mission_control.mp4`
- **Duration**: 5 minutes
- **Content**:
  - Show mission controller node code (1 min)
  - Show location monitor node code (1 min)
  - Run mission launch file (2 min)
  - Show mission completion (1 min)

### 4. Lab 3: Aroma Diffuser
- **Filename**: `04_lab3_aroma_diffuser.mp4`
- **Duration**: 7 minutes
- **Content**:
  - Show aroma mission node code (2 min)
  - Show aroma diffuser node code (2 min)
  - Run complete mission (2 min)
  - Monitor all topics (1 min)

### 5. Build and Installation
- **Filename**: `05_build_installation.mp4`
- **Duration**: 10 minutes
- **Content**:
  - Project structure overview (2 min)
  - Running setup.sh script (5 min)
  - Verification of all packages (3 min)

### 6. Gazebo Simulation
- **Filename**: `06_gazebo_simulation.mp4`
- **Duration**: 5 minutes
- **Content**:
  - Gazebo world loading
  - TurtleBot3 spawning
  - Indoor environment visibility
  - Simulation physics in action

### 7. RViz Visualization
- **Filename**: `07_rviz_visualization.mp4`
- **Duration**: 5 minutes
- **Content**:
  - RViz window with map display
  - Robot pose visualization
  - Goal marker for navigation
  - Costmap visualization
  - Planned path display

### 8. SLAM Mapping
- **Filename**: `08_slam_mapping.mp4`
- **Duration**: 8 minutes
- **Content**:
  - SLAM Toolbox startup
  - Map building in real-time
  - Sensor data visualization
  - Final map completion

### 9. Nav2 Autonomous Navigation
- **Filename**: `09_nav2_autonomous_navigation.mp4`
- **Duration**: 10 minutes
- **Content**:
  - Nav2 stack initialization
  - Goal setting via RViz
  - Robot autonomous navigation
  - Obstacle avoidance in action
  - Goal reached confirmation

### 10. Complete Mission Sequence
- **Filename**: `10_complete_mission_sequence.mp4`
- **Duration**: 15 minutes
- **Content**:
  - All systems startup (mission + simulation + SLAM + Nav2)
  - Robot initialization at home
  - Navigation to Target 1
  - Diffuser activation at Target 1
  - Navigation to Target 2
  - Diffuser activation at Target 2
  - Return to home
  - Mission completion

## Video Recording Guidelines

### Technical Specifications
- **Format**: MP4 with H.264 codec
- **Resolution**: 1920x1080 (1080p) or 1280x720 (720p)
- **Frame Rate**: 30 fps
- **Audio**: Optional (project sounds or narration)
- **File Size**: Optimized for GitHub (< 500 MB per video)

### Recording Setup

#### On Local Ubuntu with Desktop
```bash
# Method 1: Using SimpleScreenRecorder
# Install: sudo apt install simplescreenrecorder
# Start and record desired area

# Method 2: Using ffmpeg
ffmpeg -f x11grab -i :0 -f pulse -i default \
  -c:v libx264 -c:a aac -r 30 video.mp4

# Method 3: Using OBS Studio
# Install: sudo apt install obs-studio
# Configure scenes and record
```

#### On GitHub Codespaces (Terminal Only)
```bash
# Record terminal session as text
script demo_session.txt

# Run all demo commands
ros2 launch lab01_ros2_basics basics_launch.py
# (show output for 10 seconds)

# Convert terminal recording to video
# (Use asciinema or similar tools)
asciinema rec demo.cast
asciinema upload demo.cast
```

### Content Guidelines

1. **Clear Audio**:
   - Use microphone or text-to-speech
   - Explain what's happening
   - Pause between sections
   - No background noise

2. **Visual Clarity**:
   - Use large fonts (minimum 16pt)
   - Zoom into code when showing details
   - Highlight important parts
   - Use cursor to point to items

3. **Pacing**:
   - Don't rush through commands
   - Pause after command execution to show output
   - Give time for nodes to start
   - Show complete message sequences

4. **Narration Tips**:
   - Introduce each section
   - Explain what the code does
   - Show expected output
   - Highlight key features
   - End with summary

### Video Editing

If editing is needed:

```bash
# Install video editor
sudo apt install kdenlive  # KDEnlive video editor

# Or use FFmpeg for command-line editing:
# Cut video from 10s to 60s:
ffmpeg -i input.mp4 -ss 10 -to 60 -c copy output.mp4

# Compress video:
ffmpeg -i input.mp4 -crf 23 -preset medium output.mp4
```

## Video Directory Structure

```
videos/
├── README.md (this file)
├── 01_complete_demo.mp4
├── 02_lab1_ros2_basics.mp4
├── 03_lab2_mission_control.mp4
├── 04_lab3_aroma_diffuser.mp4
├── 05_build_installation.mp4
├── 06_gazebo_simulation.mp4 (optional - requires GUI)
├── 07_rviz_visualization.mp4 (optional - requires GUI)
├── 08_slam_mapping.mp4 (optional - requires GUI)
├── 09_nav2_autonomous_navigation.mp4 (optional - requires GUI)
└── 10_complete_mission_sequence.mp4 (optional - requires GUI)
```

## Demo Video Script

### 30-Minute Complete Demo

**[0:00-2:00] Introduction**
```
"This is a demonstration of the ROS 2 Aroma Diffuser Robot project.
This project showcases three progressive laboratories:
- Lab 1: ROS 2 Basics with Publisher/Subscriber nodes
- Lab 2: Navigation, SLAM, and Mission Control
- Lab 3: Autonomous Aroma Diffuser Mission"
```

**[2:00-4:00] Project Structure**
```
"Let's look at the project structure.
We have three packages under src/
Each package contains Python nodes, launch files, and configurations."
```

**[4:00-9:00] Build Process**
```
"Now let's build the project.
We'll use colcon, the ROS 2 build tool."
[Run: colcon build --symlink-install]
"The build completes successfully, building all 3 packages."
```

**[9:00-17:00] Lab 1 Demonstration**
```
"Lab 1 demonstrates fundamental ROS 2 concepts.
We have a Publisher that sends status messages,
and a Subscriber that receives and processes them."
[Show code briefly]
"Now let's run it."
[Run: ros2 launch lab01_ros2_basics basics_launch.py]
[Wait 10 seconds]
[Show message exchange]
"You can see the messages being published and received."
```

**[17:00-22:00] Lab 2 Demonstration**
```
"Lab 2 demonstrates mission control and robot location monitoring.
This is more complex - we have mission planning and autonomous navigation."
[Run: ros2 launch lab02_nav2_slam_mission_control mission_launch.py]
[Wait 12 seconds]
"Notice the mission progressing through states:
Goal Sent, Goal Accepted, Goal Reached, Mission Completed."
```

**[22:00-29:00] Lab 3 Demonstration**
```
"Lab 3 brings it all together with the aroma diffuser mission.
The mission has multiple states: navigation, diffuser control, and waiting."
[Run: ros2 launch lab03_aroma_diffuser_robot_mission aroma_mission_launch.py]
[Wait 14 seconds]
"The mission is executing the complete sequence:
Start at home, navigate to targets, activate diffuser, and return."
```

**[29:00-30:00] Conclusion**
```
"This completes the demonstration of the ROS 2 Aroma Diffuser Robot project.
All three labs are working correctly, demonstrating ROS 2 concepts,
autonomous navigation, and mission control.

The project is complete and ready for submission."
```

## Hosting on GitHub

To add videos to GitHub:

1. **File Size Limit**:
   - GitHub has 100 MB file size limit for single files
   - Use Git LFS (Large File Storage) for larger videos:
     ```bash
     git lfs install
     git lfs track "*.mp4"
     git add .gitattributes
     git add videos/
     git commit -m "Add demo videos"
     git push
     ```

2. **Alternative Hosting**:
   - YouTube (public or unlisted)
   - Vimeo
   - GitHub Releases (for larger files)
   - Cloud storage with sharing links

3. **Video Links in Documentation**:
   ```markdown
   ### Lab 1 Demo
   [Watch Lab 1 Demo](https://youtube.com/your_link)
   
   Or with GitHub LFS:
   [Lab 1 Demo](videos/02_lab1_ros2_basics.mp4)
   ```

## Notes for Submission

- Videos are optional but highly recommended
- At minimum, provide text-based terminal recordings
- Audio narration makes videos much more effective
- Clear, well-paced videos demonstrate professionalism
- Multiple shorter videos are better than one long video

---

**Recording Status**: To be captured during live testing

**Note**: Videos should be recorded after successful project execution in a proper ROS 2 environment.
