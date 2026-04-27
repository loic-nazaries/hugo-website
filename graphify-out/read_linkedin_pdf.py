"""Extract text from the LinkedIn PDF and print it."""
from pathlib import Path
import pypdf

reader = pypdf.PdfReader("C:/Users/loicn/Downloads/LinkedinProfile.pdf")
text = "\n".join(page.extract_text() or "" for page in reader.pages)
Path("graphify-out/.linkedin_profile.txt").write_text(text, encoding="utf-8")
print(f"Pages: {len(reader.pages)}")
print(text)
