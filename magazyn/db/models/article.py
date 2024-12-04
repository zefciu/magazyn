from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from magazyn.db.models.base import Base


class Article(Base):

    __tablename__ = 'articles'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    slug: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    content: Mapped[str] = mapped_column()
