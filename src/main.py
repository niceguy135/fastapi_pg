import asyncio
import os
import sys

import uvicorn

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from alembic.config import Config
from alembic import command

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.orm_queries import AsyncMainQueries, AsyncUtilsQueries
from src.dto_schemas import PresentUserAnAchievement, AchievementsAddDTO


def run_migrations(alembic_cfg):
    """
    Загрузить на БД последний миграцию
    :param alembic_cfg: alembic.Config объект с путем до конфиг. файла логики миграции
    :return: None
    """
    command.upgrade(alembic_cfg, "head")

def downgrade_migration(alembic_cfg):
    """
    Вернуть БД в чистое состояние
    :param alembic_cfg: alembic.Config объект с путем до конфиг. файла логики миграции
    :return: None
    """
    command.downgrade(alembic_cfg, "base")


def create_fastapi_app():
    """
    Создать объект, отвечающий за FastAPI, и настроить его
    :return: None
    """
    app = FastAPI(title="FastAPI")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )

    #  Users endpoints
    ##################################################
    @app.get("/users/{user_id}", tags=["users"])
    async def get_user_info(user_id: int):
        """
        Эндпоинт для получения информации о пользователе
        """
        user = await AsyncMainQueries.get_user(user_id)
        return user

    @app.post("/users/{user_id}", tags=["users"])
    async def present_user_an_achievement(body: PresentUserAnAchievement = Depends):
        """
        Эндпоинт для награждения пользователя существующим в БД достижением
        """
        await AsyncMainQueries.give_achievement_to_user(
            body.user_id,
            body.achievement_id
        )
        return HTTPException(200)
    ##################################################

    #  Achievements endpoints
    ##################################################
    @app.get("/achievements", tags=["achievements"])
    async def get_achievements_info():
        """
        Эндпоинт для получения всех существующих достижений
        """
        achievs = await AsyncMainQueries.get_all_achievements()
        return achievs

    @app.get("/achievements/{user_id}", tags=["user_achievements"])
    async def get_user_achievements(user_id: int = Depends):
        """
        Эндпоинт для получения всех присвоенных достижений пользователю
        """
        achievs = await AsyncMainQueries.take_users_achievements(user_id)
        return achievs

    @app.post("/achievements", tags=["new_achievement"])
    async def create_new_achievement(new_achiev: AchievementsAddDTO):
        """
        Эндпоинт для создания нового достижения
        """
        await AsyncMainQueries.create_new_achievement(
            new_achiev
        )
        return HTTPException(200)
    ##################################################

    #  Statistics endpoint
    ##################################################
    @app.get("/statistics", tags=["statistics"])
    async def get_statistics():
        """
        Эндпоинт для получения статистической информации
        """
        result = await AsyncMainQueries.get_statistics_data()
        return result
    ##################################################

    @app.get("/", tags=["default"])
    async def default_route():
        """
        Дефолтный эндпоинт для случаев неверного введения адреса
        """
        return HTTPException(404)

    return app


fastapi_app = create_fastapi_app()


def main():
    if "--prepare-db" in sys.argv:
        alembic_ini = Config("alembic.ini")
        run_migrations(alembic_ini)
        asyncio.run(AsyncUtilsQueries.insert_sample_data())
    elif "--clean-db" in sys.argv:
        alembic_ini = Config("alembic.ini")
        downgrade_migration(alembic_ini)
    else:
        uvicorn.run(
            app="src.main:fastapi_app",
            reload=True,
        )


if __name__ == "__main__":
    main()
