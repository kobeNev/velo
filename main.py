from data_input import *
from velo import *
from json_parser import *


bestandsnaam = "velo.geojson"
geconverteerd_woordenboek = json_naar_dictionary(bestandsnaam)

if geconverteerd_woordenboek:
    print("Het woordenboek is succesvol geconverteerd:")
    print(geconverteerd_woordenboek)
else:
    print("Fout bij het converteren van het woordenboek.")
