import json
from pathlib import Path

detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text())
doc_files = detect["files"].get("document", [])
paper_files = detect["files"].get("paper", [])
all_text_files = doc_files + paper_files

# Split into chunks of 22
chunk_size = 22
chunks = [all_text_files[i:i+chunk_size] for i in range(0, len(all_text_files), chunk_size)]
for i, chunk in enumerate(chunks):
    Path(f"graphify-out/.graphify_chunk_{i+1}.txt").write_text("\n".join(chunk))
    print(f"Chunk {i+1}: {len(chunk)} files")

print(f"\nTotal text files: {len(all_text_files)}, chunks: {len(chunks)}")
