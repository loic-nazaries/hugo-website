import json
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.analyze import god_nodes
from graphify.wiki import to_wiki
from pathlib import Path

extraction = json.loads(Path("graphify-out/.graphify_extract.json").read_text())
analysis = json.loads(Path("graphify-out/.graphify_analysis.json").read_text())

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis["communities"].items()}
gods = god_nodes(G)

output_dir = Path("graphify-out/wiki")
output_dir.mkdir(exist_ok=True)

n = to_wiki(G, communities, output_dir, god_nodes_data=gods)
print(f"Wiki written: {n} articles + index.md -> graphify-out/wiki/")
