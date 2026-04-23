from sqlalchemy.orm import Session

from app.models import posts_models
from app.schemas import posts_schemas



def create_post(db: Session, post: posts_schemas.PostCreate):
    db_post = posts_models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post