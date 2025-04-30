from app.api.spoonacular.make_request import *
from app.schemas.models.instruction import Instruction
from app.schemas.models.pantry_item import PantryItem
from app.schemas.models.recipe import Recipe


def search_recipes(query: str,
                   cuisine: str,
                   diets: str,
                   intolerances: str,
                   includeIngredients: str,
                   mtype: str,
                   page: int):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    offset = (page * NUMBER) - NUMBER
    params = {
        "query": query,
        "cuisine": cuisine,
        "diet": diets,
        "intolerances": intolerances,
        "includeIngredients": includeIngredients,
        "type": mtype,
        "fillIngredients": True,
        "addRecipeInformation": True,
        "addRecipeInstructions": True,
        "offset": offset,
        "number": NUMBER
    }
    data = make_request("GET", url, params)
    totalPages = data["totalResults"] // NUMBER
    if (data["totalResults"] % NUMBER > 0):
        totalPages = totalPages + 1

    results = data.get("results")

    recipes = []
    for r in results:
        ingredients = None
        missed = None
        used = None
        if (not (includeIngredients == "")):
            missed = []
            used = []
            for m in r.get('missedIngredients'):
                ing = PantryItem(
                    kind="ingredient",
                    id=m.get('id'),
                    name=m.get('name'),
                    image=m.get('image'),
                    amount=m.get('amount'),
                    unit=m.get('unit'),
                    aisle=m.get('aisle'),
                    meta=m.get('meta', [])
                )
                missed.append(ing)
            for m in r.get('usedIngredients'):
                ing = PantryItem(
                    kind="ingredient",
                    id=m.get('id'),
                    name=m.get('name'),
                    image=m.get('image'),
                    amount=m.get('amount'),
                    unit=m.get('unit'),
                    aisle=m.get('aisle'),
                    meta=m.get('meta', [])
                )
                used.append(ing)
        else:
            ingredients = []
            for m in r.get('usedIngredients'):
                ing = PantryItem(
                    kind="ingredient",
                    id=m.get('id'),
                    name=m.get('name'),
                    image=m.get('image'),
                    amount=m.get('amount'),
                    unit=m.get('unit'),
                    aisle=m.get('aisle'),
                    meta=m.get('meta', [])
                )

        instructions = []
        for i in data.get('analyzedInstructions').get('steps', []):
            ings = []
            for m in i.get('ingredients', []):
                ing = PantryItem(
                    kind="ingredient",
                    id=m.get('id'),
                    name=m.get('name'),
                    image=m.get('image')
                )
            ins = Instruction(
                number=i.get('number'),
                step=i.get('step'),
                ingredients=ings
            )
            instructions.append(ins)

        recipe = Recipe(
            id=r.get('id'),
            name=r.get('title'),
            image=r.get('image'),

            servings=r.get(''),
            readyInMinutes=r.get('readyInMinutes'),
            preparationMinutes=r.get('preparationMinutes'),
            cookingMinutes=r.get('cookingMinutes'),

            ingredients=ingredients,
            missedIngredientCount=r.get('missedIngredientCount'),
            missedIngredients=missed,
            usedIngredientCount=r.get('usedIngredientCount'),
            usedIngredients=used,

            instructions=instructions,

            cuisines=r.get('cuisines'),
            dishTypes=r.get('dishTypes'),
            occasions=r.get('occasions'),

            sourceUrl=r.get('sourceUrl')
        )
        recipes.append(recipe)

    return recipes


def recipe_by_id(id: int):
    url = f"https://api.spoonacular.com/recipes/{id}/information"
    data = make_request(url)
