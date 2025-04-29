from typing import Optional, List
from pydantic import BaseModel

class PantryItem(BaseModel):
    pantry_id: Optional[int] = None
    # Elements needed for list view
    kind: str
    id: int
    name: str

    # Ingredient
    image: Optional[str] = None

    # Product
    brand: Optional[str] = None
    imageType: Optional[str] = None

    # Ingredient specific extra information
    unit: Optional[str] = None
    possibleUnits: Optional[List[str]] = None
    estimatedCost: Optional[float] = None
    shoppingListUnits: Optional[List[str]] = None
    aisle: Optional[str] = None
    categoryPath: Optional[List[str]] = None
    weightPerServing: Optional[float] = None
    meta: Optional[List[str]] = None

    # Product specific extra information
    upc: Optional[str] = None
    price: Optional[float] = None
    breadcrumbs: Optional[List[str]] = None

    # Both
    calories: Optional[int] = None
    protein: Optional[int] = None
    fat: Optional[int] = None
    carbs: Optional[int] = None
    amount: Optional[int] = None
    expirationDate: Optional[str] = None
