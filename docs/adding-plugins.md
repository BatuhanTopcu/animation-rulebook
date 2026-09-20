# Adding another plugin

Keep each plugin self-contained under `plugins/<plugin-name>/`. Use a lowercase
hyphenated name and match it in the folder, manifest, and marketplace entry.
The repository's marketplace name remains `animation-rulebook` as the catalog
grows; a plugin is installed as `<plugin-name>@animation-rulebook`.

1. Create `.codex-plugin/plugin.json` inside the new plugin directory with its
   identity, version, author, description, and Codex interface metadata.
2. Put skills under `skills/<skill-name>/SKILL.md`, with any focused references
   and `agents/openai.yaml` alongside them. Keep runtime references inside the
   plugin package; do not link installed guidance to files outside its boundary.
3. Include a plugin README and the applicable license. Add renderer or service
   dependencies only if that new plugin's purpose requires them.
4. Append an entry to `.agents/plugins/marketplace.json`, preserving existing
   plugin identities and order. A repo-local source uses this shape:

```json
{
  "name": "example-plugin",
  "source": { "source": "local", "path": "./plugins/example-plugin" },
  "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
  "category": "Productivity"
}
```

5. Add the plugin to the root README catalog. For researched guidance, create
   `docs/resources/<plugin-name>.md` and link it from the documentation index.
   Record which sources contributed what and retain any applicable notices.
6. Run the package checks and exercise representative prompts before publishing.
   Include style preservation, concrete diagnosis, and honest evidence reporting
   in animation-skill evaluations. Record limits as well as successful cases.

The current resource-sync convention assumes a primary skill with the same name
as its plugin and writes its bibliography to
`skills/<plugin-name>/references/sources.md`. If a future plugin uses another
layout, update the mapping in `scripts/sync_resources.py` deliberately.

Do not duplicate a root plugin manifest to represent the collection: the root
is the marketplace, while each child directory is an independently installable
plugin. Supporting another agent platform is a separate change that should
include its own validated adapter and installation instructions.
