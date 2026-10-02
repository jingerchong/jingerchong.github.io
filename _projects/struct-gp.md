---
title: Probabilistic Human Motion Prediction
placeholder: prediction # Blueprint tile until assets/images/struct-gp/cover.webp exists
tier: normal
order: 5
year: 2026
context: MIT Mechatronics Research Lab
summary: A scalable Gaussian-process model for full-body forecasts with usable uncertainty estimates.
---

Robots working near people need forecasts that account for more than a single likely motion. My research develops a structured multitask variational Gaussian process for full-body human motion prediction, with uncertainty estimates that can inform future planning and collision avoidance work.

## Approach

I used joint-dimension factorization to keep the model scalable, a continuous 6D rotation representation to preserve kinematic consistency, and empirical coverage analysis to examine how well predicted intervals capture actual motions. Ablations tested the kernel, number of inducing points, and latent dimensionality.

## Results

On Human3.6M, the model achieved up to 50 lower KDE negative log-likelihood than strong baselines with roughly eight times fewer parameters. Its predicted intervals showed modest calibration drift at longer horizons. The mean angle error remained 3–18% higher than competitive deep-learning methods, which is an important tradeoff when comparing point accuracy with probabilistic quality.

The manuscript is under review for ICRA 2027. [Read the updated manuscript on arXiv](https://arxiv.org/abs/2603.07096).
