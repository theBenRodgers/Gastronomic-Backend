import requests
from constants import UPC_KEY

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

    return {
        'title': data.get('title', 'Unknown'),
        'brand': data.get('brand', 'Unknown'),
        'categories': data.get('categories', '').split(', '),
        'description': data.get('description', 'No description available'),
        'macros': {
            'calories': safe_int(data.get('metanutrition', {}).get('energy_value', 0)),
            'fat': safe_int(data.get('metanutrition', {}).get('fat_value', 0)),
            'carbs': safe_int(data.get('metanutrition', {}).get('carbohydrates_value', 0)),
            'protein': safe_int(data.get('metanutrition', {}).get('proteins_value', 0))
        },
    }