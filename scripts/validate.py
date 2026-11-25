"""devkit 전체 검증: 버전, 설명 길이, SEC ID, 시험 수, 링크, 금지 문구, 비밀 패턴"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def read(p):
    return Path(p).read_text(encoding="utf-8")


def text_files():
    skip = {".git", "evals", "assets"}
    for p in ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & skip) and p.suffix in {".md", ".json", ".yml", ".py", ".csv", ".svg", ""}:
            yield p


# 1. frontmatter
def check_frontmatter():
    for d in sorted(SKILLS.iterdir()):
        s = read(d / "SKILL.md")
        m = re.match(r"---\n(.*?)\n---\n", s, re.S)
        if not m:
            err(f"{d.name}: frontmatter 없음")
            continue
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name or name.group(1).strip() != d.name:
            err(f"{d.name}: name 이 폴더명과 다름")
        if not desc:
            err(f"{d.name}: description 없음")
            continue
        n = len(desc.group(1).strip().strip('"'))
        if n > 1024:
            err(f"{d.name}: description {n}자 (최대 1024)")
        elif n > 300:
            warn(f"{d.name}: description {n}자 (목표 300 이하, 스킬 목록 예산)")


# 2. 버전
def check_versions():
    ver = json.loads(read(ROOT / ".claude-plugin/plugin.json"))["version"]
    mk = json.loads(read(ROOT / ".claude-plugin/marketplace.json"))
    mv = [p.get("version") for p in mk.get("plugins", []) if p.get("version")]
    if any(v != ver for v in mv):
        err(f"marketplace.json 버전 {mv} != plugin.json {ver}")
    for rd in ("README.md", "README.ko.md"):
        if f"version-{ver}-" not in read(ROOT / rd):
            err(f"{rd}: 버전 배지가 {ver} 과 다름")
    if not re.search(rf"^## \[?{re.escape(ver)}\]?", read(ROOT / "CHANGELOG.md"), re.M):
        err(f"CHANGELOG.md: {ver} 항목 없음")
    for d in SKILLS.iterdir():
        v = re.search(r'version:\s*"?([\d.]+)"?', read(d / "SKILL.md").split("---", 2)[1])
        if v and v.group(1) != ver:
            warn(f"{d.name}/SKILL.md: metadata.version {v.group(1)} != {ver}")


# 3. SEC ID 일관성
def sec_ids(s):
    return set(re.findall(r"SEC-(\d{2})", s))


def check_sec():
    sc = SKILLS / "securecoding"
    want = {f"{i:02d}" for i in range(1, 25)}
    files = {
        "SKILL.md": sc / "SKILL.md",
        "controls.md": sc / "references/controls.md",
        "kisa-map.md": sc / "references/kisa-map.md",
        "security-report.md": sc / "templates/security-report.md",
        "security-architecture.md": sc / "templates/security-architecture.md",
    }
    for name, p in files.items():
        got = sec_ids(read(p))
        missing = sorted(want - got)
        extra = sorted(got - want)
        if name in {"SKILL.md", "controls.md", "security-report.md"} and missing:
            err(f"{name}: SEC-{missing} 없음")
        elif missing:
            warn(f"{name}: SEC-{missing} 없음")
        if extra:
            err(f"{name}: 정의되지 않은 SEC-{extra}")
    heads = set(re.findall(r"^##+ SEC-(\d{2})", read(files["controls.md"]), re.M))
    if want - heads:
        err(f"controls.md: SEC-{sorted(want - heads)} 제목(## SEC-xx) 없음")
    order = re.findall(r"^##+ SEC-(\d{2})", read(files["controls.md"]), re.M)
    if order != sorted(order):
        warn("controls.md: SEC 제목이 번호 순이 아님")


# 4. 공격 시험 수
def check_attack_tests():
    sc = SKILLS / "securecoding"
    at = read(sc / "references/attack-tests.md")
    nums = {int(n) for n in re.findall(r"^\|\s*(\d{1,2})\s*\|", at, re.M)}
    nums |= {int(n) for n in re.findall(r"^#{2,4}\s*#?(\d{1,2})[\s.:]", at, re.M)}
    if not nums:
        err("attack-tests.md: 시험 번호를 찾지 못함")
        return
    total = max(nums)
    if nums != set(range(1, total + 1)):
        err(f"attack-tests.md: 번호가 1..{total} 연속이 아님 {sorted(set(range(1, total + 1)) - nums)}")
    rep = {int(n) for n in re.findall(r"^\|\s*(\d{1,2})\s*\|", read(sc / "templates/security-report.md"), re.M)}
    if rep and not set(range(1, total + 1)) <= rep:
        err(f"security-report.md: 시험 {sorted(set(range(1, total + 1)) - rep)} 행 없음")
    for rd in ("README.md", "README.ko.md"):
        m = re.findall(r"<b>(\d+)</b><br>(?:attack tests|공격 시험)", read(ROOT / rd))
        if m and int(m[0]) != total:
            err(f"{rd}: 공격 시험 {m[0]} != {total}")
    m = re.findall(r"<b>(\d+)</b><br>(?:security controls|보안 통제)", read(ROOT / "README.md"))
    if m and int(m[0]) != 24:
        err(f"README.md: 보안 통제 {m[0]} != 24")


# 5. 링크
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")


def check_links():
    for p in ROOT.glob("*.md"):
        for t in LINK.findall(read(p)):
            if t.startswith(("http", "#", "mailto:")):
                continue
            if not (ROOT / t.split("#")[0]).exists():
                err(f"{p.name}: 깨진 링크 {t}")
    for p in re.findall(r'(?:src|href)="([^"#:]+)"', read(ROOT / "README.md")):
        if not (ROOT / p).exists():
            err(f"README.md: 없는 경로 {p}")


# 6. 금지 문구와 개인정보 및 비밀
KISA_CITE = ("행정안전부·한국인터넷진흥원", "개발·운영자")
BAD = {
    "가운뎃점": re.compile("·"),
    "긴 줄표": re.compile("—|―"),
    "옛 이름": re.compile(r"/universal-uiux"),
    "내부 값": re.compile("A" + "IP|대" + "덕|dae" + "duck|CHJ" + "EONG|snoopy" + "jch", re.I),
    "비밀 패턴": re.compile(r"AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
SKIP_FORBID = {"validate.py", "validate_uiuxpatterns.py"}


def check_text():
    for p in text_files():
        if p.name in SKIP_FORBID:
            continue
        s = read(p)
        for c in KISA_CITE:
            s = s.replace(c, "")
        for label, rx in BAD.items():
            if label == "비밀 패턴" and p.name == "controls.md":
                continue
            m = rx.search(s)
            if m:
                line = s[: m.start()].count("\n") + 1
                err(f"{p.relative_to(ROOT)}:{line}: {label} '{m.group(0)[:20]}'")


# 8. 개별 검증기
def run_uiux():
    r = subprocess.run([sys.executable, str(ROOT / "scripts/validate_uiuxpatterns.py")], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        err("validate_uiuxpatterns.py 실패: " + (r.stdout + r.stderr).strip().splitlines()[-1][:200])


# 7. 영어 사본 대조 (skills/<name>/en/ 은 한국어 원본과 ID, 코드 블록, 표 행이 같아야 함)
TOKENS = re.compile(r"SEC-\d{2}|DF-\d{2}|[A-Z]{2}-\d{2}|^#{2,4}\s*#?\d{1,2}", re.M)
HANGUL = re.compile("[가-힣]")


def en_pairs():
    for d in sorted(SKILLS.iterdir()):
        en = d / "en"
        if not en.is_dir():
            continue
        for f in sorted(en.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(en)
            src = d / ("SKILL.md" if rel.name == "SKILL.en.md" else rel)
            yield d.name, f, src


def check_en():
    for skill, f, src in en_pairs():
        label = f.relative_to(ROOT)
        if not src.exists():
            err(f"{label}: 한국어 원본 {src.relative_to(ROOT)} 없음")
            continue
        e, k = read(f), read(src)
        if f.suffix == ".md" and re.match(r"---\nname:", e):
            err(f"{label}: frontmatter name 이 있으면 스킬로 오인됨")
        if f.name != "gitignore":
            te, tk = sorted(set(TOKENS.findall(e))), sorted(set(TOKENS.findall(k)))
            if te != tk:
                err(f"{label}: ID 집합이 원본과 다름 (없음 {sorted(set(tk) - set(te))[:6]}, 추가 {sorted(set(te) - set(tk))[:6]})")
        fe, fk = e.count("```"), k.count("```")
        if fe != fk:
            err(f"{label}: 코드 블록 수 {fe} != 원본 {fk}")
        re_, rk = len(re.findall(r"^\|", e, re.M)), len(re.findall(r"^\|", k, re.M))
        if re_ != rk:
            warn(f"{label}: 표 행 수 {re_} != 원본 {rk}")
        n = len(HANGUL.findall(e))
        if n > max(40, len(e) * 0.03):
            warn(f"{label}: 한글 {n}자 남음")


def main():
    for fn in (check_frontmatter, check_versions, check_sec, check_attack_tests, check_links, check_text, check_en, run_uiux):
        try:
            fn()
        except Exception as e:  # noqa: BLE001
            err(f"{fn.__name__}: {type(e).__name__} {e}")
    for w in warns:
        print("WARN", w)
    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} fail, {len(warns)} warn")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
