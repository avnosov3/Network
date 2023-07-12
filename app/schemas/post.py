from datetime import datetime

from pydantic import BaseModel


class PostCreate(BaseModel):
    text: str
    pub_date: datetime


class PostUpdate(BaseModel):
    text: str
