---
# Copy to _projects/<slug>.md. The filename sets /projects/<slug>/.
title: Example Project                         # Required: heading and card title
tier: normal                                   # Required: featured, normal, archive, or unlisted
order: 100                                     # Required for lists; lower appears earlier
year: 2026                                    # Required for Archive; shown on detail pages
context: Course, lab, or program               # Required for Archive; optional elsewhere
summary: One verified sentence about the work. # Required: card and detail introduction
# stack: [Python, ROS]                         # Optional: detail-page chips
# award: Verified award                        # Optional: detail-page metadata
# links: {video: https://example.com}          # Optional; omit unknown links
# redirect_from: [/old-project-url/]           # Only when preserving a real old URL
# sitemap: false                               # For an intentionally empty archival page
---

Write the complete project here in Markdown. Put a cover, if available, at
`assets/images/<slug>/cover.webp`; the page discovers it automatically.

### Gallery section

Put images at `assets/images/<slug>/gallery-name/01.webp`, `02.webp`, and so on.
Add this include where the gallery belongs:

{% include gallery.html dir="gallery-name" title="Gallery section" %}
