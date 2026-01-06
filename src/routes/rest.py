from fastapi import APIRouter, Depends

from src.internal.posts.use_cases.create_post import CreatePostUseCase
from src.internal.posts.use_cases.list_posts import ListPostsUseCase
from src.internal.posts.service import get_post_service
from src.internal.posts.schemas import PostOutput, PostInput


def get_create_post_use_case():
    return CreatePostUseCase(post_service=get_post_service())


def get_list_posts_use_case():
    return ListPostsUseCase(post_service=get_post_service())


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
    return await list_posts_use_case.execute()
