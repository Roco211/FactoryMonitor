# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
from fastapi import APIRouter, Request
from .schemas import DeviceAlert
from .service import device_alert_service
router = APIRouter(prefix="/device-alert")


@router.post("/")
async def alter_add(device_alert: DeviceAlert, req: Request):
    res = await device_alert_service.alert_add(device_alert, req)
    return res

