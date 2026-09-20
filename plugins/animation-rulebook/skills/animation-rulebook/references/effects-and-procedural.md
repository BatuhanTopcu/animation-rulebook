# Effects and procedural motion

## Direct the effect as part of the scene

Specify the source, initial impulse, development, interaction, and disappearance.
An effect can carry the main performance or support another subject. Disney's
[effects process](https://www.disneyanimation.com/process/effects-animation/)
describes using motion tests and combining techniques to serve character and
story. Apply that freedom to drawn effects, particles, geometry, or simulation;
physical accuracy is one possible constraint, not the only artistic objective.

For a magical trail, identify what starts it, what it follows, and when it loses
energy or changes behavior. For an impact, keep source contact, debris launch,
dust development, and the receiver's response causally connected. Do not merely
spawn unrelated decorative motion when a character changes pose.

## Organize motion by scale

Resolve the large silhouette and travel first, then medium changes, then fine
detail. SideFX's [look-development guidance](https://www.sidefx.com/docs/houdini/pyro/pyro_look.html)
emphasizes that shape and speed depend on several interacting controls. Its
[solver documentation](https://www.sidefx.com/docs/houdini/nodes/dop/pyrosolver.html)
distinguishes broad churning from smaller flame detail. The transferable rule
is to assign different jobs to source shape, transport, breakup, and dissipation,
rather than increasing noise everywhere. No Houdini operation is required.

Keep variation correlated over space and time. Nearby leaves can share a gust
while differing in phase and flexibility; independent random positions each
frame make disconnection rather than wind. Select seeded variation for repeatable
offline work. Review whether procedural repetition becomes obvious over the
actual shot length, not only a short preview.

Use the scene's dimensions and time units consistently. A change in scale can
change how gravity, drag, and bending read; do not assume enlarging an effect
alone produces the impression of a larger event. A big plume often needs its
own development timing and shape hierarchy. Choose these through reference
and a representative trial rather than a universal slow-motion multiplier.

## Continuous state and response

For time-based smoothing toward a fixed target, a useful first-order decay is
`x(t+dt) = target + (x(t)-target) * 2^(-dt/h)`, where `h > 0` is a half-life and
`dt >= 0`. It avoids a fixed per-frame blend fraction. This is a damper, not an
oscillating spring, and exactness assumes the target stays fixed during that
interval. A moving target requires appropriate tracking or substeps. See
[Holden's spring treatment](https://theorangeduck.com/page/spring-roll-call).

When switching targets or motion clips, retaining position alone can still
produce a velocity snap. Preserve the needed state and blend offsets deliberately;
do not enforce velocity continuity across an intentional collision or cut.
For locomotion, reconcile the transition with support constraints rather than
assuming a mathematically smooth transition is physically acceptable.

## Verify cause, coherence, and repeatability

Preview the effect in the shot at low cost before adding detail. Inspect source
attachment, collisions, material response, decay, occlusion of the main action,
and seams in repeated effects. For offline procedural work, reevaluate selected
times out of order and check reproducibility; for stateful simulations, use the
defined replay or bake workflow. For interactive work, test changed targets and
different update intervals. See [timing](timing-and-motion.md) for springs and
[perception](perception-and-sampling.md) when fast detail breaks up in delivery.
