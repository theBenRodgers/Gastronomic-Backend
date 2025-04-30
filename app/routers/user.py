from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.db.users_table import *
from app.schemas.models.user import User
from app.config import get_firebase_user_from_token

router = APIRouter()

@router.get("/user", response_model=User)
async def get_user(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    uid = user["uid"]
    user = select_user(uid)
    return user

@router.post("/user")
async def create_user_endpoint(user: Annotated[dict, Depends(get_firebase_user_from_token)], u: User):
    uid = user["uid"]
    insert_user(uid)
    return {"result": "User created"}

@router.put("/user")
async def update_user(user: Annotated[dict, Depends(get_firebase_user_from_token)], u: User):
    uid = user["uid"]
    update_user(uid, u)
    return {"result": "User updated"}

@router.delete("/user")
async def delete_user(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    uid = user["uid"]
    delete_user(uid)
    return {"result": "User deleted"}
