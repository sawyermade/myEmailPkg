from setuptools import setup
import os

setup(
    name='myEmail',
    version='1.0',
    packages=['myEmail']
)

os.system('rm -rf dist build myEmail.egg-info')

