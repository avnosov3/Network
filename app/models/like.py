from sqlalchemy import Column, ForeignKey, Integer

from ..core.db import Base


class Like(Base):
    post_id = Column(Integer, ForeignKey('post.id'))
    likes = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

    OUT = 'У id поста "{post_id}" лайков "{likes}"'

    def __repr__(self):
        return self.OUT.format(self.post_id, self.likes)
