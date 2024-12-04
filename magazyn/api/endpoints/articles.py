from typing import cast

from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from magazyn.api.models.article import Article
from magazyn.db.services.article import ArticleService
from magazyn.types.articles import AbstractArticleService

article_router = APIRouter(prefix="/articles")


@article_router.post("/")
async def create_article(
    data: Article,
    article_service: AbstractArticleService = Depends(ArticleService)
) -> Response:
    await article_service.create_article(data)
    return Response(status_code=HTTP_201_CREATED)


@article_router.get("/{slug}", response_model=Article)
async def get_article(
    slug: str,
    article_service: AbstractArticleService = Depends(ArticleService),
) -> Article | Response:
    article = cast(Article, await article_service.get_by_slug(slug))
    if article is not None:
        return article
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)
