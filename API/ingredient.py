from pydantic import BaseModel

class Ingredient(BaseModel):
    user_id: int
    name: str
    servings: int | None = 1
    amount: int | None = 1
    calories: int | None = None
    protein: int | None = None
    fat: int | None = None
    carbs: int | None = None