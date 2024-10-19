from pydantic import BaseModel

# What we accept or allow a user to enter or post to our API


class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True