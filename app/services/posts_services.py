from sqlalchemy.orm import Session

from app.models import posts_models
from app.schemas import posts_schemas
from app.core.pagination import paginate_model
from app.repositories.posts_repository import PostsRepository



def create_post(db: Session, post: posts_schemas.PostCreate):
    db_post = posts_models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, limit: int, offset: int, dir:str):
    return paginate_model(posts_models.Post, db, limit, offset, dir)

def get_all_posts(db: Session):
    return PostsRepository.get_all_desc(db)


def get_post_by_id(db: Session, post_id: int):
    return PostsRepository.get_post_by_id(db, post_id)
