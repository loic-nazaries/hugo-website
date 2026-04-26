import json
from pathlib import Path

d = json.loads(Path('graphify-out/graph.json').read_text(encoding='utf-8'))
nodes = {n['id']: n for n in d['nodes']}
edges = d['edges']

# Find publication nodes
pub_nodes = {nid: n for nid, n in nodes.items() if
    any(k in n.get('label','').lower() for k in ['nazaries et al', 'fang et al', 'martins et al', 'jiang et al', 'jeffries', 'mcnee', 'rayu', 'singh et al'])}

print("Publications:", len(pub_nodes))
for nid, n in pub_nodes.items():
    print(f"\n  {n['label']}")
    # Find what connects to this publication
    for e in edges:
        s, t = e.get('source'), e.get('target')
        if s == nid or t == nid:
            other = t if s == nid else s
            if other in nodes:
                print(f"    --[{e.get('relation','')}]--> {nodes[other]['label']}")

# Also find nodes that are people/co-authors
print("\n\nPeople nodes in graph:")
for nid, n in nodes.items():
    lbl = n.get('label','')
    ft = n.get('file_type', '')
    # Look for person-like labels (Firstname Lastname patterns or 'Smriti' etc)
    if ft == 'person' or (len(lbl.split()) == 2 and lbl[0].isupper() and not any(c in lbl for c in ['(', '/', '-', ':'])):
        print(f"  [{ft}] {lbl}")
