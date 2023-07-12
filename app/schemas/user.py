from typing import Optional

from fastapi_users import schemas


class UserReadSchema(schemas.BaseUser[int]):
    first_name: str


class UserCreateSchema(schemas.BaseUserCreate):
    first_name: str


class UserUpdateSchema(schemas.BaseUserUpdate):
    first_name: Optional[str]
