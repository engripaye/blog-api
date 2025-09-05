from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class BlogResponse(BlogCreate):
    id: int

    class Config:
        orm_mode = True
