import pytest
from src.pipeline import fabriquer_enregistrements
from src.models import Utilisateur, Produit, Enregistrement

@pytest.fixture
def stats_vides():
    # cette fonction PRÉPARE la donnée, pytest l'appelle automatiquement
    return {"utilisateur": 0, "produit": 0, "ignores": 0}

def test_fabriquer_enregistrements_type_utilisateur(stats_vides):
    data = [{"type": "utilisateur", "nom": "  test  ", "age": None}] # A: ARRANGE
    
    resultats = list(fabriquer_enregistrements(data, stats_vides)) # A: ACT
    
    assert len(resultats) == 1  # ASSERT
    assert isinstance(resultats[0], Utilisateur)
    assert resultats[0].data["nom"] == "Test"  # vérifie le nettoyage
    assert resultats[0].data["age"] == 0
    assert stats_vides["utilisateur"] == 1


def test_fabriquer_enregistrements_type_produit(stats_vides):
    data = [{"type": "produit", "titre": "  test  ", "prix": -5}]
    
    resultats = list(fabriquer_enregistrements(data, stats_vides))
    
    assert len(resultats) == 1
    assert isinstance(resultats[0], Produit)
    assert resultats[0].data["titre"] == "Test"  # vérifie le nettoyage
    assert resultats[0].data["prix"] == 0
    assert stats_vides["produit"] == 1



def test_enregistrement_nettoyer_non_implemente():
    obj = Enregistrement({"x": 1})
    with pytest.raises(NotImplementedError):  # on ATTEND cette exception précise
        obj.nettoyer()  # doit planter avec NotImplementedError
    # si nettoyer() ne plante PAS, ce test échoue automatiquement