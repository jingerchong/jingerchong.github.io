# TODO — portfolio content and improvements

This is the single place to track open site work. A missing cover uses a blueprint tile in
listings and no detail-page hero; hidden drafts have `published: false` and are not launch blockers.

## Site redesign: final spec (implemented 2026-10-02)

**Status: implemented.** The specification below is retained as the design reference.

- [x] Shared tokens, typography, heading mixin, rows, entries, chips, and blueprint tiles.
- [x] Animated approved logo, one-row phone navigation, skip link, and email-first footer.
- [x] Home hero and configurable status, Publications with BibTeX, Projects, and Experience.
- [x] About, Research, Industry, education detail lines, and illustrative prediction figure.
- [x] Unified project cards and detail layout, previous/next links, YouTube and local-loop includes.
- [x] 404, social image defaults and existing project covers, project example, and agent guide.
- [x] Ruby 3.3 build and local-link checks; desktop/phone checks at 1280px and 375px.

Verification covered Home, Research, Industry, Projects, About, 404, bottle-flip,
alfredo, struct-gp, and safety-metrics (no cover/stack/links). All fit both widths;
phone navigation remains one row and BibTeX expands without overflow. Local media
loops were checked with reduced motion on/off and preference changes. The education
data already had the requested BS detail-line split. Original project wording is retained;
further editorial migrations remain a separate owner-guided pass.

Remaining non-blocking content: bottle-flip role/team and media, real missing covers,
approved research figures, and off-the-clock photos. The future list below remains deferred.

This is the single source of truth for the redesign. It replaces the earlier rounds of options
and decisions.

**Reference files** (in `examples/design/`, which is excluded from the Jekyll build):

- `site-style-mockups-final.html`: the visual reference. Open it in a browser; it has Home,
  About, Research, project-page and type-system tabs, plus a phone-width toggle. Its CSS tokens
  and components are a starting point for the Sass.
- `logo.svg`: the **approved** SVG redraw of the logo (approved 2026-10-02). Content rules from `AGENTS.md`
still apply: no invented facts, metrics, media or links.

### 1. Design tokens (`_sass/_tokens.scss`)

Build everything from these tokens; no one-off sizes, colors or margins.

- **Fonts:** IBM Plex Sans and IBM Plex Mono only, loaded from Google Fonts.
- **Sizes (7):**
  - display 3.3em (hero name)
  - title 2.25em (project page title)
  - lede 1.2em (Research lede, project TL;DR)
  - item 1.05em (project, paper, org and degree titles)
  - body 1em
  - small 0.92em (summaries, authors, secondary lines, link rows, desktop nav)
  - mono 0.8em (every mono element and the phone nav)
- **Weights:** 300 (hero "Hi, I'm" only), 400, 700. Use 600 only for mono labels and buttons.
- **Colors:**
  - text `#111`, grey `#646E78` (meta)
  - theme `#08415C`, accent `#EFCA08`, light `#D9DCD6`, paper `#f5f6f2`, deep `#062f43`
    (hero gradient)
- **Spacing (4 steps, in rem):** 0.4, 0.9, 1.6, 3.
- **Widths:** content 1040px max (28px gutters; 16px on phones). Prose capped at ~760px.
  One shared left column, `--col: 150px`. Lists, entries, skills and the About intro run the
  full width, so right-aligned dates and the headshot end on the same edge as the section rules.
- **Numerals:** `font-variant-numeric: tabular-nums` on all mono text.

### 2. Shared components (each defined once in `_sass/`)

- **Section heading:** mono uppercase label (0.8em, 600, letter-spacing 0.14em, theme color)
  plus a hairline rule to the right, with an optional "All … →" link at the end of the rule.
  Put it behind one mixin so the original style can come back (see "Original heading style"
  below).
- **Kicker:** navy box with light mono text, e.g. `Underactuated Robotics · 2023` or
  `ICRA 2024`. The patent uses an outlined variant.
- **Chip:** outlined in navy, mono, 2px radius. Used for skills and project stacks.
- **Link:** navy text with a 2px yellow underline that thickens on hover. Used for body links
  only; nav, cards and buttons keep their own styles.
- **Button:** mono uppercase, 2px navy border. Few uses.
- **Status tag:** yellow with a green dot. The text comes from a single `_config.yml` value
  (e.g. `status:`); empty it to hide the tag after accepting an offer.
- **Focus:** 3px yellow outline. Add a skip link.
- **Left-column rows (`.lc`):** `--col` + content. Used by Publications (venue/status tag on the
  left) and the Projects rows (16:10 thumbnail on the left). Hovering a row highlights its title.
