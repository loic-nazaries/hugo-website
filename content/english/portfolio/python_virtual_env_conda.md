---
title: "Python Virtual Environment (Conda)"
date: 2020-05-04T12:14:34+06:00
image: "images/headers/anaconda.jpg"
categories: ["python development","virtual environment","conda"]
description: "This is meta description."
draft: false
project_info:
- name: "Client"
  icon: "fa fa-user"
  content: ""
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

Create a **virtual environment** with Python & Conda.

---

## Technologies

- Python
- Conda
- Microsoft Visual Studio Code

---

## Description

Dans tout **projet data**, il est important de pouvoir créer un **environnement technique** reproductible par une autre personne ou sur un autre ordinateur. Ceci signifie que le langage de programmation (Python, par exemple) et la version des librairies utilisées lors de l'écriture d'un script doivent être établis dès le début du projet.

Pour cette raison, il est courant de créer un **environnement virtuel** qui va contenir toutes ces données ainsi que la structure des dossiers contenant les fichiers essentiels au projet.

Voici donc un **script**, ou ***gist***, qui détaille les différents étapes de la création d'un **environnement virtuel** avec le module "**venv**" de **Python**.

Le *gist* est disponible [**ici**](/documents/scripts_gists/create_a_virtual_environment_with_conda.html "Create a Virtual Environment with Python & Conda - HTML Version") ainsi que sur [GitHub Gist](https://gist.github.com/loic-nazaries "Create a Virtual Environment with Python & Conda - Markdown Version").

The steps are summarised below:

- [Create a folder for the project](#create-a-folder-for-the-project)
- [Create a virtual environment for the project](#create-a-virtual-environment-for-the-project)
- [Create 'default' folders and files](#create-default-folders-and-files)
- [Manage Conda](#manage-conda)
- [Manage Environments](#manage-environments)
  - [Manage environments from the default environment folder](#manage-environments-from-the-default-environment-folder)
  - [Manage environments from a specific location](#manage-environments-from-a-specific-location)
- [Manage Python](#manage-python)
- [Manage Packages](#manage-packages)
- [Use a package list to create a NEW (identical) environment](#use-a-package-list-to-create-a-new-identical-environment)
  - [Use a package list from a ```requirements.txt``` file](#use-a-package-list-from-a-requirementstxt-file)
  - [Use a package list from an 'environment.yaml' file](#use-a-package-list-from-an-environmentyaml-file)
  - [Other options for managing Conda environments and packages](#other-options-for-managing-conda-environments-and-packages)

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@museumsvictoria?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Museums Victoria</a> on <a href="https://unsplash.com/s/photos/anaconda?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
