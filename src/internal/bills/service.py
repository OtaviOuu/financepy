from fastapi import Depends
from sqlmodel import Session, select
from src.database.db import get_session
from src.internal.bills.schema import BillOutput
from src.internal.bills.model import Bill


class BillsService:
    def __init__(self, DBSession: Session):
        self.DBSession = DBSession

    def list_bills(self, user_id: int) -> list[BillOutput]:
        all_bills = self.DBSession.exec(
            select(Bill).where(Bill.user_id == user_id).order_by(Bill.id)
        ).all()

        return all_bills


def get_bills_service(session: Session = Depends(get_session)) -> BillsService:
    return BillsService(DBSession=session)
