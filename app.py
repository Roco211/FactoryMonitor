# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: Fastapp实例化
"""
from fastapi import FastAPI
from api import router
from config import settings
from database.mysql import register_mysql
from event import startup

app = FastAPI()


# 事件监听
app.add_event_handler("startup", startup(app))

