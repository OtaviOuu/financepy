from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

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
