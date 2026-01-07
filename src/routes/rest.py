from fastapi import APIRouter, Depends
from src.auth import handle_api_key
from src.internal.posts.use_cases.list_posts import (
    ListPostsUseCase,
    get_list_posts_use_case,
)

from src.internal.bills.use_cases.list_bills import (
    ListBillsUseCase,
    get_bills_use_case,
)

from src.internal.bills.use_cases.create_bill import (
    CreateBillUseCase,
    get_create_bill_use_case,
)
from src.internal.bills.schema import BillInput
from src.internal.posts.schemas import PostOutput
from src.internal.users.model import ApiUser

restRouter = APIRouter()


@restRouter.get("/posts", status_code=200)
async def list_posts(
    list_posts_use_case: ListPostsUseCase = Depends(get_list_posts_use_case),
    user: ApiUser = Depends(handle_api_key),
) -> list[PostOutput]:
    return list_posts_use_case.execute(user.id)


@restRouter.get("/bills", status_code=200)
async def list_bills(
    list_bills_use_case: ListBillsUseCase = Depends(get_bills_use_case),
    user: ApiUser = Depends(handle_api_key),
):
    return list_bills_use_case.execute(user_id=user.id)


@restRouter.post("/bills", status_code=201)
async def create_bill(
    bill_input: BillInput,
    create_bill_use_case: CreateBillUseCase = Depends(get_create_bill_use_case),
    user: ApiUser = Depends(handle_api_key),
):
    return create_bill_use_case.execute(user=user, bill_input=bill_input)
