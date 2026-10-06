# Agent guide — jingerchong.com

Read this guide with `README.md`, `_config.yml`, and `TODO.md` before editing.
This is Jinger Chong's robotics research portfolio. Preserve its navy
`#08415C`, yellow `#EFCA08`, robot-arm logo, banner, uppercase headings, and
mono section headings with a hairline rule. `_sass/_tokens.scss` defines the colors. Keep the
site compatible with Jekyll 3.10, Minima, and GitHub Pages; ordinary updates
need only Liquid, Markdown, Sass, YAML, and a small amount of vanilla JavaScript.

## Build and codebase map

Use Ruby 3.3 on Windows; Ruby 4 does not work with the locked GitHub Pages
dependencies. From the repository root:

```powershell
$env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
bundle install
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat build
python scripts/check_site.py _site
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat serve
```

Restart the server after editing `_config.yml`. `_site/` is generated and
ignored; never edit or commit it.

| Source | Purpose |
| --- | --- |
| `index.html`, `research.html`, `industry.html`, `projects.html`, `about.html` | The five navigation pages; each contains its own markup and front matter. `about.html` renders Education, Skills, Teaching, then Service from `_data/`. |
| `_projects/*.markdown`, `_projects/*.md` | Fourteen published project files (plus hidden `published: false` drafts), one per `/projects/:slug/` page, with metadata and any available writeup. The homepage features the first three `featured` projects. New projects may use `.md`. |
| `_data/*.yml` | Eight current data files: education, industry, links, publications, research, service, skills, and teaching. |
| `_layouts/default.html`, `_layouts/project.html`, `_layouts/with-banner.html`, `_includes/` | Shared page shell, project detail layout, homepage banner shell, and shared cards, galleries, navigation, and list components. Minima remains the GitHub Pages theme. |
| `assets/images/<slug>/`, `_sass/`, `assets/main.scss` | Project covers and galleries, shared colors, typography, and responsive styles. |
| `assets/citations.js`, `assets/media.js` | Clipboard citations and reduced-motion-aware local video playback. |
| `scripts/check_site.py`, `.github/workflows/site-check.yml` | Local and CI checks for generated pages, links, markup, and excluded development files. |
| `redirects/` and `industry.html` | Redirects for `/projects/archive/`, `/cv/`, and `/experience/`. Project pages have no legacy URL redirects. |
| `downloads/` | Public PDFs, including the CV path configured once as `cv_url` in `_config.yml`. |
| `examples/` | Excluded authoring guide, copyable project example, and historical design references. Every `_data` file has a commented row example. |
| `TODO.md` | The only source for editorial and launch TODOs; it is excluded from the published site. |

`_includes/header.html` generates the four navigation URLs from their labels.
Former root writeup and category URLs are retired. The retained redirects are
`/projects/archive/` to `/projects/`, `/experience/` to `/industry/`, and `/cv/`
to the PDF configured by `cv_url`.

## Current layout and design system

- Home: banner, one bio paragraph with a View my CV link, Publications, Projects
  (three featured rows), Experience with All experience link, then Contact.
  Internship availability appears only in the banner, with no separate Now paragraph.
  `tagline`, `status`, `contact_email`, and `cv_url` come from `_config.yml`.
- Navigation stays Research, Industry, Projects, About. Industry is the route/nav
  name; Experience is the heading on Home and Industry.
- Projects: FEATURED combines `featured` and `normal`, ordered together by `order`;
  MORE lists `archive`, with title/context on the left and dates aligned at the right
  edge on desktop and phones. Changing the heading does not change tier behavior.
- About: OFF THE CLOCK with a floated square headshot, Education, Skills,
  Teaching, Service. Research uses NOW, WRITEUPS (cards for `research: true` projects), and BEFORE.
- Project detail: back link, context/year kicker, title, optional metadata and
  stack chips, links, optional cover/video, TL;DR, article, previous/next.
  Previous/next follows the FEATURED grid and uses `rel="prev"` / `rel="next"`.
