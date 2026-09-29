---
title: Water Bottle Flipping Quadrotor
tier: featured
year: 2023
order: 3
context: Underactuated Robotics
stack: [Drake, Python]
summary: Direct-collocation trajectories flipped a bottle across four fill levels in simulation.
---

## Problem

Plan robust quadrotor–bottle maneuvers across changing payload conditions.

## Approach

Posed the flip as a hybrid trajectory optimization with a fixed mode sequence, solved with direct collocation in Drake. Constraints encode the quadrotor and water-bottle dynamics, the desired state at each mode transition, collision avoidance, contact forces, and impulse and collision dynamics. I then compared the resulting trajectories across water fill levels.

## Results

Demonstrated robust bottle flipping across four fill levels from 25–100%.
