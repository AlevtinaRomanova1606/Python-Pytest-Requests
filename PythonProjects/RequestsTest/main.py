import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_create = {
    
    "name": "Пеночка",
    "photo": "generate"
}
body_newname = {
    
    "pokemon_id": "47868",
    "name": "Pika"
}
body_pokeboll = {
    
    "pokemon_id": "47868"
}

'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER,json = body_create)
print(response_create.text)'''

'''response_newname = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_newname)
print(response_newname.text)'''

'''response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_pokeboll)
print(response_pokeboll.text)'''

