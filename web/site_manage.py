#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-16 下午4:04
# @Author  : LXFY
# @Site    : 
# @File    : site_manage.py
# @Software: PyCharm
from flask import request, render_template, flash, redirect, url_for
from ext import db, login_manager

from flask_login import login_required, current_user, login_user, logout_user
from models.forms import SiteListForm, LoginForm, GroupListForm
from models.lists import SiteList, GroupList, User
from libs.links import  get_all_links, get_all_groups
from . import web


@web.route('/site/manage', methods=['GET', 'POST'])
@login_required
def edit_site_list():
    groups = get_all_groups()
    siteform = SiteListForm()
    groupform = GroupListForm()
    if request.method == 'GET':
        all_links = get_all_links()
        grouplists = GroupList.query.all()
        return render_template('manage.html', sitelists=all_links, grouplists=grouplists, siteform=siteform, groupform=groupform, test=groups)
    else:
        if siteform.validate_on_submit():
            newsitelist = SiteList(current_user.id, siteform.title.data, siteform.url.data, siteform.description.data,
                                siteform.group_id.data, siteform.status.data)
            db.session.add(newsitelist)
            db.session.commit()
            flash('New site added!')
        elif groupform.validate_on_submit():
            newgroup = GroupList(groupform.parent_id.data, groupform.name.data)
            db.session.add(newgroup)
            db.session.commit()
            flash('New group added!')
        else:
            flash(siteform.errors)
        return redirect(url_for('web.edit_site_list'))


@web.route('/site/delete/<int:id>')
@login_required
def delete_site(id):
    todolist = SiteList.query.filter_by(id=id).first_or_404()
    db.session.delete(todolist)
    db.session.commit()
    flash('You have delete a site.')
    return redirect(url_for('web.edit_site_list'))


@web.route('/site/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_site(id):
    if request.method == 'GET':
        sitelist = SiteList.query.filter_by(id=id).first_or_404()
        form = SiteListForm()
        form.title.data = sitelist.title
        form.url.data = sitelist.url
        form.description.data = sitelist.description
        form.group_id.data = sitelist.group_id
        form.status.data = str(sitelist.status)
        return render_template('modify.html', form=form)
    else:
        form = SiteListForm()
        if form.validate_on_submit():
            site = SiteList.query.filter_by(id=id).first_or_404()
            site.title = form.title.data
            site.url = form.url.data
            site.description = form.description.data
            site.group_id = form.group_id.data
            site.status = form.status.data
            db.session.commit()
            flash('You have modify a site')
        else:
            flash(form.errors)
        return redirect(url_for('web.edit_site_list'))

# group
@web.route('/group/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_group(id):
    if request.method == 'GET':
        grouplist = GroupList.query.filter_by(id=id).first_or_404()
        form = GroupListForm()
        form.name.data = grouplist.name
        form.parent_id.data = grouplist.parent_id
        return render_template('modify.html', form=form)
    else:
        form = GroupListForm()
        if form.validate_on_submit():
            group = GroupList.query.filter_by(id=id).first_or_404()
            group.name = form.name.data
            group.parent_id = form.parent_id.data
            db.session.commit()
            flash('You have modify a group')
        else:
            flash(form.errors)
        return redirect(url_for('web.edit_site_list'))

