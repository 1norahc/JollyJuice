import json
import os

class API:
    def __init__(self): pass 
    
    def save_api(self, data, file_name):
        if os.path.exists(file_name):
            with open(file_name, "r+") as f:
                load_data = json.load(f)
            if data in load_data:
                print("Dane istnieją w pliku.")
            else:
                load_data.append(data)
                with open(file_name, "w+") as f:
                    json.dump(load_data, f, indent=4)
                print("Dane zostały dodane do pliku.")
        else:
            with open(file_name, "w+") as f:
                json.dump([data], f, indent=4)
            print("Plik został utworzony, a dane zostały dodane do pliku.")                
    
    def get_api(self, nazwa_pliku):
        if os.path.exists(nazwa_pliku):
            with open(nazwa_pliku, 'r') as plik:
                dane = json.load(plik)
            return dane
        else:
            return None

        