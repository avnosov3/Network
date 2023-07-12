from datetime import datetime

from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    text: str = Field(..., min_length=1)
    pub_date: datetime


class PostUpdate(BaseModel):
    text: str = Field(..., min_length=1)
