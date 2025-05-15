from fastapi import APIRouter, Depends
from typing import Annotated, List
from app.config import get_firebase_user_from_token
from app.schemas.models.recipe import Recipe
from app.api.spoonacular.spoon_recipes import *
from app.schemas.models.recipe_request import RecipeRequest
from app.db.users_table import select_user

router = APIRouter()

@router.get("/recipes")
async def get_recipes(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    pass

@router.post("/recipes/search", response_model=List[Recipe])
async def search_recipes(user: Annotated[dict, Depends(get_firebase_user_from_token)], ingredients: str):
    uid = user["uid"]
    return spoon_r_s(ingredients)

@router.get("/recipes")
async def get_recipes(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    pass

