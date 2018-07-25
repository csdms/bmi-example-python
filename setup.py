#! /usr/bin/env python
from setuptools import setup, find_packages


setup(name='bmi-heat',
      version='0.1.0',
      author='Eric Hutton',
      author_email='eric.hutton@colorado.edu',
      description='BMI Python example',
      long_description=open('README.md').read(),
      packages=find_packages(),
)
