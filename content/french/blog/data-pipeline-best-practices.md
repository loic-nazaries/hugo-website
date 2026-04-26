---
title: "Bonnes pratiques pour un pipeline de données : de la donnée brute à l'analyse"
date: 2026-04-26T10:00:00+01:00
image: "images/portfolio/data_pipeline.png"
tags: ["data engineering", "python", "ETL", "BigQuery"]
description: "Principes clés pour construire des pipelines de données fiables et maintenables — extraction, transformation, chargement et outils pour les rendre reproductibles."
draft: false
---

Un pipeline de données déplace des données depuis une ou plusieurs sources, à travers une série de transformations, vers une destination où elles peuvent être analysées ou servies. Bien le concevoir dès le départ évite d'innombrables heures de débogage.

## Le modèle ETL

La plupart des pipelines suivent le modèle Extraire → Transformer → Charger (ETL) :

1. **Extraire** — récupérer les données depuis les sources (bases de données, API, fichiers)
2. **Transformer** — nettoyer, valider, reformater et enrichir les données
3. **Charger** — écrire le résultat vers une destination (entrepôt de données, tableau de bord, fichier)

Une variante, ELT, charge d'abord les données brutes puis les transforme dans la destination — pratique courante avec les entrepôts cloud comme BigQuery.

## Principe 1 : Séparer les responsabilités

Conservez l'extraction, la transformation et le chargement dans des fonctions ou modules séparés. Cela rend chaque étape testable et remplaçable indépendamment.

```python
def extraire(chemin_source: str) -> pd.DataFrame:
    return pd.read_csv(chemin_source)

def transformer(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["date", "valeur"])
    df["date"] = pd.to_datetime(df["date"])
    df["valeur"] = df["valeur"].clip(lower=0)
    return df

def charger(df: pd.DataFrame, chemin_dest: str) -> None:
    df.to_parquet(chemin_dest, index=False)
```

## Principe 2 : Valider tôt

Détectez les données incorrectes dès l'étape d'extraction, avant qu'elles ne corrompent vos transformations.

```python
def valider(df: pd.DataFrame) -> None:
    assert "date" in df.columns, "Colonne 'date' manquante"
    assert df["valeur"].dtype in ["float64", "int64"], "La colonne valeur doit être numérique"
    assert not df.duplicated(subset=["date", "site_id"]).any(), "Enregistrements en double détectés"
```

## Principe 3 : Rendre les pipelines idempotents

Exécuter le pipeline deux fois doit produire le même résultat qu'une seule fois. Utilisez une logique d'upsert ou d'écriture par partition plutôt qu'un ajout en aveugle.

## Principe 4 : Tout journaliser

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
logger.info("Extrait %d lignes depuis %s", len(df), chemin_source)
```

Journalisez les nombres de lignes à chaque étape pour détecter les pertes silencieuses de données.

## Principe 5 : Paramétrer, ne pas coder en dur

Utilisez des fichiers de configuration ou des variables d'environnement pour les chemins, identifiants et dates. Ne codez jamais une chaîne de connexion ou un chemin de fichier directement dans une fonction.

```python
import os
DB_URL = os.environ["DATABASE_URL"]
```

## Pipelines cloud : exemple BigQuery

Pour les grands volumes de données, un entrepôt de données cloud supprime la nécessité de gérer le stockage local. Le processus ETL pour BigQuery et Data Studio est illustré dans le [projet portfolio Google BigQuery & Data Studio](/fr/portfolio/google_bigquery_datastudio), avec un script Python réutilisable publié comme GitHub Gist.

## Récapitulatif

| Pratique | Pourquoi c'est important |
|---|---|
| Séparer les étapes ETL | Tests et réutilisation indépendants |
| Valider à l'extraction | Détecter les mauvaises données tôt |
| Écritures idempotentes | Sécurité en cas de réexécution |
| Journaliser les nombres de lignes | Détecter les pertes silencieuses |
| Paramétrer la configuration | Portabilité entre environnements |

L'application cohérente de ces principes distingue un script qui a fonctionné une fois d'un pipeline qui tourne de façon fiable en production.
