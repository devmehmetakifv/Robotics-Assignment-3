# ROS 2 Humble Dockerized Three-Node System

This assignment contains three ROS 2 Python nodes, a launch package, and Docker tooling to build and run everything inside a container.

## Nodes
- `sensor_publisher_pkg`: Publishes synthetic sine-wave data (`std_msgs/msg/Float32`) at 10 Hz on `/sensor_value`.
- `data_processor_pkg`: Subscribes to `/sensor_value`, multiplies each value by `2.0`, and republishes on `/processed_value` (`std_msgs/msg/Float32`).
- `command_server_pkg`: Hosts a custom service `/compute_command` (`command_server_pkg/srv/ComputeCommand`). Responds with `HIGH` if `input > 10`, otherwise `LOW`.

## Launch
The launch file `launch/my_project.launch.py` starts all three nodes. It is installed by the `my_project` package so it can be invoked with:
```
ros2 launch my_project my_project.launch.py
```

## Build & Run (Docker)
1. Build the image:
```
docker build -t myrosapp .
```
2. Run the stack:
```
docker run --rm myrosapp
```
The container entrypoint sources ROS 2, the built workspace, and launches all nodes.

## Verify inside the container
In a second terminal:
```
docker ps               # grab the container ID
docker exec -it <container_id> bash
```
Then run:
```
ros2 topic list
ros2 topic echo /processed_value
ros2 service call /compute_command command_server_pkg/srv/ComputeCommand "input: 12.5"
```
`/processed_value` will show doubled sensor readings, and the service call will return `output: HIGH` when the input is greater than 10.

## Directory layout (key files)
- `Dockerfile`, `entrypoint.sh`
- `launch/my_project.launch.py`
- `src/sensor_publisher_pkg`: sensor publisher node (ament_python)
- `src/data_processor_pkg`: data processor node (ament_python)
- `src/command_server_pkg`: custom service definition + command server node (ament_cmake + python)
- `src/my_project`: launch package exporting the launch file
