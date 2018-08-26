#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, URL


class SiteListForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 64)])
    url = StringField('链接', validators=[URL(message="请输入正确的URL格式，http/https开头。")])
    description = StringField('简介', validators=[Optional()], default='简单描述这个网站')
    group_id = IntegerField('组别', validators=[DataRequired()], default='1')
    status = RadioField('显示状态', validators=[DataRequired()], choices=[("1", '上线'), ("0", '下线')], default='1')
    submit = SubmitField('提交')


class GroupListForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(1, 64)])
    parent_id = IntegerField('所属分组', validators=[Optional()], default='')
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('登录')
