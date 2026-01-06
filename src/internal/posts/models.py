from sqlmodel import SQLModel, Field


class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: int = Field(primary_key=True, index=True)
    title: str = Field(nullable=False)
