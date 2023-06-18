#een tweede poging om velo.py te maken

class Velo:
    def __init__(self, stations, gebruikers, fietsen, transporteurs):
        self.stations = stations
        self.gebruikers = gebruikers
        self.fietsen = fietsen
        self.transporteurs = transporteurs


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
    def __init__(self, ID, fiets=None):
        self.ID = ID
        self.fiets = fiets

    def neem_fiets(self,):
        self.fiets = None
        self.status = "onbeschikbaar"

    def plaats_fiets(self, fiets):
        self.fiets = fiets
        self.status = "beschikbaar"


class Fiets:
    def __init__(self, ID, status="beschikbaar"):
        self.ID = ID
        self.inGebruik = False
        self.status = status

    def __str__(self):
        if not self.inGebruik:
            return f"Fiets {self.ID} is beschikbaar."
        else:
            return f"Fiets {self.ID} is in gebruik."


class Gebruiker:
    def __init__(self, naam):
        self.naam = naam
        self.fiets = []
        self.maxFietsen = 1

    def __str__(self):
        return f"Gebruiker {self.naam} met fiets {self.fiets.ID}."
    

class Transporteur:
    def __init__(self, naam):
        self.naam = naam
        self.fietsen = []
        self.maxFietsen = 20

    def __str__(self):
        return f"Transporteur {self.naam} met {len(self.fietsen)} fietsen."
