#!/usr/bin/python
# coding:utf-8

"""
@author: Xxwl
@contact: xxwl@duee.cn
@file: jinja2_env.py
@time: 2019/4/16 16:04
"""

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def jinja2_environment(**options):
    """
    可以使用Django模板引擎中的{% url('') %} {% static('') %}这类的语句
    """
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
