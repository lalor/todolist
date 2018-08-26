#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午4:50
# @Author  : LXFY
# @Site    : 
# @File    : index.py
# @Software: PyCharm
from flask import render_template

from models.lists import SiteList, GroupList
from . import web


@web.route('/')
def show_navi_page():
    sitelists = SiteList.query.all()
    grouplists = GroupList.query.all()
    return render_template('index.html', sitelists=sitelists, grouplists=grouplists)