from fastapi import APIRouter, Depends

from src.internal.posts.use_cases.list_posts import (
    ListPostsUseCase,
    get_list_posts_use_case,
)
from src.internal.posts.schemas import PostOutput

restRouter = APIRouter()


@restRouter.get("/posts", status_code=200)
async def list_posts(
    list_posts_use_case: ListPostsUseCase = Depends(get_list_posts_use_case),
) -> list[PostOutput]:
    return list_posts_use_case.execute()
