# -*- coding:utf-8 -*-
"""
@Time : 2023/06/25 19:13
@Author: Roco
@Project:FactoryMonitor
@Des: 描述
"""

from tortoise import Model, fields


class DeviceAlert(Model):
    hostname = fields.CharField(max_length=80)
    alert_code = fields.CharField(max_length=4)
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    event_code = fields.CharField(max_length=4)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table_description = "设备报警表"
        table = "device_alerts"
