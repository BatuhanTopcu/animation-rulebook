---
name: animation-rulebook
description: >-
  Apply tool-independent animation craft when creating, planning, editing, or
  diagnosing animated motion: 2D or 3D scenes, characters, objects, cameras,
  effects, custom styles, motion graphics, or interface transitions. Use also
  when adding animation as a subtask of a larger build. Guides performance,
  choreography, mechanics, effects, temporal clarity, and refinement. Does not apply to
  static artwork, footage trimming without new motion, or unrelated uses of
  the word animation.
---

# Animation Rulebook

Make the action clear, intentional, and consistent with its chosen style.
Fluid animation comes from designed poses, spacing, forces, and transitions;
more frames or smoother interpolation alone do not make it good.

Treat animation as performance, visual storytelling, mechanics, and perception.
The classical twelve principles are one historical foundation, not the scope
limit or a checklist to impose on every shot. Diagnose the actual creative or
technical problem and use the craft area that addresses it.

This is a craft layer, not a rendering workflow. Use the user's chosen tool and
its applicable skills for implementation, APIs, assets, and delivery. Nothing
here requires Blender, Remotion, a service, an install, or network access.
Implicit invocation is enabled for automatic skill selection, not a guaranteed
execution hook. Explicit invocation is `$animation-rulebook`.

## Choose what to read

Use the table to select references; do not load the whole library by default.
For a substantial new scene, start with reference/planning and the relevant
craft domain. For a repair, start with review and follow the diagnosed problem.
Read medium and style guidance when their specific constraints matter. Read the
classical principles when they help with a foundational motion decision.

| Need | Reference |
| --- | --- |
| Analyze references, choose beats, test a shot before polishing | [Reference and planning](references/reference-and-planning.md) |
| Intention, subtext, listening, expression, gaze, speech | [Acting and dialogue](references/acting-and-dialogue.md) |
| Walks, runs, creature gaits, terrain, shared loads and handoffs | [Locomotion and interaction](references/locomotion-and-interaction.md) |
| Timing, spacing, forces, curves, procedural motion, loops | [Timing and motion](references/timing-and-motion.md) |
| Elemental effects, coherent variation, interrupted motion | [Effects and procedural motion](references/effects-and-procedural.md) |
| Strobing, blur, temporal sampling, perceptual continuity | [Perception and sampling](references/perception-and-sampling.md) |
| Drawn, cutout, or vector animation | [2D craft](references/2d.md) |
| Characters, objects, rigs, contacts, spatial motion | [3D craft](references/3d.md) |
| Realism, cartoons, limited animation, stop-motion, hybrids | [Style direction](references/styles.md) |
| Composition, editing, eye trace, rhythm, camera and sound | [Staging and cameras](references/staging-and-cameras.md) |
| Titles, reveals, diagrams, UI feedback and accessibility | [Motion graphics and UI](references/motion-graphics-and-ui.md) |
| Diagnose defects and verify actual playback | [Review](references/review.md) |
| Worked physical, performance, interaction, and effects trials | [Examples](references/examples.md) |
| Classical twelve principles, applications and exceptions | [Principles](references/principles.md) |
| Attribution, editorial choices, further reading | [Sources](references/sources.md) |

## Establish intent without creating a ceremony

Use the request, project, and supplied references to establish the intended
action and style. Ask only when an unresolved choice materially affects the
result. Preserve specified duration, frame rate, delivery constraints, and
existing visual language. Do not turn a simple change into a full production.

For a substantial shot, keep a short working brief:

> Action and audience takeaway; medium and style; duration and output fps;
> drawing/pose cadence; focal subject and camera; key poses and beat times;
> weight/material/contact constraints; loop or interaction requirements.

For performance, add what the character wants, what changes, and who is listening.
For effects, identify the source, development, dissipation, and story role.
For multiple shots, test their cut and sound relationship in a rough sequence.

Infer unspecified choices from the project, then state consequential
assumptions. If no frame rate is established and a fixed timeline is needed,
24 fps is a starting assumption for a film-style scene, not a universal rule.
Interactive motion uses elapsed time and the display refresh rate. Choose
exposure separately from output fps. Match a supplied style before inventing
one; when unconstrained, begin with readable poses and restrained deformation,
then tune exaggeration to the brief.

## Work from the main action outward

1. **Find the evidence.** Observe relevant performance, physical reference, or
   style examples. Separate measured facts from interpretation. Use a small
   representative motion test when a crucial style or mechanics choice is uncertain.
2. **Block the idea.** Establish the focal action, keys, extremes, meaningful
   breakdowns, and important contacts. Check that the story reads before
   refining interpolation. Pose-to-pose is useful for planned action; straight
   ahead is useful for evolving effects and successive motion. Combine them.
3. **Design time and space.** Set when events happen, then how the subject
   travels between them. Check screen-space paths, acceleration, rhythm, weight,
   and contact. A curve editor describes controls, not necessarily the visible
   motion of a hand, face, or prop.
4. **Add supporting behavior.** Layer purposeful acting and physical overlap
   around the primary action. Decide what leads and what follows. Keep still
   areas when they strengthen the shot; constant motion is not a requirement.
5. **Review and refine.** Inspect a low-cost preview at delivery speed and
   size, then scrub suspect frames. Fix the largest readability, timing, or
   contact defect before small polish. Recheck the result after a material
   change rather than running endless generic polish passes.

Keep cause and response connected across actors, props, effects, and cameras.
Preserve the action's phrase structure: preparation, accent, consequence, and
recovery can have different rhythms. Check the assembled shot or sequence;
locally pleasing curves can still fail as a performance or through a cut.

## Invariants and deliberate exceptions

- **Timing is when; spacing is how far between samples.** Output fps, pose
  exposure, and motion speed are separate choices. Do not erase twos, held
  poses, smears, or impact accents merely to increase smoothness.
- **Force and material explain change.** Mass, stiffness, damping, and scale
  are distinct. Equal gravitational acceleration does not make a heavy body
  floatier; weight can read through effort, contact, acceleration, and recovery.
- **Ease where the action calls for it.** Impacts, cuts, constant-speed travel,
  and constrained machinery may need abrupt or linear motion. Do not ease a
  freely falling object to a stop before it contacts the floor.
- **Apply principles selectively.** Do not add rubber deformation to a rigid
  object, a bounce to every arrival, or anticipation that delays urgent UI
  feedback. Preserve apparent volume/form unless the style calls for a
  deliberate change.
- **Secondary action is expressive support.** A worried glance is an acting
  choice; hair lag is physical overlap. Neither should obscure the main beat.
- **Continuity follows intent.** Avoid accidental pops, drift, penetration,
  rotation flips, and loop seams. Preserve designed discontinuities and judge
  them in playback, not by whether every curve is smooth.

## Completion evidence

Use [Review](references/review.md) when judging quality. Report the important
motion decisions, what was inspected, and any unresolved defect. A successful
render proves export worked, not that the motion works. If only code, poses,
or stills were inspected, say so; do not claim playback was visually verified.
Deliver the artifact requested by the user, not a mandatory extra report.
