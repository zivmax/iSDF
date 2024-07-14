#!/usr/bin/env python

# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup
import subprocess
import datetime

def git_version():
    try:
        # Try to get the version using git describe
        cmd = ['git', 'describe', '--tags', '--always']
        version = subprocess.check_output(cmd, universal_newlines=True).strip()
        
        # If the output starts with a 'v', remove it
        if version.startswith('v'):
            version = version[1:]
        
        # Replace '-' with '.' to make it a valid version string
        version = version.replace('-', '.')
        
        return version
    except subprocess.CalledProcessError:
        # If git command fails, use a date-based version
        now = datetime.datetime.now(datetime.timezone.utc)
        return now.strftime("%Y.%m.%d.%H%M%S")

version = "1.0+" + git_version()

setup(
    name='incSDF',
    version=version,
    author='Joe Ortiz',
    author_email='joeaortiz16@gmail.com',
    py_modules=[]
)
