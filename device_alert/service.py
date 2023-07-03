# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
from models.device_alert import DeviceAlert, AlertInfo
from datetime import datetime, timedelta
from schemas.response import base_response
from fastapi import Request
from .schemas import DeviceAlert
from models.device_alert import DeviceAlert


class DeviceAlertService:
    async def alert_add(self, devicd_alert: DeviceAlert, req: Request):
        # 插入数据
        data: dict = devicd_alert.dict()
        ip, port = req.client
        data.update({"ip": ip})
        await DeviceAlert.create(**data)
        return base_response(200, "success", "上传成功")

    async def alert_get(self, offset=None, limit=99999, **query):
        device_alert_dict = await DeviceAlert.filter(**query).limit(limit).offset(offset).order_by('-start_time').all().values()
        return base_response(200, "success", f"查询到{len(device_alert_dict)}条记录", device_alert_dict)


device_alert_service = DeviceAlertService()
