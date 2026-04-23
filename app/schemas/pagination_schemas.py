from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    limit: int
    offset: int
    current_page: int
    total_pages: int
    data: List[T]