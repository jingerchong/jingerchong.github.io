---
# DRAFT — hidden until Jinger approves. Remove `published: false` to publish.
published: false
title: NeRFs and Gaussian Splatting for Scene Composition
tier: normal
order: 7
year: 2023
context: Visual Navigation for Autonomous Vehicles
# role: TODO, Jinger's part of the work
team: Team of 2
stack: [Python, PyTorch, COLMAP, Segment Anything]
image: /assets/images/novel-view-sythesis/cover.webp
summary: Reconstructed real objects with NeRFs and Gaussian splatting, then composed and animated a splatted model inside another scene.
tldr: >-
  NeRFs and Gaussian splatting were compared on captures of small real objects. Both synthesized
  convincing novel views once background artifacts were removed, and the explicit splat
  representation made it easy to drop an animated object into a third-party scene.
# links: {code: TODO, GitHub repository with the animation GIFs, if public}
---

Neural radiance fields (NeRFs) and Gaussian splatting (GS) both learn a 3D scene from posed photos and render it from new viewpoints. A NeRF stores the scene in a neural network, while GS stores it as an explicit list of 3D Gaussians, which also makes the scene easy to edit. For Visual Navigation for Autonomous Vehicles, my teammate and I compared the two on objects we captured ourselves, then used GS to compose and animate one of them inside another scene.

We built four datasets of two objects: 15 phone photos of a painted raccoon figurine on a white table, 104 frames from a video of the same raccoon at 3 FPS, 133 DSLR photos of a toy figure on a balcony floor, and the 15 raccoon photos with the background removed by Segment Anything. COLMAP recovered the camera intrinsics and extrinsics for each set. With a single RTX 3070, we downscaled images to 1600 px wide and trained NeRFs with torch-ngp for 5 minutes to an hour, and GS with the official implementation for 30 minutes to 2 hours. In both cases, the models changed little after the first 10 minutes or 5,000 steps.

{% include figure.html src="/assets/images/novel-view-sythesis/figures/nerf-comparison.webp" alt="Side-by-side images of a toy figure: a slightly noisy NeRF render on the left and the closest real photo on the right." caption="A NeRF novel view of the toy figure after only 50 training iterations (left) and the closest reference photo (right). It already captures the lighting from the upper right, with extra noise and saturation." %}

Most of the work went into artifacts. The first raccoon models were surrounded by cloudy floaters. More continuous frames from video made this worse, not better. Switching to a DSLR pushed the artifacts farther from the object, where they took the shape of other objects in the room, which pointed to the background as the cause. Removing the background with segmentation backfired, because the masks left faint outlines that became artifacts right on the object's surface. In the end, we cropped the models by hand, discarding NeRF samples outside a 3D bounding box and deleting stray splats in the SuperSplat editor.

{% include figure.html src="/assets/images/novel-view-sythesis/figures/cleanup.webp" alt="Three renders of the raccoon Gaussian-splatting model on black: buried in a white cloud of floaters, then cropped with some haze remaining, then clean." caption="Cleaning up the raccoon GS model: the initial model buried in floaters (left), a cropped intermediate (middle), and the final model after deleting stray splats by hand (right)." %}

{% include figure.html src="/assets/images/novel-view-sythesis/figures/gs-comparison.webp" alt="Side-by-side images of a painted raccoon figurine: a Gaussian-splatting render on the left and the closest real photo on the right." caption="A novel view rendered from the cleaned GS model of the raccoon (left) and the closest reference photo (right)." %}

{% include video.html mp4="/assets/images/novel-view-sythesis/videos/gs-orbit.mp4" poster="/assets/images/novel-view-sythesis/videos/gs-orbit.webp" title="Orbit around the cleaned raccoon Gaussian-splatting model" caption="An orbit around the cleaned raccoon GS model." %}

Because a GS model is just a list of primitives, composing a scene is a rigid transformation followed by concatenation. Our script reads a CSV of rigid-body transforms and writes one .ply file per row. The first results came out "hairy" until we realized GS uses left-handed coordinate frames, and we also centered the model at its median point. To animate it, we generated a ballistic arc in height with a constant spin, rendered each frame in a browser-based GS viewer, and placed the raccoon in the "playroom" scene from the mip-NeRF 360 dataset.

{% include figure.html src="/assets/images/novel-view-sythesis/figures/composition.webp" alt="Two renders of the raccoon in the reconstructed playroom: on the left its surface is covered in spiky streaks; on the right it renders cleanly on the striped rug." caption="The raccoon composed into the mip-NeRF 360 playroom before (left) and after (right) fixing the left-handed coordinate frames, which had made the model look “hairy.”" %}

{% include video.html mp4="/assets/images/novel-view-sythesis/videos/playroom-orbit.mp4" poster="/assets/images/novel-view-sythesis/videos/playroom-orbit.webp" title="Camera orbit through the playroom with the composed raccoon" caption="A camera path through the playroom with the composed raccoon." %}

The comparison is qualitative. We judged models by eye rather than with image metrics such as PSNR, and with only a few objects. The composition holds up at a glance, but the raccoon was captured under different lighting than the playroom, so it looks out of place up close. The renderer could not update its buffer between frames, so each frame took several seconds to produce.
