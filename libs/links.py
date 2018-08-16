#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午3:53
# @Author  : LXFY
# @Site    : 
# @File    : links.py
# @Software: PyCharm

from flask import current_app
from models.lists import SiteList


def get_links_by_group(self, group_id=1):
    site_in_group = SiteList.query.filter_by(group_id=group_id)
    return site_in_group

def get_all_links():
    all_links = SiteList.query.order_by(SiteList.group_id)
    return all_links

