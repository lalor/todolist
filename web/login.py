#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午6:08
# @Author  : LXFY
# @Site    : 
# @File    : login.py
# @Software: PyCharm


from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, login_required, logout_user

from models.forms import LoginForm
from models.lists import User
from ext import login_manager
from . import web

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash('Logged in. Welcome!')
            return redirect(url_for('web.index.show_navi_page'))
        else:
            flash('Invalid username or password')
    form = LoginForm()
    return render_template('login.html', form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('web.login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()
