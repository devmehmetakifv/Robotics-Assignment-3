from setuptools import setup

package_name = 'data_processor_pkg'

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
    description='Subscribe to /sensor_value and publish processed data to /processed_value.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'data_processor = data_processor_pkg.data_processor:main',
        ],
    },
)
