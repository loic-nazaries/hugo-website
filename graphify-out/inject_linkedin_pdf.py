"""
Inject LinkedIn profile data extracted from LinkedinProfile.pdf into
.graphify_extract.json. Removes any stub nodes added previously and
replaces with accurate, complete data from the real PDF.
"""
import json
from pathlib import Path

extract_path = Path("graphify-out/.graphify_extract.json")
extract = json.loads(extract_path.read_text(encoding="utf-8"))

# ── Remove previously added stub LinkedIn nodes (they were incomplete) ─────
STUB_IDS = {
    "linkedin_profile", "skill_data_mining", "skill_machine_learning",
    "skill_data_visualisation", "skill_database_management",
    "skill_web_development", "skill_eda", "skill_etl",
    "western_sydney_university", "phd_microbiology",
    "role_freelance_analyst", "role_freelance_wsu", "role_bi_analyst_imc",
    "role_statistical_analyst_hie", "role_bi_trainer_iseg",
}
extract["nodes"] = [n for n in extract["nodes"] if n["id"] not in STUB_IDS]
extract["edges"] = [
    e for e in extract["edges"]
    if e.get("source") not in STUB_IDS and e.get("target") not in STUB_IDS
]

# ── New nodes from PDF ──────────────────────────────────────────────────────
new_nodes = [
    # LinkedIn profile page (anchor)
    {"id": "linkedin_profile",
     "label": "LinkedIn Profile – Loïc Nazaries",
     "file_type": "document",
     "url": "https://www.linkedin.com/in/loic-nazaries/"},

    # ── Work experience ──
    {"id": "softeam",
     "label": "SOFTEAM",
     "file_type": "document"},
    {"id": "role_softeam_consultant",
     "label": "Consultant Données – SOFTEAM (Oct 2025–present)",
     "file_type": "document"},

    {"id": "epsyl_alcen",
     "label": "EPSYL – ALCEN Group",
     "file_type": "document"},
    {"id": "role_epsyl_datascientist",
     "label": "Data Scientist – EPSYL-ALCEN Group (Oct 2022–Sep 2025)",
     "file_type": "document"},
    {"id": "role_epsyl_bi_analyst",
     "label": "Data & BI Analyst – EPSYL-ALCEN Group (May–Oct 2022)",
     "file_type": "document"},

    {"id": "ia_school",
     "label": "IA School Bordeaux",
     "file_type": "document"},
    {"id": "role_iaschool_trainer",
     "label": "Chargé de cours BI – IA School (Apr–May 2024)",
     "file_type": "document"},

    {"id": "iseg",
     "label": "ISEG Bordeaux",
     "file_type": "document"},
    {"id": "role_iseg_trainer",
     "label": "Chargé de cours Data Analyse & BI – ISEG (Oct 2022–Jan 2023)",
     "file_type": "document"},

    {"id": "diderot_education",
     "label": "Diderot Education",
     "file_type": "document"},
    {"id": "role_diderot_trainer",
     "label": "Chargé de cours Biostatistiques – Diderot Education (Sep 2021–May 2022)",
     "file_type": "document"},

    {"id": "bifora",
     "label": "BIFORA",
     "file_type": "document"},
    {"id": "role_bifora_analyst",
     "label": "Data Analyst – BIFORA (Jan–Jun 2021)",
     "file_type": "document"},

    {"id": "wsu_global_centre",
     "label": "WSU Global Centre for Land-Based Innovations",
     "file_type": "document"},
    {"id": "role_wsu_globalcentre",
     "label": "Data Analyst – WSU Global Centre for Land-Based Innovations (Sep 2019–Jan 2020)",
     "file_type": "document"},

    {"id": "items_media_concept",
     "label": "Items Media Concept (IMC)",
     "file_type": "document"},
    {"id": "role_imc_bi_analyst",
     "label": "Business Intelligence Analyst – Items Media Concept (Jun–Aug 2019)",
     "file_type": "document"},

    {"id": "james_hutton_institute",
     "label": "The James Hutton Institute / BioSS",
     "file_type": "document"},
    {"id": "role_hutton_biostatistician",
     "label": "Biostatisticien / Data Analyst Junior – James Hutton Institute (Jul 2007–Apr 2011)",
     "file_type": "document"},
    {"id": "role_hutton_microbiologist",
     "label": "Microbiologiste Moléculaire – James Hutton Institute (Apr–Sep 2005)",
     "file_type": "document"},

    {"id": "rowett_research_institute",
     "label": "Rowett Research Institute",
     "file_type": "document"},
    {"id": "role_rowett_ra",
     "label": "Assistant de Recherche – Rowett Research Institute (2002–2004)",
     "file_type": "document"},

    # ── Education ──
    {"id": "university_of_warwick",
     "label": "University of Warwick",
     "file_type": "document"},
    {"id": "phd_warwick",
     "label": "PhD Biostatistiques & Analyses de Données – University of Warwick (2007–2011)",
     "file_type": "document"},

    {"id": "university_of_aberdeen",
     "label": "University of Aberdeen",
     "file_type": "document"},
    {"id": "phd_aberdeen",
     "label": "PhD Microbiologie Environnementale & Biostatistiques – University of Aberdeen (2007–2011)",
     "file_type": "document"},

    {"id": "la_piscine",
     "label": "La Piscine Centre de Formation",
     "file_type": "document"},
    {"id": "training_la_piscine",
     "label": "Formation Développeur Python / Data Analyst – La Piscine (Jan–Nov 2020)",
     "file_type": "document"},

    {"id": "robert_gordon_university",
     "label": "Robert Gordon University",
     "file_type": "document"},
    {"id": "msc_robert_gordon",
     "label": "MSc Sciences des Analyses Instrumentales – Robert Gordon University (2004–2005)",
     "file_type": "document"},
    {"id": "bsc_robert_gordon",
     "label": "Licence Sciences Biologiques – Robert Gordon University (2002–2004)",
     "file_type": "document"},

    # ── Certifications ──
    {"id": "cert_sas_essentials",
     "label": "Certification SAS Programming | Essentials",
     "file_type": "document"},
    {"id": "cert_tableau_desktop",
     "label": "Certification Tableau Desktop",
     "file_type": "document"},
    {"id": "cert_sas_data_manip",
     "label": "Certification SAS Programming | Data Manipulation Techniques",
     "file_type": "document"},
    {"id": "cert_reviewing",
     "label": "Certificate of Reviewing",
     "file_type": "document"},

    # ── Patent ──
    {"id": "patent_mt_rflp",
     "label": "Patent: Multiplex Terminal-Restriction Fragment Length Polymorphism (MT-RFLP)",
     "file_type": "paper"},

    # ── Skills (key ones not already in graph) ──
    {"id": "skill_python",
     "label": "Python Programming",
     "file_type": "document"},
    {"id": "skill_web_scraping",
     "label": "Web Scraping",
     "file_type": "document"},
    {"id": "skill_sas",
     "label": "SAS Programming",
     "file_type": "document"},
    {"id": "skill_tableau",
     "label": "Tableau Software",
     "file_type": "document"},
    {"id": "skill_streamlit",
     "label": "Streamlit",
     "file_type": "document"},
    {"id": "skill_talend",
     "label": "Talend ETL",
     "file_type": "document"},
    {"id": "skill_biostatistics",
     "label": "Biostatistics",
     "file_type": "document"},
    {"id": "skill_machine_learning",
     "label": "Machine Learning",
     "file_type": "document"},
    {"id": "skill_r_shiny",
     "label": "R Shiny",
     "file_type": "document"},

    # ── Languages ──
    {"id": "lang_english",
     "label": "English (Native / Bilingual)",
     "file_type": "document"},
    {"id": "lang_french",
     "label": "French (Native / Bilingual)",
     "file_type": "document"},

    # ── Honors/Awards ──
    {"id": "award_phd_grant",
     "label": "PhD Grant",
     "file_type": "document"},
    {"id": "award_macaulay_trust",
     "label": "Macaulay Development Trust Award",
     "file_type": "document"},
    {"id": "award_conference_fund",
     "label": "Conference Travel and Training Fund",
     "file_type": "document"},
]

