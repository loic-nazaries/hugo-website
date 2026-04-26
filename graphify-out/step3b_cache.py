import json
from graphify.cache import check_semantic_cache
from pathlib import Path

detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text())
all_files = [f for files in detect["files"].values() for f in files]
cached_nodes, cached_edges, cached_hyperedges, uncached = check_semantic_cache(all_files)

if cached_nodes or cached_edges:
    Path("graphify-out/.graphify_cached.json").write_text(json.dumps({"nodes": cached_nodes, "edges": cached_edges, "hyperedges": cached_hyperedges}))
Path("graphify-out/.graphify_uncached.txt").write_text("\n".join(uncached))
print(f"Cache: {len(all_files)-len(uncached)} hit, {len(uncached)} need extraction")
print(f"Total files: {len(all_files)}, uncached: {len(uncached)}")
# Show breakdown of uncached by type
doc_files = detect["files"].get("document", [])
paper_files = detect["files"].get("paper", [])
image_files = detect["files"].get("image", [])
uncached_set = set(uncached)
print(f"Uncached docs: {len([f for f in doc_files if f in uncached_set])}")
print(f"Uncached papers: {len([f for f in paper_files if f in uncached_set])}")
print(f"Uncached images: {len([f for f in image_files if f in uncached_set])}")
