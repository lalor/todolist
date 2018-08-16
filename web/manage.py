#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午4:04
# @Author  : LXFY
# @Site    : 
# @File    : manage.py
# @Software: PyCharm
from flask import request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from ext import db, login_manager

from models.forms import SiteListForm, LoginForm
from models.lists import SiteList, GroupList, User
from libs.links import get_links_by_group, get_all_links
from . import web




@web.route('/manage', methods=['GET', 'POST'])
@login_required
def edit_site_list():
    form = SiteListForm()
    if request.method == 'GET':
        all_links = get_all_links()
        grouplists = GroupList.query.all()
        return render_template('manage.html', sitelists=all_links, grouplists=grouplists, form=form)
    else:
        if form.validate_on_submit():
            todolist = SiteList(current_user.id, form.title.data, form.url.data, form.description.data,
                                form.group_id.data, form.status.data)
            db.session.add(todolist)
            db.session.commit()
            flash('New site added!')
        else:
            flash(form.errors)
        return redirect(url_for('web.edit_site_list'))


@web.route('/')
def show_navi_page():
    sitelists = SiteList.query.all()
    grouplists = GroupList.query.all()
    return render_template('index.html', sitelists=sitelists, grouplists=grouplists)


@web.route('/delete/<int:id>')
@login_required
def delete_site(id):
    todolist = SiteList.query.filter_by(id=id).first_or_404()
    db.session.delete(todolist)
    db.session.commit()
    flash('You have delete a todo list')
    return redirect(url_for('web.edit_site_list'))


@web.route('/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_site(id):
    if request.method == 'GET':
        todolist = SiteList.query.filter_by(id=id).first_or_404()
        form = SiteListForm()
        form.title.data = todolist.title
        form.status.data = str(todolist.status)
        return render_template('modify.html', form=form)
    else:
        form = SiteListForm()
        if form.validate_on_submit():
            todolist = SiteList.query.filter_by(id=id).first_or_404()
            todolist.title = form.title.data
            todolist.status = form.status.data
            db.session.commit()
            flash('You have modify a todolist')
        else:
            flash(form.errors)
        return redirect(url_for('web.edit_site_list'))


@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash('Logged in. Welcome!')
            return redirect(url_for('web.edit_site_list'))
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
