---
# DRAFT — hidden until Jinger approves. Remove `published: false` to publish.
published: false
title: Lego-Stacking UR5 Robot Arm
tier: normal
order: 9
year: 2022
# context: TODO course
summary: A UR5 arm that picks individual bricks out of a pile using RGB-D perception and a custom self-aligning gripper.
stack: [ROS, OpenCV, Python, Arduino]
---

## Problem

Pick individual Lego bricks out of an unstructured pile and stack them.

## Approach

- **Perception:** identified each brick's location and tilt using computer vision on a composite of RGB and depth images.
- **Gripper:** built a servo-powered gripper with force sensors and self-alignment cones to seat bricks reliably, operated via keyboard input.

## Results

TODO: Success rate, stack height, video or photos.
