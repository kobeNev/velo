from data_input import *
from velo import *
from json_parser import *
import sys


bestandsnaam = "velo.geojson"
geconverteerd_woordenboek = json_naar_dictionary(bestandsnaam)

if geconverteerd_woordenboek:
    print("Het woordenboek is succesvol geconverteerd:")
    print(geconverteerd_woordenboek)
else:
    print("Fout bij het converteren van het woordenboek.")




#deel Yves
gebruiker_voor_niet_sim = Gebruiker(1, "sys", "sys")
transporteur_voor_niet_sim = Transporteur(1)
stations = velo.maak_stations()

def simulatie_modus_afhandelaar(sim_modus):
    if sim_modus == 2:
        simulatie_modus(True, stations, start)
    elif sim_modus == 1:
        with open("pickle.dat", "rb") as f:
        gegevens = pickle.load(f)
        simulatie_modus(False, gegevens[2], start, gegevens[0], gegevens[1])

def fiets_leen_terug_afhandelaar(sim_modus, gebruiker_type):
    if sim_modus == 1:
        leen_fiets(stations, gebruiker_type, gebruiker_voor_niet_sim, start)
    elif sim_modus == 2:
        zet_fiets_terug(stations, gebruiker_type, gebruiker_voor_niet_sim, start)

def start():
    if len(sys.argv) > 1:
    # simulatie modus
        if sys.argv[1] in ["-s", "-S"]:
            print("simulatie modus")
            sim_modus = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
            simulatie_modus_afhandelaar(sim_modus)
        else:
            print("geen geldige modus")
    else:
        bedrijfsmodus = int(input("1 voor simulatie, 2 voor fiets lenen/terugplaatsen, 3 voor HTML, 4 om af te sluiten: "))
    if bedrijfsmodus == 1:
        print("simulatie modus")
        sim_modus = int(input("1 voor verder gaan van vorige situatie, 2 voor opnieuw beginnen: "))
        simulatie_modus_afhandelaar(sim_modus)
    elif bedrijfsmodus == 2:
        sim_modus = int(input("1 voor lenen, 2 voor terugplaatsen: "))
        gebruiker_type = int(input("1 voor gebruiker, 2 voor transporteur: "))
        fiets_leen_terug_afhandelaar(sim_modus, "gebruiker" if gebruiker_type == 1 else "transporteur")
    elif bedrijfsmodus == 3:
        haal_html_op()
    elif bedrijfsmodus == 4:
        pass
    else:
        print("geen geldige modus")

start()