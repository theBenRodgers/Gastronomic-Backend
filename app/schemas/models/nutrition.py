from pydantic import BaseModel
from typing import List, Optional

class Nutrient(BaseModel):
    name: str
    amount: float
    unit: str
    percentOfDailyNeeds: Optional[float] = None

class Nutrition(BaseModel):
    nutrients: List[Nutrient]