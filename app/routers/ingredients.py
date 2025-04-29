from fastapi import APIRouter, Depends
from typing import Annotated
from app.config import get_firebase_user_from_token
from app.db.ingredients import *
from app.api.spoonacular.spoon_ingredients import *

router = APIRouter()

@router.get("/ingredients/search")
async def search(user: Annotated[dict, Depends(get_firebase_user_from_token)], query: str, page:int):
    info = ingredient_search(query, page)
    return info

@router.get("/ingredients/info")
async def info(user: Annotated[dict, Depends(get_firebase_user_from_token)], id:int):
    return ingredient_info(id)

@router.get("/ingredients/extra")
async def nutrition(user: Annotated[dict, Depends(get_firebase_user_from_token)], id:int, unit:str):
    return ingredient_extra(id, unit)
