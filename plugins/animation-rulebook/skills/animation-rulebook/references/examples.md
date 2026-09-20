# Worked motion examples

These are adaptable starting constructions, not presets that every scene must
use. Frame indices are zero-based and assume 24 fps where specified. Preserve
an existing project's fps and convert beat times intentionally. Apply the
chosen [style](styles.md), and verify through [review](review.md).

## 1. A rigid ball and a soft ball drop

**Intent:** make gravity, contact, and material readable without equating weight
with falling speed. Use a locked camera and a visible floor.

Use the same initial ballistic trajectory to compare the two objects, ignoring
air resistance. For a sphere of radius 0.2 scene meters and `g=9.81 m/s^2`, set
its center to `2.38 m` and initial vertical velocity to zero. Its bottom falls
`2.18 m`, reaching the floor at `t=2/3 s`, frame 16. This deliberately chooses
the starting height to align the first contact with a frame.

| Event | Time/frame | Construction |
| --- | --- | --- |
| Release | 0 s / 0 | No initial downward velocity; increasing downward spacing follows |
| First contact | 0.6667 s / 16 | Center at radius above floor for the undeformed sphere |
| Illustrative rebound apex | 1.0333 s / 24.8 | With restitution 0.55, vertical rebound speed starts at 3.597 m/s |
| Next contact | 1.4 s / 33.6 | Evaluate contact time between output samples; do not force a hidden slow stop |

For this simplified rigid bounce, rebound height above the contact center is
about `0.65945 m`. Subsequent bounce heights decrease by `e^2` while `e` remains
constant. Contact events need not align to whole frames; evaluate or author them
consistently, then sample the delivery timeline.

For the rigid version, preserve shape and show contact through trajectory and
any appropriate rotation. For the soft version, design an impact compression
and recovery, preserving the lower contact boundary and apparent volume. A
finite compression interval changes the subsequent launch time, so reauthor or
solve that contact phase rather than pretending it obeys the instantaneous
rigid-bounce timing above. Restitution, mass, and softness are separate controls;
a soft object need not bounce higher than a rigid one.

**Check:** no precontact braking, floor penetration, shape inflation, or
unpowered energy gain. A difference in free-fall speed needs another cause,
such as different drag, not just different mass. For a cartoony version, make
any extra hang time or deformation a deliberate deviation.

## 2. A two-second jump and landing

**Intent:** show a voluntary jump with effort and a supported landing. Start
with pose keys, silhouette, and foot contact, not a vertical position sine wave.

| Frames | Beat | Motion decision |
| --- | --- | --- |
| 0-6 | Establish and prepare | Lower/shift weight with readable supporting feet |
| 7-11 | Push | Extend support chain; accelerate from the ground |
| 12 | Release | Feet leave support; define the airborne launch state |
| 20 | Apex | Vertical speed reaches zero; horizontal travel can continue |
| 28 | First landing contact | Place the receiving foot/feet and preserve incoming momentum |
| 29-33 | Absorb | Body compresses while the contacts support it |
| 34-42 | Recover | Return toward the chosen pose with appropriate overlap |
| 43-47 | Resolve | Finish the thought without unwanted drifting |

These times assume a return to a comparable support height. Change them for a
different launch, landing height, scale, or style. Build the airborne path from
its constraints; do not ease each segment to a stop at every key. A landing
changes support and vertical motion, while the body and attachments can continue
into recovery.

For a 2D version on twos, preserve the output fps and expose each chosen drawing
for two frames. Put major events on that cadence, or deliberately introduce a
short local cadence change if the style permits. Do not insert automatic
in-betweens that erase the selected accents. For 3D, inspect planted feet and
the root/body relationship before adding hair or clothing motion.

**Check:** the jump has a credible source of force, the landing reads at speed,
the feet do not slide unintentionally, and the recovery does not become an
unmotivated second bounce.

## 3. A three-second heavy lift

