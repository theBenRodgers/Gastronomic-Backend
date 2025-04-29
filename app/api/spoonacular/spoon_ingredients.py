from app.api.spoonacular.make_request import *


def ingredient_search(query: str, page):
    '''
    returns
    {
        "results": [
            {
                "kind": string,
                "id": int,
                "name": string,
                "image": string
            }
        ],
        "page": int,
        "totalPages": int
    }
    '''

    url = f"https://api.spoonacular.com/food/ingredients/search"
    offset = (page * NUMBER) - NUMBER
    params = {
        "query": query,
        "offset": offset,
        "number": NUMBER
    }
    data = make_request(url, params)
    print(data)
    totalPages = data.get("totalResults") // NUMBER
    if (data.get("totalResults") % NUMBER > 0):
        totalPages = totalPages + 1

    results = []
    for r in data.get("results"):
        result = {
            "kind": "ingredient",
            "id": r.get('id'),
            "name": r.get('name'),
            "image": r.get('image')
        }
        results.append(result)

    return {
        "results": results,
        "page": page,
        "totalPages": totalPages
    }


def ingredient_info(id: int):
    '''
    returns
    {
        "id": int,
        "name": string,
        "possibleUnits": [string],
        "shoppingListUnits": [string],
        "aisle": string,
    }
    '''
    url = f"https://api.spoonacular.com/food/ingredients/{id}/information"
    data = make_request(url)
    print(data.get('possibleUnits', []))
    return {
        "possibleUnits": data.get('possibleUnits', []),
        "shoppingListUnits": data.get('shoppingListUnits', []),
        "aisle": data.get('aisle'),
        "categoryPath": data.get('categoryPath', [])
    }


def ingredient_extra(id: int, unit: str):
    url = f"https://api.spoonacular.com/food/ingredients/{id}/information"
    params = {
        "amount": 1,
        "unit": unit
    }
    data = make_request(url, params=params)
    nutrients = {n['name'].lower(): n['amount']
                 for n in data.get('nutrition', {}).get('nutrients', [])}
    return {
        "calories": nutrients.get('calories'),
        "protein": nutrients.get('protein'),
        "fat": nutrients.get('fat'),
        "carbs": nutrients.get('carbohydrates'),
        "estimatedCost": data.get('estimatedCost').get('value'),
        "weightPerServing": data.get('nutrition').get('weightPerServing').get('amount')
    }
