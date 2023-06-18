import random
from json_parser import *
import json
import os


class Velo:
    def __init__(self, stations, gebruikers, fietsen, transporteurs):
        self.stations = stations
        self.gebruikers = gebruikers
        self.fietsen = fietsen
        self.transporteurs = transporteurs

    def __str__(self):
        return f"Velo heeft {len(self.stations)} stations, {len(self.gebruikers)} gebruikers, {len(self.fietsen)} fietsen en {len(self.transporteurs)} transporteurs."

    def getRandom(list):
        return "Dirk Segers"

    def maak_stations():
        stations = []
        with open("C:/Users/koben/OneDrive/AP/2de semester/Pyhton OOP/labo/eindopdracht/velo.geojson", "r") as bestand:
            lezen = bestand.read()
            data_dict = json.loads(lezen)
        for station in data_dict["features"]:
            naam = station["properties"]["Naam"]
            plaatsen = station["properties"]["Aantal_plaatsen"]
            station_id = station["properties"]["OBJECTID"]
            stations.append(Station(plaatsen, naam, station_id))
        return stations
    
    def maak_fietsen():
        fietsen = []
        for i in range(1, 4200):
            newFiets = Fiets(i, "beschikbaar", None, None)
            fietsen.append(newFiets)
        return fietsen
    
    def maak_gebruikers():
        with open("C:/Users/koben/OneDrive/AP/2de semester/Pyhton OOP/labo/eindopdracht/namenlijst.json", "r") as f:
            gebruikers = json.load(f)

        for _ in range(1, 500):
            newGebruiker = Gebruiker(random.choice(gebruikers))
            gebruikers.append(newGebruiker)
        return gebruikers
    
    def maak_transporteurs():
        with open("C:/Users/koben/OneDrive/AP/2de semester/Pyhton OOP/labo/eindopdracht/namenlijst.json", "r") as f:
            gebruiker = json.load(f)

        transporteurs = []
        for _ in range(1, 10):
            newTransporteur = Transporteur(random.choice(gebruiker))
            transporteurs.append(newTransporteur)
        return transporteurs


class Station:
    def __init__(self, naam, locatie, aantalPlaatsen):
        self.naam = naam
        self.locatie = locatie
        self.slots = []
        for i in range(aantalPlaatsen):
            self.slots.append(Slot(i))

    def aantal_fietsen(self):
        count = 0
        for slot in self.slots:
            if slot.status == "beschikbaar":
                count += 1
        return count
    
    def __str__(self):
        return f"Station {self.naam} op locatie {self.locatie} met {len(self.slots)} slots."

class Slot:
    def __init__(self, ID, status="beschikbaar", fiets=None):
        self.ID = ID
        self.status = status
        self.fiets = fiets

    def verwijder_fiets(self):
        Slot.fiets = None
        Slot.status = "onbeschikbaar"

    def plaats_fiets(self, fiets):
        self.fiets = fiets
        Slot.status = "beschikbaar"

class Fiets:
    def __init__(self, fiets_ID, status="beschikbaar", slot=None, gebruiker=None):
        self.fiets_ID = fiets_ID
        self.status = status
        self.slot = slot
        self.gebruiker = gebruiker

    def __str__(self):
        if not self.inGebruik:
            return f"Fiets {self.ID} is beschikbaar."
        else:
            return f"Fiets {self.ID} is in gebruik."

class Gebruiker:
    namen = json_naar_dictionary("C:/Users/koben/OneDrive/AP/2de semester/Pyhton OOP/labo/eindopdracht/namenlijst.json")

    def __init__(self, Naam, lijst_fietsen=None):
        self.ID = Gebruiker.generate_unique_id()
        self.naam = Naam
        self.lijst_fietsen = lijst_fietsen if lijst_fietsen is not None else []
        self.maxFietsen = 1

    def generate_unique_id():
        return random.randint(100000, 999999)
    
    def leen_fiets(self, fiets_ID, station):
        if self.ID not in self.lijst_fietsen and len(self.lijst_fietsen) < self.maxFietsen:
            self.lijst_fietsen.append(fiets_ID)
            Slot.verwijder_fiets(fiets_ID)
            return True
        else:
            return False

    def breng_fiets_terug(self, fiets_id, station):
        if fiets_id in self.lijst_fietsen:
            self.lijst_fietsen.remove(fiets_id)
            fiets_id.inGebruik = False
            return True
        else:
            return False
        
    def __str__(self):
        return f"Gebruiker {self.naam} met ID {self.ID} heeft fiets {self.ID} in gebruik."

class Transporteur(Gebruiker):
    def __init__(self, naam, fietsen=None):
        self.naam = naam
        self.fietsen = fietsen if fietsen is not None else []
        self.maxFietsen = 20

    def neem_fietsen(self, fietsen):
        for fiets in fietsen:
            if fiets not in self.fietsen:
                self.fietsen.append(fiets)

    def breng_fietsen(self, fietsen):
        for fiets in fietsen:
            if fiets in self.fietsen:
                self.fietsen.remove(fiets)


    def __str__(self):
        return f"Transporteur {self.naam} heeft {len(self.fietsen)} fietsen."
