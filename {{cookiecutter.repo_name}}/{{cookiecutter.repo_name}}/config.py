#!/usr/bin/env python
# encoding: utf-8

"""
{{cookiecutter.project_name}} config
"""

from ConfigParser import ConfigParser


CONF = ConfigParser()
CONF.read("/etc/{{cookiecutter.project_name}}.ini")
CONF.read("./{{cookiecutter.project_name}}.ini")
