---
title: Bottle-Flipping Quadrotor
tier: featured
year: 2023
order: 6
context: 6.8210 Underactuated Robotics
role: Bottle model and dynamics; direct-collocation formulation
team: Team of 2
stack: [Drake, Python]
summary: A hybrid trajectory optimization that throws, spins, and catches a water bottle with a quadrotor in simulation.
tldr: >-
  A quadrotor throws a water bottle, lets it spin a full turn, and catches it upright, planned
  as a three-mode hybrid trajectory optimization with direct collocation in Drake. The optimizer
  found flips at fill levels from 25% to 100%, adapting the throw to the bottle's changing
  inertia.
hero_video: sze70MvoIF8
image: /assets/images/bottle-flip/cover.webp
links:
  code: https://deepnote.com/workspace/underactuated_robotics-5819da3c-978d-416b-9be6-3eab14544207/project/Bottle-Flipper-6c367b04-b2ab-4e5e-a2ff-545ac8946ff2/notebook/optimization-cba5a7ab7f7c468580b77bea0e9abd5d
---

The bottle flip is a skill people tune by feel, because how a bottle tumbles depends on how much water is inside it. For 6.8210 Underactuated Robotics, my teammate and I asked whether a quadrotor could do it: throw a bottle off one rotor, let it spin a full turn, and catch it upright. The water changes the bottle's mass, center of mass, and moment of inertia, so a trajectory planned for one fill level does not carry over to another.

I modeled a 500 mL bottle as a hollow cylinder and the water as a solid cylinder fixed to its base, with the fill height as a parameter, then combined their inertias with the parallel axis theorem. The quadrotor is Drake's Skydio 2 model. We first set the system up as a MultibodyPlant to use Drake's contact simulation, but could not extract the plant dynamics in a form the optimizer could use, so we derived the dynamics by hand and restricted the problem to the vertical plane.

We split the flip into three modes with fixed transitions at a quarter and three quarters of the horizon: the quadrotor carries and throws the bottle, the bottle flies ballistically while the quadrotor repositions, and the two move together after the catch. My teammate adapted Drake's hybrid multibody collocation example while I wrote a direct-collocation mathematical program in the style of the course's compass-gait example. We converged on the mathematical program and built its constraints in parallel, cross-checking each other's versions. The program uses implicit Euler integration with variable time steps of 5–50 ms and a 3 s limit. It enforces no slip during the throw, friction cones on the contact forces and on the throw and catch impulses, momentum transfer at each mode switch, an upside-down bottle at the halfway point, and an inelastic catch that leaves the bottle upright over the rotor at the goal. A polygon-intersection collision check did not cooperate with the other constraints, so we used a simpler, conservative one that keeps the bottle's corners above the top of the quadrotor.

{% include figure.html src="/assets/images/bottle-flip/figures/fill-levels.webp" alt="Four side-by-side plots of bottle (blue) and quadrotor (red) trajectories for 25%, 50%, 75%, and 100% fill; the bottle's peak height and the quadrotor's tilt both increase with fill level." caption="Optimized bottle (blue) and quadrotor (red) trajectories at 25%, 50%, 75%, and 100% fill, starting and ending at the same point. Fuller bottles are thrown higher, and the quadrotor tilts more to spin them." %}

The program found flip trajectories at all four fill levels we tested, from 25% to 100%. Fuller bottles have a larger moment of inertia, and the quadrotor tilted more aggressively to give them the angular acceleration they needed. Those bottles were also thrown higher, likely to clear the more steeply angled quadrotor. With the goal 1 m from the start, the bottle followed a parabola while the quadrotor swung back upright along a curved path before moving straight in to catch it.

{% include figure.html src="/assets/images/bottle-flip/figures/moving-goal.webp" alt="Plot of a bottle (blue) tracing a parabola to the left while the quadrotor (red) tilts back upright and moves across to catch it, at 25% fill." caption="With the goal 1 m to the left of the start (25% fill), the bottle follows a parabola while the quadrotor rights itself and moves across to catch it." %}

These results are simulation only, and the model leans on simplifications: hand-derived dynamics, water as a rigid mass, a perfectly inelastic catch, and a conservative collision constraint. Partly as a result, the solver sometimes failed to find a feasible trajectory, and we searched only for feasible trajectories rather than optimizing a cost. Natural next steps are to use MultibodyPlant for the dynamics and collision geometry, model sloshing with two balls inside the cylinder as Gu et al. suggest, and add costs that favor more efficient flips.
