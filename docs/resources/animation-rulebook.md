# Sources and editorial notes

Research reviewed on 2026-09-20 and 2026-09-21. Links are provenance and optional further
reading; the skill works without visiting them or installing their software.
The classical twelve principles are a historical foundation. The rulebook combines them with
performance, mechanics, effects, perception, and visual storytelling. It is an
original practical synthesis, not a reproduction of the transcript, a book,
research papers, or an upstream skill collection. Source-backed observations
and original working recommendations are distinguished below; these are not a
new numbered set of universally validated laws.

## Animation foundation

- **Frank Thomas and Ollie Johnston, _The Illusion of Life: Disney Animation_
  (1981).** Historical attribution for the twelve-principle framework. The full
  book was not accessed for this plugin.
- **Alan Becker, [12 Principles of Animation (Official Full Series)](https://www.youtube.com/watch?v=uDqjIdI4bF4).**
  This public series provides the
  foundation for posing, anticipation, staging, overlap, arcs, timing,
  exaggeration, solid forms, and appeal. Definitions and examples here are
  rewritten and applied to agent decisions rather than copied dialogue. No
  transcript or video is redistributed.
- **Kevin Koch / Animation Mentor, [Slow In and Slow Out](https://www.animationmentor.com/blog/slow-in-and-slow-out-the-12-basic-principles-of-animation/).**
  Supports the distinction between timing and spacing and the need to inspect
  visible motion rather than merely polish curves. It also discusses abrupt
  contact and why increasing smoothness is not always the goal.
- **Sony Pictures Imageworks, [Spider-Man: Into the Spider-Verse](https://www.imageworks.com/node/1371).**
  Production evidence for intentionally stepped animation and combining graphic
  techniques with 3D. Used as a bounded example of an artistic approach, not a
  prescription for every stylized project.

## Performance and reference

- **Ed Hooks, [Acting for Animators masterclass outline](https://edhooks.com/wp-content/uploads/2023/05/AFA_Masterclass-Studios-game-companies-v4.pdf).**
  Instructor-authored outline reviewed. Informs objectives, obstacles, tactics,
  and active listening in the planning and acting guides. It is not evidence for
  universal blink frequencies or a fixed physical expression of every emotion.
- **Dana Boadway-Masson / Animation Mentor, [10 Advanced Acting Performance Tips for Animators](https://www.animationmentor.com/blog/10-advanced-acting-performance-tips-for-animators/).**
  Practitioner guidance on thought, subtext, stillness, and performance within a
  pose. Used in the acting guide; not converted into a compulsory pose sequence.
- **Pif Edwards, Chris Landreth, Eugene Fiume, and Karan Singh,
  [JALI: An Animator-Centric Viseme Model for Expressive Lip Synchronization](https://www.dgp.toronto.edu/~karan/jali/) (2016).**
  Authors' project description and abstract reviewed. Supports speech context
  and separate jaw/lip contributions in the dialogue guide. No JALI software,
  rig, or model is required; this rulebook does not reproduce the algorithm.
- **Walt Disney Animation Studios, [Layout](https://www.disneyanimation.com/process/layout/).**
  Studio process description supports rough spatial blocking, camera choices,
  and checking how shots join before expensive finishing.

## Movement, interaction, and procedural craft

- **Nathaniel Seymour / Animation Mentor,
  [Tutorial: Animate Animals in Motion](https://www.animationmentor.com/blog/tutorial-animate-animals-in-motion/) (2025).**
  Practitioner tutorial informs reference-led animal motion and coordination of
  contacts and body movement. Tool-specific procedures are not imported.
- **Daniel Holden, [Spring-It-On: The Game Developer's Spring-Roll-Call](https://theorangeduck.com/page/spring-roll-call) (2021).**
  Author's mathematical explanation informs the fixed-target, time-based
  first-order damper in effects/procedural guidance. The formula is presented
  with its assumptions; no upstream implementation is bundled.
- **Daniel Holden, [Inertialization Transition Cost](https://theorangeduck.com/page/inertialization-transition-cost) (2022).**
  Author's discussion motivates checking position and velocity together during
  transitions. The rulebook adds support-state review as an editorial practice;
  it does not claim to implement the paper or guarantee feasible transitions.

## Effects and temporal perception

- **Walt Disney Animation Studios, [Effects Animation](https://www.disneyanimation.com/process/effects-animation/).**
  Studio process description informs effects as storytelling and the value of
  rough motion/design exploration before detail or simulation.
- **SideFX, [Pyro look development](https://www.sidefx.com/docs/houdini/pyro/pyro_look.html)
  and [Pyro Solver](https://www.sidefx.com/docs/houdini/nodes/dop/pyrosolver.html).**
  Official documentation informs source behavior and distinctions between broad
  flow and fine disturbance. These concepts are generalized without prescribing
  Houdini settings, requiring fluid simulation, or treating every effect as smoke.
- **Robert L. Cook / Pixar, [Stochastic Sampling](https://graphics.pixar.com/library/StochasticSampling/) (1986).**
  Author/studio abstract reviewed for sampling and aliasing. Used to distinguish
  temporal artifacts from defects in the authored path.
- **Robert L. Cook, Thomas Porter, and Loren Carpenter / Pixar,
  [Distributed Ray Tracing](https://graphics.pixar.com/library/DistributedRayTracing/paper.pdf) (1984).**
  Motion-blur discussion informs time integration over an exposure. This does
  not establish a universally correct shutter duration or artistic blur style.
- **Johannes Schmid, Robert W. Sumner, Huw Bowles, and Markus Gross / Disney Research,
  [Programmable Motion Effects](https://la.disneyresearch.com/publication/programmable-motion-effects/) (2010).**
  Research abstract reviewed. Supports treating speed lines, multiples, and
  stylized blur as authored depictions of motion; no implementation is copied.
- **Tim J. Smith, [The Attentional Theory of Cinematic Continuity](https://ualresearchonline.arts.ac.uk/id/eprint/21187/) (2012).**
  Author repository abstract reviewed. Informs attention across edits in the
  staging guide; the proposed shot-review questions are editorial applications,
  not experimental findings about every viewer or cut.

## Existing skills evaluated

- **[LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill).**
  MIT-licensed, tool-independent, primarily UI-oriented. Its separation of an
  entry point, deeper guidance, and diagnostic references informed organization.
  No upstream prose, code, timing tables, or assets are bundled. Its mandatory
  layering and universal motion rules were not adopted.
- **[dylantarre/animation-principles](https://github.com/dylantarre/animation-principles).**
  MIT-licensed collection organized across many contexts. Evaluated as a
  secondary structural reference; no collection content is bundled. This plugin
  keeps one discoverable entry point instead of many overlapping skills.
- **[remotion-dev/skills](https://github.com/remotion-dev/skills) and the locally
  installed Higgsfield motion-craft skill.** Tool-specific implementation guides,
  inspected to avoid duplicating or requiring their rendering workflows.

Repository popularity was considered when selecting references, but is not an
animation-quality guarantee or a runtime rule. Future copying or substantial
adaptation of third-party material must retain its applicable notices; the
current package contains no vendored third-party implementation or assets.

## Interactive motion

- **W3C WAI, [Understanding SC 2.3.3: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).**
  Supports disabling nonessential interaction-triggered motion while retaining
  function. This is a Level AAA criterion, not a claim of whole-product WCAG
  conformance. The suggested trial timing ranges in this rulebook are editorial
  starting points, not values mandated by W3C.

## Deliberate qualifications to simplified advice

- Frame count means duration only with exposure and playback rate specified.
- Linear motion, abrupt impacts, and still holds can be correct.
- Mass, material softness, restitution, and gravity are separate concepts.
- Secondary acting choices are distinct from physical trailing motion.
- Symmetry, flat design, mixed cadence, and nonphysical accents may serve a style.
- Readable text needs a context-specific hold, not a universal reading multiplier.
- Acting is driven by context; there is no universal blink clock or emotion pose.
- A plausible gait needs support and propulsion, not just repeating limb paths.
- Effects need coherent causes and shape development, not independent random noise.
- Blur and extra frames cannot repair weak poses, broken contacts, or unclear intent.
- Rhythm and audience attention operate across shots, not only within each curve.

The worked timelines, screen-space estimates, diagnostic tables, beat maps,
and review gates are newly authored illustrative constructions. They are not
measurements extracted from linked films or tutorials. Adapt them to each shot,
and verify claims about a delivered animation through actual playback.
