from fastapi import FastAPI

from magazyn.api.endpoints.articles import article_router

app = FastAPI()

app.include_router(article_router)
