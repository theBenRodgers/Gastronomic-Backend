import requests
from app.config import SPOONACULAR_API_KEY

NUMBER = 10

def make_request(url:str, params:dict[str, str | None] = {}, body = {}):
    params.update({'apiKey': SPOONACULAR_API_KEY})
    r = requests.get(url, params=params, json=body)
    code = r.status_code
    if (code == 200):
        return r.json()
    raise Exception(code)