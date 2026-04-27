from pathlib import Path

p = Path("C:/Users/loicn/Downloads/LinkedinProfile.pdf")
print("File exists:", p.exists())
if p.exists():
    print("Size:", p.stat().st_size, "bytes")

for lib in ["pypdf", "pdfplumber", "fitz"]:
    try:
        m = __import__(lib)
        print(lib, "available")
    except ImportError:
        print(lib, "NOT available")
