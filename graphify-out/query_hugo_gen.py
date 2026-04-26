import json
from pathlib import Path

G_data = json.loads(Path("graphify-out/graph.json").read_text())

# Build label lookup
id_to_label = {n["id"]: n.get("label", n["id"]) for n in G_data["nodes"]}

# Find nodes relevant to Hugo generation
keywords = ["layout", "baseof", "partial", "template", "hugo", "config", "content",
            "portfolio", "single", "list", "head", "footer", "header", "index"]
relevant_ids = set()
for n in G_data["nodes"]:
    label = n.get("label", "").lower()
    nid = n.get("id", "").lower()
    if any(k in label or k in nid for k in keywords):
        relevant_ids.add(n["id"])

print(f"Relevant nodes ({len(relevant_ids)}):")
for rid in sorted(relevant_ids):
    print(f"  {rid}: {id_to_label.get(rid, rid)}")

print()
print("Relevant edges:")
for e in G_data["edges"]:
    src = e.get("source")
    tgt = e.get("target")
    src_id = src if isinstance(src, str) else str(src)
    tgt_id = tgt if isinstance(tgt, str) else str(tgt)
    if src_id in relevant_ids or tgt_id in relevant_ids:
        src_label = id_to_label.get(src_id, src_id)
        tgt_label = id_to_label.get(tgt_id, tgt_id)
        print(f"  [{src_label}] --{e.get('relation','?')}--> [{tgt_label}]  ({e.get('confidence','?')})")
