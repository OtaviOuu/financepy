from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from src.internal.bills.use_cases.list_bills import get_bills_use_case, ListBillsUseCase

html_router = APIRouter()

templates = Jinja2Templates(directory="./src/templates/")


@html_router.get("/", response_class=HTMLResponse)
async def index():
    return RedirectResponse(url="/home")


@html_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="posts/index.html",
        context={"items": ["item1", "item2", "item3"]},
    )


@html_router.get("/bills", response_class=HTMLResponse)
async def bills(
    request: Request,
    list_bills_use_case: ListBillsUseCase = Depends(get_bills_use_case),
):
    bills = list_bills_use_case.execute(user_id=1)
    print(bills)
    labels = [bill.name for bill in bills]
    data = [bill.amount for bill in bills]
    return templates.TemplateResponse(
        request=request,
        name="bills/index.html",
        context={"bills": bills, "labels": labels, "data": data},
    )
