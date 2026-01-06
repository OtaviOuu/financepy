from sqlmodel import SQLModel


class PostInput(SQLModel):
    title: str


class PostOutput(SQLModel):
    id: int
    title: str
