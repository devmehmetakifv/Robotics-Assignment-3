import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DataProcessor(Node):
    """Process incoming sensor data and publish results."""

    def __init__(self) -> None:
        super().__init__('data_processor')
        self.input_topic = '/sensor_value'
        self.output_topic = '/processed_value'
        self.subscription = self.create_subscription(
            Float32,
            self.input_topic,
            self.listener_callback,
            10,
        )
        self.publisher_ = self.create_publisher(Float32, self.output_topic, 10)
        self.processed_count = 0
        self.get_logger().info('data_processor started; applying gain of 2.0 to sensor values')

    def listener_callback(self, msg: Float32) -> None:
        processed_value = msg.data * 2.0
        self.publisher_.publish(Float32(data=processed_value))
        self.processed_count += 1
        if self.processed_count % 20 == 0:
            self.get_logger().info(
                f'Processed #{self.processed_count}: input={msg.data:.3f}, output={processed_value:.3f}'
            )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = DataProcessor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
