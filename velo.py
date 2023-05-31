import random
from json_parser import *
from velo import *
import json

class Velo():
    def __init__(self, stations, gebruikers, fietsen, transporteurs):
        self.stations = stations
        self.gebruikers = gebruikers
        self.fietsen = fietsen
        self.transporteurs = transporteurs

    def __str__(self):
        return f"Velo heeft {len(self.stations)} stations, {len(self.gebruikers)} gebruikers, {len(self.fietsen)} fietsen en {len(self.transporteurs)} transporteurs."

    def getRandom(list):
        return random.choice(list)

    def maak_stations():
        stationFile = json_naar_dictionary("velo.geojson")
        stations = []
        for station in stationFile["features"]:
            info = station["properties"]
            newStation = Station(aantalPlaatsen=info["Aantal_plaatsen"], naam=info["Naam"])
            stations.append(newStation)
        return stations
    
    def maak_fietsen():
        fietsen = []
        for i in range(1, 4200):
            newFiets = Fiets()
            fietsen.append(newFiets)
        return fietsen
    
    def maak_gebruikers():
        with open("users.json", "r") as f:
            users = json.load(f)
        gebruikers = []
        for newGebruiker in range(1, 500):
            newGebruiker = Gebruiker(range(1, 500), random.choice(users), [])
            gebruikers.append(newGebruiker)
        return gebruikers
    
    def maak_transporteurs():
        transporteurs = []
        for newTransporteur in range(1, 10):
            newTransporteur = Transporteur()
            transporteurs.append(newTransporteur)
        return transporteurs
    
    def maak_transporteurs():
        transporteurs = []
        for newTransporteur in range(1, 10):
            newTransporteur = Transporteur()
            transporteurs.append(newTransporteur)
        return transporteurs

class Station():
    def __init__(self, naam, locatie, aantalPlaatsen):
        self.naam = naam
        self.locatie = locatie
        self.slots = []
        for i in range(aantalPlaatsen):
            self.slots.append(Slot())
    
    def __str__(self):
        return f"Station {self.naam} op locatie {self.locatie} \n met {len(self.slots)}"

    def verwijder_fiets (self, fiets):
        self.fiets = fiets

    def voeg_gebruiker_toe (self, gebruiker):
        self.gebruiker = gebruiker

    def verwijder_gebruiker (self, gebruiker):
        self.gebruiker = gebruiker

class Slot():
    def __init__(self, ID, status, fiets):
        self.ID = ID
        self.status = status
        self.fiets = fiets

    def maak_bezet (self, slot, fiets):
        self.slot = slot
        self.fiets = fiets

    def maak_vrij (self, slot):
        self.slot = slot

class Fiets():
    def __init__(self, ID, status, slot, gebruiker):
        self.ID = ID
        self.status = status
        self.slot = slot
        self.gebruiker = gebruiker

    def maak_uitgeleend(self, fiets, gebruiker, slot):
        self.fiets = fiets
        self.gebruiker = gebruiker
        self.slot = slot

    def maak_beschikbaar(self, fiets):
        self.fiets = fiets

class Gebruiker():
    def __init__(self, ID, Naam, lijst_fietsen):
        self.ID = ID
        self.naam = Naam
        self.lijst_fietsen = lijst_fietsen

    def leen_fiets (self, gebruiker, fiets):
        self.gebruiker = gebruiker
        self.fiets = fiets

    def Breng_fiets_terug (self, gebruiker, fiets):
        self.fiets = fiets
        self.gebruiker = gebruiker

class Transporteur():
    def __init__(self, naam, camion, fietsen):
        self.naam = naam
        self.camion = camion
        self.fietsen = fietsen


