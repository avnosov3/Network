from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.like import like_crud
from app.crud.post import post_crud
from app.models.user import User
from app.schemas.like import LikeCreateSchema

from ..validators import (
    check_double_like, check_obj_exists_by_id, check_rights_to_like
)

like_router = APIRouter()


NOT_ALLOWED_TO_DELETE = 'Вы не можете удалить чужой лайк'


@like_router.post(
    '/',
    dependencies=[Depends(current_user)]
)
async def create_like(
    like: LikeCreateSchema,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    await check_obj_exists_by_id(like.post_id, session, post_crud)
    await check_rights_to_like(like.post_id, user.id, session)
    await check_double_like(like.post_id, user.id, session)
    return await like_crud.create(like, session, user)


@like_router.delete(
    '/{post_id}',
    dependencies=[Depends(current_user)]
)
async def remove_like(
    like_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    like = await check_obj_exists_by_id(like_id, session, like_crud)
    if user.id != like.user_id:
        raise HTTPException(403, detail=NOT_ALLOWED_TO_DELETE)
    return await like_crud.remove(like, session)
