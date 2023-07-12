from sqlalchemy.ext.asyncio import AsyncSession

from .crud_base import CRUDBase
from ..models.post import Post


class CRUDPost(CRUDBase):

    async def get_likes_in_post(
        self,
        post_id: int,
        session: AsyncSession
    ):
        pass


post_crud = CRUDPost(Post)
