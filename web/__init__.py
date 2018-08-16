#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午4:03
# @Author  : LXFY
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

web = Blueprint('web', __name__)

from web import manage