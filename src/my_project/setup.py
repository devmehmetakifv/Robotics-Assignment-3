import os
from setuptools import setup

package_name = 'my_project'
here = os.path.abspath(os.path.dirname(__file__))
launch_file_abs = os.path.join(here, '..', '..', 'launch', 'my_project.launch.py')
launch_file_rel = os.path.relpath(launch_file_abs, here)

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), [launch_file_rel]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mehmet Akif Vardar',
    maintainer_email='maintainer@example.com',
    description='Launch file holder for the assignment nodes.',
    license='Apache License 2.0',
    tests_require=['pytest'],
)
