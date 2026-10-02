---
title: Autonomous Racecar Stack
tier: featured
order: 2
year: 2022
context: '6.141 Robotics: Science and Systems'
summary: Vision-based lane following and RRT/PRM path planning for a 1/10-scale autonomous racecar.
stack:
- ROS
- C++
image: /assets/images/alfredo/cover.webp
---

For 6.141 Robotics: Science and Systems, I helped program our racecar, named Alfredo, to localize, plan, and navigate autonomously across a series of increasingly complex tasks.

By the end of the course, Alfredo drove laps autonomously on an indoor track at up to 5 m/s, staying in its lane with computer vision and a pure-pursuit controller. For navigation, it planned paths through a loaded map with bidirectional rapidly-exploring random trees (RRT) or probabilistic roadmaps (PRM).

### Wall following

{% include youtube.html id="HGhFOR1zcz0" title="Alfredo wall following demonstration" %}

### Cone parking

{% include youtube.html id="uoZ6DRbXyKo" title="Alfredo cone parking demonstration" %}

### Line following on a zigzag course

{% include youtube.html id="4E7E7nPVFV8" title="Alfredo line following on a zigzag course" %}

### Line following on a circular course

{% include youtube.html id="OMkYFuFPJ6c" title="Alfredo line following on a circular course" %}
