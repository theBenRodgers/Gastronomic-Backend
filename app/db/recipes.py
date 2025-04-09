from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import requests
from app.config import get_firebase_user_from_token 
from .schemas.recipe import Recipe
from .schemas.ingredient import Ingredient

router = APIRouter()

SPOONACULAR_API_KEY = "e7c9b3ec20df45f5afaf1e18f3bfe0d7"
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"


# Pydantic model to accept ingredients input
class IngredientsRequest(BaseModel):
    ingredients: str  # Comma-separated ingredients


# Endpoint to fetch recipes from Spoonacular API based on ingredients
@router.get("/search-recipes", response_model=List[Recipe])
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

        # Transform the raw response into a list of Recipe objects
        recipe_list = []
        for recipe in recipes:
            # Assuming Spoonacular returns a list of ingredients as strings in the recipe
            ingredients_list = [
                Ingredient(name=ingredient) for ingredient in recipe.get('ingredients', [])
            ]
            # Construct the Recipe object
            recipe_data = Recipe(
                title=recipe['title'],
                ingredients=ingredients_list,
                instructions=recipe['instructions'],
                prep_time=recipe.get('prep_time'),
                cook_time=recipe.get('cook_time'),
                servings=recipe.get('servings'),
                calories=recipe.get('calories'),
                protein=recipe.get('protein'),
                fat=recipe.get('fat'),
                carbs=recipe.get('carbs'),
                source_url=recipe.get('source_url')
            )
            recipe_list.append(recipe_data)

        return recipe_list  # Return the list of Recipe objects
    else:
        raise HTTPException(status_code=500, detail="Failed to fetch recipes from Spoonacular")
