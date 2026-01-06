from sqlmodel import Session, select
from src.internal.posts.models import Post


class PostsRepository:
    def __init__(self, DBSession: Session):
        self.session = DBSession

    def get_all_posts(self, user_id: int):
        return self.session.exec(select(Post).where(Post.user_id == user_id)).all()

    def add_post(self, post):
        pass
