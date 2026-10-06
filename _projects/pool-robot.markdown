---
title: Autonomous Pool-Playing Robot
tier: featured
award: Outstanding Project
award_url: https://manipulation.csail.mit.edu/misc.html
year: 2023
order: 3
context: 6.4212 Robotic Manipulation
role: Simulation environment; co-developed shot planning and trajectory generation
team: Team of 2
stack: [Drake, Python]
hero_video: 578RsYdkPGs
image: /assets/images/pool-robot/cover.webp
summary: Shot planning by allowed angular deviation, IK trajectories, and inverse-dynamics control sank the target ball in every randomized trial.
tldr: >-
  A simulated KUKA iiwa arm plans and plays single pool shots, choosing the ball and pocket with
  the widest margin for error and tracking a five-stage cue trajectory with inverse dynamics
  control. It sank its chosen ball in all 10 randomized trials with five object balls, and the
  project won an Outstanding Project award.
links:
  code: https://deepnote.com/workspace/Underactuated-Robotics-5819da3c-978d-416b-9be6-3eab14544207/project/Pool-Robot-ed6c3404-a299-4ac8-a126-5cbc3e36db3b/notebook/main-82a99b04d3e34818b6f536ecd60f2232
---

Pool asks for precise cue control and some strategy: a good shot depends on the direction and speed of the strike as well as on which ball and pocket you choose. For 6.4212 Robotic Manipulation, my teammate and I focused on a single shot. Given a table with randomly placed balls, the robot picks a target ball and pocket, lines up the cue, and sinks the ball.

{% include figure.html src="/assets/images/pool-robot/figures/overview.webp" alt="Pipeline diagram: task planning, trajectory generation, inverse kinematics planning, inverse dynamics controller, and simulation, with ball poses, cue pose keyframes, robot state keyframes, and actuation passed between stages." caption="System overview. The task planner picks the shot, trajectory generation turns it into cue keyframes, inverse kinematics converts those to robot states, and an inverse dynamics controller drives the arm in simulation." %}

I built the simulation environment. A shortened cue is welded to the last link of a KUKA iiwa arm, using the arm model without collision geometry to keep the simulation cheap. The cue tip uses a compliant hydroelastic contact model with an estimate of leather's stiffness, and the balls and table use rigid hydroelastic contact with published pool physics constants. The pocketed table was the hardest part. Drake cannot subtract geometries, so I modeled a regulation 7 ft table in CAD, but the course's convex decomposition script was too aggressive and left low-resolution, inaccurate pockets. I rebuilt the collision geometry from primitives instead.

{% include figure.html src="/assets/images/pool-robot/figures/collision-geometry.webp" alt="Two renders of the pool table: on the left, the convex decomposition of the CAD model with coarse pockets; on the right, collision primitives overlaid on the CAD model." caption="Collision geometry from convex decomposition of the CAD table (left) and the primitives I used instead, overlaid on the CAD model (right)." %}

Following Nierhoff et al., the planner ranks shots by allowed angular deviation, the range of strike directions that still pockets the target ball without touching a cushion. For every ball–pocket pair, it intersects the angles that send the target ball into the pocket with those that clear the cushion corners, then removes angles that would hit another ball, using tangent lines between ball pairs. It projects the remaining range back to cue-ball directions, keeps only directions where the cue ball actually reaches the target ball, and removes those blocked on the cue ball's own path. Pairs that require too sharp a cut are ruled out early. The robot then aims at the middle of the widest remaining range.

{% include figure.html src="/assets/images/pool-robot/figures/angle-range.webp" alt="Sketch of a yellow target ball near a corner pocket, with one pair of dashed tangent lines to the pocket and another pair clearing the cushion corners; their overlap is shaded purple." caption="Angles that send the target ball into the pocket (blue) and that clear the cushion corners (red). Their overlap, in purple, is the starting range before other balls are checked." %}

The cue tip follows five stages: line up behind the cue ball, pause to settle, strike at 7/5 of the ball's radius and follow through by one ball diameter, pause again, and lift clear of the rolling balls. We interpolated the end-effector poses with first-order holds for position and quaternion slerp for orientation, solved inverse kinematics at each keyframe, and tracked the result with an inverse dynamics controller.

{% include figure.html src="/assets/images/pool-robot/figures/top-view.webp" alt="Top view of the simulated pool table with the iiwa arm and cue on the left, the cue ball, and purple, blue, red, orange, and yellow balls scattered across the table." caption="An example table. The yellow ball is blocked by the orange one, and the orange ball's only pocket leaves little margin, so the planner chooses the red ball into the bottom-right pocket." %}

In 10 trials with five randomly placed balls, the robot sank its selected ball every time. The ball occasionally rattled off the cushion beside the pocket before dropping. Since the arm tracked its keyframes, we traced this to a small error in the angle calculation. The scope was deliberately narrow: direct shots only with no banks, a cue ball placed within the arm's reach, no collision constraints on the arm itself, and a cue ball that kept rolling longer than it should. Deepnote's memory limit also capped the table at five balls. Next steps would be perception to read the table between shots, planning the cue ball's resting position for the next shot, and a mobile base or second arm to reach the whole table.
