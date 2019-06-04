import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lambdafunc'))
from version import VERSION

install_requires = ['boto3>=1.9.0']

setup(
    name='lambdafunc',
    version=VERSION,
    url='https://github.com/intellihr/lambdafunc',
    author='intellihr',
    author_email='admin@intellihr.com.au',
    maintainer='intellihr',
    packages=['lambdafunc'],
    install_requires=install_requires,
    description='light weight lambda function runner',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6"
    ])
