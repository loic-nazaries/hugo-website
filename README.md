# My Personal Website built with [Hugo Framework](https://gohugo.io/ "Hugo Framework")

This repository is the **single source of truth** for the Hugo source files of my personal website. The generated `public/` output is **not** committed — it is gitignored and rebuilt fresh on every deploy.

The site is published via **GitHub Actions** directly from this repository.

---

## :rocket: Deployment

The `public/` folder is **not tracked** in this repository (see `.gitignore`). It is built fresh from `content/`, `config/`, and `themes/` on every deploy:

- A **pre-push git hook** (`.githooks/pre-push`) runs `hugo --gc --minify` locally before every push, as a sanity check that the build succeeds — it does **not** commit anything.
- **GitHub Actions** (`.github/workflows/hugo.yaml`) builds the site with Hugo (extended) and deploys the freshly built `public/` folder to GitHub Pages on every push to the `main` branch.

### First-time setup (after cloning)

```bash
git config core.hooksPath .githooks
```

This activates the pre-push hook locally. It must be run once per clone since git does not apply custom hook paths automatically.

---

## :brain: Repo Knowledge Graph (Graphify)

This repo's structure is mapped with [Graphify](https://github.com/safishamsi/graphify), which scans the codebase/content and builds a navigable knowledge graph — entities (pages, templates, portfolio items, publications, etc.) and how they relate to each other. Useful before making non-trivial changes, so you (or an AI assistant) get the map instead of re-reading the whole tree.

Outputs live in `graphify-out/` (gitignored, regenerated on demand):

- `GRAPH_REPORT.md` — plain-language audit: node/edge counts, community clusters, "god nodes" (most connected), surprising cross-file connections
- `graph.json` — raw graph data (GraphRAG-ready)
- `graph.html` — interactive graph, open directly in a browser
- `query_*.py` — small helper scripts for ad-hoc lookups (collaborators, publications, Hugo template relationships) against `graph.json`

### Usage

Rebuild the full graph after significant content/structure changes:

```bash
/graphify .
```

Re-extract only new/changed files (faster, cheaper):

```bash
/graphify . --update
```

Ask a question against the existing graph:

```bash
/graphify query "how does the portfolio section link to publications?"
```

Explain a single node or trace the shortest path between two concepts:

```bash
/graphify explain "somrat theme"
/graphify path "about page" "portfolio"
```

Graphify needs an AI coding assistant (e.g. this repo's `AGENTS.md`-aware tooling) to run the semantic extraction step — it is not a standalone CLI you run in isolation.

> More information on the [Graphify GitHub Repo](https://github.com/Graphify-Labs/graphify).

---

A personal portfolio with minimalist design and responsiveness based on the [hugo-somrat](https://themes.gohugo.io/somrat/ "Somrat Theme") theme.

![Thumbnail](https://somrat.netlify.app/images/Slider/slider-1.jpg "Somrat Sorkar")

## :books: Stats for this Repo

[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fhugo-toha%2Ftoha%2Fbadge%3Fref%3Dmain&style=flat)](https://actions-badge.atrox.dev/hugo-toha/toha/goto?ref=main)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/loic-nazaries/hugo-website?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/loic-nazaries/hugo-website?style=plastic)

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/loic-nazaries/hugo-website?color=brightgreen&style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/loic-nazaries/hugo-website?style=plastic)

![GitHub contributors](https://img.shields.io/github/contributors/loic-nazaries/hugo-website?color=yellow&style=plastic)
![GitHub issues](https://img.shields.io/github/issues/loic-nazaries/hugo-website?color=important&style=plastic)
![GitHub pull requests](https://img.shields.io/github/issues-pr/loic-nazaries/hugo-website?color=yellow&style=plastic)

![GitHub language count](https://img.shields.io/github/languages/count/loic-nazaries/hugo-website?color=blueviolet&style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/loic-nazaries/hugo-website?color=blueviolet&style=plastic)
![Markdown syntax](https://img.shields.io/badge/syntax-markdown-blueviolet?style=plastic)

![GitHub License](https://img.shields.io/github/license/loic-nazaries/hugo-website?color=ff69b4&style=plastic "GitHub License")

### :chart_with_upwards_trend: [My Github Profile](https://github.com/loic-nazaries "My Github Profile") Stats

| Github Stats                                                                                                                                                   | Top Languages                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Website's GitHub Stats](https://github-readme-stats.vercel.app/api?username=loic-nazaries&count_private=true&theme=dracula&show_icons=true&hide_title=false) | ![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=loic-nazaries&exclude_repo=starter_repo,streamlit_heroku_example,awesome-markdown,jupyterlab-git,binder_test,my-first-binder,ipenywis,github-readme-stats&langs_count=10&layout=compact) |
