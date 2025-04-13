from pydantic import BaseModel
from typing import List, Optional
from app.schemas.enums.intolerance import Intolerance
from app.schemas.enums.diet import Diet
class User(BaseModel):
    fname: str
    lname: str
    intolerances: List[Intolerance]
    diets: List[Diet]
