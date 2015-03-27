#!/usr/bin/env python
# coding=utf-8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from setuptools import find_packages


def requirements_file_to_list(fn="requirements.txt"):
    with open(fn, 'rb') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=open('README.md').read(),
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(),
    install_requires=requirements_file_to_list(),
    license='GPLv2+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 or later',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
