# Contributing

Edit the plugin under `plugins/animation-rulebook/`. Keep the entry point short
enough to route by task, and put conditional detail in focused references.
Preserve explicit style choices, tool independence, and evidence-based review.

Research notes are maintained in `docs/resources/animation-rulebook.md`. To
refresh the copy shipped inside the plugin:

```sh
python scripts/sync_resources.py
```

Do not edit the generated `references/sources.md` separately. The synchronization
is only for packaging acknowledgments; the plugin has no build-time or runtime
dependency on these maintenance scripts.

## Validate changes

Python 3.11 or later and PyYAML are used only for repository checks:

```sh
python -m venv .venv
# Activate the environment using your shell's usual command.
python -m pip install -r requirements-dev.txt
python scripts/sync_resources.py --check
python scripts/validate.py
```

The repository validator checks package boundaries,
catalog identities, skill metadata, licenses, and local Markdown links; it is
not a replacement for Codex's own plugin validator or actual skill evaluation.
For substantial instruction changes, test realistic requests and update
[the validation record](docs/validation.md). A successful package check or
render is not evidence that the animation reads well in playback.

Before publishing, inspect the staged diff, retain source notices, and keep
private transcripts, local credentials, model logs, and rendered test artifacts
out of the repository. See [adding plugins](docs/adding-plugins.md) to extend
the collection.
