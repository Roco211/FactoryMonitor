# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
import datetime
from fastapi import APIRouter, Request, Query, Path
from .schemas import DeviceAlert
from .service import device_alert_service
router = APIRouter(prefix="/device-alerts")


@router.post("/")
async def alter_add(device_alert: DeviceAlert, req: Request):
    res = await device_alert_service.alert_add(device_alert, req)
    return res


@router.get("/")
async def get_alter(
        req: Request,
        start_date: str = Query(None, min_length=8, max_length=8),
        end_date: str = Query(None, min_length=8, max_length=8),
        model: str = Query(None, max_length=8),
        station: str = Query(None, max_length=8),
        alert_code: str = Query(None, max_length=8),
        limit: int = Query(99999),
        offset: int = Query(0)
) -> dict:
    # 查询参数
    query = {}

    if start_date:
        try:
            start_time = datetime.datetime.strptime(start_date, "%Y%m%d")
            query.update({"start_time__gte": start_time})
        except ValueError:
            return {"status": 400, "msg": f"日期参数错误 {start_date}"}
    if end_date:
        try:
            end_time = datetime.datetime.strptime(end_date, "%Y%m%d") + datetime.timedelta(days=1)
            query.update({"end_time__lt": end_time})
        except ValueError:
            return {"status": 400, "msg": f"日期参数错误 {start_date}"}

    if model:
        query.update({"model": model})
    if station:
        query.update({"station": station})
    if alert_code:
        query.update({"alert_code": alert_code})

    res = await device_alert_service.alert_get(offset, limit, **query)
    return res

