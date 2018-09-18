from setuptools import setup
import os

setup(
    name='myEmail',
    version='1.1',
    packages=['myEmail']
)

os.system('rm -rf dist build myEmail.egg-info')

