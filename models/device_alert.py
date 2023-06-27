# -*- coding:utf-8 -*-
"""
@Time : 2023/06/25 19:13
@Author: Roco
@Project:FactoryMonitor
@Des: 描述
"""

from tortoise import Model, fields


class DeviceAlert(Model):
    hostname = fields.CharField(max_length=64)  # 电脑名
    ip = fields.CharField(max_length=16)  # ip地址
    model = fields.CharField(max_length=16)
    station = fields.CharField(max_length=16)
    alert_code = fields.CharField(max_length=8)  # 报警代码
    start_time = fields.DatetimeField()  # 报警开始时间
    end_time = fields.DatetimeField()  # 报警结束时间
    total_time = fields.IntField()  # 时间差
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table_description = "设备报警表"
        table = "device_alerts"
