from fastapi import APIRouter

from .endpoints.like import like_router
from .endpoints.post import post_router
from .endpoints.user import user_router

main_router_v1 = APIRouter()

main_router_v1.include_router(post_router, prefix='/post', tags=['Posts'])
main_router_v1.include_router(like_router, prefix='/like', tags=['Likes'])
main_router_v1.include_router(user_router)
