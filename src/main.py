import asyncio

from data.data import creer_fichier
from src.loader import lire_fichier
from src.pipeline import fabriquer_enregistrements

async def main():
    liste_fichier = creer_fichier()
    
    stats = {"utilisateur": 0, "produit": 0, "ignores": 0}
    coroutine = [lire_fichier(fichier) for fichier in liste_fichier]
    resultat = await asyncio.gather(*coroutine)

    resultat = fabriquer_enregistrements(resultat, stats)
    for res in resultat:
        print(res)

    print(stats)

if __name__ == "__main__":
    asyncio.run(main())