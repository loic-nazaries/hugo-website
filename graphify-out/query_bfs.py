import json
from pathlib import Path
from collections import deque

graph_data = json.loads(Path('graphify-out/graph.json').read_text(encoding='utf-8'))

nodes = {n['id']: n for n in graph_data['nodes']}
adj = {}
for e in graph_data['edges']:
    s, t = e.get('source', e.get('0')), e.get('target', e.get('1'))
    if s is None or t is None:
        continue
    adj.setdefault(s, []).append((t, e))
    adj.setdefault(t, []).append((s, e))

keywords = ['research', 'scientist', 'science', 'publication', 'paper', 'collab', 'author', 'journal', 'university', 'phd', 'academic', 'study', 'conference', 'data', 'analysis', 'loic', 'portfolio', 'about']

seeds = []
for nid, n in nodes.items():
    label = (n.get('label') or '').lower()
    if any(k in label for k in keywords):
        seeds.append(nid)

print(f"Seed nodes ({len(seeds)}):")
for s in seeds[:30]:
    print(f"  {nodes[s]['label']}")

visited = set(seeds)
frontier = deque(seeds)
for hop in range(2):
    next_frontier = []
    while frontier:
        nid = frontier.popleft()
        for neighbor, edge in adj.get(nid, []):
            if neighbor not in visited:
                visited.add(neighbor)
                next_frontier.append(neighbor)
    frontier = deque(next_frontier)

print(f"\nBFS context ({len(visited)} nodes total):")
for nid in list(visited)[:60]:
    n = nodes[nid]
    print(f"  [{n.get('group', '?')}] {n['label']}")

print("\nKey relationships:")
shown = 0
for e in graph_data['edges']:
    s, t = e.get('source', e.get('0')), e.get('target', e.get('1'))
    if s is None or t is None:
        continue
    if s in visited and t in visited:
        sl = nodes[s]['label']
        tl = nodes[t]['label']
        rel = e.get('relation', e.get('label', ''))
        print(f"  {sl} --[{rel}]--> {tl}")
        shown += 1
        if shown >= 60:
            break
