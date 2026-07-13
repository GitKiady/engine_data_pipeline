import json

def creer_fichier():
    user1 = "data/user1.json"
    user2 = "data/user2.json"
    produit1 = "data/produit1.json"
    produit2 = "data/produit2.json"

    # Type "utilisateur"
    with open(user1, "w") as f:
        json.dump({"type": "utilisateur", "nom": "  julie  ", "age": 28}, f)

    with open(user2, "w") as f:
        json.dump({"type": "utilisateur", "nom": "MARC", "age": None}, f)

    # Type "produit"
    with open(produit1, "w") as f:
        json.dump({"type": "produit", "titre": "  clavier mécanique  ", "prix": 79.9}, f)

    with open(produit2, "w") as f:
        json.dump({"type": "produit", "titre": "SOURIS", "prix": -5}, f)  # prix invalide

    print("Fichiers créés.")

    return [user1, user2, produit1, produit2]
