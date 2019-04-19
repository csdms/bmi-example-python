#! /usr/bin/env python
from setuptools import setup, find_packages

import versioneer


setup(
    name="bmi-heat",
    version=versioneer.get_version(),
    author="Eric Hutton",
    author_email="eric.hutton@colorado.edu",
    description="BMI Python example",
    long_description=open("README.rst").read(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=["bmipy", "pyyaml", "scipy"],
    packages=find_packages(),
    cmdclass=versioneer.get_cmdclass(),
)


