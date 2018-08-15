#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from ext import db
from flask_login import UserMixin


class SiteList(db.Model):
    __tablename__ = 'sitelist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False, default='1')
    title = db.Column(db.String(1024), nullable=False)
    url = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, title, url, description, group_id, status):
        self.user_id = user_id
        self.title = title
        self.url = url
        self.description = description
        self.group_id = group_id
        self.status = status
        self.create_time = time.time()


class GroupList(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(64), nullable=True)

    def __init__(self, id, parent_id, name):
        self.id = id
        self.parent_id = parent_id
        self.name = name


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
