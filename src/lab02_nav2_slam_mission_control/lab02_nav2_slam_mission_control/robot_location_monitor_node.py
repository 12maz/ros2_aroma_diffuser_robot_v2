#!/usr/bin/env python3
"""
Lab 2: Robot Location Monitor Node
Monitors and publishes robot location from TF
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math
import time


class RobotLocationMonitorNode(Node):
    def __init__(self):
        super().__init__('robot_location_monitor_node')
        
        self.location_pub = self.create_publisher(String, '/robot_location', 10)
        self.get_logger().info('Robot location monitor started')
        
        # Simulated robot location
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.time_offset = time.time()
        
        # Update timer
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Simulate robot movement (circular pattern)
        elapsed = time.time() - self.time_offset
        radius = 2.0
        self.x = radius * math.cos(elapsed * 0.5)
        self.y = radius * math.sin(elapsed * 0.5)
        self.theta = elapsed * 0.5
        
        # Publish location
        location_msg = String()
        location_msg.data = f'Robot at X={self.x:.2f}, Y={self.y:.2f}, Theta={self.theta:.2f}'
        self.location_pub.publish(location_msg)
        self.get_logger().info(f'Robot location update: {location_msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = RobotLocationMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
