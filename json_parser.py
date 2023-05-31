import json
import pickle 

def json_naar_dictionary(bestandsnaam):
    woordenboek = {}
    try:
        with open(f"{bestandsnaam}", "r") as bestand:
            woordenboek = json.load(bestand)
    except FileNotFoundError:
        print(f"{bestandsnaam} niet gevonden.")
    return woordenboek

def dictionary_naar_json(bestandsnaam, dictionary):
    with open(f"{bestandsnaam}", 'w') as bestand:
        json.dump(dictionary, bestand, indent=4)

def genereer_tijdstempel(Tijd):
    uur = str(Tijd["hour"]).zfill(2)
    minuut = str(Tijd["minute"]).zfill(2)
    return f"{uur}:{minuut}"

def pickle_naar_dictionary(bestandsnaam):
    with open(bestandsnaam, 'rb') as bestand:
        pickled_data = pickle.load(bestand)
        if isinstance(pickled_data, dict):
            return pickled_data
        else:
            print("Het opgegeven pickled object is geen dictionary.")
            return None

def dictionary_naar_pickle(bestandsnaam, dictionary):
    with open(bestandsnaam, 'wb') as bestand:
        pickle.dump(dictionary, bestand)
        if isinstance(dictionary, dict):
            return True
        else:
            print("Het opgegeven object is geen dictionary.")
            return None

