from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./financepy.db"  # ou PostgreSQL, MySQL, etc.
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para debug


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
