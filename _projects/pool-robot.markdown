---
title: Autonomous Pool-Playing Robot
tier: featured
award: Outstanding Project
year: 2023
order: 1
context: Robotic Manipulation
stack: [Drake, Python]
summary: Heuristic shot planning, IK, and inverse-dynamics control sank target balls in randomized simulations.
---

## Problem

Model a pool-playing robot well enough to plan and execute shots in randomized simulation.

## Approach

Set up a Drake simulation of an IIWA arm with a cue welded to its end effector, modeling cue dynamics, ball motion, and collisions.

- **Task planning:** a heuristic planner scores candidate target balls and pockets and picks the most promising shot.
- **Trajectory generation:** a multi-stage end-effector trajectory lines up, strikes, and follows through, solved with inverse kinematics while accounting for ball dynamics, cue physics, and collision avoidance.
- **Control:** inverse-dynamics control tracks the planned trajectory.

## Results

Sank target balls consistently in randomized simulations.
