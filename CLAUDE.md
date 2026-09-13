# CLAUDE.md — jingerchong.com

Working notes for any agent touching this repo. Two parts: **how the site is built today**
(§1–3) and **the agreed restructuring plan** (§4–13).

Status as of 2026-09-02: **plan approved, no implementation started.** Only this file has been
written. Do not begin editing until the owner says go.

---

## 1. Stack and build

- Jekyll via the `github-pages` gem, theme **`minima ~2.5`** (vendored gem, not in-repo).
  Plugins: `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag`.
- Deployed by GitHub Pages from `main`. `CNAME` → `jingerchong.com`.
- Local: `bundle exec jekyll serve`. `_config.yml` is **not** hot-reloaded — restart after edits.
- `permalink: :title/` — **posts live at the site root** (`/revise/`, `/alfredo/`), *not* under
  `/projects/`. Only the `_archives` collection outputs under `/projects/:slug/`.

### Layout inheritance
```
minima's default.html  (from the gem — not in this repo)
├── _layouts/with-banner.html   → default + _includes/banner.html hero
│   └── _layouts/home.html      → index.markdown
├── _layouts/about.html         → about.markdown       (renders _schools/_jobs/_skills inline)
├── _layouts/projects.html      → projects.markdown    (loops site.categories_order)
├── _layouts/category.html      → _archives/*          (one index page per category)
├── _layouts/post.html          → _posts/*             (+ _grids image galleries)
└── _layouts/photography.html   → photography.markdown (TO BE DELETED)
```
`_layouts/resume.html` is not a page layout — it is a **partial** applied to `_jobs` and
`_schools` items via `defaults` in `_config.yml`, then echoed with `{{ job.output }}` from
`_layouts/about.html`.

### Collections
| Collection | `output` | Purpose |
|---|---|---|
| `_posts` | yes → `/:title/` | 16 deep-dive project pages |
| `_grids` | no | per-post gallery sections; `_grids/<post-slug>/grid-N.markdown` with `section:` + optional body |
| `_archives` | yes → `/projects/:slug/` | 8 **empty stub files** whose only job is to generate per-category index pages |
| `_jobs` | no | résumé experience entries (`order`, `show`, `duration`, `location`, `link`) |
| `_schools` | no | résumé education entries (same fields) |
| `_skills` | no | skill lists grouped by `category` |
| `photos` | — | declared in `_config.yml` but **no directory exists** — dead config |

### How image grids work (`_layouts/post.html:42-59`)
Grids are matched by **path substring**: `site.grids | where_exp: "grid", "grid.path contains page.slug"`.
Images are then found by globbing `site.static_files` for paths containing
`{{ site.images }}{{ page.url }}{{ grid.slug }}`. So a post at `/revise/` with `_grids/revise/grid-2.markdown`
renders every static file under `assets/images/revise/grid-2/`.

Consequences to respect:
- **Post slugs must stay unique and non-substring-overlapping.** A post slugged `revise` and another
  slugged `revise-2` would cross-contaminate grids.
- Image ordering is filesystem order — zero-pad filenames if order matters.
- Cover images are convention-only: `assets/images/<slug>/cover.webp`.

---

## 2. Design system (worth preserving — see §10)

`assets/main.scss` imports `_sass/colors.scss`, `_sass/fonts.scss`, `_sass/layout.scss`, then minima.
Heavy `!important` use throughout because it overrides the vendored theme — expect to keep doing this.

```scss
$background-color: white;
$text-color:       black;
$light-color:      #D9DCD6;   // warm grey — borders, footer text, nav links
$grey-color:       #646E78;   // post meta
$accent-color:     #EFCA08;   // yellow — hover, selection, "Jinger", badges
$theme-color:      #08415C;   // deep navy — header, footer, links, h2 rule
```

Signature elements: navy header/footer bands; the `h2:after` 3px×100px navy underline
(`_sass/layout.scss:34-42`); yellow `::selection`; uppercase letterspaced `h2`; the yellow
articulated robot-arm logo (`assets/logo.webp`, also the favicon set).

---

## 3. Known bugs in the current site

Fix these during the restructure; several are user-visible today.

