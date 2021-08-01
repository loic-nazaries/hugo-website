---
title: "Google BigQuery & Google Data Studio"
date: 2020-02-05T12:14:34+06:00
image: "images/headers/studio.jpg"
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

## Thématique

Préparer un ***dashboard*** (ou **tableau de bord**) avec Google BigQuery et Google Data Studio

---

## Technologies

- Google BigQuery
- Google Data Studio

---

## Description

Google a mis à disposition un outil de procession de données de type **Big Data** appelé **Google BigQuery**. Grâce à leur plateforme **Google Cloud Platform**, il est possible de mettre en place un pipeline de gestion et d'utilisation de données. De plus, il est possible d'utiliser **Google Data Studio** ***gratuitement(!)*** pour préparer des *dashboard* interactif ainsi que de le partager avec d'autres collaborateurs.

Voici donc un script, ou gist, qui détaille les différents étapes de la création d'un tel *workflow* (ou flux de tâches).

NOTE: le script présenté a besoin d'être édité pour bien organiser les différents étapes. Cela sera bientôt fait.

Le *gist* est disponible [**ici**](/documents/scripts_gists/create_etl_process_with_bigquery_and_data_studio.html "Create an ETL process with Google BigQuery and Google Data Studio - HTML Version") ainsi que sur [GitHub Gist](https://gist.github.com/loic-nazaries "Create an ETL process with Google BigQuery and Google Data Studio - Markdown Version") (bientôt!).

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
[Credit for the header picture] Photo by <a href="https://unsplash.com/@silver26class?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Silvestre Leon</a> on <a href="https://unsplash.com/s/photos/data-studio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
