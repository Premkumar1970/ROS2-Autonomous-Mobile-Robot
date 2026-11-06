# ROS 2 Autonomous Mobile Robot with SLAM and Navigation2

## Project Overview

Developed an autonomous mobile robot using ROS 2 Jazzy and Gazebo Sim 8, capable of mapping unknown environments, localizing itself, navigating autonomously, and avoiding obstacles in real time.

The robot uses a LiDAR sensor to perceive its surroundings and generate environmental maps using SLAM Toolbox. With Navigation2 (Nav2), the robot can plan paths, navigate to designated destinations, and dynamically adjust its movement when obstacles are detected.

The system also supports multi-waypoint navigation, allowing the robot to autonomously travel through multiple predefined destinations in sequence without requiring manual control at every location.

## Key Features

- **Autonomous Navigation:** Navigate to selected destinations using ROS 2 Navigation2.
- **SLAM Mapping:** Generate 2D occupancy grid maps of the environment using SLAM Toolbox.
- **Robot Localization:** Estimate the robot's position and orientation within the mapped environment using AMCL.
- **Real-Time Obstacle Avoidance:** Detect obstacles using LiDAR and adjust navigation paths accordingly.
- **Path Planning:** Generate and execute navigation paths using Nav2 planners and controllers.
- **Waypoint Following:** Navigate through multiple predefined destinations sequentially.
- **Simulation Visualization:** Monitor robot movement, sensor data, localization, and navigation paths using RViz2 and Gazebo.

## Technologies Used

- ROS 2 Jazzy
- Gazebo Sim 8
- Navigation2 (Nav2)
- SLAM Toolbox
- AMCL
- Python
- URDF / Xacro
- RViz2
- LiDAR
- ROS 2 Control

## System Workflow

1. Robot modelling and simulation environment setup.
2. LiDAR-based environment perception.
3. Environment mapping using SLAM Toolbox.
4. Map saving and robot localization using AMCL.
5. Navigation configuration using Nav2.
6. Global and local path planning.
7. Real-time obstacle detection and avoidance.
8. Autonomous multi-waypoint navigation.

## Project Learning Outcomes

Through this project, I gained practical experience in ROS 2 architecture, robot modelling, sensor integration, TF transformations, odometry, SLAM, localization, Nav2 configuration, path planning, and autonomous navigation.

I also developed debugging and problem-solving skills while integrating multiple ROS 2 components into a complete autonomous mobile robotics system.

## Future Improvements

- Implementation on a physical mobile robot.
- Integration of additional sensors.
- Advanced autonomous exploration.
- Multi-robot coordination.
- Real-world navigation testing.
