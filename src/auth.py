from fastapi import Security, HTTPException, status, Request, Depends
from fastapi.security import APIKeyHeader
from sqlmodel import Session, select

from src.database.db import get_session
from src.internal.users.model import ApiUser

api_key = APIKeyHeader(name="x-api-key")


async def handle_api_key(
    req: Request, db: Session = Depends(get_session), key: str = Security(api_key)
):
    res = db.exec(select(ApiUser).where(ApiUser.key == key))

    api_key_data = res.first()

    if not api_key_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid API key",
        )

    yield api_key_data
