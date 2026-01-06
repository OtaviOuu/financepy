from sqlmodel import Field, SQLModel


class Bill(SQLModel, table=True):
    __tablename__ = "bills"

    id: int = Field(primary_key=True, index=True)
    name: str = Field(nullable=False, index=True)
    amount: int = Field(nullable=False)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
