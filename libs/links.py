#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午3:53
# @Author  : LXFY
# @Site    : 
# @File    : links.py
# @Software: PyCharm

from flask import current_app
from models.lists import SiteList, GroupList
from ext import db


def get_all_links():
    all_links = SiteList.query.order_by(SiteList.group_id)
    return all_links


def get_all_groups():
    # all_groups = GroupList.query(id, name)
    all_groups = GroupList.query.with_entities(GroupList.id, GroupList.name).all()
    return all_groups