- **List (`.list`):** "Role, *Organization*" on the left, mono date on the right. Row padding
  0.15em, line-height 1.5. One component for Home Experience, Teaching and Service.
- **Entry (`.ent`):** org (item size, bold) with location on the right, then role (italic) with
  dates on the right, then bullets or detail lines. Used on Research, Industry and Education.
- **Metrics in bullets:** bold only, with no highlight (it could be mistaken for a link).
- **Blueprint tile:** a navy engineering-grid tile with a small line drawing. A temporary
  fallback for missing covers and thumbnails; real covers replace it.

### 3. Header and footer

- **Header:** navy bar with the logo on the left and four nav items (Research, Industry,
  Projects, About), uppercase sans.
  - Nav size is `small` on desktop and `mono` on phones. It stays **one row** on phones; four
    items fit at 390px.
  - The active page gets yellow text plus a 2px yellow underline.
- **Logo:** an SVG redraw of the robot arm with separate parts.
  - On hover (and on keyboard focus), the shoulder and elbow rotate a few degrees and the
    gripper opens. No motion under `prefers-reduced-motion`.
  - Use the **approved** redraw at `examples/design/logo.svg`; no further tracing is needed.
    - Groups and rotation origins (viewBox units): `.sh` shoulder about (446.5, 503.5), `.el`
      elbow about (287.5, 346), `.f1`/`.f2` fingers about (382.5, 251.5).
    - Hover values from the mockup: `.sh` −7°, `.el` +12°, `.f1` −16°, `.f2` +16°.
    - Inline the SVG in `_includes/header.html` so CSS can animate the groups.
  - Jinger's original `logo.psd` isn't needed; if it's ever added, keep it out of the published
    site.
  - Optionally reuse the SVG as the favicon.
- **Footer:**
  - A "CONTACT" section heading in yellow.
  - **`jinger@mit.edu`** as a large clickable `mailto:` link, the main item.
  - Four labeled links with icons: Google Scholar, GitHub, LinkedIn, CV (PDF).
  - Colophon: "Updated <Mon YYYY> · Set in IBM Plex · Built with Jekyll · © <year> Jinger
    Chong". The date comes from `site.time`.
  - No pitch line, no source link.

### 4. Home (`index.html`)

Order, chosen for impact on research-internship reviewers:

1. **Hero:**
   - Full-bleed banner photo with a navy gradient from the **right**. Right-aligned "Hi, I'm"
     (300) / "Jinger" (700, yellow).
   - Tagline "Human intent prediction · Autonomous navigation" (mono).
   - Status tag "Open to Summer 2027 research internships".
   - On phones the gradient runs from the bottom, and the background position keeps Jinger in
     frame.
2. **Bio:** the first bio paragraph only, plus "More about me →". No headshot on Home.
3. **Now line:** "NOW" label + "Seeking a Summer 2027 robotics research internship in human
   intent prediction, perception, or uncertainty-aware navigation/HRI. View my CV →". The text
   is updated to match the tagline.
4. **Publications:**
   - Left column: venue kicker + status.
   - Right: title (item), authors (small, "J. Chong" bold), and a links row.
   - **Cite** toggle: a native `<details>` showing the paper's BibTeX, stored in a `bibtex`
     field in `publications.yml`. The exact entries are in "Content ready for handoff" below.
     The patent has no Cite toggle.
   - Paper PDFs come from arXiv links; nothing is hosted locally. The patent links to Google
     Patents.
   - Later: a `links.project` field once paper writeups exist, and teaser thumbnails in the
     left column once figures exist.
5. **Projects** (heading "Projects", link "All projects →"): `.lc` rows for the featured
   projects, each with a thumbnail, kicker (`context · year`), title and summary.
6. **Experience** (heading "Experience", link "All experiences →"): `.list` rows, e.g.
   "Computer Vision Research Intern, *GE Vernova Advanced Research Center*" with the year.
   Three roles, no cards, no bullets.
7. **Footer.**

### 5. About (`about.html`)

1. **Outside the lab:**
   - The hobbies paragraph, moved from Home with its wording unchanged.
   - **Headshot square, on the right**, with its edge on the shared right edge. The paragraph
     stays at a readable width.
2. **Education:** one MIT `.ent` header (Cambridge, MA), then one entry per degree with dates on
   the right. The BS lines are:
   - "GPA: 4.8/5.0 · Minors in Computer Science and Chinese"
   - "NEET Autonomous Machines Certificate · Tau Beta Pi · Pi Tau Sigma" (one line of its own)

   This needs a `_data/education.yml` change: one detail per line.
