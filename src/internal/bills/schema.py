from sqlmodel import SQLModel


class BillInput(SQLModel):
    name: str
    amount: float


class BillOutput(SQLModel):
    id: int
    name: str
    amount: float
