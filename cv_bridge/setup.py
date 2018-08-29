#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
import sys

d = generate_distutils_setup()

d['packages'] = ['cv_bridge']
if sys.platform != 'win32':
  d['package_dir'] = {'' : 'python/'}
else:
  d['package_dir'] = {'' : 'python'}

setup(**d)
