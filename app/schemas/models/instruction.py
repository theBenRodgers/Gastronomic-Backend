from pydantic import BaseModel
from typing import List, Optional

from app.schemas.models.pantry_item import PantryItem

class Instruction(BaseModel):
    number: int
    step: str
    ingredients: Optional[List[PantryItem]] = None