from pathlib import Path
import sys
import re

TEMPLATE = Path("templates/task_request.md")
OUT_DIR = Path("tasks")

def next_id():
    existing = sorted(OUT_DIR.glob("T-*.md"))
    if not existing:
        return "T-001"
    nums = [int(re.search(r"T-(\d+)", p.name).group(1)) for p in existing]
    return f"T-{max(nums)+1:03d}"

def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "새 작업"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    task_id = next_id()
    text = TEMPLATE.read_text(encoding="utf-8").replace("T-000", task_id, 1)
    text = text.replace("[작업 이름]", title, 1)
    path = OUT_DIR / f"{task_id}.md"
    path.write_text(text, encoding="utf-8")
    print(path)

if __name__ == "__main__":
    main()
