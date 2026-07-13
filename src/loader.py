import json

async def lire_fichier(fichier):
    try:
        with open(fichier, "r") as f:
            data = json.load(f)
            return data
        
    except FileNotFoundError as fnfe:
        print(fnfe)
        return None
    except json.JSONDecodeError as jde:
        print(jde)
        return None
    