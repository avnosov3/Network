from fastapi import APIRouter

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreateSchema, UserReadSchema, UserUpdateSchema

user_router = APIRouter()

user_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_register_router(UserReadSchema, UserCreateSchema),
    prefix='/auth',
    tags=['auth'],
)
user_router.include_router(
    fastapi_users.get_users_router(UserReadSchema, UserUpdateSchema),
    prefix='/users',
    tags=['users'],
)
