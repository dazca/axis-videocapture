#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:57:21 2021

@author: danney
"""

from distutils.core import setup

__version__ = "0.0"

setup(
    name="axispy",
    version=__version__,
    description="Object to use an AXIS Camera as OpenCV's VideoCapture",
    author="Dani Azemar",
    author_email="dani.azemar@gmail.com",
    packages=["axispy"],
    install_requires=["sensecam_control"],
    extras_require={
        'dev': [
            'pytest',
            'python-dotenv'
        ]
    classifiers=[
        "License :: MIT",
        # 'License :: Other/Proprietary License',
        "Programming Language :: Python :: 3.8+",
    ],
)
