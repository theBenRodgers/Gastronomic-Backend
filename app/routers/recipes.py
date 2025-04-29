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

@router.get("/recipes/search", response_model=List[Recipe])
async def search_recipes(user: Annotated[dict, Depends(get_firebase_user_from_token)], r : RecipeRequest):
    uid = user["uid"]
    user = select_user(uid)

    cuisine = ",".join(r.cuisine) if r.cuisine else "",
    ingredients = ",".join(r.ingredients) if r.ingredients else "",
    mtype = ",".join(r.mtype) if r.mtype else "",
    diets = ",".join(user.diets) if user.diets else "",
    intolerances = ",".join(user.intolerances) if user.intolerances else "",
    return search_recipes(r.query, cuisine, diets, intolerances, ingredients, mtype, 1)

@router.get("/recipes")
async def get_recipes(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    pass

