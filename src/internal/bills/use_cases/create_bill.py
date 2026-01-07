from time import sleep

from fastapi import Depends
from src.internal.bills.service import BillsService, get_bills_service
from src.internal.bills.schema import BillInput, BillOutput
from src.internal.users.model import ApiUser


class CreateBillUseCase:
    def __init__(self, bill_service: BillsService):
        self.bill_service = bill_service

    def execute(self, bill_input: BillInput, user: ApiUser) -> BillOutput:
        new_bill = self.bill_service.create_bill(bill_input=bill_input, user=user)
        print("mandando email...")
        return new_bill


def get_create_bill_use_case(
    bills_service: BillsService = Depends(get_bills_service),
) -> CreateBillUseCase:
    return CreateBillUseCase(bill_service=bills_service)
