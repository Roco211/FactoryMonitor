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
    hostname: str = Field(max_length=16)
    model: str
    station: str
    line: str
    category: str
    shift: str
    alert_code: str
    alert_desc: str
    start_time: str
    end_time: str
    time_difference: int
    shift: str
    category: str