3. **Skills:** chip rows, with category labels (mono, grey) in the left column.
4. **Teaching** and **Service:** `.list`.
5. Later: an off-the-clock photo strip under the paragraph, once there are photos.

### 6. Research (`research.md`) and Industry (`industry.html`)

- **Research NOW:**
  - The first sentence is a lede (lede size); the rest is a normal paragraph.
  - The signature figure sits beside it: an illustrative plot of a predicted path with
    uncertainty, captioned "Fig. 0 … Illustrative". Replace it with a real approved figure later.
  - No focus chips.
- **Research and Industry entries** use `.ent` with mono dates and locations. No timeline rail.
- Later: "→ writeup" links from entries, once the writeups exist.

### 7. Projects index (`projects.html`)

- **Grid cards:**
  - Merge `content-card` and `project-card` into **one** card include.
  - Each card shows the kicker (`context · year`) above the title and a 16:10 cover, with the
    blueprint tile as fallback.
  - Hover: navy border plus highlighted title.
- **"More" list:** mono years in a left column, then "Title, *context*".
- **Order:** unchanged for now. Moving the research projects first waits until their writeups
  exist.

### 8. Project pages (`_layouts/project.html`)

1. "← Projects" link (mono).
2. Kicker `context · year`, then the title (title size, uppercase, yellow highlighter underline).
3. **Meta list** (`dl`, mono grey keys):
   - ROLE, TEAM, AWARD if present.
   - **STACK** as outlined chips.
4. **Links row** at the top only:
   - Fixed order and labels: Paper, arXiv, Code, Video, Report, Slides, Poster, Website. Other
     keys are capitalized.
   - Show "(PDF)" after .pdf targets. Skip empty or `#` values.
5. **Hero:** full width, 16:9, from `assets/images/<slug>/cover.webp`. If `hero_video` (a
   YouTube ID) is set, it fills the slot instead. No cover means no slot.
6. **TL;DR:** lede size with a yellow left rule. Comes from `tldr`, falling back to `summary`.
7. **Prose body:**
   - Use `##` only on long pages, with descriptive wording.
   - Sub-headings use the section-heading component.
8. **Previous / next** links at the bottom, following the grid order.

**Front matter:**
- `title`, `summary` (one sentence, cards), `tldr` (2–3 sentences, page).
- `tier`, `order`, `year`, `context`, `role`, `team`, `award`.
- `stack` (list), `links` (map), `hero_video`.
- Missing fields disappear cleanly.

**Media conventions:**
- **YouTube:** `_includes/youtube.html` (`id`, `title`, optional `caption`). It uses
  youtube-nocookie.com, lazy loading and a responsive 16:9 frame. It replaces the four raw
  iframes in `alfredo.markdown`.
- **Local loops:** `_includes/video.html` for muted, looping mp4/webm, with no autoplay under
  reduced motion.
- **PDF writeups:** at `downloads/<slug>/<name>.pdf`, linked from `links`. Check them for
  private content first.

**Migration:** convert pages one at a time, together with Jinger. `bottle-flip` is already
converted; fill its `role`, `team` and media.

### 9. Site-wide extras

- **404 page:** "Trajectory not found" with a small planned-path drawing and a "Back to home"
  button.
- **Social share card:** set an `image:` default in `_config.yml`; `jekyll-seo-tag` is already
  installed. Project pages can reuse their covers.

### Content ready for handoff

**BibTeX for the Cite toggles** (supplied by Jinger 2026-10-02). Add each as a `bibtex: |`
block on the matching entry in `_data/publications.yml`, copied verbatim.

ICRA 2027 / arXiv entry (Structured Multitask Gaussian Processes…):

```bibtex
@misc{chong2026structuredmultitaskgaussianprocesses,
      title={Structured Multitask Gaussian Processes for Probabilistic Full-Body Human Motion Prediction},
      author={Jinger Chong and Xiaotong Zhang and Kamal Youcef-Toumi},
      year={2026},
      eprint={2603.07096},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2603.07096},
}
```

ICRA 2024 entry (How Does Perception Affect Safety…):

```bibtex
@INPROCEEDINGS{10610657,
  author={Zhang, Xiaotong and Chong, Jinger and Youcef-Toumi, Kamal},
  booktitle={2024 IEEE International Conference on Robotics and Automation (ICRA)},
  title={How Does Perception Affect Safety: New Metrics and Strategy},
  year={2024},
  volume={},
  number={},
  pages={13411-13417},
  keywords={Measurement;Accuracy;Computational modeling;Collaboration;Detectors;Real-time systems;Inference algorithms},
  doi={10.1109/ICRA57147.2024.10610657}}
```

