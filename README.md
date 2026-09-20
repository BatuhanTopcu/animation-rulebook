# Animation Rulebook

Tool-independent animation craft for coding agents: plan the action, make the
movement convincing, preserve the style, and review what actually plays back.

This repository is a **Codex plugin collection**, starting with Animation
Rulebook. Each plugin lives in its own directory so more can be added without
changing the existing plugin's identity or installation command.

## Available plugins

| Plugin | What it adds |
| --- | --- |
| [Animation Rulebook](plugins/animation-rulebook/README.md) | Scene-first 2D and 3D animation guidance: performance, mechanics, timing, effects, perception, cameras, custom styles, and motion graphics/UI. |

The rulebook has one discoverable skill, 15 focused reference documents, and
nine worked examples. The classical twelve principles are one part of its
coverage. It needs no renderer, MCP server, connector, or runtime package.

## Install in Codex

```sh
codex plugin marketplace add https://github.com/BatuhanTopcu/animation-rulebook.git
codex plugin add animation-rulebook@animation-rulebook
```

Start a new Codex task after installation. The skill allows automatic selection
when creating, planning, editing, or repairing animated motion, including
animation within a larger task. Selection is contextual, not a guaranteed hook.
Invoke it explicitly with `$animation-rulebook` when needed.

For local development, clone the repository and register the checkout instead:

```sh
gh repo clone https://github.com/BatuhanTopcu/animation-rulebook.git
cd animation-rulebook
codex plugin marketplace add .
codex plugin add animation-rulebook@animation-rulebook
```

Git access is required while the repository is private. See
[installation notes](docs/installation.md) for verification and existing installs.

## Try it

- "Use $animation-rulebook to fix a heavy lift that looks weightless."
- "Plan a 2D jump on twos at 24 fps, preserving a limited-animation style."
- "Diagnose this quiet dialogue scene: the listener feels frozen and every word gets a gesture."
- "Keep this hybrid scene stepped while making the dust plume and moving camera read clearly."

The skill complements implementation skills for Blender, Remotion, and other
tools. It does not install them or replace their APIs and rendering workflows.
Static artwork and footage trimming without new motion are outside its scope.

## Repository layout

```text
.agents/plugins/marketplace.json    Codex catalog for this collection
plugins/
  animation-rulebook/
    .codex-plugin/plugin.json      Plugin identity and metadata
    skills/animation-rulebook/     Skill, invocation metadata, and references
    README.md                      Plugin overview
    LICENSE                        License included in the installed package
docs/
  resources/animation-rulebook.md   Research bibliography and editorial notes
  adding-plugins.md                How to extend the collection
  validation.md                   Validation evidence and limits
scripts/                           Repository maintenance and validation
```

## Research and development

Read the [documentation index](docs/README.md),
[research sources](docs/resources/animation-rulebook.md), and
[contribution guide](CONTRIBUTING.md).

[MIT licensed](LICENSE). Third-party sources remain under their own terms;
attribution and the scope of their use are documented in the bibliography.
