---
title: "Pipeline de données"
date: 2021-05-19T12:14:34+06:00
image: "images/headers/pipeline.jpg"
categories: ["data mining","python development","statistics"]
description: "This is meta description."
draft: false
project_info:
- name: "Client"
  icon: "fas fa-users"
  content: "BIFORA"
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

**Pipeline** d'intégration, de nettoyage et de validation de données.

---

## Technologies

- Python (librairies Numpy, Pandas, Matplotlib, Seaborn, Click)

---

## Description

Une **base de données relationnelle** de type  « **flocon de neige** » a été modélisée à partir de fichiers de type et d'origine multiples (enregistreurs automatiques, mesures manuelles, fichiers au formats variés - .csv, .txt, tableur, *etc.*). Grâce aux fonctionnalités Python, ces données ont été uniformisées et "nettoyées" tout en respectant les bonnes pratiques statistiques (par exemple, pas de "*cherry-picking*", ni de "*data dredging*", *etc.* - *cf.*
[*Data Fallacies to avoid*](/documents/data-fallacies-to-avoid.pdf "Data Fallacies to avoid")).

En particulier, les trois étapes suivantes sont importantes dans tout projet de « ***Data Science*** » (ou **Science des données**) :

1. **Typage des variables** (*category*, *integers*/*floats*, *strings*, *booleans*, *dates*). Très important, en particulier, pour diminuer l'utilisation de la mémoire vive d'un ordinateur ou serveur

2. **Remplacement** (ou ***imputation***) des **valeurs manquantes** (**Figure 1**). C'est une étape importante qui permet de préserver la puissance statistique d'un jeux de données

    | Avant imputation                                                                                                                                                  | Après imputation                                                                                                                                                   |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |                                                                                                                                                                   |
    | [<img alt="N2O Transformations" width="350" align="left" src="/images/portfolio/ghg_flux_data_missing_data_raw_heatmap.png" />][Missing Values BEFORE Imputation] | [<img alt="N2O Transformations" width="350" align="left" src="/images/portfolio/ghg_flux_data_missing_data_clean_heatmap.png" />][Missing Values AFTER Imputation] |
    &nbsp;

    **Figure 1**: Le remplacement (ou **imputation**) de valeurs manquantes par approche mathématique. Ici, quand la valeur d'une mesure répliquée (sept (7) réplications en général) était manquante (**panneau gauche**), elle a été remplacée par la **valeur "moyenne"** des autres échantillons répliqués. Les valeurs manquantes restantes (**panneau droit**) représentent des données non-répliquées qui peuvent être imputées en utilisant des approches de « ***Machine Learning*** » (ou **apprentissage automatique**) plus puissantes (non détaillé ici).

3. Transformation des variables pour obtenir une distribution dite « **normale** » (**Figure 2**). Le but est donc de diminuer le nombre de **valeurs « extrêmes**, c'est-à-dire des valeurs *très* éloignées de la valeur moyenne.

    [<img alt="N2O Transformations" width="1000" align="left" src="/images/portfolio/n2o_flux_distrib_violinplots.png" />][N2O Data Transformations]
    &nbsp;

    **Figure 2**: Transformation mathématique des émissions d'oxyde nitreux (N<sub>2</sub>O). Les différents « ***violin plots*** » représentent les diverses transformations des **données brutes** pour rechercher une « **distribution normale** » (par exemple, transformation standardisée, transformation en racine carrée, *etc.*). Le but est d'approcher une **distribution symétrique** et donc d'éviter des queues (gauches ou droites).

De manière plus générale, il s'agit de préparer les jeux de données pour les étapes d'**analyses statistiques et de modélisation** (« *machine learning* »).

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@quinten149?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Quinten de Graaf</a> on <a href="https://unsplash.com/s/photos/pipeline?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<!-- definitions -->
[Missing Values BEFORE Imputation]: /images/portfolio/ghg_flux_data_missing_data_raw_heatmap.png "Missing Values BEFORE Imputation"
[Missing Values AFTER Imputation]: /images/portfolio/ghg_flux_data_missing_data_clean_heatmap.png "Missing Values AFTER Imputation"
[N2O Data Transformations]: /images/portfolio/n2o_flux_distrib_violinplots.png "N2O Data Transformations"