- Contact: clickable email, Scholar/GitHub/LinkedIn/CV links and a generated date.
- `_sass/_tokens.scss`: IBM Plex Sans/Mono, seven type sizes, four spacing steps,
  shared content/article widths and left column. Shared styles live in
  `fonts.scss` and `layout.scss`; section rules use one mixin. Keep keyboard focus
  and reduced-motion behavior. Test the banner and navigation down to 320px.
- `project-card.html` is the grid card; `project-row.html` is the compact Home row.
  Both reuse `project-image.html` and `kicker.html`.
- `examples/design/` contains historical visual references, not current authoring
  instructions. Current source and this guide take precedence over their old labels.
- `TODO.md` contains only future actions and decisions not to implement. Remove
  completed work rather than accumulating implementation history.
- Keep development files out of `_site`: README, guides, examples, scripts,
  dependency manifests, and local `Claude outputs/` are excluded. Local design
  exports are ignored by Git; preserve them rather than bundling them into commits.

## How to add content

Build and preview the affected route locally at desktop and phone width before
pushing. Open every local link and image, check wording and confidentiality,
and use only verified public facts and URLs. Project slug changes retire the
old URL; do not create a redirect for it.

- **Project:** Copy `examples/project.md` to `_projects/<slug>.md`. Fill
  `title`, `tier`, `order`, and `summary`; use `year` and `context` for the More list.
  The filename sets `/projects/<slug>/`. `featured` appears on the homepage
  (first three by order) and Projects FEATURED grid; `normal` also appears in that grid;
  `archive` appears in the list headed MORE on `/projects/`; `unlisted` has a page but no card or
  More row. Lower `order` values appear earlier within the relevant list.
  Write the full article below the front matter; use descriptive `##` headings
  only for longer articles. Optional `tldr` (2–3 sentences, falling back to
  `summary`), `role`, `team`, `award`, and `stack` appear on the detail page;
  optional `award_url` links the award text to a verified source. An `award` also
  appears as a yellow badge beside the kicker on cards, Home rows, and the project page.
  `research: true` also shows the card under WRITEUPS on `/research/` (it stays in the
  Projects grid as well).
  Verified `links` appear at the top in `paper`, `arxiv`, `code`, `video`, `report`,
  `slides`, `poster`, `website` order, then other keys. A `paper` PDF is labeled
  PDF (other paper URLs: Paper); other PDF targets get a `(PDF)` suffix.
  Empty and `#` targets are skipped. Keep public PDF writeups in `downloads/<slug>/`.
  A project without a cover shows no image in listings and no detail-page hero.
- **Writeup format:** Follow `struct-gp`: no `##`/`###` section headers; a short problem
  paragraph, method and individual contribution, results with numbers, then tradeoffs or
  next steps, with `figure.html` figures between paragraphs. Write `tldr` and `summary` in an
  impact-focused, mostly impersonal voice; first person belongs in the prose. Course
  teammates stay unnamed. Use at most one gallery per page, with 2 or 4 curated images.
- **Gallery:** Place files under `assets/images/<slug>/<descriptive-name>/`
  as `01.webp`, `02.webp`, and so on. Add
  `{% include gallery.html dir="descriptive-name" title="Descriptive title" %}`
  at the desired point in the project's Markdown body. The include uses the
  project filename slug and sorts matching files by path. Keep only image files
  in gallery folders (including any subfolders). The
  optional cover lives at `assets/images/<slug>/cover.webp` (16:10 in listings,
  16:9 on the page). Set `image` to its path for social sharing; the default is
  the site banner. Set `hero_video` to a YouTube ID to replace the page hero.
  Use `youtube.html` with `id`, `title`, and optional `caption` for embeds;
  use `video.html` with `mp4` and/or `webm`, `title`, optional `poster` and
  `caption` for local loops. Local loops have controls and respect reduced motion.
  Use `figure.html` with `src`, `alt`, and optional `caption` for one captioned image or plot.
