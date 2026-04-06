from pathlib import Path
import sys
import re

TEMPLATE = Path("templates/decision_log.md")
OUT_DIR = Path("decisions")

def next_id():
    existing = sorted(OUT_DIR.glob("D-*.md"))
    if not existing:
        return "D-001"
    nums = [int(re.search(r"D-(\d+)", p.name).group(1)) for p in existing]
    return f"D-{max(nums)+1:03d}"

def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "새 결정"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    decision_id = next_id()
    text = TEMPLATE.read_text(encoding="utf-8").replace("D-000", decision_id, 1)
    text = text.replace("[결정명]", title, 1)
    path = OUT_DIR / f"{decision_id}.md"
    path.write_text(text, encoding="utf-8")
    print(path)

if __name__ == "__main__":
    main()
