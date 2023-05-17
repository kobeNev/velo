class station ():
    def __init__(self, ID, naam, locatie, slots, fietsen, gebruikers):
        self.ID = ID
        self.naam = naam
        self.locatie = locatie
        self.aantal_slots = slots
        self.fietsen = fietsen
        self.aantal_gebruikers = gebruikers
    
    def voeg_fiets_toe (self, fiets):
        self.fiets = fiets

    def verwijder_fiets (self, fiets):
        self.fiets = fiets

    def voeg_gebruiker_toe (self, gebruiker):
        self.gebruiker = gebruiker

    def verwijder_gebruiker (self, gebruiker):
        self.gebruiker = gebruiker

class slot ():
    def __init__(self, ID, status, fiets):
        self.ID = ID
        self.status = status
        self.fiets = fiets

    def maak_bezet (self, slot, fiets):
        self.slot = slot
        self.fiets = fiets

    def maak_vrij (self, slot):
        self.slot = slot

class fiets ():
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

class gebruiker ():
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

class transporteur ():
    def __init__(self) -> None:
        pass