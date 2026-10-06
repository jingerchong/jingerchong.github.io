---
title: Perception Metrics for Safe Human–Robot Collaboration
tier: normal
research: true # Also shown as a card under Writeups on /research/
order: 2
year: 2024
context: MIT Mechatronics Research Lab
role: Co-author; image-cropping analysis for object detection
summary: Safety metrics that tie a detector's accuracy and speed to collision risk, plus an attentive processing strategy that cuts inference time by up to 30%.
tldr: >-
  A robot that works beside people needs to know how its object detector's accuracy and speed
  translate into collision risk. This ICRA 2024 paper models that link, introduces two
  perception-based safety metrics, and shows that processing only the relevant parts of each
  frame cuts inference time by up to 30% at similar accuracy, lowering collision probability by
  11–14%.
links:
  paper: /downloads/perception-affect-safety-icra-2024.pdf
  ieee: https://ieeexplore.ieee.org/document/10610657
hero_video: Wzxi5bz6Ysg
image: /assets/images/safety-metrics/cover.webp
---

Object detectors are usually judged by accuracy or by speed, but a robot working beside a person needs to know how both affect safety. A detector that is accurate but slow reports where a hand was, not where it is now. With Xiaotong Zhang and Kamal Youcef-Toumi, I contributed to an ICRA 2024 paper that models how three families of perception metrics, namely detection rate, detection quality, and latency, translate into the chance of a collision between a robot and a person.

The paper models two objects, such as a robot's end effector and a person's hand, as they move relative to each other in the camera frame. It defines when a collision occurs from their relative position and velocity, then accounts for missed detections, errors in the detected position, and processing delay. From this model, it derives two safety metrics: Critical Collision Probability (CCP) and Average Collision Probability (ACP).

To show that the metrics can guide algorithm design, the paper proposes an attentive processing strategy. Instead of running a large detector on the full frame, it crops the regions that matter, packs them into a smaller input, and processes that input with a network chosen from an ensemble. My part was analyzing how cropping affects YOLOv7 detections on a large-scale dataset, which informed this strategy.

{% include figure.html src="/assets/images/safety-metrics/figures/attentive-processing.webp" alt="Pipeline diagram: history inputs and the current frame feed an attentive region generator, aggregation optimizer, and input feature aggregation; a network selector chooses from an ensemble of networks, and results are mapped back to the global frame." caption="The attentive processing strategy. Relevant regions of the current frame are cropped and aggregated into a smaller input, processed by a network chosen from an ensemble, and mapped back to the full frame." %}

The strategy was tested on 79 videos from the LaSOT tracking benchmark, about 243,000 frames, with three YOLOv7 models. It reduced inference time by up to 30.1% and total time per frame by up to 26.5% at a similar level of accuracy. For the largest model, it lowered CCP by 11.3% and ACP by 13.5%. That model was also the most accurate on the benchmark, yet without the strategy its slow processing made it the most dangerous for human–robot collaboration, a clear case of why speed–accuracy tradeoffs matter for safety.

{% include figure.html src="/assets/images/safety-metrics/figures/collision-probability.webp" alt="Three heat maps of collision probability over relative distance and velocity: the baseline model, the attentive strategy, and the percentage decrease between them." caption="Collision probability as a function of relative distance and velocity for (a) the baseline detector and (b) the attentive processing strategy, and (c) the percentage decrease." %}

These results come from offline evaluation on a single-object tracking benchmark rather than a closed-loop robot, and most of the remaining accuracy loss came from the smaller networks in the ensemble, which the authors expect fine-tuning on cropped inputs to recover.
