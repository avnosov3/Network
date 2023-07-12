from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.post import post_crud

POST_NOT_FOUND = 'Проект не найден'


async def check_post_exists_by_id(
    id: int,
    session: AsyncSession
):
    post = await post_crud.get(id, session)
    if post is None:
        raise HTTPException(
            status_code=404,
            detail=POST_NOT_FOUND
        )
    return post
