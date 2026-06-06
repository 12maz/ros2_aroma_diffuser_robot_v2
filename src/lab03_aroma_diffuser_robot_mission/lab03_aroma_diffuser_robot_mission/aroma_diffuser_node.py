#!/usr/bin/env python3
"""
Lab 3: Aroma Diffuser Node
Controls diffuser on/off state
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import time


class AromaDiffuserNode(Node):
    def __init__(self):
        super().__init__('aroma_diffuser_node')
        
        # Publishers
        self.diffuser_state_pub = self.create_publisher(String, '/aroma/diffuser_state', 10)
        
        # Subscribers
        self.create_subscription(
            String, '/aroma/diffuser_command', self.diffuser_command_callback, 10)
        
        self.diffuser_on = False
        self.get_logger().info('Aroma Diffuser Node started')

    def diffuser_command_callback(self, msg):
        """Handle diffuser commands"""
        command = msg.data.strip().upper()
        
        if command == 'ON':
            self.diffuser_on = True
            self.get_logger().info('Diffuser ON')
            state_msg = String()
            state_msg.data = 'Diffuser: ON'
            self.diffuser_state_pub.publish(state_msg)
        elif command == 'OFF':
            self.diffuser_on = False
            self.get_logger().info('Diffuser OFF')
            state_msg = String()
            state_msg.data = 'Diffuser: OFF'
            self.diffuser_state_pub.publish(state_msg)


def main(args=None):
    rclpy.init(args=args)
    node = AromaDiffuserNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
