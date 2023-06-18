import random
import json_parser
from velo import * 
import json

def str(self):
    for station in self.stations:
        print(station)

def toevoegen_gebruiker(self,id, naam, lijst_fietsen):
    new=Gebruiker(id, naam, lijst_fietsen)
    self.users[len(self.users)+1]=new
    return new

def toevoegen_fiets(self,id, status, slot,user_id):
    new=Fiets(id, status, slot,user_id)
    self.bikes[len(self.bikes)+1]=new
    return new

def toevoegen_station(self, naam, locatie, aantalPlaatsen):
    new=Station(id, naam, locatie, aantalPlaatsen)
    self.stations[len(self.stations)+1]=new
    return new

def toevoegen_station(self,naam, camion, fietsen):
    new=Transporteur(naam, camion, fietsen)
    self.transporters[len(self.transporters)+1]=new
    return new

def uitlezen_station(self):
    with open("velo.geojson","r") as f:
        velo_data = json.load(f)
    for station_new in velo_data["features"]:
        new= self.toevoegen_station(name=station_new["properties"]["Straatnaam"],
                                    location=station_new["properties"]["Postcode"],
                                capacity=station_new["properties"]["Aantal_plaatsen"])