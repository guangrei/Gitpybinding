#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='gitbinding',
    version='v1.0.2',
    packages=['gitbinding', ],
    license='MIT',
    author="guangrei",
    author_email="myawn@pm.me",
    description="python binding git command.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="git",
    url="https://github.com/guangrei/Gitpybinding",
)
