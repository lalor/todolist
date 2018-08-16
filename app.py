#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user, current_user

from forms import SiteListForm, LoginForm
from ext import db, login_manager
from models import SiteList, User, GroupList
from . import create_app


app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
