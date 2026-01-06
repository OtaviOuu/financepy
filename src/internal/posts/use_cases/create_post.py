from src.internal.posts.service import PostsService

from src.internal.posts.schemas import PostInput, PostOutput


class CreatePostUseCase:
    def __init__(self, post_service: PostsService):
        self.post_service = post_service

    def execute(self, post_input: PostInput) -> PostOutput:
        return {"id": 1, "title": post_input.title}
