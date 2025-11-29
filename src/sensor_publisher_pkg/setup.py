from setuptools import setup

package_name = 'sensor_publisher_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mehmet Akif Vardar',
    maintainer_email='maintainer@example.com',
    description='Publisher node emitting synthetic sensor data.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = sensor_publisher_pkg.sensor_publisher:main',
        ],
    },
)
