from fastapi import APIRouter, Depends

from src.internal.posts.use_cases.create_post import (
    CreatePostUseCase,
    get_create_post_use_case,
)
from src.internal.posts.use_cases.list_posts import (
    ListPostsUseCase,
    get_list_posts_use_case,
)
from src.internal.posts.schemas import PostOutput, PostInput

restRouter = APIRouter()


@restRouter.post("/posts", response_model=list[PostOutput], status_code=201)
async def create_post(
    post_input: PostInput,
    create_post_use_case: CreatePostUseCase = Depends(get_create_post_use_case),
) -> PostOutput:
    return await create_post_use_case.execute(post_input=post_input)


@restRouter.get("/posts", status_code=200)
async def list_posts(
    list_posts_use_case: ListPostsUseCase = Depends(get_list_posts_use_case),
) -> list[PostOutput]:
    return list_posts_use_case.execute()
