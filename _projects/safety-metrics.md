---
title: Perception-Aware Safety Metrics
tier: normal
order: 6
year: 2024
context: MIT Mechatronics Research Lab
summary: Connecting detection quality and latency to collision risk in human-robot collaboration.
---

Object detectors are often judged by accuracy or speed alone, while a robot needs to know how those properties affect safety. With Xiaotong Zhang and Kamal Youcef-Toumi, I contributed to an ICRA 2024 study that connects detection rate, detection quality, and latency to collision risk in human-robot collaboration.

## My contribution

I built a test rig pairing a UR5 arm with adjustable cameras and evaluated how image cropping affected YOLOv7 detections on a large-scale dataset. That analysis contributed to the team's work on perception-aware safety.

## Method and results

The paper introduces Critical Collision Probability (CCP) and Average Collision Probability (ACP) to connect perception behavior to safety. It also evaluates an attentive processing strategy that focuses computation on relevant parts of a frame. In the paper's experiments, this reduced inference time by up to 30.09% while maintaining similar accuracy, and lowered CCP and ACP relative to the baseline by 11.25% and 13.50%.

Read the [ICRA 2024 paper](https://doi.org/10.1109/ICRA57147.2024.10610657) or the [public PDF hosted by the first author](https://xiaotongzh.com/assets/pdf/ICRA_2024_final.pdf).
