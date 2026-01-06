from src.internal.posts.service import PostsService, get_post_service
from fastapi import Depends


class ListPostsUseCase:
    def __init__(self, posts_service: PostsService):
        self.posts_service = posts_service

    def execute(self, user_id: int) -> list:
        return self.posts_service.list_posts(user_id=user_id)


def get_list_posts_use_case(
    posts_service: PostsService = Depends(get_post_service),
) -> ListPostsUseCase:
    return ListPostsUseCase(posts_service=posts_service)
