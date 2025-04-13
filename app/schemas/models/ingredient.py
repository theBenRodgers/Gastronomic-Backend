import datetime
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.enums.aisle import Aisle
from app.schemas.enums.badge import Badge

class Ingredient(BaseModel):
    spoonacular_id: int
    title: str
    image: Optional[str]
    aisle: Aisle
    badges: List[Badge]
    brand: str
    expiration: Optional[List[datetime.date]]
    servings: float | None = 1
    amount: float | None = 0
    calories: float | None = None
    protein: float | None = None
    fat: float | None = None
    carbs: float | None = None