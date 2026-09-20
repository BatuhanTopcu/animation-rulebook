# Installation

## From GitHub

Use the Codex CLI with a Git identity that can access this repository:

```sh
codex plugin marketplace add https://github.com/BatuhanTopcu/animation-rulebook.git
codex plugin add animation-rulebook@animation-rulebook
```

The first `animation-rulebook` is the plugin name; the name after `@` is this
repository's marketplace. Register the marketplace once, then choose plugins
from it individually as the collection grows.

Start a new Codex task to pick up the plugin. Ask for animation naturally, or
write `$animation-rulebook` to select the skill explicitly. Implicit selection
allows the agent to choose relevant guidance; it does not inject the skill into
every task. No lifecycle hook or renderer setup is needed.

## From a checkout

```sh
gh repo clone https://github.com/BatuhanTopcu/animation-rulebook.git
cd animation-rulebook
codex plugin marketplace add .
codex plugin add animation-rulebook@animation-rulebook
```

The explicit HTTPS clone avoids depending on an SSH key. GitHub authentication
must already be available for a private repository. Register either the remote
source or your development checkout for this marketplace name.

## Check the installation

```sh
codex plugin marketplace list --json
codex plugin list --json
```

Confirm the marketplace points at the intended repository and the plugin is
enabled. A simple trial is to ask for a restrained heavy-lift repair, then check
whether the agent loaded the rulebook and relevant references. An installed
manifest alone does not prove automatic selection for every possible prompt.

If the earlier personal copy is already installed as
`animation-rulebook@personal`, it is a separate installation. Use Codex's plugin
manager to keep only the desired copy enabled when switching to this repository.
Publishing this repository does not change that existing personal installation.

## Developer updates

Edit the checkout, run the checks in [CONTRIBUTING.md](../CONTRIBUTING.md), update
the plugin version when shipping changed content, and reinstall from the chosen
marketplace. Start a new task afterward. Avoid editing installed cache files;
they are copies, not the source of truth.
