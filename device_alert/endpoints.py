# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
import datetime
import os

from fastapi import APIRouter, Request, Query, Path
from typing import Union
from .schemas import DeviceAlert, DeviceAlertUpdate
from .service import device_alert_service
from schemas.response import base_response
router = APIRouter(prefix="/device-alerts")


@router.post("/", description="上传设备报警参数", summary="设备报警信息上传")
async def alter_add(device_alert: DeviceAlert, req: Request):
    unique = {
        "model": device_alert.model,
        "station": device_alert.station,
        "line": device_alert.line,
        "alert_code": device_alert.alert_code,
        "start_time": device_alert.start_time
    }
    is_exist = await device_alert_service.check_server_info_existence(**unique)
    if not is_exist:
        res = await device_alert_service.alert_add(device_alert, req)
        return res
    else:
        return base_response(409, "fail", f"此报警信息已存在")


@router.get("/", description="设备报警参数条件查询", summary="设备报警信息查询")
async def alter_get(
        req: Request,
        start_date: str = Query(None, min_length=8, max_length=8, description="开始日期"),
        end_date: str = Query(None, min_length=8, max_length=8, description="结束日期"),
        model: str = Query(None, max_length=8, description="机种名"),
        station: str = Query(None, max_length=8, description="站别名"),
        line: str = Query(None, max_length=8, description="站别名"),
        category: str = Query(None, max_length=8, description="报警代码"),
        alert_code: str = Query(None, max_length=8, description="报警代码"),
        shift: str = Query(None, max_length=8, description="报警代码"),
        limit: int = Query(99999, description="分页获取每页数量"),
        offset: int = Query(0, description="分页获取数据偏移量"),

) -> Union[dict]:
    # 查询参数
    query = {}

    shift_delta_hours = int(os.getenv('SHIFT_TIMEDELTA_HOURS'))
    if start_date:
        try:
            start_time = datetime.datetime.strptime(start_date, "%Y%m%d") - datetime.timedelta(hours=shift_delta_hours)
            query.update({"start_time__gte": start_time})
        except ValueError:
            return {"code": 400, "status": "fail", "message": "日期参数错误", "data": []}
    if end_date:
        try:
            end_time = datetime.datetime.strptime(end_date, "%Y%m%d") \
                       + datetime.timedelta(days=1) - datetime.timedelta(hours=shift_delta_hours)
            query.update({"end_time__lt": end_time})
        except ValueError:
            return {"code": 400, "status": "fail", "message": "日期参数错误", "data": []}

    if model:
        query.update({"model": model})
    if station:
        query.update({"station": station})
    if alert_code:
        query.update({"alert_code": alert_code})
    if line:
        query.update({"line": line})
    if category:
        query.update({"category": category})
    if shift:
        query.update({"shift": shift})

    res = await device_alert_service.alert_get(offset, limit, **query)
    return res


@router.patch("/", description="修改一条设备报警参数", summary="设备报警信息修改")
async def alert_update(
        device_alert_update: DeviceAlertUpdate
):
    unique = {
        "model": device_alert_update.model,
        "station": device_alert_update.station,
        "line": device_alert_update.line,
        "alert_code": device_alert_update.alert_code,
        "start_time": device_alert_update.start_time
    }
    is_updated = await device_alert_service.alert_update(unique, **device_alert_update.dict())
    if is_updated:
        return base_response(200, "success", "资源更新成功")
    else:
        return base_response(304, "fail", "资源未被更新")


@router.delete("/", description="删除一条设备报警参数", summary="设备报警信息删除")
async def alert_delete(
        device_alert_update: DeviceAlertUpdate
):
    unique = {
        "model": device_alert_update.model,
        "station": device_alert_update.station,
        "line": device_alert_update.line,
        "alert_code": device_alert_update.alert_code,
        "start_time": device_alert_update.start_time
    }
    is_deleted = await device_alert_service.alert_delete(unique)
    if is_deleted:
        return base_response(200, "success", "资源删除成功")
    else:
        return base_response(404, "fail", "未找到该资源")


@router.get("/models", description="查询设备报警信息表中已维护机种", summary="设备报警已维护机种查询")
async def models_get():
    models = await device_alert_service.field_distinct_get("model")
    return base_response(200, "success", "获取机种成功", models)


@router.get("/lines", description="查询设备报警信息表中已维护线别", summary="设备报警已维护线别查询")
async def models_get():
    models = await device_alert_service.field_distinct_get("line")
    return base_response(200, "success", "获取线别成功", models)


@router.get("/stations", description="查询设备报警信息表中已维护站别", summary="设备报警已维护站别查询")
async def models_get():
    models = await device_alert_service.field_distinct_get("station")
    return base_response(200, "success", "获取站别成功", models)