1. **`_layouts/resume.html:4`** — `<a href="{{ school.link }}">` references an undefined variable.
   The layout serves both `_jobs` and `_schools`, so there is no `school` in scope. Should be
   `{{ page.link }}`. **Every org/university heading on `/about/` is currently a link with an empty
   `href`.**
2. **Unconditional cover images** — `_layouts/post.html:38`, `_layouts/home.html:31`,
   `_layouts/category.html:17` all emit `<img src=".../cover.webp">` with no existence check.
   Any entry lacking a cover renders broken. Must be guarded before adding confidential entries.
3. **`_jobs/edventures-stem.markdown:11`** links to `/edventures/` — no such page. 404.
4. **`_posts/2021-04-25-jansens-linkage.markdown` is an empty file** but is linked from
   `_schools/ib-diploma.markdown:13`.
5. **`categories_order` is incomplete** — `_config.yml:30-33` lists only `Build, Code, Teach`, but
   posts use 8 categories and `_archives/` has 8 stubs. `Research` and `Work` items never appear on
   `/projects/`.
6. **`_posts/2020-01-07-toy-for-toddlers.markdown:4`** uses `category:` (singular) with an array,
   unlike every other post's `categories:`.
7. **`_posts/2020-01-06-flashlight.markdown`** — filename says 2020-01-06, front matter says `2021-01-06`.
8. **`site.webmanifest:16`** has `"theme_color": "#ffffff"`, contradicting
   `_includes/custom-head.html:5-6` which correctly uses `#08415C`.
9. **`collections: photos:`** (`_config.yml:64`) has no directory.
10. **Repo hygiene** — untracked in root: `.DS_Store`, `Jinger Chong_Resume.docx`,
    `Jinger Chong_Resume.pdf`, `headshot.jpg`. Unused and committed: `tripod_submission.png` (1.1 MB).
    **Anything left in the repo root gets copied into the built site.** See §9 — the résumé must not
    be published unredacted.

---

## 4. Repositioning goal

Move from "undergrad mechanical engineer / hobbyist maker" to **robotics researcher / PhD candidate**,
targeted at **robotics research internship applications**. Retain the existing visual identity and a
measured amount of personality — this is a *seniority* edit, not a redesign.

Owner's stated research identity (use this language):
- **Primary interest: perception.**
- **Thesis: intent prediction for autonomous navigation.**

The single biggest positioning problem is not the palette or the avatar — it is
**`featured: true`**. Four of the six posts on the homepage are hobbyist projects
(Iron Man model kit, elementary-school workshop, controller soldering, seminar robot car).

---

## 5. Decisions already made (do not re-litigate)

| Question | Decision |
|---|---|
| Taxonomy | **Option A** (function-based) — see §7 |
| Employer names | **OK to name** GE Vernova and Microsoft |
| Microsoft patent | **Published application — link it publicly** |
| GE Vernova patent | **Unpublished — no link, blurb only, no proprietary detail** |
| Google Scholar | `https://scholar.google.com/citations?user=7LDpc4UAAAAJ&hl=en` |
| CV PDF download | **Yes, add** — redact per §9 |
| Photography page | **Delete** |
| Instagram | **Drop from footer** |
| Archive category | **Keep in nav** |
| URLs | **Keep root-level `/:title/`** — no migration |
| Publications page | **Defer** — only one published paper; blurb-style records for now |
| Headshot | **Real photo** — `headshot.jpg` supplied |
| Contact email | See §9 — recommend `jinger@mit.edu` primary |

---

## 6. Target site structure

### Nav (`_config.yml` → `navbar_order`)
```
Research   →  /research/    (NEW — lightweight records; the flagship page)
Projects   →  /projects/    (existing — deep dives only)
Archive    →  /projects/archive/   (existing category-page mechanism)
About      →  /about/
Contact    →  #footer
```
**Research goes first.** Cheapest, highest-leverage repositioning move in the whole plan.

Note: `_includes/header.html:27-36` builds nav by looking up `site.pages` by **path**, so
`navbar_order` entries are filenames (`about.markdown`), not URLs. A new `research.markdown` must be
added there. Archive is an `_archives` collection page, **not** a `site.pages` entry — either add a
hardcoded nav link or special-case it in the include.

