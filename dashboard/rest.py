import requests
base_url = 'http://localhost:8090/'

def get_all(name):
    url = base_url + name
    response = requests.get(url)
    return response