# ── Edges ───────────────────────────────────────────────────────────────────
new_edges = [
    # LinkedIn profile ↔ person
    {"source": "linkedin_profile", "target": "loic_nazaries",
     "relation": "belongs to", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "linkedin_profile",
     "relation": "listed on", "confidence": "EXTRACTED"},

    # ── Experience ──
    # SOFTEAM
    {"source": "linkedin_profile", "target": "role_softeam_consultant",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_softeam_consultant", "target": "softeam",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "softeam",
     "relation": "currently works at", "confidence": "EXTRACTED"},
    {"source": "softeam", "target": "skill_web_scraping",
     "relation": "involves", "confidence": "EXTRACTED"},

    # EPSYL
    {"source": "linkedin_profile", "target": "role_epsyl_datascientist",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "role_epsyl_bi_analyst",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_epsyl_datascientist", "target": "epsyl_alcen",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "role_epsyl_bi_analyst", "target": "epsyl_alcen",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "epsyl_alcen",
     "relation": "worked at", "confidence": "EXTRACTED"},
    {"source": "role_epsyl_datascientist", "target": "skill_machine_learning",
     "relation": "applied", "confidence": "EXTRACTED"},
    {"source": "role_epsyl_bi_analyst", "target": "skill_talend",
     "relation": "used", "confidence": "EXTRACTED"},
    {"source": "role_epsyl_bi_analyst", "target": "skill_streamlit",
     "relation": "used", "confidence": "EXTRACTED"},

    # IA School
    {"source": "linkedin_profile", "target": "role_iaschool_trainer",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_iaschool_trainer", "target": "ia_school",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "ia_school",
     "relation": "taught at", "confidence": "EXTRACTED"},
    {"source": "role_iaschool_trainer", "target": "skill_tableau",
     "relation": "taught", "confidence": "EXTRACTED"},
    {"source": "role_iaschool_trainer", "target": "skill_r_shiny",
     "relation": "taught", "confidence": "EXTRACTED"},

    # ISEG
    {"source": "linkedin_profile", "target": "role_iseg_trainer",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_iseg_trainer", "target": "iseg",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "iseg",
     "relation": "taught at", "confidence": "EXTRACTED"},

    # Diderot Education
    {"source": "linkedin_profile", "target": "role_diderot_trainer",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_diderot_trainer", "target": "diderot_education",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "diderot_education",
     "relation": "taught at", "confidence": "EXTRACTED"},
    {"source": "role_diderot_trainer", "target": "skill_biostatistics",
     "relation": "taught", "confidence": "EXTRACTED"},

    # BIFORA
    {"source": "linkedin_profile", "target": "role_bifora_analyst",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_bifora_analyst", "target": "bifora",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "bifora",
     "relation": "worked for", "confidence": "EXTRACTED"},
    {"source": "role_bifora_analyst", "target": "skill_python",
     "relation": "used", "confidence": "EXTRACTED"},
    {"source": "role_bifora_analyst", "target": "skill_streamlit",
     "relation": "used", "confidence": "EXTRACTED"},
    {"source": "role_bifora_analyst", "target": "skill_talend",
     "relation": "used", "confidence": "EXTRACTED"},
    {"source": "role_bifora_analyst", "target": "skill_tableau",
     "relation": "used", "confidence": "EXTRACTED"},

    # WSU Global Centre
    {"source": "linkedin_profile", "target": "role_wsu_globalcentre",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_wsu_globalcentre", "target": "wsu_global_centre",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "wsu_global_centre",
     "relation": "worked at", "confidence": "EXTRACTED"},
    {"source": "role_wsu_globalcentre", "target": "skill_sas",
     "relation": "used", "confidence": "EXTRACTED"},
    {"source": "role_wsu_globalcentre", "target": "skill_tableau",
     "relation": "used", "confidence": "EXTRACTED"},

    # IMC
    {"source": "linkedin_profile", "target": "role_imc_bi_analyst",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_imc_bi_analyst", "target": "items_media_concept",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "items_media_concept",
     "relation": "worked at", "confidence": "EXTRACTED"},
    {"source": "role_imc_bi_analyst", "target": "skill_talend",
     "relation": "used", "confidence": "EXTRACTED"},

    # James Hutton / BioSS
    {"source": "linkedin_profile", "target": "role_hutton_biostatistician",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "role_hutton_microbiologist",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_hutton_biostatistician", "target": "james_hutton_institute",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "role_hutton_microbiologist", "target": "james_hutton_institute",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "james_hutton_institute",
     "relation": "worked at", "confidence": "EXTRACTED"},
    {"source": "role_hutton_microbiologist", "target": "patent_mt_rflp",
     "relation": "resulted in", "confidence": "EXTRACTED"},

    # Rowett
    {"source": "linkedin_profile", "target": "role_rowett_ra",
     "relation": "lists experience", "confidence": "EXTRACTED"},
    {"source": "role_rowett_ra", "target": "rowett_research_institute",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "rowett_research_institute",
     "relation": "worked at", "confidence": "EXTRACTED"},

    # ── Education ──
    {"source": "linkedin_profile", "target": "phd_warwick",
     "relation": "lists education", "confidence": "EXTRACTED"},
    {"source": "phd_warwick", "target": "university_of_warwick",
     "relation": "awarded by", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "university_of_warwick",
     "relation": "studied at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "phd_warwick",
     "relation": "holds degree", "confidence": "EXTRACTED"},

    {"source": "linkedin_profile", "target": "phd_aberdeen",
     "relation": "lists education", "confidence": "EXTRACTED"},
    {"source": "phd_aberdeen", "target": "university_of_aberdeen",
     "relation": "awarded by", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "university_of_aberdeen",
     "relation": "studied at", "confidence": "EXTRACTED"},

    {"source": "linkedin_profile", "target": "training_la_piscine",
     "relation": "lists education", "confidence": "EXTRACTED"},
    {"source": "training_la_piscine", "target": "la_piscine",
     "relation": "at", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "la_piscine",
     "relation": "trained at", "confidence": "EXTRACTED"},

    {"source": "linkedin_profile", "target": "msc_robert_gordon",
     "relation": "lists education", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "bsc_robert_gordon",
     "relation": "lists education", "confidence": "EXTRACTED"},
    {"source": "msc_robert_gordon", "target": "robert_gordon_university",
     "relation": "awarded by", "confidence": "EXTRACTED"},
    {"source": "bsc_robert_gordon", "target": "robert_gordon_university",
     "relation": "awarded by", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "robert_gordon_university",
     "relation": "studied at", "confidence": "EXTRACTED"},

    # ── Certifications ──
    {"source": "linkedin_profile", "target": "cert_sas_essentials",
     "relation": "lists certification", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "cert_tableau_desktop",
     "relation": "lists certification", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "cert_sas_data_manip",
     "relation": "lists certification", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "cert_reviewing",
     "relation": "lists certification", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "cert_sas_essentials",
     "relation": "holds", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "cert_tableau_desktop",
     "relation": "holds", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "cert_sas_data_manip",
     "relation": "holds", "confidence": "EXTRACTED"},

    # Certs ↔ skills
    {"source": "cert_sas_essentials", "target": "skill_sas",
     "relation": "validates", "confidence": "EXTRACTED"},
    {"source": "cert_sas_data_manip", "target": "skill_sas",
     "relation": "validates", "confidence": "EXTRACTED"},
    {"source": "cert_tableau_desktop", "target": "skill_tableau",
     "relation": "validates", "confidence": "EXTRACTED"},

    # ── Patent ──
    {"source": "loic_nazaries", "target": "patent_mt_rflp",
     "relation": "invented", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "patent_mt_rflp",
     "relation": "lists patent", "confidence": "EXTRACTED"},

    # ── Skills ──
    {"source": "linkedin_profile", "target": "skill_python",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_web_scraping",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_machine_learning",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_biostatistics",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_tableau",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_sas",
     "relation": "lists skill", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "skill_streamlit",
     "relation": "lists skill", "confidence": "EXTRACTED"},

    # ── Languages ──
    {"source": "linkedin_profile", "target": "lang_english",
     "relation": "lists language", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "lang_french",
     "relation": "lists language", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "lang_english",
     "relation": "speaks", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "lang_french",
     "relation": "speaks", "confidence": "EXTRACTED"},

    # ── Awards ──
    {"source": "linkedin_profile", "target": "award_phd_grant",
     "relation": "lists award", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "award_macaulay_trust",
     "relation": "lists award", "confidence": "EXTRACTED"},
    {"source": "linkedin_profile", "target": "award_conference_fund",
     "relation": "lists award", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "award_phd_grant",
     "relation": "received", "confidence": "EXTRACTED"},
    {"source": "loic_nazaries", "target": "award_macaulay_trust",
     "relation": "received", "confidence": "EXTRACTED"},

    # ── Cross-links to existing papers/nodes ──
    # PhD thesis → Nazaries 2011
    {"source": "phd_aberdeen", "target": "nazaries_2011",
     "relation": "published as", "confidence": "EXTRACTED"},
    {"source": "phd_warwick", "target": "nazaries_2011",
     "relation": "published as", "confidence": "EXTRACTED"},
    # Hutton role → methane papers
    {"source": "role_hutton_biostatistician", "target": "nazaries_et_al_2011",
     "relation": "produced", "confidence": "EXTRACTED"},
    {"source": "role_hutton_biostatistician", "target": "nazaries_et_al_2013a",
     "relation": "produced", "confidence": "EXTRACTED"},
    # HIE role → methane/GHG papers
    {"source": "role_hutton_microbiologist", "target": "nazaries_2005",
     "relation": "produced", "confidence": "EXTRACTED"},
]

# ── Merge (skip duplicates) ─────────────────────────────────────────────────
existing_ids = {n["id"] for n in extract["nodes"]}
added_nodes = 0
for n in new_nodes:
    if n["id"] not in existing_ids:
        extract["nodes"].append(n)
        existing_ids.add(n["id"])
        added_nodes += 1
    else:
        # Update existing node with richer data from PDF
        for existing in extract["nodes"]:
            if existing["id"] == n["id"]:
                existing.update(n)
                break

existing_edge_keys = {
    (e.get("source"), e.get("target"), e.get("relation"))
    for e in extract["edges"]
}
added_edges = 0
for e in new_edges:
    key = (e["source"], e["target"], e["relation"])
    if key not in existing_edge_keys:
        # Add _src/_tgt for graphify compatibility
        e["_src"] = e["source"]
        e["_tgt"] = e["target"]
        extract["edges"].append(e)
        existing_edge_keys.add(key)
        added_edges += 1

extract_path.write_text(
    json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Added {added_nodes} nodes, {added_edges} edges")
print(f"Total: {len(extract['nodes'])} nodes, {len(extract['edges'])} edges")
