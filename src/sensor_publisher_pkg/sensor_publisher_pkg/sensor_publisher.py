import math

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorPublisher(Node):
    """Publish synthetic sensor readings at 10 Hz."""

    def __init__(self) -> None:
        super().__init__('sensor_publisher')
        self.topic_name = '/sensor_value'
        self.publisher_ = self.create_publisher(Float32, self.topic_name, 10)
        self.timer_period = 0.1
        self.start_time = self.get_clock().now()
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.get_logger().info('sensor_publisher started; publishing sine wave data at 10 Hz')

    def timer_callback(self) -> None:
        elapsed = self.get_clock().now() - self.start_time
        elapsed_sec = elapsed.nanoseconds * 1e-9
        msg = Float32()
        msg.data = 10.0 + 5.0 * math.sin(elapsed_sec)
        self.publisher_.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = SensorPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