**Intent:** communicate a heavy prop through preparation, grip, and effort.
This is an animation construction, not instruction on safe human lifting.

| Frames | Beat | Motion decision |
| --- | --- | --- |
| 0-8 | Assess | A specific look or stance establishes intent |
| 9-18 | Reach and grip | Place hands before the prop begins moving |
| 19-28 | Load support | Adjust feet/body; show tension while the prop still rests |
| 29-46 | Lift | Coordinate body extension, grip, and prop acceleration |
| 47-60 | Stabilize | Counterbalance the combined load and absorb residual movement |
| 61-71 | Hold | Maintain support and resolve the performance |

Keep the prop stationary on its support until enough force is implied to move
it. Avoid a prop rising first while hands catch up. Once gripped, keep the
relationship coherent; the body can move around that constraint. In a static
hold, evaluate balance of the body plus load. During the lift, dynamic balance
and support forces matter more than a static center-of-mass rule.

Contrast a light version by changing preparation, acceleration, posture, and
recovery, not simply multiplying the duration. A capable character can lift a
heavy object quickly; its effort and load response should still read. Keep
rigid corners rigid unless the prop's design calls for deformation.

**Check:** grip is stable, the load does not float, supporting feet behave
correctly, and the main effort remains visible from the delivery camera.

## 4. A turn and reaction

**Intent:** a character notices something and recognizes its significance.
Use the request's emotion rather than defaulting every reaction to a large
cartoon surprise.

For a 1.5-second, 36-frame trial, establish the starting attention around frames
0-5, notice a new target around 6-9, turn or reorient around 10-18, then let
recognition and its expression develop around 19-27 and hold through 35.
These are beat regions, not a requirement that only one body part move at a time.

Choose whether eyes, head, torso, or a recoil leads based on the cause. A small
thought can happen mainly in the eyes; a startling external impact may move the
body first. Design a head or hand breakdown to avoid accidental straight-line
cuts through the silhouette. A brief overshoot is optional and must suit the
character's energy.

For a stepped treatment, hold the strongest poses and design the connective
accent explicitly. Check that head turns retain construction in 2D and avoid
rotation-route flips in 3D. Keep a supporting hand gesture from hiding the face
at the recognition beat.

**Check:** the viewer can tell what changed in the character's attention, the
reaction is emotionally specific, and its final hold is intentional.

## 5. A title or product reveal

**Intent:** introduce a subject, then let the viewer understand its name or
feature. Begin with hierarchy and actual copy.

For a three-second trial, establish the subject over roughly the first
0.5 seconds, introduce its short label over the next 0.3 seconds, and leave
most of the remaining time for a complete readable composition. Rework that
allocation if the copy, product detail, language, or audience needs more time.
Do not consume the entire duration with entrances.

Choose a single clear spatial idea: an object turns into its useful view, a
mask reveals a title, or a label settles beside an established feature.
Coordinate the support rather than making every element bounce independently.
A restrained reveal can use little deformation and no overshoot. A playful
one can use a clear accent while preserving the reading interval.

If this is UI instead of a video, acknowledge user action immediately and keep
the interface usable during the transition. Under reduced motion, preserve the
same information and final state through a direct change or suitable minimal
dissolve rather than a large translation, spin, or zoom.

**Check:** hierarchy is clear, complete text remains readable long enough,
transforms keep the intended anchors, and the exit does not interrupt the
message. Inspect interaction and reduced-motion behavior only when applicable.

## 6. Reassurance with a concealed problem

**Intent:** a character says "Everything is ready" while trying to keep a guest
from noticing a broken vase. This is a performance problem before it is a
lip-sync problem. Use [Acting and dialogue](acting-and-dialogue.md).

