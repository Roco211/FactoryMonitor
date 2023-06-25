from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql

def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        print("app启动")
        await register_mysql(app)

    return app_start