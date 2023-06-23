# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: 描述
"""
from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/")
async def get_all_user():
    return "ALL USER"

