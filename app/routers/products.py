from fastapi import APIRouter, Depends
from typing import Annotated
from app.schemas.models.ingredient import Ingredient
from app.config import get_firebase_user_from_token
from app.db.ingredients import *
from app.api.spoonacular.spoon_products import *

router = APIRouter()

@router.get("/products/search")
async def search_products(user: Annotated[dict, Depends(get_firebase_user_from_token)], query: str, page:int):
    info = product_search(query, page)
    return info

@router.get("products/upc")
async def search_upc(user: Annotated[dict, Depends(get_firebase_user_from_token)], upc: int):
    info = prod_by_upc(upc)
    return info