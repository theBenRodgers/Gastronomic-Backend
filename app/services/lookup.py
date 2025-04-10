import requests
from app.config import UPC_KEY
from app.schemas.ingredient import Ingredient

def lookup(upc):

    url = "https://api.upcdatabase.org/product/{}?apikey={}".format(upc, UPC_KEY)
    response = requests.request("GET", url)
    data = response.json()
    return parse(data)

def verify(data):
    return not ("error" in data or data['category'].lower() != 'food')

def parse(data):
    if not verify(data):
        return None

    def safe_int(value):
        try:
            return int(float(value))
        except ValueError:
            return 0
    
    info = {
        'title': data.get('title', 'Unknown'),
        'brand': data.get('brand', 'Unknown'),
        'calories': safe_int(data.get('metanutrition', {}).get('energy_value', 0)),
        'fat': safe_int(data.get('metanutrition', {}).get('fat_value', 0)),
        'carbs': safe_int(data.get('metanutrition', {}).get('carbohydrates_value', 0)),
        'protein': safe_int(data.get('metanutrition', {}).get('proteins_value', 0))
        }
    
    return Ingredient(name=info['name'],
                        brand=info['brand'],
                        calories=info['calories'],
                        fat=info['fat'],
                        carbs=info['carbs'],
                        protein=info['protein'])
     
    