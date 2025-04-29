from app.api.spoonacular.make_request import *

def product_search(query: str, page):
    url = f"https://api.spoonacular.com/food/products/search"
    offset = (page * NUMBER) - NUMBER
    params = {
        "query": query,
        "addProductInformation": True,
        "offset": offset,
        "number": NUMBER
    }
    data = make_request(url, params=params)
    totalPages = data["totalProducts"] // NUMBER
    if (data["totalProducts"] % NUMBER > 0):
        totalPages = totalPages + 1

    results = []
    for r in data.get("products"):
        nutrients = {n['name'].lower(): n['amount'] for n in r.get('nutrition', {}).get('nutrients', [])}
        result = {
            "kind": "product",
            "id": r.get('id'),
            "name": r.get('title'),
            "brand": r.get('brand'),
            "imageType": r.get('imageType'),
            "upc": r.get('upc'),
            "price": r.get('price'),
            "breadcrumbs": r.get('breadcrumbs', []),
            "category": r.get('category'),
            "calories": nutrients.get('calories'),
            "protein": nutrients.get('protein'),
            "fat": nutrients.get('fat'),
            "carbs": nutrients.get('carbohydrates')
        }
        results.append(result)
    return {
        "results": results,
        "page": page,
        "totalPages": totalPages
    }


def prod_by_upc(upc: int):
    url = "https://api.spoonacular.com/food/products/upc/{upc}"
    data = make_request(url)
    nutrients = {n['name'].lower(): n['amount']
                 for n in data.get('nutrition', {}).get('nutrients', [])}
    return {
        "kind": "product",
        "id": data.get('id'),
        "name": data.get('title'),
        "brand": data.get('brand'),
        "imageType": data.get('imageType'),
        "upc": data.get('upc'),
        "price": data.get('price'),
        "breadcrumbs": data.get('breadcrumbs', []),
        "category": data.get('category'),
        "calories": nutrients.get('calories'),
        "protein": nutrients.get('protein'),
        "fat": nutrients.get('fat'),
        "carbs": nutrients.get('carbohydrates'),
    }

