# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
from datetime import datetime
from fastapi import APIRouter, Request, Query, Path
from .schemas import DeviceAlert
from .service import device_alert_service
router = APIRouter(prefix="/device-alert")


@router.post("/")
async def alter_add(device_alert: DeviceAlert, req: Request):
    res = await device_alert_service.alert_add(device_alert, req)
    return res


@router.get("/{date}")
async def get_alter(
        req: Request,
        date: str = Path(..., min_length=8, max_length=8),
        model: str = Query(None, max_length=8),
        station: str = Query(None, max_length=8),
        alert_code: str = Query(None, max_length=8),
        limit: int = Query(99999),
        offset: int = Query(0)
) -> dict:
    # 查询参数
    query = {}

    if date:
        try:
            date = datetime.strptime(date, "%Y%m%d")
        except ValueError:
            return {"status": 400, "msg": f"日期参数错误 {date}"}
    if model:
        query.update({"model": model})
    if station:
        query.update({"station": station})
    if alert_code:
        query.update({"alert_code": alert_code})

    res = await device_alert_service.alert_get(date, offset, limit, **query)
    return res