- **Publication or patent:** Copy the commented entry in
  `_data/publications.yml`. Fill `title`, `authors`, `venue`, and `year`; add
  `status` and verified `links.paper` / `links.arxiv` when available. `bibtex: |`
  stores the exact citation copied by CITE (`assets/citations.js`), with accessible
  success/failure feedback; do not use a dropdown. Patents use `type: patent` or
  `links.google_patents` and may also have CITE. Set `links.writeup` to a project URL
  to make the title and thumbnail open that writeup (otherwise they open `paper`) and to show
  the same CITE button on that project page; `writeup` never appears in the link row. File
  order controls homepage order. The kicker reads `VENUE · YEAR` (`Patent · YEAR`), and any
  `status` other than Published appears as an outlined chip beside it, mirroring project
  rows (`CONTEXT · YEAR` plus an award chip). Optional `image` adds a 16:10 thumbnail in place
  of the left-column label, which then moves above the title.
- **Industry role:** Copy the commented entry in `_data/industry.yml`. Fill
  `org`, `role`, `start`, `end`, `location`, and `bullets`; `link` is optional.
  The homepage Experience list shows one line per role; `home: false` hides a
  row there, and `home_role`/`home_date` override its label and date.
  Rows display in file order. Check that every bullet is approved for public
  use. No template or image edit is needed.
- **Research entry:** Copy the commented entry in `_data/research.yml` (same
  fields as Industry). Set `current: true` for a role under NOW on `/research/`;
  other rows appear under BEFORE. File order controls order within each group.
- **Draft project:** Add `published: false` to the front matter. Jekyll skips
  it entirely (no page, card, or sitemap entry) until the line is removed.
- **Teaching entry:** Copy the commented entry in `_data/teaching.yml`. Fill
  `role`, `organization`, academic-term `date` (Spring, Fall, or IAP), and
  sortable `datetime` (`YYYY-MM`, using the latest term for combined dates).
  Rows appear newest first on About. Add `writeup` only for a real page or
  verified external URL. No image is needed.
- **Service entry:** Copy the commented entry in `_data/service.yml`. Fill
  `role`, `organization`, year-only `date`, sortable `datetime` (`YYYY-MM`),
  and `group` (`reviewing`, `outreach`, or `community`). Omit the visible date
  when the organization name already dates the role. If the sort key's year
  differs from the visible year, set `time_datetime` to that year. Entries
  appear newest first across all groups. Add `writeup` only for a real page
  or verified external URL. No image is needed.

## Accuracy and change workflow

- Preserve authored content while reorganizing. Use current
  owner-provided material and verified sources for claims; do not infer
  dates, degrees, metrics, awards, publication status, or media. `TODO.md`
  tracks open work.
- Keep the private résumé, phone number, street address, proprietary work,
  and unpublished patent material out of public output. The public CV is
  `downloads/jinger-chong-cv.pdf`; verify redaction before replacing it.
- Course-project pages never name teammates: write "my teammate" and use
  `team: Team of N`. Publication co-authors may be named. Course report PDFs
  stay in `private/reports/<slug>/` (Git-ignored and excluded from the build);
  put their key points and figures in the writeup instead of linking the PDF.
- Jinger approved the remaining K–12 outreach photos for public display.
- Missing media should disappear cleanly. Record the asset needed in
  `TODO.md`; do not add a broken image, dead `href="#"`, or invented media.
- Keep semantic headings, meaningful alt text, keyboard focus, readable
  contrast, responsive layouts, and reduced-motion behavior for future
  autoplay media.
- Inspect `git status` before editing and preserve unrelated changes. After
  editing, build with Ruby 3.3; check `/`, `/research/`, `/industry/`,
  `/projects/`, `/about/`, a project page, retired project URLs, and the
  redirects. Check local assets and run `git diff --check`.

`README.md` contains the quick local setup. This is the sole agent-specific
guide in the repository.
