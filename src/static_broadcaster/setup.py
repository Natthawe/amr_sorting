import os
from glob import glob
from setuptools import find_packages
from setuptools import setup

package_name = 'static_broadcaster'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='natthawe',
    maintainer_email='natthawejumjai@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf_static = static_broadcaster.tf_static:main',
            'moteus_tf_static = static_broadcaster.moteus_tf_static:main'
        ],
    },
)
