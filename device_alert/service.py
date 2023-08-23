# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
import time
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

        current_date = datetime.now() - timedelta(days=3)
        _, week, _ = (current_date + timedelta(days=1)).isocalendar()
        data.update({"week": int(week)})
        await DeviceAlert.create(**data)
        return base_response(200, "success", "上传成功")

    async def alert_get(self, offset=None, limit=99999, **query):
        start = time.time()
        device_alert_dict = await DeviceAlert.filter(**query).order_by('-start_time').limit(limit).offset(
            offset * limit).all().values()
        t = round(float(time.time() - start), 2)
        return base_response(200, "success", f"查询到{len(device_alert_dict)}条记录,耗时{t}s", device_alert_dict)

    async def alert_update(self, unique, **query):
        is_update = await DeviceAlert.filter(**unique).update(**query)
        if is_update:
            return True
        else:
            return False

    async def alert_delete(self, unique):
        is_deleted = await DeviceAlert.filter(**unique).delete()
        if is_deleted:
            return True
        else:
            return False

    async def check_server_info_existence(self, **query):
        is_exist = await DeviceAlert.filter(**query).first()
        if is_exist:
            return True
        else:
            return False

    async def field_distinct_get(self, field):
        datas = await DeviceAlert.raw(
            f"""
            SELECT DISTINCT {field} FROM device_alerts;
            """
        )
        res = [getattr(data, field) for data in datas]
        return res


device_alert_service = DeviceAlertService()
