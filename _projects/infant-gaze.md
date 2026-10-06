---
# DRAFT — hidden until Jinger approves. Remove `published: false` to publish.
published: false
title: Few-Shot Fine-Tuning for Infant Gaze Coding
tier: normal
order: 8
year: 2023
context: 6.8300 Computer Vision
role: Datasets and fine-tuning framework; co-ran experiments
team: Team of 2
stack: [PyTorch, OpenCV, NumPy, Python]
summary: Fine-tuned the iCatcher+ infant gaze classifier on a few labeled frames per video to test whether personalization improves accuracy.
tldr: >-
  Automated infant gaze coding could speed up developmental studies. Fine-tuning the iCatcher+
  gaze classifier on 2–9 labeled frames from a new video improved accuracy on some videos but
  not others, so the benefit of per-infant personalization remained inconclusive.
links:
  code: https://github.com/eugeniafeng/gaze_coding
---

Developmental psychologists use where and how long infants look to study attention and learning, but coding gaze frame by frame by hand is slow. iCatcher+ automates this for videos collected through Lookit, an online platform where families take part in studies by webcam. It labels each frame as left, right, or away with human-level agreement, and its authors suggested personalizing the model with calibration frames as future work. My teammate and I tested that idea using few-shot adaptive gaze estimation (FAZE): fine-tune the pretrained gaze classifier on k labeled frames from a new video, then measure its accuracy on that video.

We selected six public Lookit test videos the model had never seen, balanced across age, race/ethnicity, and gender, each with over 10,000 annotated frames. I built the datasets and the fine-tuning framework, and my teammate built the model and testing framework. The pipeline uses iCatcher+'s face detector, a lowest-face selector in place of its face classifier (which outperforms it by less than 2%), and its ResNet-18 gaze classifier. Because we fine-tuned on single frames, we repeated each frame five times to fill the model's five-frame input window. We varied k from 2 to 9 and trained for 15 epochs, based on a sweep. Sampling frames at random first produced a model that predicted one class for every frame, so for k ≥ 3 we included at least one frame of each class.

{% include figure.html src="/assets/images/infant-gaze/figures/k-samples.webp" alt="Line plot of test accuracy from 0 to 0.7 versus number of calibration samples from 0 to 9 for six videos and their average; individual videos vary widely while the average stays near 0.4." caption="Test accuracy for each of the six videos and their average (black) as the number of calibration frames k increases; k = 0 is the pretrained model. Individual videos swing widely, but the average barely moves." %}

Our reproduction of iCatcher+ reached 40.88% average accuracy across the six videos, with a best of 53.96%, compared with the 82.23% the authors report. The released weights did not support our single-frame setup, and retraining on thousands of videos was beyond our compute, so we could not close that gap. Fine-tuning gave its best average accuracy of 47.96% at k = 9, followed by 44.26% at k = 5. Three videos improved noticeably while the other three stayed flat or got slightly worse, and with one trial per value of k, we could not call the effect significant.

{% include figure.html src="/assets/images/infant-gaze/figures/per-video.webp" alt="Bar chart of test accuracy for videos 1 to 6, comparing the pretrained iCatcher+ model with the few-shot model averaged over k; few-shot is higher for videos 1 to 3 and similar or lower for videos 4 to 6." caption="Test accuracy per video for the pretrained model (blue) and the fine-tuned model averaged over all values of k (orange). Videos 1–3 improved, while videos 4–6 stayed flat or dropped slightly." %}

The main lesson was to secure a faithful baseline before measuring an improvement on top of it. With more time, we would retrain iCatcher+ to its reported accuracy, run repeated trials per k, and draw fine-tuning frames from Lookit's calibration trials, in which a spinning ball moves between the two sides of the screen, rather than from random labeled frames. That would also require checking that infants actually follow the ball during calibration.
