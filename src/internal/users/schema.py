from sqlmodel import SQLModel


class UserOutput(SQLModel):
    id: int
    name: str
    active: bool
    api_key: str
