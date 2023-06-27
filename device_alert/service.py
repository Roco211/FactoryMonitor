# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
from models.device_alert import DeviceAlert
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
        return {"status": 200, "msg": "OK"}



device_alert_service = DeviceAlertService()
