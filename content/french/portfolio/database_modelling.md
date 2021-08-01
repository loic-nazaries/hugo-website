---
title: "Modélisation de base de données"
date: 2020-06-01T12:14:34+06:00
image: "images/headers/library.jpg"
categories: ["database management","business intelligence","SQL"]
description: "This is meta description."
draft: false
project_info:
- name: "Client"
  icon: "fas fa-user"
  content: "La Piscine"
# - name: "Project Link"
#   icon: "fas fa-link"
#   content: "https://examplesite.com/"
# - name: "New Item"
#   icon: "fas fa-globe"
#   content: "Add whatever you want"
# - name: "Loop Item"
#   icon: "fas fa-redo"
#   content: "This is in a loop"
---

---

## Thématique

Modélisation d'une **base de données**.

---

## Technologies

- SQL
- PostgreSQL & pgAdmin4 | Oracle SQL*Plus
- UML

---

## Description

Un **système de gestion de base de données relationnelle** (SGBDR) a été construit pour le projet « ***EucFACE*** ». La base de données a été implémentée avec le logiciel **[PostgreSQL](https://www.postgresql.org/ "PostgreSQL")** (version 12.5) et **pgAdmin4**.

Note: le projet *EucFACE* est présenté [**ici**](/portfolio/eucface "EucFACE Site Presentation").

Cliquer [**ici**](/documents/RDBMS_UML.html "RDBMS UML - EucFACE") pour ouvrir la structure UML de l'application ***Greenhouse Gas Estimation Portal*** (voir l'article "Tableau de bord"). Y sont contenus les diagrammes de contexte, de fonctionnalités, de cas d'utilisation et d'activité de la base de données EucFACE.

Les **Figure 1** et **Figure 2** montrent, respectivement, le **modèle conceptuel des données** (**MCD**) et le **modèle physique des données** (**MPD**) de la base de données relationnelle EucFACE. Sa structure est de type  « **flocon de neige** ».

### Modèle conceptuel des données (MCD)

&nbsp;
[<img alt="MCD EucFACE" width="700" src="/images/portfolio/EucFACE_MCD.png" />][MCD EucFACE]&nbsp;

**Figure 1**: Modèle conceptuel des données (**MCD**) de la base de données relationnelle du projet "[EucFACE](https://github.com/loic-nazaries/loic-nazaries.github.io/blob/main/eucface_site_presentation.md "Présentation du site EucFACE")".

### Modèle physique des données (MPD)

&nbsp;
[<img alt="MPD EucFACE" width="700" src="/images/portfolio/RDBMS_model.png" />][MPD EucFACE]&nbsp;

**Figure 2**: Diagramme du système de gestion de base de données relationnelle (**SGBDR**) du projet "[EucFACE](https://github.com/loic-nazaries/loic-nazaries.github.io/blob/main/eucface_site_presentation.md "Présentation du site EucFACE")".

<!-- credits -->
[Credit for the background picture] Photo by <a href="https://unsplash.com/@tofi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tobias Fischer</a> on <a href="https://unsplash.com/s/photos/database?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<!-- definitions -->
[MCD EucFACE]: /images/portfolio/EucFACE_MCD.png "Modèle conceptuel des données - EucFACE"
[MPD EucFACE]: /images/portfolio/RDBMS_model.png "Modèle physique des données - EucFACE"
