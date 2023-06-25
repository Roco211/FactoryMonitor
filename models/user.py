# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:11
@Author: Roco
@Project:app
@Des: user模型
"""

from tortoise import Model, fields


class User(Model):
    username = fields.CharField(max_length=16)
    password = fields.CharField(max_length=16)

    class Meta:
        table_description = "用户表"
        table = "users"
