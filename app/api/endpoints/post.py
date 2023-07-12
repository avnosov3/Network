from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.post import post_crud
from app.schemas.post import PostCreate

post_router = APIRouter()


@post_router.post('/post/')
async def create_post(
    post: PostCreate, session: AsyncSession = Depends(get_async_session)
):
    return await post_crud.create(post, session)
