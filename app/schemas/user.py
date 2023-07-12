from typing import Optional

from fastapi_users import schemas


class UserReadSchema(schemas.BaseUser[int]):
    nickname: str


class UserCreateSchema(schemas.BaseUserCreate):
    nickname: str


class UserUpdateSchema(schemas.BaseUserUpdate):
    nickname: Optional[str]