**Other content already decided:**
- Email `jinger@mit.edu` (footer, `mailto:`).
- Tagline "Human intent prediction · Autonomous navigation".
- Status "Open to Summer 2027 research internships".
- The Now-line text in section 4.

**Still needed from Jinger (not blockers):**
- bottle-flip `role` and `team`.
- Real covers to replace the blueprint tiles.
- Approved figures for struct-gp and the Research signature figure.
- Photos for the off-the-clock strip.

### Original heading style (for switching back)

- `h2`: uppercase, `font-size: 2em !important`, `font-weight: 700 !important`,
  `letter-spacing: 0.05em` (in `_sass/fonts.scss`), `margin: 0.75em 0` (in
  `_sass/layout.scss`).
- `h2:after`: absolute block, `height: 3px`, `width: 100px`, `margin-top: 0.25em`, navy
  `background` (in `_sass/layout.scss` and `_sass/_tokens.scss`).
- Footer CONTACT heading: the same, with a yellow bar.

### Future list (not now)

- Lead card for the research project.
- Sticky side meta on long project pages.
- Project filter chips (at 9+ grid projects).
- Numbered figure captions.
- Off-the-clock photo strip.
- Facts strip under the banner.
- Consistent cover treatment (maybe).
- Hosting the ICRA 2024 accepted manuscript (not needed while arXiv covers it).

**Not doing:**
- Industry cards on Home.
- Timeline rail / kinematic-chain motif.
- Metric highlights.
- Hover-to-play clips.
- Navy statement band.
- Alternating paper bands.
- Dark mode.
- Method chips per industry role.
- Research focus chips.

### Implementation prompt

```text
You are working in Jinger Chong's Jekyll portfolio (jingerchong.github.io). First read
AGENTS.md, README.md, _config.yml and TODO.md, and follow them: build with Ruby 3.3, stay
compatible with GitHub Pages, never invent content, and check git status and preserve unrelated
changes.

Implement "Site redesign: final spec" in TODO.md exactly, using
examples/design/site-style-mockups-final.html as the visual reference and
examples/design/logo.svg as the approved logo. If something in the spec is unclear
or needs content you don't have, stop and ask; don't guess. Work in phases and build/preview after each one:

1. Foundation: tokens (fonts, 7 sizes, weights, colors, 4 spacing steps, widths, --col) and the
   shared components in section 2, replacing the old h2 style behind one mixin. Remove styles
   the new components make obsolete.
2. Header and footer (section 3), including the SVG logo with hover motion, the one-row phone
   nav, the active-page underline and the email-first footer with the colophon.
3. Home (section 4): mirrored hero, status from _config.yml, bio + Now, Publications with the
   Cite toggle (copy the BibTeX verbatim from "Content ready for handoff"), Projects rows and
   the Experience list.
4. About, Research and Industry (sections 5–6), including the education.yml line split. Keep
   all wording unchanged except where the spec says otherwise.
5. Projects index and project pages (sections 7–8): one card include, blueprint fallback, the
   new layout and front matter, the youtube/video includes, the alfredo iframe swap, and a
   rewritten examples/project.md. Update the Project and Gallery bullets in AGENTS.md.
6. Extras (section 9): the 404 page and the social share image default.
7. Verify: build with Ruby 3.3. Check /, /research/, /industry/, /projects/, /about/, the 404,
   bottle-flip, alfredo, struct-gp and one project with no cover/stack/links, at 1280px and
   375px. Confirm only token sizes are used (grep the Sass for stray font-size values), check
   every local link and PDF, run git diff --check, then update TODO.md (tick off finished items,
   note follow-ups).
```

## Project and writeup progress tracker

Status describes the current source, not an approval to publish new claims. Update this table when
a page is added, hidden, or materially revised. The slug is the `/projects/<slug>/` URL unless
marked planned.

