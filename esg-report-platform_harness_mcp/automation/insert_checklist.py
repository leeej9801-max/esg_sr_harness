from pathlib import Path
import sys
import re

TEMPLATE = Path("templates/review_checklist.md")
OUT_DIR = Path("reviews")

def next_id():
    existing = sorted(OUT_DIR.glob("R-*.md"))
    if not existing:
        return "R-001"
    nums = [int(re.search(r"R-(\d+)", p.name).group(1)) for p in existing]
    return f"R-{max(nums)+1:03d}"

def main():
    task_id = sys.argv[1] if len(sys.argv) > 1 else "T-000"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    review_id = next_id()
    text = TEMPLATE.read_text(encoding="utf-8").replace("R-000", review_id, 1)
    text = text.replace("T-000", task_id, 1)
    path = OUT_DIR / f"{review_id}.md"
    path.write_text(text, encoding="utf-8")
    print(path)

if __name__ == "__main__":
    main()
