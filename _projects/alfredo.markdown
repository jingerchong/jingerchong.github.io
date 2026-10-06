---
title: Autonomous Racecar Navigation
tier: featured
order: 4
year: 2022
context: '6.141 Robotics: Science and Systems'
role: LiDAR sensor model for localization; path shortcutting; experimental evaluation
team: Team of 5
summary: Wall following, visual servoing, particle-filter localization, and sampling-based planning on a 1/10-scale autonomous racecar.
tldr: >-
  A 1/10-scale racecar learned to follow walls, track lines and cones with a camera, localize
  itself in a known map, and plan paths through it. Its particle filter localized the car to
  within 2.3 cm on average in simulation, and path shortcutting made sampled paths 10–15%
  shorter.
stack:
- ROS
- C++
image: /assets/images/alfredo/cover.webp
links:
  code: https://github.com/rss2022-3
---

In 6.141 Robotics: Science and Systems, our team of five built up the full autonomy stack for a 1/10-scale racecar, one capability at a time, testing each on the real car. Over the semester, our car, Alfredo, learned to follow walls with LiDAR, park in front of a cone and follow a taped line with a camera, localize itself in a known map, and plan and track paths through it. I also wrote the experimental evaluations for three of our four lab reports, comparing our approaches against measured benchmarks.

For wall following, a PID controller was unstable on hardware because of communication delays, so we switched to a pure-pursuit controller with a 2 m look-ahead. It tracked the wall with about 12 cm of average error at both 1 m/s and 4 m/s. Counterintuitively, it turned more accurately at the higher speed, because the fixed look-ahead distance suits faster driving. A safety controller predicted the car's stopping footprint from a bicycle model and braked if any LiDAR return fell inside it.

{% include youtube.html id="HGhFOR1zcz0" title="Alfredo wall following demonstration" caption="Wall following on the racecar." %}

For localization, we implemented Monte Carlo localization, a particle filter that combines an odometry motion model with a LiDAR sensor model. I wrote the sensor model, which scores each particle by how likely the current scan is from that pose in the known map. It mixes four cases: a correct hit on the mapped surface, an unexpectedly short reading from an unmapped obstacle, a missed return at maximum range, and random noise. In simulation, the filter localized the car with 2.3 cm of average error, compared with 1.24 m from the motion model alone.

{% include youtube.html id="4E7E7nPVFV8" title="Alfredo line following on a zigzag course" caption="Visual servoing: following a taped line on a zigzag course." %}

For path planning, we split into subteams that built A* search, bidirectional rapidly-exploring random trees (BiRRT), and probabilistic roadmaps (PRM) on a map of the Stata Center basement, with pure pursuit to track the result. I worked on the sampling-based side and implemented path shortcutting, which straightens the jagged paths these planners produce and shortened them by 10–15%. Once its roadmap was built, PRM answered a query in 0.42 s, compared with about 12 s for A* and BiRRT.

The planners traded speed for tracking quality. PRM queried fastest, but its paths were harder to follow: the car tracked them with over 0.5 m of average error, compared with 0.25 m for BiRRT. The bigger lesson was about teamwork. Our localization lab, squeezed between midterms and spring break, exposed communication gaps in the team. After we talked them through, we split the path-planning lab into subteams from the first day, and it became our most organized and best-benchmarked lab.

{% include youtube.html id="uoZ6DRbXyKo" title="Alfredo cone parking demonstration" caption="Visual servoing: parking in front of a cone." %}
