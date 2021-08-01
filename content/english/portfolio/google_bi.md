---
title: "Google Business Intelligence"
date: 2020-02-10T12:14:34+06:00
image: "images/headers/google.jpg"
categories: ["database management","SQL","data visualisation","ETL"]
description: "This is meta description."
draft: false
project_info:
- name: "Client"
  icon: "fa fa-user"
  content: "Blog"
- name: "Project Link"
  icon: "fas fa-link"
  content: ""
# - name: "New Item"
#   icon: "fas fa-globe"
#   content: "Add whatever you want"
# - name: "Loop Item"
#   icon: "fas fa-redo"
#   content: "This is in a loop"
---

---

## Theme

**Data Visualisation** with Google BigQuery & Google Data Studio.

---

## Technologies

- Google BigQuery
- Google Data Studio

---

## Description

Dans ce projet, le ***dashboard*** décrit le coût des budgets investis dans la production de films dans chaque pays. Il s'agit du "*IMDB 5000 Movie Dataset*".

Par example, le film le plus coûteux a été produit en 2006 en Corée du Sud. Par contre, les USA est le pays avec le plus gros budget pour le cinéma.

**NOTE**: les sommes indiquées ne sont pas réelles. Le jeux de données a été téléchargé depuis le site [Kaggle.com](https://www.kaggle.com "Kaggle.com") en utilisant le lien [**suivant**](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset "IMDB 5000 Movie Dataset").

[<img alt="IMDB Dashboard" width="700" src="/images/portfolio/IMDB-project.png" />][IMDB Dashboard]

Méthodologie:

- Créer une instance d'ETL avec **Google BigQuery** depuis la console de **[Google Cloud Platform](https://console.cloud.google.com)**.
- Importer le fichier .csv depuis [Kaggle.com](https://www.kaggle.com "Kaggle.com").
- Connecter la source de données à l'instance d'ETL en utilisant le **data connector** BigQuery.
- Formuler une requête SQL.
- Créer un rapport (*dashboard*) avec **Data Studio**.

Le *gist* est disponible [**ici**](/documents/scripts_gists/create_etl_process_with_bigquery_and_data_studio.html "Create an ETL Process with Google BigQuery and Google Data Studio - HTML Version").

Les étapes sont résumées ci-dessous:

- [Google Cloud Platform](#google-cloud-platform)
- [Start a New Project](#start-a-new-project)
- [Create a Dataset](#create-a-dataset)
- [Create a Table using BigQuery](#create-a-table-using-bigquery)
- [Query the dataset](#query-the-dataset)
- [Prepare a Dashboard](#prepare-a-dashboard)
- [Connect a data source](#connect-a-data-source)
- [Explore Public Datasets](#explore-public-datasets)

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@mitchel3uo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mitchell Luo</a> on <a href="https://unsplash.com/s/photos/google?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<!-- definitions -->
[IMDB Dashboard]: /images/portfolio/IMDB-project.png "IMDB Dashboard"
