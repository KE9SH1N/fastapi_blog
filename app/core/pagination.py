from sqlalchemy.orm import Session
import math

def paginate_model(model, db: Session, limit: int = 10, offset: int = 0):
    query = db.query(model)
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