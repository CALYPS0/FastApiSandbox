import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String)
    rating = sa.Column(sa.Integer)
    time_created = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    time_updated = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())
    author_id = sa.Column(sa.Integer, sa.ForeignKey("author.id"))

    author = relationship("Author")


class Author(Base):
    __tablename__ = "author"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    time_created = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    time_updated = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())
