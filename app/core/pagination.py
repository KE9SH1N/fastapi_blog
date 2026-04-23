from sqlalchemy.orm import Session
import math

def paginate_model(model, db: Session, limit: int = 10, offset: int = 0, dir: str = "desc"):
    query = db.query(model)
    if dir == "desc":
        query = query.order_by(model.created_at.desc())
    else:
        query = query.order_by(model.created_at.asc())
    total = query.count()
    items = query.limit(limit).offset(offset).all()

    current_page = (offset // limit) + 1
    total_pages = math.ceil(total / limit)

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "current_page": current_page,
        "total_pages": total_pages,
        "data": items
    }