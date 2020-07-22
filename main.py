from flask import Flask
import requests
from pokecard import Pokecard
import json

app = Flask(__name__)

@app.route('/pokecards')
def hello_world():
    cards = list()
    response = json.loads(requests.get('https://api.pokemontcg.io/v1/cards?name=charizard').content)['cards']
    print(response[0]['id'])
    for card in response:
        cards.append(str(Pokecard(card['id'], card['name'], card['series'], card['set'])))
    return ' -------- '.join(cards)