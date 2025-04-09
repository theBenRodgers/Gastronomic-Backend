from fastapi import APIRouter, Depends, HTTPException
from typing import List
import requests
from app.config import get_firebase_user_from_token
from .schemas.recipe import Recipe
from .schemas.ingredient import Ingredient

router = APIRouter()

SPOONACULAR_API_KEY = "e7c9b3ec20df45f5afaf1e18f3bfe0d7"
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"

@router.get("/search-recipes", response_model=List[Recipe])
async def search_recipes(ingredients: str, user: dict = Depends(get_firebase_user_from_token)):
    print(f"Searching recipes for: {ingredients}")  # Debugging

    response = requests.get(SPOONACULAR_API_URL, params={
        "ingredients": ingredients,
        "apiKey": SPOONACULAR_API_KEY,
        "number": 5  # Limit results
    })

    print(f"Status Code: {response.status_code}")  # Check response status
    print(f"Response: {json.dumps(response.json(), indent=2)}")  # Pretty-print JSON

    if response.status_code == 200:
        recipes = response.json()

        if not recipes:  
            raise HTTPException(status_code=404, detail="No recipes found from Spoonacular")

        # Convert Spoonacular's response into Recipe objects
        recipe_list = []
        for recipe in recipes:
            ingredients_list = [
                Ingredient(name=ing["name"]) for ing in recipe.get('usedIngredients', []) + recipe.get('missedIngredients', [])
            ]
            recipe_data = Recipe(
                title=recipe['title'],
                ingredients=ingredients_list,
                source_url=recipe.get('sourceUrl')  # Corrected field
            )
            recipe_list.append(recipe_data)

        return recipe_list

    else:
        raise HTTPException(status_code=response.status_code, detail=f"Spoonacular API Error: {response.text}")
