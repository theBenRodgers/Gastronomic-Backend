import datetime
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.enums.aisle import Aisle
from app.schemas.enums.badge import Badge

class Product(BaseModel):
    sp_prod_id: Optional[int]
    title: str
    brand: Optional[str]
    badges: List[Badge]
    importantBadges: List[Badge]
    breadcrumbs: List[str]
    category: Optional[str]
    aisle: Optional[Aisle]
    price: float
    ingredientCount: Optional[int]
    ingredientList: List[str]
    expiration: Optional[List[datetime.date]]
    serving_no: Optional[float]
    serving_size: Optional[float]
    servings_unit: Optional[str]
    calories: float | None = None
    protein: float | None = None
    fat: float | None = None
    carbs: float | None = None
    amount: float | None = 0