from datetime import datetime

from sqlalchemy import Column, DateTime, Text
from sqlalchemy.orm import relationship

from ..core.db import Base


class Post(Base):
    text = Column(Text, nullable=False)
    pub_date = Column(DateTime, default=datetime.utcnow)
    likes = relationship('Like', cascade='delete')

    OUT = ('текст поста {text:.15} дата публикации {pub_date}')

    def __repr__(self):
        return self.OUT.format(self.text, self.pub_date)
