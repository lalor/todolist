#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午3:52
# @Author  : LXFY
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint

libs = Blueprint('libs', __name__)

from libs import links