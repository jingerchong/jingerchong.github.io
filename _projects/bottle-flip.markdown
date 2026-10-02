---
title: Water Bottle Flipping Quadrotor
tier: featured
year: 2023
order: 3
context: Underactuated Robotics
# role: TODO, your part (e.g. "Sole author", or what you owned in the team)
# team: TODO, e.g. "Team of 3" or "Solo"
stack: [Drake, Python]
summary: Direct-collocation trajectories flipped a bottle across four fill levels in simulation.
tldr: >-
  I posed flipping a water bottle with a quadrotor as a hybrid trajectory optimization and
  solved it with direct collocation in Drake. In simulation, the planner produced robust flips
  across four fill levels, from 25% to 100%.
# hero_video: TODO, YouTube ID of a simulation clip, if one exists
# links: {video: TODO, report: /downloads/bottle-flip/final-report.pdf}
---

The goal was to plan quadrotor–bottle maneuvers that stay robust as the payload changes. The
amount of water in the bottle changes how it moves, so a flip tuned for one fill level may not
work for another.

I posed the flip as a hybrid trajectory optimization with a fixed mode sequence and solved it
with direct collocation in Drake. The constraints encode the quadrotor and water-bottle
dynamics, the desired state at each mode transition, collision avoidance, contact forces, and
impulse and collision dynamics.

I then compared the resulting trajectories across water fill levels, and the optimizer found a
robust flip at each of the four levels tested, from 25% to 100%.

{% comment %}
Drafting prompts for our pass together (not rendered):
- What was the mode sequence (e.g. carry, release, flight, landing)? One sentence makes the
  hybrid formulation concrete.
- What was hardest: contact/impact constraints, convergence, initial guesses? Worth a
  descriptive ## header if it becomes a paragraph.
- How did the trajectories differ by fill level? A plot or a side-by-side simulation loop would
  be a good hero.
- Any limitation: simulation only, a fixed mode sequence, water modeled as a rigid mass?
{% endcomment %}
