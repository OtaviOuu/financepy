from sqlmodel import Session, select
from src.internal.posts.models import Post


class PostsRepository:
    def __init__(self, DBSession: Session):
        self.session = DBSession

    def get_all_posts(self):
        return self.session.exec(select(Post)).all()

    def add_post(self, post):
        pass
