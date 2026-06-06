#!/usr/bin/env python3
"""
Lab 1: Publisher Node
Publishes status messages to /aroma_robot/status topic
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, '/aroma_robot/status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.counter = 0
        self.get_logger().info('Publisher started')

    def timer_callback(self):
        self.counter += 1
        msg = String()
        msg.data = f'Publishing message: Robot Status #{self.counter} - System OK'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing message: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
