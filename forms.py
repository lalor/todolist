#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Optional


class TodoListForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 64)])
    url = StringField('链接', validators=[DataRequired()])
    description = StringField('简介', validators=[Optional()], default='A good website.')
    group_id = IntegerField('组别', validators=[DataRequired()], default='1')
    status = RadioField('是否完成', validators=[DataRequired()],  choices=[("1", '是'),("0",'否')])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('登录')
