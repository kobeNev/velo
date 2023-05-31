import json
import random

with open('namenlijst.json') as json_file:
    data = json.load(json_file)

random_naam = random.choice(data[0:1000])

print(random_naam)
