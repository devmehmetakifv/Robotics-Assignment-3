cmake_minimum_required(VERSION 3.5)
project(command_server_pkg)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/ComputeCommand.srv"
)

ament_python_install_package(command_server_app)

install(PROGRAMS
  scripts/command_server
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

install(DIRECTORY srv
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
