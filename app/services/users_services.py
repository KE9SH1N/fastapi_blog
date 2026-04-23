from sqlalchemy.orm import Session


from app.schemas import users_schemas
from app.models import users_models



def create_user(db: Session, user: users_schemas.UserCreate):
    db_user = users_models.User(email=user.email, hashed_password=user.hashed_password, user_name=user.user_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(users_models.User).filter(users_models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users_models.User).offset(skip).limit(limit).all()


def delete_user(db: Session, user_id: int):
    db_user = db.query(users_models.User).filter(users_models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def get_users_by_name(db: Session, name: str):
    query = db.query(users_models.User)

    if name:
        query = query.filter(users_models.User.name.ilike(f"%{name}%"))

    return query.all()