### Homepage (`_layouts/home.html`)
- Replace the `where: 'featured', true` post loop with a **"Selected work"** block that draws from
  **both** content types, so research with no project page can still appear. Today the homepage
  structurally cannot show the best work.
- Add an identity row under the bio: **LinkedIn · GitHub · Google Scholar · Email**.
- Drop banner type from `6em` → `~3.5em`, add a one-line research descriptor (§10).
- Swap the sketch for the real headshot; fix `alt="sketch"` → the owner's name (`home.html:9`).

### Social links
`_includes/social.html` is minima's stock include: ~18 hardcoded platform branches, **no Google
Scholar**, and it points at `/assets/minima-social-icons.svg` (the gem's sprite) which has no
`#scholar` symbol.

**Chosen approach:** replace it with a small hand-written include driven by `_data/links.yml`,
with an inline Scholar SVG. Drops the dead branches, and lets the same include be reused in the
header/homepage rather than only the footer.

```yaml
# _data/links.yml
- {label: Google Scholar, url: "https://scholar.google.com/citations?user=7LDpc4UAAAAJ&hl=en", icon: scholar}
- {label: GitHub,   url: "https://github.com/jingerchong",        icon: github}
- {label: LinkedIn, url: "https://linkedin.com/in/jingerchong",   icon: linkedin}
- {label: CV,       url: "/downloads/jinger-chong-cv.pdf",        icon: file}
```
Remove `instagram` from `_config.yml:43`.

---

## 7. Taxonomy (Option A, approved)

```yaml
categories_order:
  - Research               # published / in-review output, lab work
  - Perception & Autonomy  # perception, prediction, estimation, autonomy stacks
  - Systems & Hardware     # mechanisms, embedded, test infrastructure
  - Teaching               # TA, curriculum, outreach
  - Archive                # early maker work — last, excluded from homepage
```

Convention for the Research/Perception overlap: **`Research` = things with a paper, patent, or lab
affiliation. The topic buckets = everything else.** The MRL intent-prediction work is `Research`.

`_archives/` stubs must be renamed to match the new slugs
(`research`, `perception-autonomy`, `systems-hardware`, `teaching`, `archive`) — `_layouts/category.html:7`
does `page.slug | capitalize` to look up `site.categories[title]`, which **will not round-trip
multi-word or ampersand names**. Fix by adding an explicit `title:` to each stub and using that
instead of `capitalize`.

Archive stays in nav but is excluded from the homepage and listed last.

Rejected alternatives, for context: **B** (Publications & Patents / Research / Industry / Teaching)
— stronger, revisit once the ICRA 2027 paper is accepted; one `area:` rename away by design.
**C** (topic-only: Perception / Motion & Prediction / Mechanisms) — where this lands in 2–3 years.

---

## 8. Content model: two types

The existing `_jobs`/`_schools` pattern (non-output collection rendered as an inline list) is already
the right shape for lightweight entries. **Extend it; do not invent a new mechanism.**

### Type A — deep dive (`_posts`, mechanism unchanged)
```yaml
---
title:   Autonomous Racecar Stack
date:    2022-03-20
area:    Perception & Autonomy        # replaces `categories`
venue:   6.141 Robotics: Science & Systems
summary: >                            # replaces excerpt truncation
  Localization, path planning, and vision-based control on a
  1/10-scale racecar running ROS.
cover:   true                         # gates the cover <img> — see bug 2
featured: true
---
```
`summary:` replaces `post.excerpt | truncatewords: 12`, which currently mangles descriptions
mid-sentence in three templates.

### Type B — lightweight record (new, **`output: false`**)
No page is generated, so **there is no thin page to pad**.

```yaml
# _config.yml
collections:
  records:
    output: false
```
```yaml
# _records/gev-blade-inspection.markdown
---
title:     Autonomous Wind Turbine Blade Inspection
type:      industry          # publication | patent | industry | research | teaching
org:       GE Vernova Advanced Research Center
org_link:  https://www.gevernova.com/
role:      Computer Vision Research Intern
period:    Jun 2026 – Aug 2026
area:      Perception & Autonomy
status:    Patent pending
confidential: true           # gates links, cover, and grids in the template
order:     95                # same convention as _jobs
show:      true              # same convention as _jobs
links:                       # omit entirely when confidential
  - {label: Patent application, url: "https://patents.google.com/..."}
page:      /alfredo/         # OPTIONAL — see below
---

Two to four sentences: impact + method. No proprietary detail.
```

Rendered by a new `_layouts/research.html` on `research.markdown`, grouped by `type`, sorted
`order | reverse`. This is structurally the same loop as `_layouts/about.html:22-31`, so it
**inherits the existing `.resume` two-column CSS for free** — no new layout CSS required.

### The `page:` field is the key to the whole design
`_records` becomes the single ordered source of truth for everything, and any record may optionally
point at a `_posts` deep dive:

- **Confidential internship** → record only, no `page:`. Renders as a blurb. Nothing to pad.
- **Paper in review** → record now with `status: Under review`. On acceptance, add a `_posts` page
  and **one line** of YAML. No re-categorization, no moved URL, no lost ordering — the list entry
  simply becomes clickable.
- **Existing strong project** → both a `_posts` page and a thin record, so it also appears under Research.

This matters because the repo already shows the failure mode it avoids:
`_posts/2021-04-25-jansens-linkage.markdown` is an empty file that is nonetheless linked from
`_schools/ib-diploma.markdown:13`, and `_posts/2020-08-31-rl-in-2048.markdown:10` still promises a
JavaScript GUI announced in 2020.

`confidential: true` must gate `links`, `cover`, and grids in the template — belt and braces on top
of simply omitting the fields, so a confidential entry can never render a broken image or dead link.

---

## 9. Assets, CV, and contact

### Headshot
`headshot.jpg` — **3223×3223, 1.29 MB.** Too large to ship. Convert to
`assets/headshot.webp` at ~800×800 (plus a ~1600px `@2x` if a retina variant is wanted) and
overwrite the existing sketch path so `site.headshot` in `_config.yml:37` keeps working.

Retire the sketch (`assets/headshot.webp`, current hand-drawn version — **copy it aside before
overwriting**) to a small footer or 404 easter egg so the personality survives without carrying the
professional first impression. Keep the robot-arm logo/favicon exactly as-is.

### Banner
`assets/banner.webp` is a photo of the owner at a drill press in goggles and a mask, 400px full-bleed
on **every** page. Technically fine work, but "undergrad in the shop" is precisely the read being
moved away from, and it is the first thing a visitor sees. Candidates: the UR5 rig, a
LiDAR/point-cloud visualization, or an abstract navy/yellow gradient. Lower priority than the
avatar, higher visual weight — raise it with the owner rather than swapping silently.

### CV PDF — redaction required
The résumé PDF currently sits in the repo root. **Jekyll copies root files into the built site**, so
committing it publishes it at `jingerchong.com/Jinger%20Chong_Resume.pdf`.

Plan:
1. Add `.DS_Store`, `*.docx`, and the working résumé PDF to `.gitignore`, or move the sources out of
   the repo entirely.
2. Publish a deliberately-prepared copy at **`downloads/jinger-chong-cv.pdf`** (alongside the
   existing `downloads/revise-product-sheet.pdf`).
3. **Redact from the public copy: the phone number.** It is the only genuinely sensitive field —
   there is no street address, and email / city / GPA / advisor are all normal on a public academic CV.
   GPA is a positive here (5.0/5.0 graduate) — keep it.

### Contact email
The résumé uses **`jinger@mit.edu`**. `_config.yml:22` currently uses `me@jingerchong.com`.

**Recommendation: show `jinger@mit.edu` first, keep `me@jingerchong.com` as a listed secondary.**
The MIT address matches the CV, the papers, and the patent filing — consistency across those is
what makes an application look coherent, and an institutional address reads more credible to
research recruiters. But MIT addresses lapse after graduation, and the personal domain is the
durable one, so it should not disappear. `jekyll-seo-tag` and the `h-card` markup in
`_includes/footer.html` both key off `site.email` — set that to the MIT address and render the
secondary separately.

---

## 10. Typography and color: keep vs. tweak

### Keep explicitly — this is the identity, do not let the edit flatten it
- **`$theme-color: #08415C` + `$accent-color: #EFCA08`** (`_sass/colors.scss:5-6`). Distinctive,
  high-contrast, already reads technical. Navy/yellow is exactly what a robotics lab would pick.
- **The `h2:after` accent underline** (`_sass/layout.scss:34-42`). The site's signature move and
  genuinely good. Use it on `/research/` too.
- **Yellow `::selection`** (`colors.scss:8-16`) — a confident detail most portfolios skip.
- **Uppercase letterspaced `h2`** (`_sass/fonts.scss:13-21`) — reads editorial, not juvenile.
- **Yellow robot-arm logo** and navy header/footer bands. All working.

### Reads undergrad — change
| What | Where | Change |
|---|---|---|
| `6em` "Hi, I'm Jinger" | `_sass/fonts.scss:36-43` | **Highest-impact single CSS change.** Drop to ~3.5em; add a descriptor line — e.g. *"Robotics & perception · MIT"*. A 96px greeting says personal blog; a name plus a research area says researcher. |
| Body copy tone | `index.markdown:8-12` | **Keep** "my name is pronounced like *ginger*" — memorable, one line. **Cut** "Oh, and I like Japanese food" and "I like building things, and then making them to do stuff for me." One personality line charms; three read freshman. |
| Same, in posts | `abes-outreach:12`, `soccer-robot:12`, `revise:12` | Cut "public speaking and comedy skills", "by some miracle", and the "haven't finished sorting out the documentation" apology. |
| `text-transform: lowercase` on badges | `_sass/fonts.scss:58-61` | Deliberate lowercase is a *casual* signal, and the new labels carry real meaning. Switch to sentence case. |
| `$base-font-weight: 300` | `_sass/fonts.scss:1` | Thin for the longer research prose being added. Body → 400; keep 300 for large display text. |
| `theme_color: "#ffffff"` | `site.webmanifest:16` | → `#08415C`, matching `custom-head.html`. |

**Typeface:** currently minima's default Helvetica/Arial system stack — neutral, fast, unlicensed,
genuinely fine. If one upgrade is wanted, the highest-return move is **not** a new body face but a
**monospace accent for metadata** (`ICRA 2027 · under review`, `Patent pending`, dates, venues).
Mono metadata against a clean sans body is a strong, cheap "technical document" signal and plays
well with the navy/yellow being kept.

---

## 11. Disposition of every existing post

### Keep as full deep-dive pages (4)
| File | Why | Required change |
|---|---|---|
| `_posts/2022-03-20-alfredo.markdown` | Real robotics: localization, planning, vision. 4 embedded videos. | `area: Perception & Autonomy`. **Rename** — "Alfredo" alone reads cute; title it for the work (e.g. "Autonomous Racecar Stack"), keep the robot's name in the body. |
| `_posts/2021-12-20-revise.markdown` | 20-person capstone, granular jamming, product sheet + Vimeo webcast. Best systems story on the site. | `area: Systems & Hardware`. Trim the line-12 apology. |
| `_posts/2020-08-31-rl-in-2048.markdown` | TD-learning, 93% win rate, done at NCTU CGI Lab — a **research internship**, not a game. | `area: Research`. Reframe around lab + method. Delete the stale 2020 GUI promise (line 10). |
| `_posts/2019-01-16-abes-outreach.markdown` | Only substantive teaching page; 40+ photos across 5 grids. | `area: Teaching`. **Remove `featured: true`.** Cut the line-12 close. |

### Demote to `_records` (4)
- `_posts/2020-12-08-segway-robot.markdown` — one sentence, 3 photos; real 2.004 controls content, not a page's worth.
- `_posts/2020-01-07-toy-for-toddlers.markdown` — one sentence, but a genuine research instrument for MIT ECCL. Belongs under Research.
- `_posts/2020-03-05-rf-controllers.markdown` — **currently featured**; careful assembly, not design. Fold into a NEET teaching record.
- `_posts/2021-01-30-minibot.markdown` — **currently featured**; a seminar robot car that Alfredo strictly supersedes.

Also collapse `_posts/2019-11-24-esp-splash.markdown` and `_posts/2018-04-19-sjcs-robocup.markdown`
together with ABES into **one Teaching group** — three thin teaching pages dilute; one credible
teaching record does not.

### Move to Archive (6)
| File | Why |
|---|---|
| `_posts/2019-07-27-iron-man.markdown` | A model kit and a display case, **featured on the homepage.** Single biggest hobbyist signal on the site. |
| `_posts/2020-01-10-home-upgrades.markdown` | Fridge fixes, a clock, a key holder. Charming; not a researcher's portfolio. |
| `_posts/2019-12-30-rubber-band-turret.markdown` | Freshman-seminar rubber band shooter. |
| `_posts/2020-01-06-flashlight.markdown` | 2.670, a 3-day IAP class. Every MIT MechE has this exact flashlight. |
| `_posts/2019-08-25-soccer-robot.markdown` | Pre-orientation first-robot project, framed as "by some miracle." |
| `_posts/2021-04-25-jansens-linkage.markdown` | **Empty file**, currently a broken link from `ib-diploma.markdown:13`. Either write it or drop the link. |

**"Archive" means re-categorize and drop from nav prominence — not `rm`.** The webp assets are small
and already committed; deleting buys nothing.

---

## 12. New entries from the résumé

Résumé decoded 2026-09-02 from `Jinger Chong_Resume.pdf`. **The PDF uses subset-font encoding**;
text was recovered by reconstructing the glyph maps. Prose came through cleanly. **A handful of
bolded numerals did not** — every one is flagged `⚠️CONFIRM` below. Do not publish a flagged
number without asking.

### Résumé facts that change `/about/`
The current `_schools`/`_jobs` content is roughly two years stale.

- **PhD Candidate, Mechanical Engineering, MIT** — Advisor: **Kamal Youcef-Toumi**. GPA 5.0/5.0.
  Expected graduation ⚠️CONFIRM. **There is no PhD entry in `_schools/` at all**, yet
  `index.markdown:10` already claims "SM-PhD student".
- **SM, Mechanical Engineering, MIT** — GPA 5.0/5.0, **Sep 2023 – May 2025**.
  `_schools/masters.markdown` currently says `Sep 2023 - Dec 2024` and `GPA: N/A`. Both wrong.
- **BS, Mechanical Engineering, MIT** — Minor in Computer Science and Chinese, GPA 4.9/5.0,
  Sep 2019 – May 2023. (Repo omits the Chinese minor pairing and lists NEET/honor societies —
  reconcile.)
- Coursework named on the résumé: Underactuated Robotics, Visual Navigation for Autonomous
  Vehicles, Algorithms, Robot Interaction (⚠️CONFIRM — possibly "Human-Robot Interaction").
- `_jobs/mrl-urop.markdown` still says `Sep 2022 - Present` with only the UR5/YOLOv7 bullets —
  needs the intent-prediction work added.
- **Résumé sections are:** Education, Experience, Publications & Patents, Projects, Technical Skills.
  No separate awards section (the one award is inline in Projects).

### Publications & patents (verbatim from résumé)
1. **J. Chong, ⚠️CONFIRM-initial Zhang, K. Youcef-Toumi**, "Towards Scalable Probabilistic Human
   Motion Prediction with Gaussian Processes for Safe Human-Robot Collaboration," ***ICRA 2027***,
   **under review**. → the **flagship**; first item on `/research/`.
2. **⚠️CONFIRM-initial Zhang, J. Chong, K. Youcef-Toumi**, "How Does Perception Affect Safety? New
   Metrics and Strategy," ***ICRA 2024***. → the one **published** paper.
3. **J. Chong et al., "Multi-Function Hinge,"** U.S. Patent Application Publication
   **No. US 2026/0143604 A1** (⚠️CONFIRM the 7-digit serial), 2026, pending. → **published
   application: link it.** Third-party verifiable, worth more than any project page on the site.

### Records to create
| # | Entry | `type` | Notes |
|---|---|---|---|
| 1 | MIT MRL — intent prediction / ICRA 2027 | `publication` | Flagship. Outperformed baselines incl. **Motron (CVPR 2022)** on probabilistic full-body motion prediction (**Human3.6M**). Structured multitask variational Gaussian process, joint-dimension factorization, continuous **6D** rotation representation; validated by empirical coverage analysis and ablations over kernel, inducing points, latent dimensionality. **⚠️CONFIRM both bolded metrics** — the margin (something "… nats …") and the "N× fewer parameters" figure both decoded ambiguously. |
| 2 | ICRA 2024 perception/safety paper | `publication` | Second author. |
| 3 | Microsoft — Multi-Function Hinge | `patent` | Mechanical Engineering Intern, **Jun 2024 – Aug 2024**. Owned end-to-end design and prototyping from concept through alpha; translated benchmarking and user-study findings into specs and first-order models for spring selection, material choice, friction tuning. Converged on target torque profile via iterative fabrication/measurement of 3D-printed and CNC-machined prototypes. **Link the published application.** |
| 4 | GE Vernova ARC — blade inspection | `industry` | Computer Vision Research Intern, **Jun 2026 – Aug 2026**. `confidential: true`, **no links**. Visual localization for an inspection crawler along **50–75 m** blades, chunked into overlapping windows: COLMAP SfM with sequential **ALIKED + LightGlue** matching on perspective views rendered from equirectangular imagery. Cascaded coarse-to-fine geometric verification filter. Delivered a **2–5 hour per blade** single-node pipeline slated for deployment; **invention disclosure under internal patent review**. **⚠️CONFIRM**: the "reduced inspector review volume by X" figure, and the candidate-pair scale (decoded as 10^a–10^b, exponents unresolved). |
| 5 | Rotor Technologies — LiDAR compression | `industry` | Graduate Engineering Intern, **Jun 2023 – Sep 2023**. **⚠️CONFIRM ratio:** résumé decodes as **100:1**, but `_jobs/rotor-grad-intern.markdown:11` says 50:1 — reconcile. H.265 encoding for low-latency streaming for remotely-piloted helicopters; sensor emulation from recorded video + packet captures; bandwidth reduced up to **3×** via azimuth-level decimation and adaptive bitrate. Strongest deep-dive candidate among the industry items **if** plots are shareable. |
| 6 | Rotor Technologies — subscale helicopter infra | `industry` | Undergraduate Engineering Intern, Jun 2022 – Aug 2022. Expanded test infrastructure **1 → 3 units**; integrated onboard power/data; bridged EKF + airspeed from **PX4** to proprietary flight software. |
| 7 | MIT MRL — UR5 rig + YOLOv7 study | `research` | Sep 2022 – Present. Adjustable UR5 camera rig **adopted lab-wide** for validating perception and manipulation algorithms. Already half-written at `_jobs/mrl-urop.markdown:11-12`. |
| 8 | MIT — Intro to Robotics TA | `teaching` | Teaching Assistant, Jan 2024 – May 2024. Built embedded C++ and **ESP32-S3** platforms for labs in motor control, kinematics, computer vision, ⚠️CONFIRM (one bolded topic unresolved), sensor interface. Revamped curriculum and lab handouts for a **50+**-student graduate robotics course with ⚠️CONFIRM instructional staff. |
| 9 | MIT ECCL — toddler research instrument | `research` | From the demoted `toy-for-toddlers` post. |
| 10 | NCTU CGI Lab — TD-learning 2048 | `research` | Points at the kept `rl-in-2048` page via `page:`. |

### Two résumé projects **not on the site at all** — strong deep-dive candidates
Both use Drake + Python and are more research-credible than anything currently featured:

- **Autonomous Pool-Playing Robot** — Robotic Manipulation (6.4210), **Outstanding Project award**,
  Sep – Dec 2023. Physics-based single-shot simulation modeling cue dynamics, ball motion,
  collisions; sinks target balls consistently in randomized simulations using a heuristic task
  planner with IK and inverse-dynamics control. **The award makes this the best unclaimed asset on
  the résumé — promote it.**
- **Water Bottle Flipping Quadrotor** — Underactuated Robotics, Feb – May ⚠️CONFIRM year (2023 vs
  2024 decoded ambiguously). Robust bottle-flipping across 4 fill levels (25–100%) using
  direct-collocation hybrid trajectory optimization; modeled quadrotor–bottle dynamics with
  constraints for transitions, collisions, contact/impulse forces, and states.

### Skills (`_skills/`) — replace with résumé versions
- **Languages:** Python, C++, MATLAB, Julia, LaTeX *(résumé drops Java, HTML, CSS, SQL, OpenSCAD,
  Google Apps Script — the trimmed list reads more senior; adopt it)*
- **Tools:** PyTorch, GPyTorch, OpenCV, COLMAP, hloc, ROS, Drake, Eigen, NumPy, SciPy,
  scikit-learn, libpcap, FFmpeg, Git
- **Hardware:** SolidWorks, Fusion 360, 3D printing, laser cutting, CNC, machining, soldering,
  electronics and sensor integration
- `_skills/multimedia.markdown` is already `show: false` — delete with the photography page.
- Note the résumé's three categories differ from the repo's four (`Languages` / `Frameworks` /
  `Fabrication` / `Multimedia`). Rename to match: Languages / Tools / Hardware.

---

## 13. Implementation order

Do it in this sequence — each step leaves the site in a working state.

1. **Hygiene first.** `.gitignore` (`.DS_Store`, `*.docx`, working résumé PDF); delete
   `tripod_submission.png`. Prevents accidentally publishing the unredacted résumé.
2. **Fix the bugs in §3** — especially bug 1 (`resume.html` empty hrefs) and bug 2 (unguarded
   cover images, which blocks confidential records).
3. **Remove photography** — `photography.markdown`, `_layouts/photography.html`,
   `_skills/multimedia.markdown`, the `photos:` collection key, `navbar_order` entry, and the
   `instagram` social link.
4. **Assets** — convert `headshot.jpg` → `assets/headshot.webp` (~800px); preserve the old sketch
   elsewhere first.
5. **Links** — `_data/links.yml` + rewritten `_includes/social.html` with inline Scholar icon;
   redacted CV at `downloads/jinger-chong-cv.pdf`; set `site.email`.
6. **Taxonomy** — new `categories_order`; rename `_archives/` stubs and give each an explicit
   `title:`; fix `_layouts/category.html`'s `capitalize` lookup.
7. **`_records` collection** — `_config.yml` entry, `_layouts/research.html`, `research.markdown`,
   nav entry. Populate with the 10 records in §12.
8. **Re-categorize the 16 existing posts** per §11 — `area:` in, `categories:` out, `summary:`
   added, `featured:` corrected. **This is where the actual repositioning happens.**
9. **Update `/about/`** — new PhD `_schools` entry, corrected SM dates, new `_jobs` for GE Vernova /
   Microsoft / Intro to Robotics TA, updated MRL bullets, rewritten `_skills`.
10. **Homepage** — Selected-work block drawing from both types; identity row; banner type scale;
    trimmed bio prose.
11. **Two new deep dives** (pool robot, quadrotor) once the owner supplies writeups/media.
12. **Typography pass** (§10) last, so it applies to final content.

### Verify before declaring done
- `bundle exec jekyll build` clean; `/research/`, `/projects/`, each category page, `/about/`,
  and every kept post render.
- No broken `cover.webp` requests (bug 2) and no empty `href=""` on `/about/` (bug 1).
- Grid galleries still resolve for every kept post (slug-substring matching, §1).
- No confidential record emits a link, cover, or grid.
- Résumé PDF is **not** in the built site at the repo root; the redacted CV **is** at
  `/downloads/jinger-chong-cv.pdf` with the phone number gone.
- Every `⚠️CONFIRM` number in §12 either confirmed by the owner or omitted.

---

## 14. Open items for the owner

1. **All `⚠️CONFIRM` numbers in §12** — the bolded metrics, the patent serial, the co-author's first
   initial, the Rotor ratio (100:1 vs the repo's 50:1), the quadrotor project year, the PhD
   expected-graduation date. Easiest fix: paste the affected résumé lines as plain text.
2. **Expected PhD graduation date** for the new `_schools` entry.
3. **Banner image** — keep the drill-press photo or replace (§9)?
4. **Pool robot / quadrotor** — supply writeups + media to build those deep dives?
5. **Rotor LiDAR compression** — are any plots or figures shareable? Determines deep dive vs. record.
6. **ORCID** — worth adding alongside Scholar?
