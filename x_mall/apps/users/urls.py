#!/usr/bin/python
# coding:utf-8

"""
@author: Xxwl
@contact: xxwl@duee.cn
@file: urls.py
@time: 2019/4/16 17:39
"""
from . import views
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register')
]
