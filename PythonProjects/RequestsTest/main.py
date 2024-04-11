import requests 

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
json = {
    "name": "Бэндер",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},

              headers={'Content-Type': 'application/json', 'trainer_token': '85577d38354252abb2f9ad43d0a492ad'})

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
json = {
    "pokemon_id": "29625",
    "name": "Гомер",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"

},

              headers={'Content-Type': 'application/json', 'trainer_token': '85577d38354252abb2f9ad43d0a492ad'})

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
json = {
    "pokemon_id": "29625"
},

              headers={'Content-Type': 'application/json', 'trainer_token': '85577d38354252abb2f9ad43d0a492ad'})

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')