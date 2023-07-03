# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
import datetime
from fastapi import APIRouter, Request, Query, Path
from typing import Union
from .schemas import DeviceAlert
from .service import device_alert_service
from schemas.response import base_response
router = APIRouter(prefix="/device-alerts")


@router.post("/", description="上传设备报警参数")
async def alter_add(device_alert: DeviceAlert, req: Request):
    res = await device_alert_service.alert_add(device_alert, req)
    return res


@router.get("/", description="设备报警参数条件查询")
async def alter_get(
        req: Request,
        start_date: str = Query(None, min_length=8, max_length=8, description="开始日期"),
        end_date: str = Query(None, min_length=8, max_length=8, description="结束日期"),
        model: str = Query(None, max_length=8, description="机种名"),
        station: str = Query(None, max_length=8, description="站别名"),
        alert_code: str = Query(None, max_length=8, description="报警代码"),
        limit: int = Query(99999, description="分页获取每页数量"),
        offset: int = Query(0, description="分页获取数据偏移量"),

) -> Union[dict]:
    # 查询参数
    query = {}

    if start_date:
        try:
            start_time = datetime.datetime.strptime(start_date, "%Y%m%d")
            query.update({"start_time__gte": start_time})
        except ValueError:
            return {"code": 400, "status": "fail", "message": "日期参数错误", "data": []}
    if end_date:
        try:
            end_time = datetime.datetime.strptime(end_date, "%Y%m%d") + datetime.timedelta(days=1)
            query.update({"end_time__lt": end_time})
        except ValueError:
            return {"code": 400, "status": "fail", "message": "日期参数错误", "data": []}

    if model:
        query.update({"model": model})
    if station:
        query.update({"station": station})
    if alert_code:
        query.update({"alert_code": alert_code})

    res = await device_alert_service.alert_get(offset, limit, **query)
    return res

