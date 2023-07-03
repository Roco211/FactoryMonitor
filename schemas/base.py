# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:35
@Author: Roco
@Project:FactoryMonitor
@Des: 基础数据校验
"""
from pydantic import BaseModel, Field
from typing import Any


class BaseResp(BaseModel):
    code: int
    status: str
    message: str
    data: Any