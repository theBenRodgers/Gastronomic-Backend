from pydantic import BaseModel

class Ingredient(BaseModel):
    name: str
    brand: str
    servings: int | None = 1
    amount: int | None = 0
    calories: int | None = None
    protein: int | None = None
    fat: int | None = None
    carbs: int | None = None