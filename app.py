#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

import pymysql
from flask import Flask, render_template, g

SECRET_KEY = 'This is my key'

app = Flask(__name__)
app.secret_key = SECRET_KEY


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


@app.route('/')
def show_todo_list():
    sql = 'select id, user_id, title, status, create_time from todolist'
    with g.db as cur:
        cur.execute(sql)
        todo_list = [ dict(id=row[0], user_id=row[1], title=row[2], status=bool(row[3]), create_time=row[4]) for row in cur.fetchall()]
    return render_template('index.html', todo_list=todo_list)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
