import random
import json

voornamen = ["Wolter","Gertruida","Teunis","Hendrikje","Gerritdina","Johannes","Geesken","Everhardus","Janne","Willemijn","Aaltje","Egbertus","Hermijntje","Bastiaan","Grietje","Leendert","Gesina","Klaaske","Albertus","Adriana"]
achternamen = ["Van der Linden", "White", "Hendrikszoon", "Brouwer", "De Vries", "Jansen", "Van den Berg", "Bosman", "Van Dijk", "Mulder", "Jacobsz", "Smit", "Gerritsen", "Pieterszoon", "Bakker", "Van Leeuwen", "Vos", "Hermans", "Kuipers", "Meijer", "Van der Meer"]

user = []

for i in range(1000):
    voornaam = random.choice(voornamen)
    achternaam = random.choice(achternamen)
    user.append(voornaam + ' ' + achternaam)

with open('namenlijst.json', 'w') as outfile:
    json.dump(user, outfile)