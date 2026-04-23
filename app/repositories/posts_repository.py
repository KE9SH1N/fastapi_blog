from sqlalchemy.orm import Session
from app.models import posts_models


class PostsRepository:

    @staticmethod
    def get_all_desc(db: Session):
        return (
            db.query(posts_models.Post)
            .order_by(posts_models.Post.created_at.desc())
            .all()
        )
    
    @staticmethod
    def get_post_by_id(db: Session, post_id: int):
        return db.query(posts_models.Post).filter(posts_models.Post.id == post_id).first()