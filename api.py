# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: api聚合
"""
from fastapi import APIRouter
from user.endpoints import router as user_router
from schemas.base import BaseResp


router = APIRouter(prefix="/api/v1")

router.include_router(user_router)


@router.get("/ping", response_model=BaseResp)
async def ping():
    res = {
        "status": 200,
        "msg":"pong"
    }
    return res