# Motion graphics and interface motion

This is a smaller companion to the scene guides. Use the same attention and
timing principles, but match the constraints of a title sequence, explainer,
data view, or responsive interface. These contexts do not share one timing scale.

## Graphics, typography, and reveals

Establish what changes and why: reveal a relationship, emphasize a word, connect
two states, explain a process, or introduce a subject. Choose the minimum motion
needed to make that relationship clear. Position, scale, opacity, clipping,
shape, and rotation are options rather than mandatory layers.

Choreograph by information hierarchy. A title can establish the topic before a
supporting label appears; related elements can arrive together. Stagger when it
clarifies grouping or rhythm. Do not delay important information behind a long
decorative cascade, or impose a fixed maximum stagger on all cinematic work.

Keep text readable during its useful hold. Distinguish an entrance that reveals
letters from the interval when the complete phrase can actually be read. Estimate
from the real copy, complexity, audience, and viewing size, then preview. A moving
or partially occluded word may need a different hold than a large static label.
Do not treat reading the line aloud three times as a universal duration formula.

Anchor transforms according to the intended visual relationship. A label that
belongs to a tracked object should remain attached or detach intentionally.
Scale around a suitable origin; avoid an accidental baseline jump or a word
drifting away from its pointer. Keep motion in and out compatible with the scene's
spatial logic, unless contrast is the intended effect.

For data graphics, preserve truthful values and identity through transitions.
Use motion to reveal changes, not to imply measurements unsupported by the data.
Avoid crossing trajectories that make labels or entities ambiguous.

## UI feedback and interruption

An interface must stay responsive while it animates. Confirm an input promptly;
do not add theatrical anticipation before acknowledging a press. Animation can
continue after the state change without blocking the next meaningful input.

Match the duration to travel, prominence, interaction frequency, and the user's
need to act. Begin with the existing product's motion system. When none exists,
rough trial ranges are about 80-180 ms for small feedback and 180-350 ms for a
modest transition; these are tuning starting points, not accessibility thresholds
or universal standards. A cinematic reveal may legitimately take much longer.

Use easing, linear progress, an intentional snap, or a spring according to the
state relationship. Opacity-only changes can be appropriate. Avoid generic
bounces, arbitrary shadow lag, and ambient motion that adds no information.

Handle interrupted or reversed transitions from the current visible state.
Where continuous motion is intended, preserve velocity as appropriate rather
than restarting from an obsolete endpoint. On resize, navigation, cancellation,
or changed data, converge to the correct state without trapping input or leaving
an element half-present. Use actual progress for determinate indicators; a
decorative loop must not falsely imply completion.

## Reduced motion

For interactive content, respect the platform or user's reduced-motion setting.
W3C's guidance on interaction-triggered animation supports disabling nonessential
motion while preserving essential functionality and information. See
[W3C SC 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
This criterion is Level AAA; it is not a complete accessibility audit.

Provide a clear alternative: remove large translations, spins, parallax, and
oscillation; keep the state change legible through a direct replacement or a
brief unobtrusive dissolve where suitable. Do not replace a long travel with an
equally distracting zoom. Keep focus, status, and meaning intact. Avoid adding
unnecessary flashing effects. The user's request may require additional
accessibility work; do not infer complete conformance from a single preference.

## Review

Check the real entrance, readable hold, and exit at delivery size. In an
interface, exercise repeated input, reversal, changing layout/data, and the
reduced-motion path. Judge both motion and the final state. Consult the relevant
tool skill for actual APIs, performance, and rendering rather than importing a
framework dependency into this rulebook.
