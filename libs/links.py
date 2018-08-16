#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午3:53
# @Author  : LXFY
# @Site    : 
# @File    : links.py
# @Software: PyCharm

from flask import current_app
from models import SiteList

def get_links_by_group(group_id=1):
    sitelists = SiteList.query.all()
    print(sitelists)
    pass

get_links_by_group(1)