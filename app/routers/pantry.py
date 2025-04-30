from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.config import get_firebase_user_from_token
from app.db.pantry_table import *
from app.schemas.models.pantry_item import PantryItem



router = APIRouter()

@router.get("/pantry")
async def get_pantry(user: Annotated[dict, Depends(get_firebase_user_from_token)], ):
    uid = user["uid"]
    results = select_pantry(uid)
    return results

@router.get("/pantry/item")
async def get_pantry(user: Annotated[dict, Depends(get_firebase_user_from_token)], 
                     pantry_id: int):
    uid = user["uid"]
    return select_pantry_item(uid, pantry_id)
    
@router.post("/pantry")
async def add_pantry_item(user: Annotated[dict, Depends(get_firebase_user_from_token)], 
                     item: PantryItem):
    uid = user["uid"]
    create_pantry_item(uid, item)
    return {'result' : 'Pantry Item Added'}

@router.put("/pantry")
async def change_pantry_item(user: Annotated[dict, Depends(get_firebase_user_from_token)], 
                             item: PantryItem):
    if item.pantry_id == None:
        raise HTTPException(status_code=400, detail="No pantry_id")
    uid = user["uid"]
    update_pantry_item(uid, item)
    return {'result' : 'Pantry Item Changed'}

@router.delete("/pantry")
async def delete_pantry_item(user: Annotated[dict, Depends(get_firebase_user_from_token)], 
                             pantry_id: int):
    uid = user["uid"]
    delete_pantry_item(uid, pantry_id)
    return {'result' : 'Pantry Item Deleted'}
