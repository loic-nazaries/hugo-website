---
title: "Python Virtual Environments: venv vs Conda"
date: 2026-04-26T09:00:00+01:00
image: "images/portfolio/python_virtual_environment.png"
tags: ["python", "tutorial", "conda", "workflow"]
description: "A practical guide to creating and managing Python virtual environments with both venv and Conda — when to use each and how to keep your projects clean."
draft: false
---

Managing dependencies is one of the first challenges you face when working on multiple Python projects. Two tools dominate the ecosystem: Python's built-in `venv` module and `Conda`. This post explains when to use each and shows the essential commands.

## Why Isolate Environments?

Each project may require different versions of the same library. Without isolation, installing a package for one project can break another. Virtual environments solve this by giving each project its own sandboxed Python installation.

## Creating a Virtual Environment with venv

`venv` is part of the Python standard library — no installation needed.

```bash
# Create the environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS / Linux)
source .venv/bin/activate

# Install packages
pip install pandas scikit-learn

# Save dependencies
pip freeze > requirements.txt

# Deactivate
deactivate
```

Use `venv` when you are working with pure Python packages and pip.

## Creating an Environment with Conda

Conda goes further: it manages both Python versions and non-Python dependencies (e.g. GDAL, CUDA libraries).

```bash
# Create an environment with a specific Python version
conda create --name myenv python=3.11

# Activate it
conda activate myenv

# Install packages (Conda channel first, then pip for the rest)
conda install pandas scikit-learn
pip install streamlit

# Export the environment
conda env export > environment.yml

# Recreate from file
conda env create -f environment.yml

# Deactivate
conda deactivate
```

## Which One Should You Use?

| Scenario | Recommendation |
|---|---|
| Pure Python project, pip packages only | `venv` |
| Project needing specific Python version | `conda` |
| Geospatial, scientific, or GPU-heavy project | `conda` |
| Sharing with a team on different OS | `conda` (environment.yml) |
| Lightweight CI/CD pipeline | `venv` |

## Practical Tips

- Commit `requirements.txt` or `environment.yml` to version control — never commit the environment folder itself.
- Name your environment after the project, not generically (e.g. `eucface-analysis`, not `myenv`).
- For Conda, prefer `conda-forge` as your primary channel for more up-to-date packages.

See also the [portfolio pages on Python virtual environments](/en/portfolio/python_virtual_environment) and [Conda environments](/en/portfolio/python_virtual_env_conda) for scripts you can reuse directly.
