# Perception, sampling, and motion clarity

Judge the delivered image sequence, not only the animation data. Intentional
stepping, bad spacing, temporal aliasing, render noise, and playback hitches
require different remedies.

## Diagnose the kind of discontinuity

| Observation | Investigation | Appropriate direction |
| --- | --- | --- |
| A landmark jumps off its intended path | Poses, spaces, constraints, simulation | Repair motion continuity or explain the accent |
| A clean path appears strobed in fast playback | Screen displacement, cadence, exposure | Adjust sampling or depiction while preserving style |
| Fine repeated features seem to reverse/freeze | Repetition frequency and relative movement | Test temporal filtering or change the visible detail |
| A stable surface sparkles or changes grain | Render sampling, shading, denoising | Inspect the image pipeline before retiming animation |
| Preview skips while frame renders are regular | Playback performance and presentation timing | Evaluate a reliable playback/export path |

The last two rows are diagnostic checks, not a requirement to use a particular
renderer. Do not explain every visible hitch as a lack of easing.

## Keep four separate clocks

Distinguish simulation/evaluation steps, drawing or pose exposure, output frame
rate, and the exposure interval used to depict blur. More samples inside a
frame can improve temporal integration without adding presented frames or
changing a character's pose cadence. Conversely, interpolating extra output
frames can alter a deliberately held style.

Pixar's [sampling research](https://graphics.pixar.com/library/StochasticSampling/)
explains why sampled images can contain aliasing artifacts and why sample
placement matters. Its [distributed ray-tracing paper](https://graphics.pixar.com/library/DistributedRayTracing/paper.pdf)
addresses integration through time, including changing visibility and shadows.
The craft implication is bounded: blur and sampling are image-formation choices;
they cannot repair an incorrect performance or foot contact.

For a continuously moving screen landmark, an approximate displacement per
output frame is `speed_in_pixels_per_second / fps`. Approximate blur length at
constant screen velocity is `speed_in_pixels_per_second * exposure_seconds`.
These estimates do not establish a universal acceptable pixel threshold.
Perspective, camera-relative speed, image contrast, and the intended style matter.

An original diagnostic example: at 600 px/s and 24 fps, displacement is 25 px
per frame. An exposure of 1/48 second integrates about 12.5 px of that travel.
Holding poses for two frames is a different decision; where the landmark's
position itself steps, it may jump 50 px between changes. Test what the actual
camera and transform hierarchy produce rather than applying these numbers
blindly to every layer.

## Choose a depiction, not just more smoothing

Photographic blur, drawn smears, speed lines, multiple images, and crisp held
poses communicate movement differently. Disney Research's [Programmable Motion
Effects](https://la.disneyresearch.com/publication/programmable-motion-effects/)
demonstrates several of these representations. Choose one consistent with the
art direction; automatic blur is not a substitute for a designed action accent.

For a stepped character under a continuous camera, inspect relative motion,
contacts, and attached 2D details at output cadence. Do not globally interpolate
the poses to conceal an isolated registration problem. Test blur around a held
pose change, where interpolation or shutter sampling can introduce an unintended
in-between or ghost. Keep dramatic impact frames legible.

Review at delivery speed, size, and a representative playback path. Compare
the same short interval with the proposed change, not still-frame attractiveness
alone. Preserve deliberate roughness; report when playback conditions prevent
a reliable assessment.
