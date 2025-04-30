from typing import List
from pydantic import BaseModel

class User(BaseModel):
    fname: str
    lname: str
    intolerances: List[str] = []
    diets: List[str] = []
