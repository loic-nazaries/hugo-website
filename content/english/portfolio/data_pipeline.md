---
title: "Data Pipeline"
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

## Theme

Data integration, cleansing and validation **pipeline**.

---

## Technologies

- Python (Numpy, Pandas, Matplotlib, Seaborn, Click libraries)

---

## Description

Une **base de données relationnelle** de type  « **flocon de neige** » a été modélisée à partir de fichiers de type et d'origine multiples (enregistreurs automatiques, mesures manuelles, fichiers au formats variés - .csv, .txt, tableur, *etc.*). Grâce aux fonctionnalités Python, ces données ont été uniformisées et "nettoyées" tout en respectant les bonnes pratiques statistiques (par exemple, pas de "*cherry-picking*", ni de "*data dredging*", *etc.* - *cf.*
[*Data Fallacies to avoid*](/documents/data-fallacies-to-avoid.pdf "Data Fallacies to avoid")).

En particulier, les trois étapes suivantes sont importantes dans tout projet de « ***Data Science*** » :

1. **Typage des variables** (*category*, *integers*/*floats*, *strings*, *booleans*, *dates*). Très important, en particulier, pour diminuer l'utilisation de la mémoire vive d'un ordinateur ou serveur

2. **Remplacement** (ou ***imputation***) des **valeurs manquantes** (**Figure 1**). C'est une étape importante qui permet de préserver la puissance statistique d'un jeux de données

    | Before Imputation                                                                                                                                                 | After Imputation                                                                                                                                                   |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |                                                                                                                                                                   |
    | [<img alt="N2O Transformations" width="350" align="left" src="/images/portfolio/ghg_flux_data_missing_data_raw_heatmap.png" />][Missing Values BEFORE Imputation] | [<img alt="N2O Transformations" width="350" align="left" src="/images/portfolio/ghg_flux_data_missing_data_clean_heatmap.png" />][Missing Values AFTER Imputation] |
    &nbsp;

    **Figure 1**:  The replacement (or **imputation**) of missing values by mathematical approach. Here, when the value of a replicated measurement (usually seven (7) replicates) was missing (*left panel*), it was replaced by the **"mean" value** of the other replicated samples. The remaining missing values (*right panel*) represent non-replicated data which can be imputed using more powerful machine learning approaches (not detailed here).

3. Transformation des variables pour obtenir une distribution dite « **normale** » (**Figure 2**). Le but est donc de diminuer le nombre de **valeurs « extrêmes »**, c'est-à-dire des valeurs *très* éloignées de la valeur moyenne.

    [<img alt="N2O Transformations" width="1000" align="left" src="/images/portfolio/n2o_flux_distrib_violinplots.png" />][N2O Data Transformations]
    &nbsp;

    **Figure 2**: Mathematical transformation of nitrous oxide (N<sub>2</sub>O) emissions. The various « violin plots » represent different transformation of the **raw data** in order to seek « **normal distribution** » *(e.g.* standardised transformation, square-root transformation, *etc.*). The aim is to reach a **symmetrical distribution** and thus avoid (left- or right-handed) tails.

De manière plus générale, il s'agit de préparer les jeux de données pour les étapes d'**analyses statistiques et de modélisation** (« *machine learning* »).

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@quinten149?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Quinten de Graaf</a> on <a href="https://unsplash.com/s/photos/pipeline?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<!-- definitions -->
[Missing Values BEFORE Imputation]: /images/portfolio/ghg_flux_data_missing_data_raw_heatmap.png "Missing Values BEFORE Imputation"
[Missing Values AFTER Imputation]: /images/portfolio/ghg_flux_data_missing_data_clean_heatmap.png "Missing Values AFTER Imputation"
[N2O Data Transformations]: /images/portfolio/n2o_flux_distrib_violinplots.png "N2O Data Transformations"
