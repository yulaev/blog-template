from sqlalchemy import String, Date
from sqlalchemy.orm import *
from datetime import date

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "post"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(1000))
    date_posted: Mapped[date] = mapped_column(Date)

    def __repr__(self) -> str:
        return f"{self.author} posted '{self.title}' on {self.date_posted}"