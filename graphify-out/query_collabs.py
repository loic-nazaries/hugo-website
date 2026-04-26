import json
from pathlib import Path

d = json.loads(Path('graphify-out/graph.json').read_text(encoding='utf-8'))
nodes = {n['id']: n for n in d['nodes']}
edges = d['edges']

loic_edges = [e for e in edges if
    'nazaries' in e.get('source','').lower() or
    'nazaries' in e.get('target','').lower() or
    'loic' in e.get('source','').lower() or
    'loic' in e.get('target','').lower()]
print("Edges involving Loic:", len(loic_edges))

collab_nodes = {}
for e in loic_edges:
    for k in ['source', 'target']:
        nid = e.get(k)
        if nid and nid in nodes and 'nazaries' not in nid.lower() and 'loic' not in nid.lower():
            lbl = nodes[nid]['label']
            rel = e.get('relation', '')
            collab_nodes[lbl] = rel

print("\nConnected nodes and relationships:")
for lbl, rel in sorted(collab_nodes.items()):
    print(f"  [{rel}] {lbl}")
