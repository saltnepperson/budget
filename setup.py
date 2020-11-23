import ast
import re

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    INSTALL_REQUIRED = f.read().splitlines()

setup(
    name='budget',
    version='0.0.1',
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    data_files=[('config', [
        'config/local-config.py',
        'config/docker-config.py',
        'config/test-config.py'
    ])],
    zip_safe=False,
    install_requires=INSTALL_REQUIRED,
    include_package_data=True,
    extras_require={
        'tests': [
            'pytest==3.4.2'
        ]
    }
)