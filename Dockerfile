FROM ros:humble-ros-base

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

# Install colcon for building the workspace
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-colcon-common-extensions build-essential python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ws

# Copy source and supporting files into the workspace
COPY src src
COPY launch launch
COPY entrypoint.sh /entrypoint.sh
COPY README.md README.md
COPY SSF_HASH.txt SSF_HASH.txt

RUN chmod +x /entrypoint.sh

# Build the workspace
RUN source /opt/ros/humble/setup.bash && colcon build

# Auto-source ROS and workspace setup for interactive shells
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc \\
    && echo "source /ws/install/setup.bash" >> /root/.bashrc

ENTRYPOINT ["/entrypoint.sh"]
