# Lab 1: ROS 2 Basics - Publisher and Subscriber

## Lab Objectives

1. Understand ROS 2 node creation using rclpy
2. Implement publisher nodes
3. Implement subscriber nodes
4. Establish topic-based communication
5. Create and use launch files
6. Monitor topics using command-line tools

## Architecture

```
Publisher Node (publisher_node)
         |
         | publishes
         v
    Topic: /aroma_robot/status
         |
         | subscribes
         v
Subscriber Node (subscriber_node)
```

## Key Components

### Publisher Node
- Creates a ROS 2 node named "publisher_node"
- Creates a publisher on `/aroma_robot/status` topic
- Publishes String messages every 1 second
- Logs messages to console

### Subscriber Node
- Creates a ROS 2 node named "subscriber_node"
- Subscribes to `/aroma_robot/status` topic
- Receives and logs messages
- Demonstrates message handling

### Launch File
- Launches both publisher and subscriber nodes
- Configures output to screen
- Allows single command execution of both nodes

## Topics Used

- **Topic Name**: `/aroma_robot/status`
- **Message Type**: `std_msgs/String`
- **Publishing Rate**: 1 Hz (every 1 second)
- **Data Format**: String with robot status information

## Expected Output

```
[publisher_node]: Publisher started
[publisher_node]: Publishing message: Robot Status #1 - System OK
[publisher_node]: Publishing message: Robot Status #2 - System OK
[publisher_node]: Publishing message: Robot Status #3 - System OK
...

[subscriber_node]: Subscriber started
[subscriber_node]: Received message: Publishing message: Robot Status #1 - System OK
[subscriber_node]: Communication successful
[subscriber_node]: Received message: Publishing message: Robot Status #2 - System OK
[subscriber_node]: Communication successful
...
```

## Learning Outcomes

### ROS 2 Concepts
- Node lifecycle (create, spin, destroy)
- Publishers and Subscribers
- Topics and message types
- Launch files and node orchestration
- ROS 2 logging and debugging
- Timer callbacks for periodic tasks
- Subscription callbacks for receiving messages

### Python Patterns
- Object-oriented node design
- Timer-based callbacks
- Graceful shutdown handling
- Exception handling

### Troubleshooting Skills
- Topic monitoring with `ros2 topic`
- Message inspection with `ros2 topic echo`
- Node introspection with `ros2 node`
- Log level configuration

## Files

- `lab01_ros2_basics/publisher_node.py` - Publisher implementation
- `lab01_ros2_basics/subscriber_node.py` - Subscriber implementation
- `launch/basics_launch.py` - Launch file
- `package.xml` - Package metadata
- `setup.py` - Python package setup
- `setup.cfg` - Build configuration

## Execution

### Method 1: Launch File (Recommended)
```bash
ros2 launch lab01_ros2_basics basics_launch.py
```

### Method 2: Individual Nodes
```bash
# Terminal 1
ros2 run lab01_ros2_basics publisher_node

# Terminal 2
ros2 run lab01_ros2_basics subscriber_node
```

### Method 3: With Topic Monitoring
```bash
# Terminal 1
ros2 run lab01_ros2_basics publisher_node

# Terminal 2
ros2 topic echo /aroma_robot/status

# Terminal 3
ros2 topic list
ros2 topic info /aroma_robot/status
```

## Understanding the Code

### Publisher Node Highlights
```python
# Create a ROS 2 node
class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        
        # Create a publisher
        self.publisher_ = self.create_publisher(
            String, '/aroma_robot/status', 10)
        
        # Create a timer for periodic publishing
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.counter = 0
    
    def timer_callback(self):
        # Create and publish a message
        msg = String()
        msg.data = f'Publishing message: Robot Status #{self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.counter += 1
```

### Subscriber Node Highlights
```python
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        
        # Create a subscription
        self.subscription = self.create_subscription(
            String, '/aroma_robot/status', 
            self.listener_callback, 10)
    
    def listener_callback(self, msg):
        # Handle received message
        self.get_logger().info(f'Received: {msg.data}')
        self.get_logger().info('Communication successful')
```

## Quality Checks

✅ Nodes create successfully
✅ Publisher publishes messages
✅ Subscriber receives messages
✅ Messages appear in logs
✅ Topic echo shows data
✅ Launch file starts both nodes
✅ Nodes shutdown gracefully
✅ No errors or warnings

## Extensions

### Possible Modifications
1. Change publishing rate (modify timer interval)
2. Change message content or format
3. Add multiple publishers on different topics
4. Add message filtering in subscriber
5. Add timestamp to messages
6. Add counters and statistics

### Advanced Topics
- Quality of Service (QoS) settings
- Message serialization
- Topic remapping
- Node composition
- Message filters
- Multi-node synchronization

## Integration with Other Labs

This lab provides the foundation for:
- Lab 2: Mission status communication
- Lab 3: Diffuser command and state topics

All subsequent labs use the pub/sub pattern demonstrated here.

---

**Lab 1 Duration**: 30 minutes
**Difficulty**: Beginner
**Prerequisites**: Basic Python, basic ROS 2 knowledge
