import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'


def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id' : 4047})
    assert response.status_code == 200



def test_name():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id' : 4047})
    assert response.json()['trainer_name'] == 'generate'