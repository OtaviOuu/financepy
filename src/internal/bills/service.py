from fastapi import Depends
from src.internal.bills.schema import BillInput, BillOutput
from src.internal.bills.repository import get_bill_repository, BillRepository
from src.internal.users.model import ApiUser


class BillsService:
    def __init__(self, bill_repository: BillRepository):
        self.bill_repository = bill_repository

    def list_bills(self, user_id: int) -> list[BillOutput]:
        return []

    def create_bill(self, bill_input: BillInput, user: ApiUser) -> BillOutput:
        return self.bill_repository.create(bill_input=bill_input, user=user)


def get_bills_service(
    bills_repository: BillRepository = Depends(get_bill_repository),
) -> BillsService:
    return BillsService(bill_repository=bills_repository)
