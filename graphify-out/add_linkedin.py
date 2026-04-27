"""
Inject a LinkedIn profile node (and related professional nodes)
into .graphify_extract.json, then rebuild graph.json.

LinkedIn blocks unauthenticated scraping, so we derive the profile
from website content already in the corpus.
"""
import json
from pathlib import Path

extract_path = Path("graphify-out/.graphify_extract.json")
extract = json.loads(extract_path.read_text(encoding="utf-8"))

# ── new nodes ──────────────────────────────────────────────────────────────
new_nodes = [
    {
        "id": "linkedin_profile",
        "label": "LinkedIn Profile – Loïc Nazaries",
        "file_type": "document",
        "url": "https://www.linkedin.com/in/loic-nazaries/",
    },
    # Skills listed on the profile / website
    {"id": "skill_data_mining",         "label": "Data Mining",            "file_type": "document"},
    {"id": "skill_machine_learning",    "label": "Machine Learning",       "file_type": "document"},
    {"id": "skill_data_visualisation",  "label": "Data Visualisation",     "file_type": "document"},
    {"id": "skill_database_management", "label": "Database Management",    "file_type": "document"},
    {"id": "skill_web_development",     "label": "Web Development",        "file_type": "document"},
    {"id": "skill_eda",                 "label": "Exploratory Data Analysis","file_type": "document"},
    {"id": "skill_etl",                 "label": "ETL Tools",               "file_type": "document"},
    # Education
    {"id": "western_sydney_university", "label": "Western Sydney University","file_type": "document"},
    {"id": "phd_microbiology",
     "label": "PhD – Land-use Changes & Methanotrophic Communities",
     "file_type": "paper"},
    # Work experience (key roles)
    {"id": "role_freelance_analyst",
     "label": "Data Analyst Freelance – BIFORA (2020–present)",
     "file_type": "document"},
    {"id": "role_freelance_wsu",
     "label": "Data Analyst Freelance – Global Center for Land-Based Innovations, WSU (2019–2020)",
     "file_type": "document"},
    {"id": "role_bi_analyst_imc",
     "label": "Business Intelligence Analyst – IMC Mérignac (2019)",
     "file_type": "document"},
    {"id": "role_statistical_analyst_hie",
     "label": "Statistical Research Analyst – Hawkesbury Institute for the Environment, WSU (2011–2019)",
     "file_type": "document"},
    {"id": "role_bi_trainer_iseg",
     "label": "BI Trainer (Tableau) – ISEG Bordeaux (2020–present)",
     "file_type": "document"},
]

# ── new edges ──────────────────────────────────────────────────────────────
new_edges = [
    # LinkedIn profile ↔ person
    {"source": "linkedin_profile", "target": "loic_nazaries",
     "relation": "belongs to", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "loic_nazaries"},
    {"source": "loic_nazaries", "target": "linkedin_profile",
     "relation": "listed on", "confidence": "EXTRACTED",
     "_src": "loic_nazaries", "_tgt": "linkedin_profile"},

    # Skills
    {"source": "linkedin_profile", "target": "skill_data_mining",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_data_mining"},
    {"source": "linkedin_profile", "target": "skill_machine_learning",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_machine_learning"},
    {"source": "linkedin_profile", "target": "skill_data_visualisation",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_data_visualisation"},
    {"source": "linkedin_profile", "target": "skill_database_management",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_database_management"},
    {"source": "linkedin_profile", "target": "skill_web_development",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_web_development"},
    {"source": "linkedin_profile", "target": "skill_eda",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_eda"},
    {"source": "linkedin_profile", "target": "skill_etl",
     "relation": "lists skill", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "skill_etl"},

    # Education
    {"source": "linkedin_profile", "target": "western_sydney_university",
     "relation": "lists education", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "western_sydney_university"},
    {"source": "western_sydney_university", "target": "phd_microbiology",
     "relation": "awarded", "confidence": "EXTRACTED",
     "_src": "western_sydney_university", "_tgt": "phd_microbiology"},
    {"source": "loic_nazaries", "target": "phd_microbiology",
     "relation": "holds degree", "confidence": "EXTRACTED",
     "_src": "loic_nazaries", "_tgt": "phd_microbiology"},
    {"source": "loic_nazaries", "target": "western_sydney_university",
     "relation": "studied at", "confidence": "EXTRACTED",
     "_src": "loic_nazaries", "_tgt": "western_sydney_university"},

    # Experience roles on LinkedIn
    {"source": "linkedin_profile", "target": "role_freelance_analyst",
     "relation": "lists experience", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "role_freelance_analyst"},
    {"source": "linkedin_profile", "target": "role_freelance_wsu",
     "relation": "lists experience", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "role_freelance_wsu"},
    {"source": "linkedin_profile", "target": "role_bi_analyst_imc",
     "relation": "lists experience", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "role_bi_analyst_imc"},
    {"source": "linkedin_profile", "target": "role_statistical_analyst_hie",
     "relation": "lists experience", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "role_statistical_analyst_hie"},
    {"source": "linkedin_profile", "target": "role_bi_trainer_iseg",
     "relation": "lists experience", "confidence": "EXTRACTED",
     "_src": "linkedin_profile", "_tgt": "role_bi_trainer_iseg"},

    # Roles ↔ existing org/person nodes
    {"source": "role_freelance_analyst", "target": "bifora",
     "relation": "at", "confidence": "EXTRACTED",
     "_src": "role_freelance_analyst", "_tgt": "bifora"},
    {"source": "role_statistical_analyst_hie", "target": "hawkesbury_institute",
     "relation": "at", "confidence": "EXTRACTED",
     "_src": "role_statistical_analyst_hie", "_tgt": "hawkesbury_institute"},

    # PhD connects to existing Nazaries papers
    {"source": "phd_microbiology", "target": "nazaries_2011",
     "relation": "published as", "confidence": "EXTRACTED",
     "_src": "phd_microbiology", "_tgt": "nazaries_2011"},

    # About page already links to skills
    {"source": "about_page", "target": "skill_data_mining",
     "relation": "describes", "confidence": "EXTRACTED",
     "_src": "about_page", "_tgt": "skill_data_mining"},
    {"source": "about_page", "target": "skill_machine_learning",
     "relation": "describes", "confidence": "EXTRACTED",
     "_src": "about_page", "_tgt": "skill_machine_learning"},
]

# ── merge (skip duplicates by id / source+target) ─────────────────────────
existing_ids = {n["id"] for n in extract["nodes"]}
for n in new_nodes:
    if n["id"] not in existing_ids:
        extract["nodes"].append(n)
        existing_ids.add(n["id"])

existing_edge_keys = {
    (e.get("source"), e.get("target"), e.get("relation"))
    for e in extract["edges"]
}
for e in new_edges:
    key = (e["source"], e["target"], e["relation"])
    if key not in existing_edge_keys:
        extract["edges"].append(e)
        existing_edge_keys.add(key)

extract_path.write_text(json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated extract: {len(extract['nodes'])} nodes, {len(extract['edges'])} edges")
