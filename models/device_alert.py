# -*- coding:utf-8 -*-
"""
@Time : 2023/06/25 19:13
@Author: Roco
@Project:FactoryMonitor
@Des: 描述
"""

from tortoise import Model, fields


class DeviceAlert(Model):
    hostname = fields.CharField(max_length=64, description="客户端电脑名")  # 电脑名
    ip = fields.CharField(max_length=16, description="客户端IP")  # ip地址
    model = fields.CharField(max_length=16, description="机种名")
    station = fields.CharField(max_length=16, description="站别名")
    line = fields.CharField(max_length=8, description="线别")
    category = fields.CharField(max_length=8, description="报警类别")  # 类别
    shift = fields.CharField(max_length=8, description="报警开始时的班别")  # 班别
    alert_code = fields.CharField(max_length=8, description="报警代码")  # 报警代码
    alert_desc = fields.CharField(max_length=255, description="报警描述")  # 报警代码
    start_time = fields.DatetimeField(description="报警开始时间")  # 报警开始时间
    end_time = fields.DatetimeField(description="报警结束时间")  # 报警结束时间
    time_difference = fields.IntField(description="开始到结束时间差")  # 时间差
    week = fields.SmallIntField(description="报警发生周别")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table_description = "设备报警表"
        table = "device_alerts"


class AlertInfo(Model):
    alert_code = fields.CharField(max_length=8, description="设备报警代码")  # 报警代码
    start_number = fields.IntField(description="触发序号")  # 触发序号
    end_number = fields.IntField(description="结束序号")  # 结束序号
    start_event = fields.CharField(max_length=64, description="触发报警事件")  # 触发事件
    end_event = fields.CharField(max_length=65, description="结束报警事件")  # 终止事件
    alert_desc = fields.CharField(max_length=255, description="报警事件描述")  # 异常描述

    class Meta:
        table_description = "设备报警描述表"
        table = "alert_info"
