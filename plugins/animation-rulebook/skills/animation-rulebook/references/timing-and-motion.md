# Timing, spacing, and motion construction

## Separate the quantities

- **Timing:** event positions on a timeline and durations between them.
- **Spacing:** displacement between successive observations of a landmark.
- **Output fps:** samples presented per second by a fixed-rate delivery.
- **Exposure:** how long a drawing or pose is held. Twos at 24 fps means 12 pose
  changes per second when every pose is held for two frames; output remains 24.
- **Path:** where something travels. Its shape does not specify its speed.

Number frames from zero when using the examples. Convert with `t = frame / fps`
and name any different convention. A clip lasting `T` seconds at `F` fps has
`N = T*F` frames when that product is integral, normally indexed `0..N-1`.
The boundary at `t=T` is not an extra unique frame of that clip.

For constant sampling interval `dt`, estimate velocity with
`v[i] = (p[i+1]-p[i])/dt` and acceleration with
`a[i] = (v[i+1]-v[i])/dt`. Inspect world space for mechanics and screen space for
what viewers actually see. A parent transform or moving camera can change
visible spacing even when local curves look regular.

## Shape the change for its cause

| Motion | Useful construction | Common mistake |
| --- | --- | --- |
| Deliberate reach | Preparation if needed, acceleration, controlled arrival | Equal easing on every joint |
| Gravity-driven flight | Continuous ballistic path between contacts | Slow approach to the floor without a force |
| Impact | Correct contact, fast velocity change, material response | Smoothed-through penetration |
| Constant transport | Linear distance over time | Unnecessary stops at every waypoint |
| Elastic settle | Damped oscillation when elasticity supports it | Perpetual decorative wobble |
| Graphic hold/snap | Chosen exposures and meaningful poses | Spline interpolation that erases the accent |

Compare duration and spacing separately: retain the same start/end time and
change acceleration, then retain a spacing profile and change total duration.
This makes the actual cause of a weak action easier to isolate.

## Ballistic motion and contact

For a chosen upward-positive axis and constant gravitational magnitude `g`:

```
x(t) = x0 + vx0*t
y(t) = y0 + vy0*t - 0.5*g*t*t
vy(t) = vy0 - g*t
```

Use consistent units. Gravity changes vertical velocity; without another force,
horizontal velocity is constant. The apex has zero vertical velocity but need
not have zero horizontal velocity. Stylized hang time may deviate deliberately;
make it a style decision, not an unnoticed interpolation artifact.

Find contact against the visible surface or shape bounds, not the object's
origin. For a bouncing sphere, the bottom reaches the ground before the center.
With a static floor and a simplified normal bounce, `v_after = -e*v_before`
for `0 <= e <= 1`. Tangential motion needs a separate friction/rolling choice.
An unsupported bounce should not gain height; a powered jump can add energy.
Mass does not enter the ideal free-fall acceleration. Material compliance and
contact duration are separate from that calculation.

For a soft impact, hold the lowest contact boundary while deforming the shape,
then release it when contact ends. Do not preserve volume at the expense of
unexplained floor penetration. During a settling rest, remove unintended residual
drift. These are useful simplified models, not a substitute for collision or
deformation systems when the scene requires them.

## Easing, overshoot, and springs

An interpolation curve is a proposed spacing pattern. Evaluate the visible
subject. Do not automatically replace all linear keys with splines or smooth
every tangent across contact.

Distinguish **positional overshoot** (travel past the target) from **deformation**
(shape change) and **follow-through** (continued motion after the driver stops).
They can coexist but should not be added as interchangeable decorations.

A one-axis spring model is `m*x'' + c*x' + k*(x-target) = 0`. For positive `m,k`,
the damping ratio is `zeta = c/(2*sqrt(k*m))`: below 1 can oscillate, 1 is
critically damped, above 1 is overdamped. "Increase mass" is not a complete
art-direction instruction because response also depends on stiffness, damping,
and starting conditions.

For a designed settle, `offset(t) = A*exp(-lambda*t)*cos(omega*t+phi)` with
positive `lambda` gives a decreasing envelope. Fit amplitude and phase to the
incoming state; pasting it onto an unrelated motion can introduce a pop.
For an interrupted transition, start from the current position and preserve
velocity when the intended response calls for continuity. A collision or snap
may deliberately change velocity. End residual motion when visually negligible
and use a stable final state when needed.

## Deterministic procedural motion

- Evaluate from scene time for frame rendering and scrubbing. Avoid adding a
  fixed amount each rendered frame, which depends on evaluation order or fps.
- If stateful simulation is necessary, use a defined fixed step, initial state,
  and reproducible seed or a baked result; do not change behavior with playback
  performance. Live interaction may be stateful by design.
- Keep random variation coherent over time and attached to a purpose. Independent
  random offsets on every sample usually make chatter rather than organic motion.
- Retiming means adjusting event times and dynamics intentionally. Changing
  output fps alone should not accidentally change the action's duration.

## Loop boundaries

Choose a cycle length `T` and compare the complete evaluated state at `0` and
`T`, including attachments and camera. For a continuous loop, positions and
orientations must meet, and velocity/direction should meet where appropriate.
A held or stepped loop should preserve its intended exposure rhythm instead.

Sample one cycle on `[0,T)`. Encoding both the first pose and a duplicate at the
end can add an extra hold. Rotation may wrap numerically by 360 degrees yet be
visually continuous; compare orientations and the intended spin direction.
For locomotion with root travel, compare the cycle modulo its intended root
displacement rather than forcing world position to reset. Inspect several
repetitions, including secondary motion and any seeded effect phase.

See [examples](examples.md) for beat construction and [review](review.md) for
diagnosing floatiness, spacing irregularities, and seams.