| Beat | Actor's tactic | Visible evidence to test |
| --- | --- | --- |
| Guest approaches | Welcome and redirect attention | Face/stance orient toward guest; avoid a gratuitous glance revealing the vase too early |
| Reassurance | Maintain confidence | Use the actual recording's emphasis; do not gesture on every word |
| Guest looks past them | Recover control | Listener's new gaze causes a change in the actor's tactic |
| Resolution | Block the view or admit the problem | A specific choice changes the pose or staging |

Build one version with restrained acting and one with a larger defensive move.
Choose by the brief and whether the viewer understands the situation. Preserve
the character's design; a suspicious eyebrow and random eye darts are not a
substitute for an objective. For speech, inspect closures, jaw/lip coordination,
and transitions in context rather than giving each phoneme an isolated pose.

**Check:** the guest is an active participant, gaze targets remain coherent,
mouth motion fits the supplied audio, and the performance communicates without
every body part moving. With no recording, plan the beats provisionally and do
not claim synchronized dialogue.

## 7. A creature walks, turns, and stops

**Intent:** an animal approaches a bowl, changes direction around an obstacle,
and arrives under control. Specify the animal and gait before posing its legs;
use [Locomotion and interaction](locomotion-and-interaction.md).

Observe several comparable steps, identifying contact, load, push, and release
for each foot. Block trunk travel and the support sequence together. Mark the
turn's new footholds, then adapt stride length, body orientation, and timing so
the feet can reach them. Do not rotate a finished straight walk over planted
feet. Begin deceleration early enough for the remaining support steps; let the
final posture suit drinking rather than ending in a generic walk-cycle pose.

For an in-place source cycle, apply root travel once. Compare distance advanced
per cycle with contact-foot displacement, and inspect world-space sliding.
Do not copy one species' footfall order or anatomy onto another.

**Check:** forward motion has support and propulsion, turn steps are reachable,
the trunk does not jump at a transition, and the head's bowl attention survives
the body's movement. Inspect the whole approach at delivery speed, not only a
seamlessly repeating middle step.

## 8. An interrupted handoff

**Intent:** two people transfer a rigid tray, but the receiver hesitates. Start
with a shared tray path and support states, then fit both performances around
them. Consult [Locomotion and interaction](locomotion-and-interaction.md).

Establish giver support, first receiver contact, shared support, receiver taking
load, and giver release. When the receiver hesitates, choose a causal response:
the giver keeps supporting, withdraws, or deliberately lets go with consequences.
Do not silently switch ownership and teleport the tray to the receiver's hands.
During shared support, reconcile both grips with the same prop; avoid two
independent hand trajectories fighting over it. On release, preserve the intended
position and motion, including any deliberate jolt and the participants' response.

**Check:** there is a readable transfer of responsibility, contacts remain
coherent, the tray stays rigid, and the receiver's hesitation changes the giver's
action. This works with keyed poses or procedural motion; it requires no physics
engine. Test interruptions before adding finger or clothing detail.

## 9. A stylized impact plume

**Intent:** a character lands, producing a brief graphic dust plume that clears
in time to reveal their expression. Use [Effects and procedural motion](effects-and-procedural.md)
and [Perception and sampling](perception-and-sampling.md).

Block contact first, outward dust spread second, then curl/drift and dissipation.
Choose a few large shapes that frame the character, smaller shapes supporting
their flow, and sparse fine detail only where readable. Let ground and wind
affect the development coherently. Seed variation for repeatable review instead
of inventing unrelated random offsets on every frame.

For a held graphic style, design the effect's exposures and silhouettes. A
continuous camera can move while those shapes hold; inspect their combined
screen-space displacement. If the plume strobes, first distinguish excessive
spacing from unintended playback hitches or noisy rendering. Compare a revised
breakdown, a style-compatible smear, or smaller camera movement. Do not blur the
whole shot automatically or fill every held pose with smooth interpolation.

**Check:** dust begins from the landing cause, scale and direction remain clear,
the face becomes readable at the chosen beat, and repeated playback reproduces
the same effect. A successful simulation or export alone does not pass this test.
