# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: Fastapp实例化
"""
from fastapi import FastAPI
from api import router


def create_app():
    _app = FastAPI()
    _app.include_router(router)
    return _app


app = create_app()