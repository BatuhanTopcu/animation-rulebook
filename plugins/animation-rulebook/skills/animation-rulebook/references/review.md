# Motion review and diagnosis

## Inspect evidence in the right order

1. Read the brief and style constraints. Establish what is supposed to feel
   smooth, held, heavy, elastic, abrupt, or unusual.
2. Watch actual playback at delivery speed and intended viewing size. Identify
   the largest issue with the audience's reading before opening curves.
3. Scrub a relevant interval around that issue. Track visible landmarks,
   silhouettes, spacing, contacts, and camera-relative movement.
4. Inspect the controls, hierarchy, exposures, or simulation only to explain the
   observed problem. Compare a small targeted correction in playback.
5. Recheck the corrected interval in its surrounding context and, for a loop,
   across several cycles. Stop when the brief is met and material defects are
   resolved; do not accumulate polish that changes the intended style.

If no playable artifact is available, use the available timeline, pose sequence,
code, or stills to make a bounded assessment. State what remains unverified and
what preview would resolve it. A static frame cannot prove cadence, a smooth
curve cannot prove screen-space spacing, and successful export cannot prove
readability. Never invent viewing results, frame measurements, or render success.

## Symptom to investigation to correction

| Symptom | Inspect first | Likely targeted correction |
| --- | --- | --- |
| Floaty jump/fall | Apex duration, gravity spacing, support, contact timing | Restore motivated acceleration and decisive contact; keep intentional hang time |
| Robotic performance | Repeated timing, identical channels, paths, acting intention | Design a specific breakdown, leading part, or rhythm contrast; do not randomize everything |
| Jitter or pops | Landmark spacing, space switches, noise seed, rotations, camera | Correct the discontinuity or inconsistent sampling; preserve chosen stepped cadence |
| Sliding feet/hands | Contact relative to floor, platform, or prop; root travel | Maintain the contact relationship during the plant, then release/roll deliberately |
| Weightless lift | Preparation, combined balance, grip, acceleration, recovery | Establish support and effort before the load moves; coordinate body and object |
| Rubber rigid object | Deformation channels, scale inheritance, response profile | Use articulation/pose or rigid motion; reduce unintended squash |
| Excessive bounce | Material intent, damping, amplitude, transition history | Reduce or remove oscillation and converge to a stable state |
| Mushy impact | Precontact easing, interpolation through contact, compression timing | Preserve incoming speed until contact; design a sharp event and appropriate recovery |
| Arc bump or limb shortening | Landmark route, pivot, hierarchy, breakdown, foreshortening | Correct the path or pose rather than merely smoothing local curves |
| Busy or unreadable action | Simultaneous focal changes, silhouette, contrast, occlusion | Simplify, reframe, or separate important beats |
| Unmotivated camera | Camera purpose, anchor, subject-relative speed | Lock it or redesign the reveal/tracking; remove distracting drift |
| Broken loop | Full boundary state, velocity, exposure, duplicate endpoint | Match the intended seam and cycle cadence; account for root displacement |
| Typography cannot be read | Complete-copy hold, display size, occlusion | Extend the useful hold or simplify the sequence, not just total duration |
| Interface feels sluggish | Input acknowledgement, blocking, cascade length | Acknowledge immediately, shorten decorative work, support interruption |
| Correct motion but empty acting | Objective, listener, thought changes, pose rhythm | Choose a specific intention and readable response; remove gestures that only illustrate words |
| Mouth chatter or mechanical speech | Recorded phrasing, closures, neighboring shapes | Coordinate articulation and expression; do not reset for every phoneme |
| Gait breaks during turns or blending | Support phase, root travel, next placement, velocity | Reconcile the transition and contact schedule rather than smoothing all limbs |
| Shared prop pops or seems unsupported | Grip relationships, transfer timing, object trajectory | Coordinate the shared event and handoff of support |
| Detailed effects feel arbitrary | Source, energy, transport, breakup, decay | Establish a causal life cycle and large shape before fine variation |
| Smooth curves but choppy delivery | Screen displacement, exposure, output timing, playback | Distinguish sampling artifacts from motion defects before choosing a fix |
| Individually good shots cut awkwardly | Focal location, screen direction, audio, event continuity | Adjust the cut or staging and verify in the assembled sequence |

Treat these as hypotheses. For example, jitter may be a deliberate stop-motion
texture, and linear motion may be correct for a conveyor. Confirm the cause
before changing the implementation.

For these additional domains, consult [performance](acting-and-dialogue.md),
[locomotion and interaction](locomotion-and-interaction.md),
[effects](effects-and-procedural.md), and [perception](perception-and-sampling.md).

## Relevant acceptance checks

Select the checks the task needs; do not demand every check for a tiny edit.

- **Readability:** the intended action and focal point can be understood in one
  normal-speed viewing; key poses remain legible at delivery size.
- **Performance and causality:** intention, reaction, and support transfer are
  understandable where they apply; facial speech works with the actual audio.
  Effects and other participants respond to the shared event.
- **Style:** cadence, exaggeration, deformation, and camera choices remain
  consistent with the brief and reference, including intentional imperfections.
- **Motion logic:** starts, accelerations, direction changes, and stops have a
  physical or graphic cause. Impact and hold behavior match the chosen style.
- **Contacts and form:** no unintended drift, penetration, lost grip, collapse,
  scale change, or rotation flip during the inspected range.
- **Support:** secondary acting and physical overlap reinforce the main beat
  without taking over; residual energy resolves appropriately.
- **Continuity:** transitions and loop boundaries have the intended position,
  orientation, velocity, exposure, and state behavior.
- **Sequence and perception:** the cut preserves or deliberately changes the
  viewer's understanding; sampling, blur, and playback preserve the chosen look.
- **Interactive behavior:** feedback, interruption, and reduced-motion states
  remain usable when those concerns apply.
- **Delivery:** duration, frame rate, dimensions, and output meet the request;
  this technical check complements visual review rather than replacing it.

## Communicate actionable findings

For each material defect, describe the observed symptom, the relevant time/frame
interval if known, the probable cause, and the smallest useful correction. Mark
inferred causes as hypotheses. Avoid arbitrary numerical quality scores.

For completion, briefly say what changed and what was inspected. If useful, name
the remaining limitation: "Checked pose continuity and contact samples; playback
cadence has not been visually verified." Do not produce a long review report
unless that is the requested deliverable.
