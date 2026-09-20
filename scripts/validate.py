"""Check this collection's catalog, package boundaries, metadata, and local links.

This is a repository contract check, not the full Codex ingestion validator.
"""

import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

from sync_resources import sync_resources


NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"\d+\.\d+\.\d+(?:-[\w.-]+)?(?:\+[\w.-]+)?")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    result = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(result, dict), f"Expected a JSON object: {path}")
    return result


def validate(root: Path) -> dict:
    root = root.resolve()
    catalog = read_json(root / ".agents/plugins/marketplace.json")
    require(NAME.fullmatch(catalog.get("name", "")), "Invalid marketplace name")
    entries = catalog.get("plugins")
    require(isinstance(entries, list) and entries, "Marketplace must list plugins")
    seen = set()
    plugin_roots = []
    skills = 0
    for entry in entries:
        name = entry.get("name", "")
        require(NAME.fullmatch(name) and name not in seen, f"Invalid/duplicate plugin: {name}")
        seen.add(name)
        require(entry.get("source") == {"source": "local", "path": f"./plugins/{name}"},
                f"Plugin source must point to ./plugins/{name}")
        policy = entry.get("policy", {})
        require(policy.get("installation") in {"AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"},
                f"Invalid installation policy: {name}")
        require(policy.get("authentication") in {"ON_INSTALL", "ON_USE"}, f"Invalid auth policy: {name}")
        require(entry.get("category"), f"Missing category: {name}")
        plugin = (root / "plugins" / name).resolve()
        require(plugin.is_relative_to(root / "plugins"), f"Plugin escapes collection: {name}")
        plugin_roots.append(plugin)
        manifest = read_json(plugin / ".codex-plugin/plugin.json")
        require(manifest.get("name") == name, f"Manifest name mismatch: {name}")
        require(VERSION.fullmatch(manifest.get("version", "")), f"Invalid version: {name}")
        require(manifest.get("description") and manifest.get("author", {}).get("name"),
                f"Missing plugin description/author: {name}")
        interface = manifest.get("interface", {})
        require(all(interface.get(key) for key in ("displayName", "shortDescription", "longDescription",
                                                 "developerName", "category", "defaultPrompt")),
                f"Missing interface metadata: {name}")
        require((plugin / "LICENSE").is_file(), f"Package is missing its license: {name}")
        require((plugin / "README.md").is_file(), f"Package is missing its README: {name}")
        skill_root = (plugin / manifest.get("skills", "./skills")).resolve()
        require(skill_root.is_relative_to(plugin), f"Skills escape package: {name}")
        if "skills" in manifest:
            require(skill_root.is_dir(), f"Missing skill directory: {name}")
        for skill_file in sorted(skill_root.glob("*/SKILL.md")):
            skills += 1
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", skill_file.read_text(encoding="utf-8"), re.S)
            require(match, f"Missing frontmatter: {skill_file}")
            metadata = yaml.safe_load(match.group(1))
            require(isinstance(metadata, dict), f"Invalid frontmatter: {skill_file}")
            skill_name = metadata.get("name", "")
            require(NAME.fullmatch(skill_name) and skill_name == skill_file.parent.name,
                    f"Skill name/folder mismatch: {skill_file}")
            require(isinstance(metadata.get("description"), str) and metadata["description"].strip(),
                    f"Missing skill description: {skill_file}")
            ui_file = skill_file.parent / "agents/openai.yaml"
            if ui_file.exists():
                ui = yaml.safe_load(ui_file.read_text(encoding="utf-8"))
                require(isinstance(ui, dict), f"Invalid invocation metadata: {ui_file}")
                implicit = ui.get("policy", {}).get("allow_implicit_invocation", True)
                require(isinstance(implicit, bool), f"Invocation policy must be boolean: {ui_file}")

    folders = {path.name for path in (root / "plugins").iterdir() if path.is_dir()}
    require(folders == seen, "Plugin folders and marketplace entries differ")
    resource_errors = sync_resources(root, check=True)
    require(not resource_errors, "\n".join(resource_errors))

    files = list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))
    files += list((root / "plugins").rglob("*.md"))
    links = 0
    for path in files:
        boundary = next((plugin for plugin in plugin_roots if path.resolve().is_relative_to(plugin)), root)
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", content):
            target = target.strip("<>")
            require(not re.match(r"[A-Za-z]:[\\/]", target), f"Machine-local link in {path}: {target}")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(boundary) and resolved.exists(),
                    f"Missing or out-of-package link in {path.relative_to(root)}: {target}")
            links += 1
    return {"plugins": len(seen), "skills": skills, "markdown_files": len(files), "local_links": links}


if __name__ == "__main__":
    try:
        result = validate(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, TypeError, AttributeError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}")
        raise SystemExit(1)
    print("Validation passed: " + json.dumps(result))
