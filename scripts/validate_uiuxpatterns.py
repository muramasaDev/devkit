"""python scripts/validate_uiuxpatterns.py: exit 0 when the uiuxpatterns skill is consistent."""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "skills" / "uiuxpatterns"
REF = ROOT / "references"

CATEGORIES = {
    "FB": "feedback.md", "FM": "forms.md", "LD": "loading.md",
    "AI": "ai-interfaces.md", "ES": "empty-states.md", "GS": "gestures.md",
    "MO": "motion.md", "NV": "navigation.md", "DP": "dark-patterns.md",
    "IC": "icon-terminology.md",
}
FIELDS = [
    "ID", "Korean Name", "English Name", "Category", "Definition", "Purpose",
    "User Problem", "When to Use", "When Not to Use", "Interaction Behavior",
    "Required States", "Visual Guidelines", "Accessibility",
    "Responsive Considerations", "Implementation Guidelines",
    "Common Mistakes", "Related Patterns", "Reference Image",
]
FORBIDDEN = "·・—–"

sys.stdout.reconfigure(encoding="utf-8")
errors = []


def read(p):
    return p.read_text(encoding="utf-8")


def check_skill_md():
    m = re.match(r"---\n(.*?)\n---\n", read(ROOT / "SKILL.md"), re.S)
    if not m:
        return errors.append("SKILL.md: no frontmatter")
    get = lambda key: (re.search(rf"^\s*{key}:\s*(.+)$", m.group(1), re.M) or [None, ""])[1].strip()
    if get("name") != ROOT.name:
        errors.append(f"SKILL.md: name != {ROOT.name}")
    if not 0 < len(get("description")) <= 1024:
        errors.append("SKILL.md: description missing or over 1024 chars")


def catalog():
    rows = {}
    for line in read(REF / "pattern-catalog.md").splitlines():
        m = re.match(r"\|\s*([A-Z]{2}-\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            rows[m[1]] = (re.sub(r"\s*\(.*\)$", "", m[2]), m[3])
    return rows


def check_patterns(cat):
    total = 0
    for prefix, fname in CATEGORIES.items():
        blocks = re.split(r"^## (?=[A-Z]{2}-\d{2} )", read(REF / fname), flags=re.M)[1:]
        ids = [b[:5] for b in blocks]
        for pid, block in zip(ids, blocks):
            body = re.split(r"^## ", block, flags=re.M)[0]
            found = re.findall(r"^- ([A-Za-z ]+?):[ \t]*(.*)$", body, re.M)
            if [n for n, _ in found] != FIELDS:
                errors.append(f"{fname} {pid}: fields differ from the 18-field spec")
            errors.extend(f"{fname} {pid}: empty '{n}'" for n, v in found if not v.strip())
            ko, en = cat.get(pid, ("?", "?"))
            head = body.splitlines()[0]
            if ko not in head or en.lower() not in head.lower():
                errors.append(f"{fname} {pid}: title differs from catalog ({ko}, {en})")
        if ids != [f"{prefix}-{i:02d}" for i in range(1, 10)]:
            errors.append(f"{fname}: ids {ids}")
        total += len(ids)
    if len(cat) != 90:
        errors.append(f"pattern-catalog.md: {len(cat)} patterns, expected 90")
    return total


def check_links():
    skill = read(ROOT / "SKILL.md")
    for f in [ROOT / "SKILL.md", *ROOT.glob("*/*.md")]:
        text = read(f)
        # assets/ is not shipped
        for p in set(re.findall(r"`((?:references|templates)/[^`\s*<>]+)`", text)):
            if not (ROOT / p).exists():
                errors.append(f"{f.name}: missing {p}")
        if f.parent == REF:
            for p in set(re.findall(r"`([a-z0-9-]+\.md)`", text)):
                if not (REF / p).exists():
                    errors.append(f"{f.name}: missing {p}")
            if f"references/{f.name}" not in skill:
                errors.append(f"SKILL.md: references/{f.name} not listed")


def check_style():
    for f in [ROOT / "SKILL.md", *ROOT.glob("*/*.md")]:
        for i, line in enumerate(read(f).splitlines(), 1):
            if any(ch in line for ch in FORBIDDEN):
                errors.append(f"{f.name}:{i}: forbidden punctuation")


def main():
    check_skill_md()
    cat = catalog()
    total = check_patterns(cat)
    check_links()
    check_style()
    print(f"catalog {len(cat)}, detailed {total}, fields {len(FIELDS)}")
    print("\n".join(["FAIL", *errors]) if errors else "OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
