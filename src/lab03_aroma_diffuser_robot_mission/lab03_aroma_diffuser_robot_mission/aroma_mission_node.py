#!/usr/bin/env python3
"""
Lab 3: Aroma Mission Node
Orchestrates the complete aroma diffuser mission
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class AromaMissionNode(Node):
    def __init__(self):
        super().__init__('aroma_mission_node')
        
        # Publishers
        self.diffuser_cmd_pub = self.create_publisher(String, '/aroma/diffuser_command', 10)
        self.mission_status_pub = self.create_publisher(String, '/aroma/mission_status', 10)
        
        self.get_logger().info('Starting Mission')
        
        # Mission state
        self.mission_step = 0
        self.step_start_time = time.time()
        self.mission_complete = False
        
        # Mission timer
        self.timer = self.create_timer(1.0, self.mission_timer_callback)

    def publish_status(self, status_text):
        """Publish mission status"""
        msg = String()
        msg.data = status_text
        self.mission_status_pub.publish(msg)
        self.get_logger().info(status_text)

    def publish_diffuser_command(self, command):
        """Send diffuser command"""
        msg = String()
        msg.data = command
        self.diffuser_cmd_pub.publish(msg)

    def mission_timer_callback(self):
        """Execute mission steps"""
        if self.mission_complete:
            return
        
        elapsed = time.time() - self.step_start_time
        
        if self.mission_step == 0:
            # Start at home
            self.publish_status('At Home - Mission initialized')
            self.mission_step = 1
            self.step_start_time = time.time()
        
        elif self.mission_step == 1:
            if elapsed < 2:
                self.publish_status('Navigating to Target 1')
            else:
                self.publish_status('Goal Reached - Target 1')
                self.mission_step = 2
                self.step_start_time = time.time()
        
        elif self.mission_step == 2:
            if elapsed < 1:
                self.publish_diffuser_command('ON')
                self.publish_status('Diffuser ON')
            else:
                self.mission_step = 3
                self.step_start_time = time.time()
        
        elif self.mission_step == 3:
            if elapsed < 2:
                self.publish_status('Waiting - Diffuser active')
            else:
                self.publish_status('Diffuser OFF')
                self.publish_diffuser_command('OFF')
                self.mission_step = 4
                self.step_start_time = time.time()
        
        elif self.mission_step == 4:
            if elapsed < 2:
                self.publish_status('Navigating to Target 2')
            else:
                self.publish_status('Goal Reached - Target 2')
                self.mission_step = 5
                self.step_start_time = time.time()
        
        elif self.mission_step == 5:
            if elapsed < 1:
                self.publish_diffuser_command('ON')
                self.publish_status('Diffuser ON')
            else:
                self.mission_step = 6
                self.step_start_time = time.time()
        
        elif self.mission_step == 6:
            if elapsed < 2:
                self.publish_status('Waiting - Diffuser active')
            else:
                self.publish_status('Diffuser OFF')
                self.publish_diffuser_command('OFF')
                self.mission_step = 7
                self.step_start_time = time.time()
        
        elif self.mission_step == 7:
            if elapsed < 2:
                self.publish_status('Navigating back to Home')
            else:
                self.publish_status('Mission Completed - Robot at Home')
                self.mission_complete = True


def main(args=None):
    rclpy.init(args=args)
    node = AromaMissionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
