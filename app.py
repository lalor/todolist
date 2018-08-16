#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user, current_user

from forms import SiteListForm, LoginForm
from ext import db, login_manager
from models import SiteList, User, GroupList

SECRET_KEY = 'This is my key'

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:10ruMYSQL@localhost:3306/flask_navi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/')
def show_navi_page():
    sitelists = SiteList.query.all()
    grouplists = GroupList.query.all()
    return render_template('index.html', sitelists=sitelists, grouplists=grouplists)


@app.route('/manage', methods=['GET', 'POST'])
@login_required
def edit_site_list():
    form = SiteListForm()
    if request.method == 'GET':
        sitelists = SiteList.query.all()
        grouplists = GroupList.query.all()
        return render_template('manage.html', sitelists=sitelists, grouplists=grouplists, form=form)
    else:
        if form.validate_on_submit():
            todolist = SiteList(current_user.id, form.title.data, form.url.data, form.description.data,
                                form.group_id.data, form.status.data)
            db.session.add(todolist)
            db.session.commit()
            flash('New site added!')
        else:
            flash(form.errors)
        return redirect(url_for('edit_site_list'))


@app.route('/delete/<int:id>')
@login_required
def delete_todo_list(id):
    todolist = SiteList.query.filter_by(id=id).first_or_404()
    db.session.delete(todolist)
    db.session.commit()
    flash('You have delete a todo list')
    return redirect(url_for('edit_site_list'))


@app.route('/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_todo_list(id):
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
        return redirect(url_for('edit_site_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash('you have logged in!')
            return redirect(url_for('edit_site_list'))
        else:
            flash('Invalid username or password')
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout!')
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
