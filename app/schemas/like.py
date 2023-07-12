from pydantic import BaseModel, StrictBool


class LikeCreateSchema(BaseModel):
    post_id: int
    likes: StrictBool
