from pydantic import BaseModel
from typing import List, Optional
from .ingredient import Ingredient

class Recipe(BaseModel):
    id: int
    image: str
    imageType: str
    likes: int
    missedIngredientCount: int
    missedIngredients: List[Ingredient]
    title: str
    ingredients: List[Ingredient]
    instructions: str
    prep_time: Optional[int] = None
    cook_time: Optional[int] = None
    servings: Optional[int] = None
    calories: Optional[int] = None
    protein: Optional[int] = None
    fat: Optional[int] = None
    carbs: Optional[int] = None
    source_url: Optional[str] = None