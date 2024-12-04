from pydantic import BaseModel


class Article(BaseModel):
    title: str
    slug: str
    content: str
