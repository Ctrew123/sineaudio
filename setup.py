from setuptools import find_packages, setup

setup(
    name='sineaudio',
    packages=find_packages(include=['sineaudio', 'setuptools']),
    version='0.1.0',
    description='sineaudio software package',
    author='Matthew Squire, Cameron Trew, Luke Sargent, Aron Russell',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'setuptools'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)