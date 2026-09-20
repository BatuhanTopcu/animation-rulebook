# Validation record

## Animation guidance

The local skill was evaluated on 2026-09-20 and 2026-09-21 before this repository
was assembled. Eight fresh read-only Codex CLI sessions used the installed
catalog and default model, with no external services or rendering.

| Check | Observed result |
| --- | --- |
| Natural 3D heavy-lift request | Selected the skill without naming it; prioritized support, grip, load transfer, planted contacts, and restraint. |
| Explicit foundation scenarios | Addressed rigid/soft bounce, 2D on twos, a heavy 3D lift, a stepped hybrid, typography reveal, and reduced-motion UI. |
| Natural dialogue repair | Selected the skill; addressed intention, the listener, excessive gestures, and neighboring mouth shapes. |
| Explicit expanded scenarios | Addressed dialogue without audio, creature turns/stops, an interrupted handoff, stepped effects, temporal sampling, and time-based damping. |
| Static poster request, twice | Did not load the animation rulebook. |
| Plain footage trim request, twice | Did not load the animation rulebook or introduce new motion. |

The animation responses preserved the requested style, identified concrete
corrections and checks, and stated absent footage/audio/playback evidence.
Numerical bounce examples, fixed-target half-life decay across update rates,
and screen-space sampling estimates were checked independently.

These are observed planning and discovery results, not a benchmark proving
better rendered animation. Selection is not guaranteed for every prompt.
No animation was rendered or visually evaluated in these checks. Private local
session logs and the supplied transcript are not distributed with the repository.

## Repository packaging

The collection adds a root marketplace, per-plugin packages, documentation,
bundled license, resource synchronization, and local validation checks. The skill's motion
guidance and invocation policy are preserved; publication-specific metadata and
source acknowledgment wording were updated.

Run `python scripts/sync_resources.py --check` and `python scripts/validate.py`
from the repository root. The checks cover catalog identity, package boundaries,
skill metadata, licenses, local links, and parity with the canonical bibliography.
PyYAML is a development-only dependency; no Python code or runtime is required
by the installed animation plugin.

Before the initial repository push on 2026-09-21, Codex's bundled skill and plugin
validators both passed. Repository checks passed for one plugin, one skill,
24 Markdown files, and 69 local links. A clean local-marketplace installation
matched all 20 packaged files byte for byte. Sixteen existing instruction and
metadata files were preserved byte for byte from the previously tested plugin;
only publication metadata and bibliography presentation changed.

Negative packaging trials rejected a missing local link, a link escaping the
plugin boundary, an unsynchronized bibliography, and a mismatched catalog path.
These trials used separate fixtures and did not alter the delivered plugin.

## Future changes

For packaging-only edits, run structural checks and an installation smoke test.
For substantial craft changes, exercise realistic prompts for the affected
domains, inspect which references the agent actually reads, and record what was
and was not verified. Visual claims require reviewing the delivered animation
at its intended speed and size.
