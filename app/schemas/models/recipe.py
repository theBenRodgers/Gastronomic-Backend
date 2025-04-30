from pydantic import BaseModel
from typing import List, Optional

from app.schemas.models.instruction import Instruction
from app.schemas.models.pantry_item import PantryItem
from app.schemas.models.nutrition import Nutrition


class Recipe(BaseModel):
    id: int
    name: str
    image: str

    servings: Optional[int] = None
    readyInMinutes: Optional[int] = None
    preparationMinutes: Optional[int] = None
    cookingMinutes: Optional[int] = None

    ingredients: Optional[List[PantryItem]] = None
    missedIngredientCount: Optional[int] = None
    missedIngredients: Optional[List[PantryItem]] = None
    usedIngredientCount: Optional[int] = None
    usedIngredients: Optional[List[PantryItem]] = None

    instructions: Optional[List[Instruction]] = None
    nutrition: Optional[Nutrition] = None

    cuisines: Optional[List[str]] = None
    dishTypes: Optional[List[str]] = None
    occasions: Optional[List[str]] = None

    sourceUrl: Optional[str] = None