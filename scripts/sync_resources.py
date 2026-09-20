"""Bundle repository bibliographies so installed plugins retain their sources."""

import argparse
from pathlib import Path
import re


def sync_resources(root: Path, check: bool) -> list[str]:
    errors = []
    for source in sorted((root / "docs/resources").glob("*.md")):
        name = source.stem
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"Invalid resource filename: {source.name}")
            continue
        plugin = root / "plugins" / name
        skill = plugin / "skills" / name
        target = skill / "references/sources.md"
        if not (skill / "SKILL.md").is_file() or not target.resolve().is_relative_to(plugin.resolve()):
            errors.append(f"No valid matching primary skill for {source.name}")
            continue
        expected = (
            f"<!-- Generated from docs/resources/{name}.md; edit that file and run "
            "python scripts/sync_resources.py in the repository. -->\n\n"
            + source.read_text(encoding="utf-8")
        )
        actual = target.read_text(encoding="utf-8") if target.is_file() else None
        if actual == expected:
            continue
        if check:
            errors.append(f"Stale bundled bibliography: {target.relative_to(root)}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8", newline="\n")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    errors = sync_resources(Path(__file__).resolve().parents[1], args.check)
    print("\n".join(errors) if errors else "Resource copies are up to date.")
    raise SystemExit(bool(errors))
