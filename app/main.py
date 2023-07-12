from fastapi import FastAPI

from .core.config import settings
from .api.routers import main_router_v1

app = FastAPI(title=settings.app_title)
app.include_router(main_router_v1)
