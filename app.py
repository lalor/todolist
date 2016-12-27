#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

import time

import pymysql
from flask import (Flask, render_template, g, session, redirect, url_for,
                request, flash)
from flask_bootstrap import Bootstrap

SECRET_KEY = 'This is my key'

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'admin'


def connect_db():
    """Returns a new connection to the database."""
    return pymysql.connect(host='127.0.0.1',
            user='laimingxing',
            passwd='laimingxing',
            db='test',
            charset='utf8')


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.after_request
def after_request(response):
    """Closes the database again at the end of the request."""
    g.db.close()
    return response


@app.route('/', methods=['GET', 'POST'])
def show_todo_list():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'GET':
        sql = 'select id, user_id, title, status, create_time from todolist'
        with g.db as cur:
            cur.execute(sql)
            todo_list = [ dict(id=row[0], user_id=row[1], title=row[2], status=bool(row[3]), create_time=row[4]) for row in cur.fetchall()]
        return render_template('index.html', todo_list=todo_list)
    else:
        title = request.form['title']
        status = request.form['status']
        with g.db as cur:
            sql = """insert into todolist(`user_id`, `title`, `status`,
            `create_time`) values ({0}, '{1}', {2}, {3})""".format( 1, title, status, int(time.time()))
            app.logger.info(sql)
            cur.execute(sql)
        flash('You have add a new todo list')
        return redirect(url_for('show_todo_list'))


@app.route('/delete')
def delete_todo_list():
    id = request.args.get('id', None)
    if id is None:
        abort(404)
    else:
        sql = "delete from todolist where id = {0}".format(id)
        with g.db as cur:
            cur.execute(sql)
        flash('You have delete a todo list')
        return redirect(url_for('show_todo_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('Invalid username')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Invalid password')
        else:
            session['logged_in'] = True
            flash('you have logged in!')
            return redirect(url_for('show_todo_list'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you have logout!')
    return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
