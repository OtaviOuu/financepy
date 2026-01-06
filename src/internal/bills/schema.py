from sqlmodel import SQLModel, Column, Field, TIMESTAMP, text


class Bill(SQLModel, table=True):
    __tablename__ = "bills"

    id: int = Field(primary_key=True, index=True)
    name: str = Field(nullable=False, index=True)
