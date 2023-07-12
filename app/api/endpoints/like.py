from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.like import like_crud
from app.schemas.like import LikeCreateSchema
from ..validators import check_post_exists_by_id

like_router = APIRouter()


@like_router.post('/')
async def create_like(
    like: LikeCreateSchema,
    session: AsyncSession = Depends(get_async_session)
):
    await check_post_exists_by_id(like.post_id, session)
    return await like_crud.create(like, session)
