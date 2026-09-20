# Locomotion, creatures, and shared actions

## Build a support sequence, not a moving pose loop

For each limb, identify contact, support, release, and swing. Observe the actual
subject and gait before assigning offsets: a quadruped is not a biped cycle
duplicated onto four legs. Note footfall order, which limbs share support, and
how the trunk moves between supports. Anatomy constrains which joints and
surfaces do the work. The animal-motion workflow in [Animation Mentor's
tutorial](https://www.animationmentor.com/blog/tutorial-animate-animals-in-motion/)
supports reference-led posing, weight transfers, and distinct paw transitions.
Its particular rig operations are not universal requirements.

Choose a traveling cycle or an in-place cycle intentionally. For a repeat with
net root displacement `D` and period `T`, average travel speed is `D/T`.
This is a consistency check, not a formula for instantaneous speed. A planted
contact should remain stationary relative to its support, while the body moves
over it. Do not add root travel twice when combining a clip and an external path.

## Starts, stops, turns, and terrain

Design entry into and exit from the cycle. Starting requires a support strategy;
stopping needs enough deceleration and a receiving step unless a force or style
explains a sharper event. A turn changes future foot placement and trunk
orientation, not just a heading value applied after the feet were animated.

On a slope, step, or moving surface, adapt placement and clearance together with
the body's support. Extending a leg to reach the ground can stretch the pose or
leave the weight unsupported. If the target is beyond reach, move the body,
replant, or change the step instead of silently distorting anatomy. For creatures,
use observed anatomy; visible backward-looking limb angles are not sufficient
to identify which joint is a knee or ankle.

When transitioning between motions, examine compatible support phases and
direction of travel as well as pose similarity. Position and velocity differences
jointly affect a transition; [Daniel Holden's transition analysis](https://theorangeduck.com/page/inertialization-transition-cost)
is a technical reference for that distinction. A smooth blend alone does not
guarantee planted contacts or a valid path. Preserve the current visible state
on interruption, then reconcile contacts and the next action's requirements.

## Shared objects and multi-character causality

Author the shared event once and coordinate participants around it. For a
handoff, establish the object trajectory, receiver contact, transfer of support,
giver release, and recovery. A free-flight toss intentionally has an unsupported
interval; a careful hand-to-hand pass usually does not. Avoid two independent
hand animations each trying to place the same rigid object differently.

For a shared load, each participant's step and adjustment should account for
the load and the partner. For a push or pull, give the environment and receiver
an appropriate response; do not animate only the initiator's effort. Pauses,
resistance, and reaction latency can express a relationship. These are authored
choreography decisions, not requirements for a physics engine.

## Verify

Inspect support phases and object-space grips through starts, turns, transitions,
and the loop seam. Test the assembled interaction, not isolated characters.
Check that corrections for one contact do not break another or move the root
unexpectedly. See [3D craft](3d.md) for constraints and pivots and
[timing](timing-and-motion.md) for root-displacement loop boundaries.
