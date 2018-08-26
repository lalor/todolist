#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午4:03
# @Author  : LXFY
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

web = Blueprint('web', __name__)

from web import site_manage
from web import index
from web import group_manage
from web import login