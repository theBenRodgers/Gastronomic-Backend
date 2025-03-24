from fastapi import APIRouter, Depends
from typing import Annotated
from app.schemas.ingredient import Ingredient
from app.services.lookup import lookup
from app.config import get_firebase_user_from_token
from app.db.ingredients import *

router = APIRouter()

@router.get("/ingredients")
async def get_ingredients(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    uid = user["uid"]
    return select_ingredients(uid)

@router.post("/ingredients")
async def create_ingredient(user: Annotated[dict, Depends(get_firebase_user_from_token)], ingredient: Ingredient):
    uid = user["uid"]
    insert_ingredient(uid, ingredient)
    return {'result' : 'Ingredient Created'}

@router.get("/ingredients/upc")
async def get_from_upc(user: Annotated[dict, Depends(get_firebase_user_from_token)], upc: str):
    uid = user["uid"]
    ingredient = lookup(upc)
    insert_ingredient(uid, ingredient)
    return {'result' : 'Ingredient Created'}

@router.put("/ingredients")
async def change_ingredient(user: Annotated[dict, Depends(get_firebase_user_from_token)], ingredient: Ingredient, iid : int):
    uid = user["uid"]
    update_ingredient(uid, iid, ingredient)
    return {'result' : 'Ingredient Updated'}

@router.delete("/ingredients")
async def remove_ingredient(user: Annotated[dict, Depends(get_firebase_user_from_token)], iid : int):
    uid = user["uid"]
    delete_ingredient(uid, iid)
    return {'result' : 'Ingredient Deleted'}
