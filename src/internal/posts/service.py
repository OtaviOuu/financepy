from src.internal.posts.repository import PostsRepository
from fastapi import Depends
from sqlmodel import Session
from src.database.db import get_session


class PostsService:
    def __init__(self, session: Session):
        self.repository = PostsRepository(session)

    def list_posts(self):
        return self.repository.get_all_posts()

    def create_post(self, title: str):
        new_post = {"id": 3, "title": title}

        return new_post


def get_post_service(session: Session = Depends(get_session)) -> PostsService:
    return PostsService(session=session)
