from sqlmodel import SQLModel


class BillOutput(SQLModel):
    id: int
    name: str
    amount: float
