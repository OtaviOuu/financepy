from fastapi import APIRouter, Depends

from src.internal.posts.use_cases.create_post import CreatePostUseCase
from src.internal.posts.service import PostsService
from src.internal.posts.schemas import PostOutput, PostInput


def get_create_post_use_case():
    return CreatePostUseCase(post_service=PostsService())


restRouter = APIRouter()


@restRouter.post("/posts", response_model=list[PostOutput], status_code=201)
async def get_posts(
    post_input: PostInput,
    create_post_use_case: CreatePostUseCase = Depends(get_create_post_use_case),
) -> PostOutput:
    return await create_post_use_case.execute(post_input=post_input)
