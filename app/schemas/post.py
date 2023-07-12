from datetime import datetime

from pydantic import BaseModel, Extra


class PostCreateSchema(BaseModel):
    text: str
    pub_date: datetime
    # user_id: int

    class Config:
        min_anystr_length = 1


class PostUpdateSchema(BaseModel):
    text: str

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
