#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from command_server_pkg.srv import ComputeCommand


class CommandServer(Node):
    """Provide the /compute_command service."""

    def __init__(self) -> None:
        super().__init__('command_server')
        self.service = self.create_service(
            ComputeCommand,
            '/compute_command',
            self.handle_compute_command,
        )
        self.get_logger().info('command_server ready on /compute_command')

    def handle_compute_command(self, request: ComputeCommand.Request, response: ComputeCommand.Response):
        response.output = 'HIGH' if request.input > 10.0 else 'LOW'
        self.get_logger().info(
            f'Received input={request.input:.3f}; responding with {response.output}'
        )
        return response


def main(args=None) -> None:
    rclpy.init(args=args)
    node = CommandServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
