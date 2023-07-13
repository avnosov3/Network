from fastapi import FastAPI

from .api.routers import main_router_v1

app_title = 'megatronics'

app = FastAPI(title=app_title)
app.include_router(main_router_v1)