| Project or writeup | Slug | Status | Next content step |
| --- | --- | --- | --- |
| Human motion prediction | `struct-gp` | Published; text-only | Approved figure or prediction loop; public code link if available |
| Perception-aware safety | `safety-metrics` | Published; text-only | Approved figure or diagram; public code link if available |
| Autonomous Pool-Playing Robot | `pool-robot` | Published; needs evidence | Cover, individual contribution, stronger result or limitation |
| Autonomous Racecar Stack | `alfredo` | Published; needs polish | Individual contribution and main technical challenge |
| Water Bottle Flipping Quadrotor | `bottle-flip` | Published; migrated to new format (first) | Fill `role`/`team`, cover or hero video, comparison or failure cases |
| Granular-Jamming Vise | `revise` | Published; needs polish | Shorter design-iteration and outcome narrative |
| Temporal-Difference Learning for 2048 | `2048-rl` | Published; linked from NCTU research | No open writeup task |
| Rubber Band Turret | `rubber-band-turret` | Published | No open writeup task |
| Minibot | `minibot` | Published | No open writeup task |
| Soccer Robot | `soccer-robot` | Published | No open writeup task |
| Modular Play Instrument for Cognition Research | `toy-for-toddlers` | Published | No open writeup task |
| RF Controllers | `rf-controllers` | Published | No open writeup task |
| ESP Splash | `esp-splash` | Published | No open writeup task |
| K-12 Robotics Outreach | `abes-outreach` | Published | No open writeup task |
| Jansen’s Linkage | `jansens-linkage` | Hidden; no writeup | Approved blurb or restored essay/media before restoring |
| Gaussian Splatting and NeRF | `novel-view-sythesis` | Hidden draft | Task, method, datasets, results, figures |
| Few-Shot Adaptive Infant Gaze Classification | `infant-gaze` | Hidden draft | Context, evaluation, privacy-safe results |
| Lego-Stacking UR5 Robot Arm | `ur5-lego` | Hidden draft | Context, results, approved media |
| Edventures / Edgerton STEM Mentor | `edventures` | Planned; on hold | Owner story and articles/media before drafting |

## Project writeups and evidence to add while sending applications

The two research stories now have text-first pages based on the public papers and the existing CV.
Use only owner-approved figures, results, and public URLs for further additions.

- [ ] **Human motion prediction.** Add an approved figure or 4-second predicted-pose loop and a
      public code link if available. The writeup links the updated ICRA manuscript on arXiv.
- [ ] **Perception-aware safety.** Add an approved figure or diagram and a public code link if
      available. The writeup already includes the verified ICRA 2024 DOI and first-author PDF.
- [ ] **Autonomous Pool-Playing Robot.** The current page covers problem, approach, and result;
      add a simulation screenshot or short loop at `assets/images/pool-robot/cover.webp`,
      Jinger's specific contribution, and a clearer result or limitation if documented.
- [ ] **Autonomous Racecar Stack (Alfredo).** The course outcome, algorithms, and video captions
      are present. Add Jinger's own role and main technical challenge when documented. Add a
      standalone code link only if useful and public.
- [ ] **Water Bottle Flipping Quadrotor.** The method and four-fill-level result are present; add a
      flip diagram or short loop at `assets/images/bottle-flip/cover.webp`, explain
      Jinger's contribution, and give any approved comparison or failure cases.
- [ ] **Granular-Jamming Vise (ReVise).** Jinger's role is now described. Consider a shorter
      reader-facing account of the design iterations and final outcome. The CAD, brochure, and
      direct webcast links were checked.

### Parked drafts — keep hidden until Jinger supplies details

- [ ] `novel-view-sythesis.md`: identify the actual task, Jinger's implementation, datasets,
      comparison, results, and approved figures. The current file is a skeleton with TODO text.
- [ ] `infant-gaze.md`: confirm course/lab and Jinger's role; supply before/after accuracy
      and evaluation details. Use diagrams and aggregate metrics, with no identifiable infant frames.
- [ ] `ur5-lego.md`: confirm course, Jinger's role, success rate or stack height, and
      approved photos/video.
- [ ] **Edventures / Edgerton STEM Mentor:** wait for articles or media links and Jinger's story.
      Notes from the retired jobs collection: scheduled and managed STEM programs; ran an underwater
      ROV workshop and interactive physics classes; advised a student engineering club on project
      design; redesigned a controller for ergonomics and fabrication. Jan 2020 and Jan 2021;
      Barcelona, Ferrara, remote. Draft `_projects/edventures.md` as hidden first. After approval,
      link the Service entry and decide whether it merits a Projects card or stays Service-only.

## Site improvements during applications

- [ ] Add strong, rights-cleared covers to the three featured projects, replacing the blueprint
      tiles. The racecar has a cover; pool and quadrotor do not. The banner photo stays; the
      redesign mirrors its gradient so Jinger stays visible.
- [ ] Add a short teaching writeup for the Spring 2023 2.00B Lab Instructor role if there are
      approved photos and useful detail (Fusion 360 and Illustrator workshops for 70+ students;
      coached a six-member team). Optionally add Rotor 2022's subscale-helicopter CAD/SAS and
      procurement work after public wording is approved.
- [ ] Add verified talks if useful. Revisit a dedicated Publications
      page once the list grows. Keep the old sketch only if it adds value as a footer or 404 detail.
