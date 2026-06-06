#!/usr/bin/env python3
"""
Lab 1: Subscriber Node
Subscribes to /aroma_robot/status topic
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String, '/aroma_robot/status', self.listener_callback, 10)
        self.subscription  # Prevent unused variable warning
        self.get_logger().info('Subscriber started')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: {msg.data}')
        self.get_logger().info('Communication successful')


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
