# Animation Rulebook plugin

One tool-independent skill for planning, making, diagnosing, and refining
animated motion. Start with [SKILL.md](skills/animation-rulebook/SKILL.md); it
routes the agent to the references relevant to the current shot.

Coverage includes 2D and 3D craft, reference analysis, acting and dialogue,
locomotion and shared actions, effects, procedural response, temporal sampling,
staging and cameras, custom styles, and a smaller motion-graphics/UI section.
The twelve classical principles sit alongside these broader craft areas.

The working method is proportional to the task: establish intent and evidence,
block the main action, refine timing and contacts, add supporting behavior, and
inspect actual playback. Stepped poses, stillness, impacts, and intentional
imperfections can be correct for the chosen style. Maximum smoothness is not a
quality criterion by itself.

Explicit invocation: `$animation-rulebook`. Automatic selection is enabled for
animation work, including animation introduced inside a larger task. Static
images and plain footage trimming are excluded. There is no always-on hook.

No renderer, connector, MCP server, or runtime dependency is included. Use the
chosen tool's implementation skill alongside this craft guidance. If playback
has not been inspected, the agent must say so rather than claim visual quality.

The [bundled source acknowledgments](skills/animation-rulebook/references/sources.md)
remain available in standalone installations. [MIT license](LICENSE).
