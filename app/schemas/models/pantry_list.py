from typing import Optional, List
from pydantic import BaseModel
from app.schemas.models.pantry_item import PantryItem


class PantryList(BaseModel):
    results: List[PantryItem]
    page: int
    totalPages: int
