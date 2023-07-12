from fastapi import APIRouter

from .endpoints.post import post_router

main_router_v1 = APIRouter()

main_router_v1.include_router(post_router, prefix='/post', tags=['Posts'])
