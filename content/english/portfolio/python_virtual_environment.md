---
title: "Python Virtual Environment"
date: 2020-04-18T12:14:34+06:00
image: "images/headers/python.jpg"
categories: ["python development","virtual environment"]
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

Create a **virtual environment** with Python.

---

## Technologies

- Python
- Microsoft Visual Studio Code

---

## Description

Dans tout **projet data**, il est important de pouvoir créer un **environnement technique** reproductible par une autre personne ou sur un autre ordinateur. Ceci signifie que le langage de programmation (Python, par exemple) et la version des librairies utilisées lors de l'écriture d'un script doivent être établis dès le début du projet.

Pour cette raison, il est courant de créer un **environnement virtuel** qui va contenir toutes ces données ainsi que la structure des dossiers contenant les fichiers essentiels au projet.

Voici donc un **script**, ou ***gist***, qui détaille les différents étapes de la création d'un **environnement virtuel** avec le module "**venv**" de **Python**.

Le *gist* est disponible [**ici**](/documents/scripts_gists/create_a_virtual_environment_with_python.html "Create a Virtual Environment with Python - HTML Version") ainsi que sur [GitHub Gist](https://gist.github.com/loic-nazaries "Create a Virtual Environment with Python - Markdown Version").

The steps are summarised below:

- [Create a folder for the project](#create-a-folder-for-the-project)
- [Create a virtual environment for the project](#create-a-virtual-environment-for-the-project)
- [Activate the new virtual environment ```venv```](#activate-the-new-virtual-environment-venv)
- [Create 'default' folders and files](#create-default-folders-and-files)
- [Record the dependencies for the project](#record-the-dependencies-for-the-project)
- [Install a Python Library](#install-a-python-library)
- [Save the new dependencies](#save-the-new-dependencies)
- [Check dependency clashes after installing all packages](#check-dependency-clashes-after-installing-all-packages)
- [Deactivate the virtual environment](#deactivate-the-virtual-environment)

<!-- credits -->
[Credit for the header picture] Photo by <a href="https://unsplash.com/@davidclode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">David Clode</a> on <a href="https://unsplash.com/s/photos/python?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
