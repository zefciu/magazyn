from typing import cast
from unittest.mock import AsyncMock

from starlette.status import HTTP_201_CREATED

from magazyn.api.endpoints.articles import create_article
from magazyn.api.models.article import Article
from magazyn.types.articles import AbstractArticleService


async def test_create_article(
    article_data: Article
) -> None:
    article_service = cast(AbstractArticleService, AsyncMock())
    result = await create_article(
        article_data,
        cast(AbstractArticleService, article_service)
    )
    assert result.status_code == HTTP_201_CREATED
    cast(AsyncMock, article_service.create_article).\
        assert_called_once_with(article_data)
