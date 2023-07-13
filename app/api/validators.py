from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.post import post_crud
from ..crud.like import like_crud

LIKE_NOT_FOUND = 'Лайк не найден'
POST_NOT_FOUND = 'Пост не найден'
OBJECT_NOT_FOUND = 'Объект не найден'
COULD_NOT_LIKE = 'Невозомжно поставить лайк своему посту'
LIKE_EXISTS = 'Вы уже поставили лайк'


async def check_obj_exists_by_id(
    id: int,
    session: AsyncSession,
    crud,
    status_code=404,
    detail=OBJECT_NOT_FOUND
):
    obj_db = await crud.get(id, session)
    if obj_db is None:
        raise HTTPException(
            status_code=status_code,
            detail=detail
        )
    return obj_db


async def check_rights_to_like(
    post_id: int,
    user_id: int,
    session: AsyncSession
):
    post = await post_crud.get(post_id, session)
    if post.user_id == user_id:
        raise HTTPException(
            status_code=403,
            detail=COULD_NOT_LIKE
        )
    return post


async def check_double_like(
    post_id: int,
    user_id: int,
    session: AsyncSession
):
    if await like_crud.exists_like(post_id, user_id, session):
        raise HTTPException(
            status_code=400,
            detail=LIKE_EXISTS
        )
