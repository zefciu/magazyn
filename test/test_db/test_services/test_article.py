
import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from magazyn.api.models.article import Article
from magazyn.db.services.article import ArticleService
from magazyn.types.articles import AbstractArticleService
from magazyn.db.models.article import Article as DBArticle


@pytest.fixture()
async def article_service(session: AsyncSession) -> AbstractArticleService:
    return ArticleService(session)


async def test_create_article(
    session: AsyncSession,
    article_service: AbstractArticleService
) -> None:
    title = "Test Article"
    slug = "test-article"
    content = "Lorem ipsum dolor sit amet"
    await article_service.create_article(Article(
        title="Test Article",
        slug=slug,
        content="Lorem ipsum dolor sit amet"
    ))
    query = select(DBArticle).where(DBArticle.slug == slug)
    article = (await session.execute(query)).scalar()
    assert article is not None
    assert article.title == title
    assert article.slug == slug
    assert article.content == content
