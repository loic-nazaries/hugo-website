---
title: "Environnements virtuels Python : venv ou Conda ?"
date: 2026-04-26T09:00:00+01:00
image: "images/portfolio/python_virtual_environment.png"
tags: ["python", "tutoriel", "conda", "workflow"]
description: "Guide pratique pour créer et gérer des environnements virtuels Python avec venv et Conda — quand utiliser l'un ou l'autre et comment garder vos projets propres."
draft: false
---

La gestion des dépendances est l'un des premiers défis rencontrés lorsqu'on travaille sur plusieurs projets Python. Deux outils dominent : le module `venv` intégré à Python et `Conda`. Cet article explique quand utiliser chacun et présente les commandes essentielles.

## Pourquoi isoler les environnements ?

Chaque projet peut nécessiter des versions différentes d'une même bibliothèque. Sans isolation, l'installation d'un paquet pour un projet peut en casser un autre. Les environnements virtuels résolvent ce problème en donnant à chaque projet sa propre installation Python cloisonnée.

## Créer un environnement avec venv

`venv` fait partie de la bibliothèque standard Python — aucune installation requise.

```bash
# Créer l'environnement
python -m venv .venv

# L'activer (Windows)
.venv\Scripts\activate

# L'activer (macOS / Linux)
source .venv/bin/activate

# Installer des paquets
pip install pandas scikit-learn

# Sauvegarder les dépendances
pip freeze > requirements.txt

# Désactiver
deactivate
```

Utilisez `venv` lorsque vous travaillez avec des paquets Python purs via pip.

## Créer un environnement avec Conda

Conda va plus loin : il gère à la fois les versions Python et les dépendances non-Python (par exemple GDAL, bibliothèques CUDA).

```bash
# Créer un environnement avec une version Python spécifique
conda create --name monenv python=3.11

# L'activer
conda activate monenv

# Installer des paquets (canal Conda en priorité, puis pip)
conda install pandas scikit-learn
pip install streamlit

# Exporter l'environnement
conda env export > environment.yml

# Recréer à partir du fichier
conda env create -f environment.yml

# Désactiver
conda deactivate
```

## Lequel utiliser ?

| Situation | Recommandation |
|---|---|
| Projet Python pur, paquets pip uniquement | `venv` |
| Projet nécessitant une version Python spécifique | `conda` |
| Projet géospatial, scientifique ou GPU | `conda` |
| Partage en équipe sur différents OS | `conda` (environment.yml) |
| Pipeline CI/CD léger | `venv` |

## Conseils pratiques

- Versionnez `requirements.txt` ou `environment.yml` — ne commitez jamais le dossier d'environnement lui-même.
- Nommez l'environnement d'après le projet, pas de façon générique (par ex. `analyse-eucface`, pas `monenv`).
- Avec Conda, préférez le canal `conda-forge` pour des paquets plus à jour.

Voir aussi les pages portfolio sur les [environnements virtuels Python](/fr/portfolio/python_virtual_environment) et les [environnements Conda](/fr/portfolio/python_virtual_env_conda) pour des scripts directement réutilisables.
