from typing import Protocol


class AbstractArticle(Protocol):
    slug: str
    title: str
    content: str


class AbstractArticleService(Protocol):
    async def get_by_slug(self, slug: str) -> AbstractArticle | None:
        ...

    async def create_article(self, article_data: AbstractArticle) -> None:
        ...
