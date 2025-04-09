from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import requests
from app.config import get_firebase_user_from_token

router = APIRouter()

SPOONACULAR_API_KEY = "e7c9b3ec20df45f5afaf1e18f3bfe0d7"
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"


# Pydantic model to accept ingredients input
class IngredientsRequest(BaseModel):
    ingredients: str  # Comma-separated ingredients


# Endpoint to fetch recipes from Spoonacular API based on ingredients
@router.get("/search-recipes", response_model=dict)
async def search_recipes(ingredients: str, user: dict = Depends(get_firebase_user_from_token)):
    # Log the ingredients to verify it's being received
    print("Received ingredients:", ingredients)
    
    # Send request to Spoonacular API
    response = requests.get(SPOONACULAR_API_URL, params={
        "ingredients": ingredients,
        "apiKey": SPOONACULAR_API_KEY,
        "number": 10
    })

    # Check if the request was successful
    if response.status_code == 200:
        recipes = response.json()
        return {"recipes": recipes}
    else:
        # Log the response content for debugging
        print("Spoonacular API error:", response.text)
        raise HTTPException(status_code=500, detail="Failed to fetch recipes from Spoonacular")
