from fastapi import FastAPI

from src.routes.rest import restRouter
from src.routes.html import html_router

app = FastAPI()


app.include_router(html_router, prefix="")
app.include_router(restRouter, prefix="/api/rest")
