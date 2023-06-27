# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:11
@Author: Roco
@Project:app
@Des: 描述
"""

from pydantic import BaseModel, Field


class DeviceAlert(BaseModel):
    """
    设备报警模型校验
    """
    hostname: str = Field(max_length=32)
    model: str = Field(max_length=8)
    station: str = Field(max_length=8)
    alert_code: str = Field(max_length=8)
    start_time: str
    end_time: str
    total_time: int
