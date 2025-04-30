from pydantic import BaseModel

class BasicRecipe(BaseModel):
    id: int
    title: str
    image: str
    imageType: str