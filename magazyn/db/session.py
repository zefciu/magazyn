from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker

from magazyn.settings import Settings


def get_engine(settings: Settings):
    return create_async_engine("postgresql+asyncpg://" + settings.db_url)


async def get_session(engine: Annotated[AsyncEngine, Depends(get_engine)]) -> AsyncSession :
    session_maker = async_sessionmaker(bind=engine)
    async with session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        await session.commit()