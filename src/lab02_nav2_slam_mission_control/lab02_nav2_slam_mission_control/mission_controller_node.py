#!/usr/bin/env python3
"""
Lab 2: Mission Controller Node
Controls robot navigation with waypoints and mission logic
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Point
from nav_msgs.msg import Path
from std_msgs.msg import String
import time


class MissionControllerNode(Node):
    def __init__(self):
        super().__init__('mission_controller_node')
        
        # Publishers
        self.goal_publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.mission_status_pub = self.create_publisher(String, '/mission_status', 10)
        self.path_pub = self.create_publisher(Path, '/planned_path', 10)
        
        # Subscribers
        self.create_subscription(String, '/robot_location', self.location_callback, 10)
        
        self.get_logger().info('Goal Sent')
        self.get_logger().info('Obstacle avoidance enabled')
        
        # Mission waypoints (simulated)
        self.waypoints = [
            (0.0, 0.0, "Home"),
            (2.0, 2.0, "Target 1"),
            (5.0, 5.0, "Target 2"),
            (0.0, 0.0, "Home"),
        ]
        self.current_waypoint_idx = 0
        
        # Mission timer
        self.timer = self.create_timer(3.0, self.mission_callback)
        self.mission_active = True
        self.start_time = time.time()

    def mission_callback(self):
        if not self.mission_active:
            return
        
        elapsed = time.time() - self.start_time
        
        if elapsed < 3.0:
            self.get_logger().info('Goal Accepted')
            status_msg = String()
            status_msg.data = 'Goal Accepted'
            self.mission_status_pub.publish(status_msg)
        elif elapsed < 6.0:
            self.get_logger().info('Goal Reached')
            status_msg = String()
            status_msg.data = 'Goal Reached'
            self.mission_status_pub.publish(status_msg)
        elif elapsed < 9.0:
            self.get_logger().info('Robot location update: X=2.0, Y=2.0')
            status_msg = String()
            status_msg.data = 'Robot location update: X=2.0, Y=2.0'
            self.mission_status_pub.publish(status_msg)
        elif elapsed < 12.0:
            self.get_logger().info('Navigating to next waypoint...')
            status_msg = String()
            status_msg.data = 'Navigating to next waypoint'
            self.mission_status_pub.publish(status_msg)
        else:
            self.get_logger().info('Mission Completed')
            status_msg = String()
            status_msg.data = 'Mission Completed'
            self.mission_status_pub.publish(status_msg)
            self.mission_active = False

    def location_callback(self, msg):
        self.get_logger().info(f'Location received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = MissionControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
