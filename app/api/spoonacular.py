import requests
from app.schemas.models.ingredient import Ingredient
from app.schemas.models.basic_recipe import BasicRecipe
from app.schemas.models.product import Product
from app.schemas.enums.aisle import Aisle
from app.schemas.enums.badge import Badge
from app.schemas.enums.intolerance import Intolerance
from app.schemas.enums.cuisine import Cuisine
from app.schemas.enums.mealtype import MealType
from app.schemas.enums.diet import Diet
from app.config import SPOONACULAR_API_KEY

def make_request(method:str, url:str, params:dict[str, str | None]):
    r = requests.request(method, url, params=params)
    code = r.status_code
    if (code == 200):
        return r.json()
    raise Exception(code)
    
def get_by_upc(upc:int)->Product:
    url = "https://api.spoonacular.com/food/products/upc/{upc}"
    params = {
        "apiKey" : SPOONACULAR_API_KEY
    }
    data = make_request("GET", url, params)
    nutrients = {n['name'].lower(): n['amount'] for n in data.get('nutrition', {}).get('nutrients', [])}
    ingredient_list = [ingredient.strip() for ingredient in data.get('ingredientList', '').split(',') if ingredient.strip()]
    return Product(
        sp_prod_id=data.get('id'),
        title=data.get('title'),
        brand=data.get('brand'),
        badges=[Badge(b) for b in data.get('badges', [])],
        importantBadges=[Badge(b) for b in data.get('importantBadges', [])],
        breadcrumbs=data.get('breadcrumbs', []),
        category=data.get('category'),
        aisle=Aisle(data['aisle']) if data.get('aisle') else None,
        price=data.get('price', 0.0),
        ingredientCount=data.get('ingredientCount'),
        ingredientList=ingredient_list,
        expiration=None,
        serving_no=data.get('servings', {}).get('number'),
        serving_size=data.get('servings', {}).get('size'),
        servings_unit=data.get('servings', {}).get('unit'),
        calories=nutrients.get('calories'),
        protein=nutrients.get('protein'),
        fat=nutrients.get('fat'),
        carbs=nutrients.get('carbohydrates'),
        amount=0.0  # Default value; adjust as needed
    )

def search_recipes(query:str, 
                   cuisine:list[Cuisine], 
                   excludeCuisine:list[Cuisine],
                   diet:list[Diet],
                   intolerances:list[Intolerance],
                   includeIngredients:list[str],
                   excludeIngredients:list[str],
                   mtype:MealType,
                   offset:int,
                   number:int):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "query": query,
        "cuisine": ",".join(c.value for c in cuisine) if cuisine else None,
        "excludeCuisine": ",".join(c.value for c in excludeCuisine) if excludeCuisine else None,
        "diet": ",".join(c.value for c in diet) if diet else None,
        "intolerances": ",".join(c.value for c in intolerances) if intolerances else None,
        "includeIngredients": ",".join(c.value for c in includeIngredients) if includeIngredients else None,
        "excludeIngredients": ",".join(c.value for c in excludeIngredients) if excludeIngredients else None,
        "type": mtype,
        "offset": offset,
        "number": number
    }
    data = make_request("GET", url, params).get('results')

    r_list = []

    for r in data:
        recipe = BasicRecipe(
                    id=r.get('id'),
                    title=r.get('title'),
                    image=r.get('image'),
                    imageType=r.get('imageType'))
        
        r_list.append(recipe)

    return r_list

def recipe_by_id(id:int):
    url = f"https://api.spoonacular.com/recipes/{id}/information"
    params = {
        "apiKey" : SPOONACULAR_API_KEY
    }
    data = make_request("GET", url, params)
