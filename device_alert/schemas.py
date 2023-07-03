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
    hostname: str = Field(max_length=16, description="主机名")
    model: str = Field(max_length=16, description="机种名")
    station: str = Field(max_length=16, description="站别名")
    line: str = Field(max_length=16, description="线别")
    category: str = Field(max_length=16, description="报警分类")
    shift: str = Field(max_length=16, description="班别")
    alert_code: str = Field(max_length=16, description="报警代码")
    alert_desc: str = Field(max_length=16, description="报警描述")
    start_time: str = Field(max_length=16, description="报警开始时间")
    end_time: str = Field(max_length=16, description="报警结束时间")
    time_difference: int = Field(description="报警持续时间")
