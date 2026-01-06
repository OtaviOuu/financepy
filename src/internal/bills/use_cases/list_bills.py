from src.internal.bills.schema import BillOutput
from src.internal.bills.service import BillsService, get_bills_service
from fastapi import Depends


class ListBillsUseCase:
    def __init__(self, bills_service):
        self.bills_service = bills_service

    def execute(self) -> list[BillOutput]:
        return self.bills_service.list_bills()


def get_bills_use_case(
    bills_service: BillsService = Depends(get_bills_service),
) -> ListBillsUseCase:
    return ListBillsUseCase(bills_service=bills_service)
