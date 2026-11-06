from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    GroupAction,
)
from launch_ros.actions import SetRemap
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Package locations
    nav2_bringup_dir = FindPackageShare('nav2_bringup')
    robot_package_dir = FindPackageShare('my_fbot_package')

    # Launch arguments
    map_file = LaunchConfiguration('map')
    params_file = LaunchConfiguration('params_file')
    use_sim_time = LaunchConfiguration('use_sim_time')
    autostart = LaunchConfiguration('autostart')

    # Load the saved map and start AMCL
    localization_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                nav2_bringup_dir,
                'launch',
                'localization_launch.py'
            ])
        ),
        launch_arguments={
            'map': map_file,
            'params_file': params_file,
            'use_sim_time': use_sim_time,
            'autostart': autostart
        }.items()
    )

    # Start Nav2 navigation servers
    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                robot_package_dir,
                'launch',
                'navigation_core.launch.py'
            ])
        ),
        launch_arguments={
            'params_file': params_file,
            'use_sim_time': use_sim_time,
            'autostart': autostart
        }.items()
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'map',
            default_value='/home/prem/fbot_ws/maps/warehouse_map.yaml'
        ),

        DeclareLaunchArgument(
            'params_file',
            default_value=PathJoinSubstitution([
                robot_package_dir,
                'config',
                'nav2',
                'nav2_params.yaml'
            ])
        ),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true'
        ),

        DeclareLaunchArgument(
            'autostart',
            default_value='true'
        ),

        # Connect Nav2 velocity output to your robot controller
        GroupAction([
            SetRemap(
                src='odom',
                dst='/diff_cont/odom'
            ),

            localization_launch,
            navigation_launch
        ])
    ])
