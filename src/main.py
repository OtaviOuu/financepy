from fastapi import FastAPI, Depends


from src.auth import handle_api_key
from src.routes.rest import restRouter
from src.routes.html import html_router
from src.database.db import init_db

app = FastAPI(
    dependencies=[
        Depends(handle_api_key),
    ]
)
init_db()


app.include_router(html_router, prefix="")
app.include_router(restRouter, prefix="/api/rest")
