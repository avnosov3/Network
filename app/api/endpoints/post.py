from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.post import post_crud
from app.schemas.post import PostCreate

post_router = APIRouter()

POSTS_NOT_FOUND = 'Посты не найдены'


@post_router.post('/')
async def create_post(
    post: PostCreate, session: AsyncSession = Depends(get_async_session)
):
    return await post_crud.create(post, session)


@post_router.get('/')
async def get_all_posts(session: AsyncSession = Depends(get_async_session)):
    posts = await post_crud.get_all(session)
    if posts is None:
        raise HTTPException(
            status_code=404,
            detail=POSTS_NOT_FOUND
        )
    return posts
