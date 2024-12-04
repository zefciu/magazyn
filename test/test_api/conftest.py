import pytest

from magazyn.api.models.article import Article


@pytest.fixture
def article_data() -> Article:
    return Article(
        title="My article",
        slug="my-article",
        content="Lorem ipsum <em>dolor</em> sit amet.",
    )
