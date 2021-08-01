---
title: "Dashboard"
date: 2021-01-10T12:14:34+06:00
image: "images/headers/dashboard.jpg"
categories: ["data visualisation","web app","python development","dashboard"]
description: "This is meta description."
draft: false
project_info:
- name: "Client"
  icon: "fa fa-user"
  content: "La Piscine"
- name: "Project Link"
  icon: "fas fa-link"
  content: "[Greenhouse Gas Estimation Portal](https://exam-piscine-heroku-redone.herokuapp.com/)"
# - name: "New Item"
#   icon: "fas fa-globe"
#   content: "Add whatever you want"
# - name: "Loop Item"
#   icon: "fas fa-redo"
#   content: "This is in a loop"
---

---

## Theme

Deployment of a **web application** to create an **interactive dashboard** for data analysis.

---

## Technologies

- Python (Streamlit library)

---

## Description

Un tableau de bord (« *dashboard* ») interactif a été construit pour observer et tester les émissions des gaz à effet de serre sous différentes conditions. Cette **application web** appelée « ***Greenhouse Gas Estimation Portal*** » a été codé avec la librairie Python [Streamlit](https://www.streamlit.io/ "Streamlit.io") et déployée sur [Heroku.com](https://www.heroku.com/ "Heroku.com"). L'application peut être accédée par le lien [**suivant**](https://exam-piscine-heroku-redone.herokuapp.com/ "Greenhouse Gas Estimation Portal App").

Il s'agit d'une application entièrement réglable une fois que l'utilisateur a créé un compte. Voici une liste (non-exhaustive) des options disponibles:

- téléchargement du fichier de données (format .csv ou .pkl)
- sélection des variables à inclure dans l'analyse
- typage des variables
- choix des variables dépendantes et indépendantes
- « *dummification* » possible des variables
- génération d'un résumé statistique (moyenne, écart-type, kurtosis/skewness, pourcentage des valeurs manquantes, *etc.*)
- agrégation des données par groupe (date, traitement, année, *etc.*)
- analyses univariées et bivariées
- analyses de corrélation
- analyses statistiques de type « REML » (*restriction likelihood*)
- envoie des résultats à l'utilisateur par *email*

Des captures d'écran sont disponibles dans la (**Figure 1**).
Elles reflètent certaines des options disponibles à l'utilisateur.

| Login to GHG Estimation Portal                                                                                                                                         | Variable Selection                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [<img alt="Login Screenshot" width="500" align="left" src="/images/portfolio/streamlit_login_screenshot.png" />][Login Screenshot]&nbsp;                               | [<img alt="Login Screenshot" width="500" align="left" src="/images/portfolio/streamlit_vars_selection_screenshot.png" />][Variable Selection Screenshot]&nbsp; |
| **Time-Series Analysis**                                                                                                                                               | **Email Option**                                                                                                                                               |
| [<img alt="Time-Series Analysis Screenshot" width="500" align="left" src="/images/portfolio/streamlit_time_series_screenshot.png" />][Time-Series Analysis Screenshot] | [<img alt="Email Option Screenshot" width="500" align="left" src="/images/portfolio/streamlit_email_screenshot.png" />][Email Option Screenshot]               |
&nbsp;

**Figure 1**: Screenshots of various steps and options available to the user on the web application « Greenhouse Gas Estimation Portal ».

Note: Dans l'avenir, une section de *machine learning* sera disponible. Il sera en autre possible de procéder à une modélisation temporelle des émissions des gaz à effet de serre.

**EDIT**: application non disponible au moment de la préparation de cette page (10/01/2021).

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@jannerboy62?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nick Fewings</a> on <a href="https://unsplash.com/s/photos/dashboard?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<!-- definitions -->
[Login Screenshot]: /images/portfolio/streamlit_login_screenshot.png "Metro Map Data Science"
[Variable Selection Screenshot]: /images/portfolio/streamlit_vars_selection_screenshot.png "Variable Selection Screenshot"
[Time-Series Analysis Screenshot]: /images/portfolio/streamlit_time_series_screenshot.png "Time-Series Analysis Screenshot"
[Email Option Screenshot]: /images/portfolio/streamlit_email_screenshot.png "Email Option Screenshot"
