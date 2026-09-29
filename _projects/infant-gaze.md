---
# DRAFT — hidden until Jinger approves. Remove `published: false` to publish.
published: false
title: Few-Shot Adaptive Infant Gaze Classification
tier: normal
order: 6
year: 2023
# context: TODO course or lab
summary: Fine-tuned a pretrained CNN with fewer than 10 labeled frames from a new video to classify infant gaze across the rest of that video.
stack: [PyTorch, OpenCV, NumPy, Python]
---

## Problem

Gaze classifiers trained on one set of videos generalize poorly to a new infant, camera, or setting, while labeling every new video by hand is slow.

## Approach

Used few-shot learning: a pre-trained convolutional neural network was further trained on fewer than 10 labeled frames from a new video, then evaluated on the remaining frames of that same video.

## Results

TODO: Accuracy before vs. after adaptation. Use diagrams and metrics only — no identifiable infant frames.
