from setuptools import setup

ros_package_name = 'command_server_pkg'
python_package_name = 'command_server_app'

setup(
    name=ros_package_name,
    version='0.0.0',
    packages=[python_package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + ros_package_name]),
        ('share/' + ros_package_name, ['package.xml']),
        ('share/' + ros_package_name + '/srv', ['srv/ComputeCommand.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mehmet Akif Vardar',
    maintainer_email='maintainer@example.com',
    description='Service server that returns HIGH/LOW based on an input threshold.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'command_server = command_server_app.command_server:main',
        ],
    },
)
