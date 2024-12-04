from fastapi import Depends
from prompt_toolkit.key_binding.bindings.named_commands import get_by_name
from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from magazyn.db.models.article import Article as OrmArticle

from magazyn.api.models.article import Article
from magazyn.db.session import get_session


class ArticleService:
    def __init__(
        self,
        session: AsyncSession = Depends(get_session)
    ):
        self.session = session

    async def get_by_slug(self, slug: str) -> Article | None:
        query = select(OrmArticle).filter(OrmArticle.slug == slug)
        try:
            orm_article = (await self.session.execute(query)).scalar_one()
        except NoResultFound:
            return
        return Article(
            id=orm_article.id,
            title=orm_article.title,
            slug=orm_article.slug,
            content=orm_article.content,
        )

    async def create_article(self, article_data: Article) -> None:
        query = insert(OrmArticle)
        await self.session.execute(query, {
            "title": article_data.title,
            "slug": article_data.slug,
            "content": article_data.content,
        })