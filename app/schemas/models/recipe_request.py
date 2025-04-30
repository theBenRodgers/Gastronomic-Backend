from typing import List, Optional
from pydantic import BaseModel

class RecipeRequest(BaseModel):
    query: Optional[str] = None
    cuisine: Optional[str] = None
    ingredients: Optional[List[str]] = None
    mtype: Optional[str] = None
    page: int