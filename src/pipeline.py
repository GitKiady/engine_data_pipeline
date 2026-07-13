from src.models import Produit, Utilisateur


def fabriquer_enregistrements(liste_data, stats):
    for data in liste_data:
        if not isinstance(data, dict):
            stats["rejetes"] += 1
            continue

        type_data = data.get("type")
        if type_data == "utilisateur":
            stats["utilisateur"] += 1
            yield Utilisateur(data)
        elif type_data == "produit":
            stats["produit"] += 1
            yield Produit(data)
        else:
            stats["ignores"] += 1