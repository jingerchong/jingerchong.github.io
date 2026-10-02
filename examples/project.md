---
# Copy to _projects/<slug>.md. The filename sets /projects/<slug>/.
title: Example Project                         # Required: heading and card title
tier: normal                                   # Required: featured, normal, archive, or unlisted
order: 100                                     # Required for lists; lower appears earlier
year: 2026                                    # Required for More; shown on detail pages
context: Course, lab, or program               # Required for More; optional elsewhere
summary: One verified sentence about the work. # Required: card introduction
tldr: >-
  Two or three sentences about the problem, your contribution, and the
  verified outcome or limitation. Falls back to summary when absent.
published: false                              # Remove after public-content review
# role: Your verified individual contribution
# team: Verified team size or collaborators
# stack: [Python, ROS]                         # Optional: detail-page chips
# award: Verified award                        # Optional: detail-page metadata
# links: {video: https://example.com}          # Optional; omit unknown links
# placeholder: quadrotor                     # pool, quadrotor, prediction, safety; default arm
# hero_video: YouTube ID                       # Optional; replaces cover in the page hero
# image: /assets/images/<slug>/cover.webp      # Optional; social share cover
# sitemap: false                               # For an intentionally empty archival page
---

Write the complete project here in Markdown. Put a cover, if available, at
`assets/images/<slug>/cover.webp`; the page discovers it automatically. Cards
use a 16:10 crop and the page hero uses 16:9. Missing covers use a blueprint
tile in listings and no hero on the detail page. Previous/next follows grid order.

The Projects page combines `featured` and `normal` projects under FEATURED;
only the first three `featured` projects appear on Home. `archive` goes under
MORE; `unlisted` has a detail page but no listing.

Links appear at the top only, ordered paper, arxiv, code, video, report, slides,
poster, website, then other keys. Use `paper` for the manuscript: a PDF target
is labeled PDF; other targets are labeled Paper. Other PDF links receive a
`(PDF)` suffix. Empty and `#` values disappear. Store reviewed public writeups in `downloads/<slug>/`.
Use descriptive `##` headings only when a longer article needs them.

## Gallery section

Put images at `assets/images/<slug>/gallery-name/01.webp`, `02.webp`, and so on.
Add this include where the gallery belongs:

{% include gallery.html dir="gallery-name" title="Gallery section" %}

For YouTube, use the privacy-enhanced, lazy-loading include:

{% include youtube.html id="VIDEO_ID" title="Descriptive video title" caption="Optional caption" %}

For local loops, use either or both formats, plus an optional poster:

{% include video.html mp4="/assets/images/slug/demo.mp4" webm="/assets/images/slug/demo.webm" title="Descriptive title" caption="Optional caption" %}

Local loops have controls and only autoplay when reduced motion is off.
Keep unknown metadata and media absent; never publish example URLs.
