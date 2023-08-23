# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:11
@Author: Roco
@Project:app
@Des: 工具类
"""
import datetime
import calendar


def get_month_range(year: int, month: int):
    _, last_day = calendar.monthrange(year, month)
    start_date = datetime.datetime(year, month, 1)
    end_date = datetime.datetime(year, month, last_day) + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
    return start_date, end_date