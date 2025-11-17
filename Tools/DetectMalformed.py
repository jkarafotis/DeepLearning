from pathlib import Path
'''
Simple tool to sort out any bad data in our collection
! Assure you are located in the top level of the DeepLearning Repository !
'''

# 🔧 Data class folder
DataPath = r"data\ModelNet40\airplane"
root = Path(DataPath)


def first_meaningful_line(p: Path) -> str | None:
    """Return the first non-empty, non-comment line (stripped), or None."""
    try:
        with p.open("r", encoding="utf-8", errors="ignore") as f:
            for ln in f:
                s = ln.strip()
                if not s:
                    continue
                if s.lstrip().startswith("#"):  # comment
                    continue
                return s
    except Exception as e:
        print(f"[warn] Failed to read {p}: {e}")
    return None


def is_malformed_off_header(line: str) -> bool:
    """True if header looks like 'OFF540 496 0' instead of 'OFF' on its own line."""
    if not line or not line.startswith("OFF"):
        return False
    rest = line[3:].strip()
    return bool(rest)  # if anything follows OFF directly → malformed


bad_files = []
total = 0

for p in root.rglob("*.off"):
    total += 1
    line = first_meaningful_line(p)
    if line and is_malformed_off_header(line):
        bad_files.append(p)

print(f"\nScanned {total} .off files under: {root.resolve()}")
print(f"Found {len(bad_files)} malformed OFF headers:\n")

for i, p in enumerate(bad_files, 1):
    print(f"{i:>3}. {p}")
