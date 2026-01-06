from src.internal.posts.service import PostsService


class ListPostsUseCase:
    def __init__(self, posts_service: PostsService):
        self.posts_service = posts_service

    def execute(self):
        return self.posts_service.list_posts()
