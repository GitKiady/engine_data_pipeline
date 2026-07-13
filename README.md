# Engine Data Pipeline

Pipeline de traitement de données asynchrone et polymorphe, capable d'ingérer des fichiers JSON hétérogènes (utilisateurs, produits), de les valider, nettoyer, et classifier — sans planter sur des données corrompues ou incomplètes.

## Pourquoi ce projet

Ce projet illustre un cas réel de pipeline de données : des fichiers arrivent avec des structures différentes, parfois invalides (JSON cassé, champs manquants), et le système doit rester robuste tout en restant extensible (ajouter un nouveau type de données sans modifier le code existant).

## Fonctionnalités

- Lecture **asynchrone parallèle** de fichiers JSON (`asyncio`)
- Gestion résiliente des erreurs (fichiers corrompus, vides, introuvables)
- **Polymorphisme** : dispatch automatique vers la bonne classe selon le type de donnée (`Utilisateur`, `Produit`), extensible à de nouveaux types sans modifier le code appelant
- Nettoyage automatique des données (normalisation de casse, valeurs par défaut)
- Statistiques de traitement (acceptés / ignorés par type)

## Structure du projet

```
engine-data-pipeline/
├── src/
│   ├── models.py       # Classes Enregistrement, Utilisateur, Produit
│   ├── loader.py        # Lecture asynchrone des fichiers
│   ├── pipeline.py       # Génération polymorphe des enregistrements
│   └── main.py          # Point d'entrée
├── data/
│   └── data.py          # Génération des fichiers JSON d'exemple
├── tests/
│   └── test_pipeline.py
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python -m src.main
```

## Tests

```bash
python -m pytest tests/ -v
```

## Stack technique

Python 3.12, asyncio, pytest