# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 配置
"""

from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)


settings = Config()