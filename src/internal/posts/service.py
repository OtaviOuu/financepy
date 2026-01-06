class PostsService:
    def get_posts(self):
        return [{"id": 1, "title": "First Post"}, {"id": 2, "title": "Second Post"}]

    def create_post(self, title: str):
        new_post = {"id": 3, "title": title}

        return new_post
