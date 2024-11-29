import os
import sys

import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(1, os.path.join(sys.path[0], '..'))


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

    return app


fastapi_app = create_fastapi_app()

if __name__ == "__main__":
    uvicorn.run(
        app="src.main:fastapi_app",
        reload=True,
    )
