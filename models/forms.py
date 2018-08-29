#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Optional, URL

from app import create_app
from libs.links import get_all_groups
from ext import db
from models.lists import GroupList

# TODO fix all_groups in libs.links
create_app().app_context().push()


class SiteListForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 64)])
    url = StringField('链接', validators=[URL(message="请输入正确的URL格式，http/https开头。")])
    description = StringField('简介', validators=[Optional()])
    group_id = SelectField('组别', validators=[DataRequired()],  coerce=int)
    status = RadioField('显示状态', validators=[DataRequired()], choices=[("1", '上线'), ("0", '下线')], default='1')
    submit = SubmitField('提交')

    def __init__(self, *args, **kwargs):
        super(SiteListForm, self).__init__(*args, **kwargs)
        self.group_id.choices =all_groups = GroupList.query.with_entities(GroupList.id, GroupList.name).all()


class GroupListForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired(), Length(1, 64)])
    parent_id = IntegerField('所属分组', validators=[Optional()], default='')
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('登录')
