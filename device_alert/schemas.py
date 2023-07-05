# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:11
@Author: Roco
@Project:app
@Des: 描述
"""

from pydantic import BaseModel, Field
from typing import Optional


class DeviceAlert(BaseModel):
    """
    设备报警模型校验
    """
    hostname: str = Field(max_length=32, description="主机名")
    model: str = Field(max_length=32, description="机种名")
    station: str = Field(max_length=32, description="站别名")
    line: str = Field(max_length=32, description="线别")
    category: str = Field(max_length=32, description="报警分类")
    shift: str = Field(max_length=32, description="班别")
    alert_code: str = Field(max_length=32, description="报警代码")
    alert_desc: str = Field(max_length=255, description="报警描述")
    start_time: str = Field(max_length=32, description="报警开始时间")
    end_time: str = Field(max_length=32, description="报警结束时间")
    time_difference: int = Field(description="报警持续时间")


class DeviceAlertUpdate(DeviceAlert):
    """
    设备报警信息Patch校验模型
    """
    hostname: Optional[str] = Field(max_length=32, description="主机名")
    category: Optional[str] = Field(max_length=32, description="报警分类")
    shift: Optional[str] = Field(max_length=32, description="班别")
    alert_desc: Optional[str] = Field(max_length=255, description="报警描述")
    end_time: Optional[str] = Field(max_length=32, description="报警结束时间")
    time_difference: Optional[str] = Field(description="报警持续时间")
