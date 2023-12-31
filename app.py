# -*- coding:utf-8 -*-
"""
@Time : 2023/06/23 15:12
@Author: Roco
@Project:app
@Des: Fastapp实例化
"""
from fastapi import FastAPI
from api import router
from config import settings
from event import startup
import uvicorn

app = FastAPI()


# 事件监听
app.add_event_handler("startup", startup(app))

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="app:app",  host="0.0.0.0", port=8000, reload=True)
