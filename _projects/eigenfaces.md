---
# DRAFT — hidden until Jinger approves. Remove `published: false` to publish.
published: false
title: Eigenfaces for Face Recognition
tier: archive
order: 5
year: 2024
context: 18.0651 Matrix Methods in Data Analysis
role: Equal contribution
team: Team of 2
stack: [Python, scikit-learn, NumPy]
summary: Tuned an eigenfaces recognizer on two benchmarks, reaching 95.3% on Olivetti Faces but only 26.5% on Labeled Faces in the Wild.
tldr: >-
  Eigenfaces recognizes faces by projecting them onto their principal components. With its test
  split, number of components, and classifier tuned through repeated trials and t-tests, it
  reached 95.3% accuracy on the aligned Olivetti Faces dataset but only 26.5% on the more varied
  Labeled Faces in the Wild.
links:
  code: https://github.com/jingerchong/eigenfaces
---

Eigenfaces is a classic approach to face recognition: principal component analysis (PCA) finds the directions that best capture how faces vary, and a new face is recognized by comparing its projection onto those directions with the training faces. It is fast and simple, but it assumes aligned, front-facing faces under similar lighting. For 18.0651, my teammate and I implemented it and tested how far careful tuning could take it on two public datasets: Olivetti Faces, with 40 people photographed against a uniform background, and the aligned "funneled" version of Labeled Faces in the Wild (LFW), with thousands of web photos.

We tuned three choices in order: the fraction of data held out for testing, the number of principal components, and the classifier, comparing L1 and L2 nearest-neighbor matching, k-nearest neighbors, and linear, RBF, and polynomial support vector machines (SVMs). Each setting ran for 20 randomized, stratified trials, and we used t-tests at 95% confidence to decide whether a difference was real, picking the faster option when it was not. For LFW, we also removed people with an outlying number of photos. One person had 530 images, and with them included, the model labeled most test faces as that person.

On Olivetti, a 20% test split, 21 components, and L1 matching reached 95.3% ± 2.2% mean accuracy, up from an 89% baseline, at about 65 µs per face. On LFW, a 20% split, 54 components, and a linear SVM reached 26.5% ± 1.1%, up from 14%. That gap is the main lesson: eigenfaces works well when faces are aligned and lit consistently, but it does not generalize to varied poses, lighting, and backgrounds. We also found that an online tutorial's reported 85% LFW accuracy came largely from predicting the overrepresented person for most faces. Modern deep models such as FaceNet exceed 99% on LFW, but at a training cost of thousands of hours, compared with seconds for eigenfaces.
