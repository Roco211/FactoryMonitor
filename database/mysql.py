# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:09
@Author: Roco
@Project:app
@Des: mysql数据库配置
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os

# -----------------------数据库配置-----------------------------------
DB_ORM_CONFIG = {
    "connections": {  # 连接配置池
        "base": {   # 名为base的连接
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('MYSQL_BASE_HOST', '127.0.0.1'),
                'user': os.getenv('MYSQL_BASE_USER', 'root'),
                'password': os.getenv('MYSQL_BASE_PSW', '12345678'),
                'port': int(os.getenv('MYSQL_BASE_PORT', 3306)),
                'database': os.getenv('MYSQL_BASE_DB', 'test'),
            }
        },
    },
    "apps": {
        "base": {  # 名为base的tortoise应用
                "models": ["models.user"],  # 指定注册的模型为modes.base
                "default_connection": "base"  # 默认使用的连接配置，上述connections的base
                },
    },
    'use_tz': False,  # 指定是否使用时区
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,  # 通过依赖注入的app对象
        config=DB_ORM_CONFIG,  # orm配置
        generate_schemas=True,  # 是否生成表
        add_exception_handlers=False,  # 是否添加异常处理类
    )
