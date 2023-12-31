from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/front/pointcloud2_xyzi'),
                        ('scan', '/front/scan')],
            parameters=[{
                'target_frame': 'front_laser',
                'transform_tolerance': 0.01,
                'min_height': -0.18,
                'max_height': 0.3,
                'angle_min': -0.7679448709, #-90 =-1.5708, #43.5 = -0.75921822462, # -M_PI/2
                'angle_max': 0.7679448709,  # 90 = 1.5708, #43.5 = -0.75921822462, # M_PI/2
                'angle_increment': 0.0087, #0.01745329238474369,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.5,
                'range_max': 3.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    ])