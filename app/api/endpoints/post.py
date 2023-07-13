from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.post import post_crud
from app.crud.like import like_crud
from app.models.user import User
from app.schemas.post import PostCreateSchema, PostUpdateSchema
from ..validators import check_obj_exists_by_id

post_router = APIRouter()

POSTS_NOT_FOUND = 'Посты не найдены'
NOT_ALLOWED_TO_UPDATE = 'Нельзя редактировать чужие посты'
NOT_ALLOWED_TO_DELETE = 'Нельзя удалять чужие посты'


@post_router.post(
    '/',
    dependencies=[Depends(current_user)]
)
async def create_post(
    post: PostCreateSchema,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await post_crud.create(post, session, user)


@post_router.get('/')
async def get_all_posts(session: AsyncSession = Depends(get_async_session)):
    return await post_crud.get_all(session)


@post_router.get('/{post_id}')
async def get_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await check_obj_exists_by_id(post_id, session, post_crud)


@post_router.get(
    '/{post_id}/likes',
    dependencies=[Depends(current_user)]
)
async def get_likes_in_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await like_crud.get_likes_in_post(post_id, session)


@post_router.get(
    '/{post_id}/count-likes',
    dependencies=[Depends(current_user)]
)
async def count_likes(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await like_crud.count_likes_in_post(post_id, session)


@post_router.patch(
    '/{post_id}',
    dependencies=[Depends(current_user)]
)
async def update_post(
    post_id: int,
    post: PostUpdateSchema,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    post_db = await check_obj_exists_by_id(post_id, session, post_crud)
    if post_db.user_id != user.id:
        raise HTTPException(403, detail=NOT_ALLOWED_TO_UPDATE)
    return await post_crud.update(post_db, post, session)


@post_router.delete(
    '/{post_id}',
    dependencies=[Depends(current_user)],
)
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    post_db = await check_obj_exists_by_id(post_id, session, post_crud)
    if post_db.user_id != user.id:
        raise HTTPException(403, detail=NOT_ALLOWED_TO_DELETE)
    return await post_crud.remove(post_db, session)
