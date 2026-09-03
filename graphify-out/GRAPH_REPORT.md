# Graph Report - hugo-website  (2026-09-03)

## Corpus Check
- 9 files · ~2,685,774 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 181 nodes · 288 edges · 16 communities detected
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]

## God Nodes (most connected - your core abstractions)
1. `se()` - 10 edges
2. `ce()` - 10 edges
3. `e()` - 9 edges
4. `g()` - 8 edges
5. `M()` - 8 edges
6. `we()` - 7 edges
7. `Ee()` - 7 edges
8. `l()` - 7 edges
9. `l()` - 6 edges
10. `e()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `o()` --calls--> `g()`  [INFERRED]
  themes\somrat\static\plugins\bootstrap\bootstrap.min.js → themes\somrat\static\plugins\wow.min.js
- `n()` --calls--> `g()`  [INFERRED]
  themes\somrat\static\plugins\bootstrap\bootstrap.min.js → themes\somrat\static\plugins\wow.min.js
- `se()` --calls--> `g()`  [INFERRED]
  themes\somrat\static\plugins\jQuery\jquery.min.js → themes\somrat\static\plugins\wow.min.js
- `ce()` --calls--> `g()`  [INFERRED]
  themes\somrat\static\plugins\jQuery\jquery.min.js → themes\somrat\static\plugins\wow.min.js
- `Oe()` --calls--> `k()`  [INFERRED]
  themes\somrat\static\plugins\jQuery\jquery.min.js → themes\somrat\static\plugins\wow.min.js

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (25): Biomathematics and Statistics Scotland, Brajesh K. Singh, Business Intelligence, Catarina S. Martins, Data Visualisation, Diderot Education, Epsyl - Alcen Group, IA School (+17 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (12): e(), i(), l(), n(), o(), s(), t(), we() (+4 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (22): Afforestation, ARIMA, Carbon Dioxide, Database Modelling, EucFACE Experiment, Greenhouse Gas Emissions, Greenhouse Gas Estimation Portal, Greenhouse Gas Modelling (+14 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (14): ze(), e(), f(), A(), c(), d(), e(), i() (+6 more)

### Community 4 - "Community 4"
Cohesion: 0.12
Nodes (3): ct(), dt(), V()

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (9): ce(), Ee(), l(), P(), se(), t(), Te(), xe() (+1 more)

### Community 6 - "Community 6"
Cohesion: 0.36
Nodes (8): be(), de(), s(), c(), h(), l(), o(), r()

### Community 7 - "Community 7"
Cohesion: 0.22
Nodes (9): BIFORA, Conda, Data Pipeline, Extract Transform Load, Google BigQuery, Google Data Studio, IMDB 5000 Movie Dataset, Python (+1 more)

### Community 8 - "Community 8"
Cohesion: 0.32
Nodes (8): A(), b(), Ie(), le(), Oe(), ve(), we(), ye()

### Community 9 - "Community 9"
Cohesion: 0.29
Nodes (8): bt(), d(), I(), j(), M(), qt(), w(), X()

### Community 10 - "Community 10"
Cohesion: 0.25
Nodes (8): Geographical Modelling, Geostatistics, Kriging, Multiplex Terminal Restriction Fragment Length Polymorphism, Machine Learning, Methanotrophs, Environmental Drivers of the Geographical Distribution of Methanotrophs, Random Forest

### Community 11 - "Community 11"
Cohesion: 0.33
Nodes (6): Agricultural Management Practices, Grains Research and Development Corporation, Key Performance Indicator, KPI Modelling, Soil Multifunctionality and Agricultural Management Practices, Soil Multifunctionality

### Community 13 - "Community 13"
Cohesion: 0.67
Nodes (2): e(), t()

### Community 14 - "Community 14"
Cohesion: 0.67
Nodes (4): _e(), et(), fe(), tt()

### Community 15 - "Community 15"
Cohesion: 0.67
Nodes (3): Ae(), ge(), k()

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (2): Chlorpyrifos, Smriti Rayu

## Knowledge Gaps
- **Thin community `Community 13`** (4 nodes): `e()`, `i()`, `t()`, `jquery.waypoints.min.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `Chlorpyrifos`, `Smriti Rayu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `g()` connect `Community 1` to `Community 5`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `ce()` connect `Community 5` to `Community 8`, `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `e()` connect `Community 3` to `Community 5`, `Community 6`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `se()` (e.g. with `h()` and `g()`) actually correct?**
  _`se()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ce()` (e.g. with `e()` and `g()`) actually correct?**
  _`ce()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `e()` (e.g. with `ce()` and `l()`) actually correct?**
  _`e()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._