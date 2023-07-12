from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .crud_base import CRUDBase
from ..models.like import Like


class CRUDLike(CRUDBase):

    async def get_likes_in_post(
        self,
        post_id: int,
        session: AsyncSession
    ):
        likes = await session.execute(
            select(Like).where(
                Like.post_id == post_id
            )
        )
        likes = likes.scalars().all()
        return likes

    async def count_likes_in_post(
        self,
        post_id,
        session: AsyncSession
    ):
        likes = await session.execute(
            select(Like.likes).where(
                Like.post_id == post_id
            )
        )
        likes = likes.scalars().all()
        return sum(likes)


like_crud = CRUDLike(Like)
