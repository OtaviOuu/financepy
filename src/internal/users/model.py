from datetime import datetime
from sqlmodel import SQLModel, Field


class ApiUser(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(..., description="The name of the user")
    key: str = Field(..., description="The API key associated with the user")
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="The date and time the user was last updated",
    )
