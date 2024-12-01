import os
import sys

import uvicorn

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from alembic.config import Config
from alembic import command

sys.path.insert(1, os.path.join(sys.path[0], '..'))


def run_migrations(alembic_cfg):
    command.upgrade(alembic_cfg, "head")

def downgrade_migration(alembic_cfg):
    command.downgrade(alembic_cfg, "base")


def create_fastapi_app():
    app = FastAPI(title="FastAPI")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )

    #  Users endpoints
    ##################################################
    @app.get("/users/{user_id}", tags=["users"])
    async def get_user_info(user_id: int):
        pass

    @app.post("/users/{user_id}", tags=["users"])
    async def present_user_an_achievement(body = Body()):
        pass
    ##################################################

    #  Achievements endpoints
    ##################################################
    @app.get("/achievements", tags=["achievements"])
    async def get_achievements_info():
        pass

    @app.get("/achievements/{user_id}}", tags=["user_achievements"])
    async def get_user_achievements(user_id: int):
        pass

    @app.post("/achievements", tags=["new_achievement"])
    async def create_new_achievement(body = Body()):
        pass
    ##################################################

    #  Statistics endpoint
    ##################################################
    @app.get("/statistics", tags=["statistics"])
    async def get_statistics():
        pass
    ##################################################

    @app.get("/", tags=["default"])
    async def default_route():
        return HTTPException(404)

    return app


fastapi_app = create_fastapi_app()

if __name__ == "__main__":
    alembic_ini = Config("alembic.ini")
    run_migrations(alembic_ini)
    uvicorn.run(
        app="src.main:fastapi_app",
        reload=True,
    )
    downgrade_migration(alembic_ini)
