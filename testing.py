from velo import *
#Ik had nog al veel errors in mijn code
#omdat het omzetten van de geojson naar dictionalry niet lukte
#daarom heb ik deze soms vervange door de naam "Dirk Segers"

#spijtig genoeg heb ik ook te veel uitgesteld 
# om nog aan de omzetting en handmatige simulatie te beginnen

# Maak een Velo-object en initialiseer de klassen
velo = Velo([], [], [], [])
stations = Velo.maak_stations()
fietsen = Velo.maak_fietsen()
gebruikers = Velo.maak_gebruikers()
transporteurs = Velo.maak_transporteurs()

# Voeg enkele stations toe aan het Velo-object
Velo.stations = stations

# Voeg enkele fietsen toe aan het Velo-object
Velo.fietsen = fietsen

# Voeg enkele gebruikers toe aan het Velo-object
Velo.gebruikers = gebruikers

# Voeg enkele transporteurs toe aan het Velo-object
Velo.transporteurs = transporteurs

# Test de __str__-methode van het Velo-object
print(velo)

# Kies een willekeurig station uit de lijst
random_station = Velo.getRandom(velo.stations)
print(f"Willekeurig station: {random_station}")

# Test de functionaliteit van de Gebruiker-klasse
gebruiker = Velo.getRandom(velo.gebruikers)
fiets = Velo.getRandom(velo.fietsen)

print(f"Voor het lenen van de fiets: {gebruiker}")
gebruiker1 = Gebruiker("Dirk Segers") 
gebruiker1.leen_fiets(fiets_ID=fiets, station=random_station) 
print(f"Na het lenen van de fiets: {gebruiker}")

# Test de functionaliteit van de Transporteur-klasse
transporteur = Velo.getRandom(velo.transporteurs)
fietsen_voor_transport = Velo.getRandom(velo.fietsen)
station_voor_transport = Velo.getRandom(velo.stations)

transporteur = Transporteur("Dirk Segers")
transporteur.neem_fietsen(fietsen=fietsen_voor_transport)
print(f"Na het nemen van de fietsen: {transporteur}")

transporteur = Transporteur("Dirk Segers") 
transporteur.breng_fietsen(fietsen=fietsen_voor_transport)
print(f"Na het terugbrengen van de fietsen: {transporteur}")
