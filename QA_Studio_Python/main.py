import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1b208a8a403ebb066ee65c84bebd8adf'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Буль",
    "photo_id": 126
}

body_change = {
    "pokemon_id": "375199",
    "name": "Питон"
}

body_pokeball = {
    "pokemon_id": "375199"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)