from pydantic import BaseModel
from typing import List, Optional
from .ingredient import Ingredient

class Recipe(BaseModel):
    title: str
    ingredients: List[Ingredient]  # Uses Ingredient schema
    instructions: str
    prep_time: Optional[int] = None  # Time in minutes
    cook_time: Optional[int] = None
    servings: Optional[int] = None
    calories: Optional[int] = None
    protein: Optional[int] = None
    fat: Optional[int] = None
    carbs: Optional[int] = None
    source_url: Optional[str] = None  # URL to the recipe source