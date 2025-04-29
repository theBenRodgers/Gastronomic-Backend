from fastapi import APIRouter, Depends
from typing import Annotated
from app.services.lookup import lookup
from app.config import get_firebase_user_from_token
from app.db.user import *
from app.schemas.models.user import User

router = APIRouter()

@router.get("/user")
async def get_user(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    uid = user["uid"]
    data = select_user(uid)[0]
    return data

@router.post("/user")
async def create_user(user: Annotated[dict, Depends(get_firebase_user_from_token)], u: User):
    uid = user["uid"]
    insert_user(uid, u)
    return {'result' : 'User Created'}

@router.put("/user")
async def change_user(user: Annotated[dict, Depends(get_firebase_user_from_token)], u: User):
    uid = user["uid"]
    update_user(uid, u)
    return {'result' : 'User Updated'}