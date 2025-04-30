import requests

def getToken():
    key = "AIzaSyCrqUozVlJPhEzWLlwWBuYEFYNNrKHHLIA"
    email = "benrodgers0@gmail.com"
    password = "8&9Ncdj@"
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={key}"
    data = {
        "email": email,
        "password": password
    }
    r = requests.post(url, json=data)
    return r.json()['idToken']

def makeRequest(method, url):
    url = f"http://127.0.0.1:8000{url}"
    requests.request(method, url)
