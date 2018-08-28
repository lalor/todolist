#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午4:03
# @Author  : LXFY
# @Site    :
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from flask_bootstrap import Bootstrap
from ext import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object('secure')
    app.config.from_object('settings')
    register_blueprint(app)
    bootstrap = Bootstrap(app)

    db.init_app(app)
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

    login_manager.login_view='web.login'
    login_manager.login_message='请先登录'
    login_manager.init_app(app)
    return app

def register_blueprint(app):
    from web import web
    # from libs import libs
    # app.register_blueprint(libs)
    app.register_blueprint(web)

