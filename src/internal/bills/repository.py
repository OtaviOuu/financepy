from src.internal.bills.model import Bill
from src.internal.bills.schema import BillInput, BillOutput
from src.internal.users.model import ApiUser
from sqlmodel import Session
from fastapi import Depends
from src.database.db import get_session


class BillRepository:
    def __init__(self, DBSession: Session):
        self.DBSession = DBSession

    def create(self, bill_input: BillInput, user: ApiUser) -> BillOutput:
        new_bill = Bill(
            user_id=user.id,
            amount=bill_input.amount,
            name=bill_input.name,
        )

        self.DBSession.add(new_bill)

        self.DBSession.commit()

        return BillOutput.model_validate(new_bill)


def get_bill_repository(session: Session = Depends(get_session)) -> BillRepository:
    return BillRepository(DBSession=session)
