from src.internal.posts.service import PostsService, get_post_service
from fastapi import Depends
from src.internal.posts.schemas import PostInput, PostOutput


class CreatePostUseCase:
    def __init__(self, post_service: PostsService):
        self.post_service = post_service

    def execute(self, post_input: PostInput) -> PostOutput:
        return {"id": 1, "title": post_input.title}


def get_create_post_use_case(
    post_service: PostsService = Depends(get_post_service),
) -> CreatePostUseCase:
    return CreatePostUseCase(post_service=post_service)
