from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from magazyn.settings import get_settings


@pytest.fixture
async def session() -> AsyncGenerator[AsyncSession]:
    settings = get_settings()
    engine = create_async_engine("postgresql+asyncpg://" + settings.db_url)
    async with async_sessionmaker(bind=engine)() as s:
        try:
            yield s
        finally:
            await s.rollback()
