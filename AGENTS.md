# Agent guide — jingerchong.com

Read this guide with `README.md`, `_config.yml`, and `TODO.md` before editing.
This is Jinger Chong's robotics research portfolio. Preserve its navy
`#08415C`, yellow `#EFCA08`, robot-arm logo, banner, uppercase headings, and
underlined section headings. `_sass/_tokens.scss` defines the colors. Keep the
site compatible with Jekyll 3.10, Minima, and GitHub Pages; ordinary updates
need only Liquid, Markdown, Sass, YAML, and a small amount of vanilla JavaScript.

## Build and codebase map

Use Ruby 3.3 on Windows; Ruby 4 does not work with the locked GitHub Pages
dependencies. From the repository root:

```powershell
$env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
bundle install
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat build
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat serve
```

Restart the server after editing `_config.yml`. `_site/` is generated and
ignored; never edit or commit it.

| Source | Purpose |
| --- | --- |
| `index.html`, `research.md`, `industry.html`, `projects.html`, `about.html` | The five navigation pages; each contains its own markup and front matter. |
| `_projects/*.md` and remaining `.markdown` files | One file per project at `/projects/:slug/`, with metadata and full writeup. The homepage features the first three `featured` projects. |
| `_data/*.yml` | Ordered rows for Industry, publications, education, skills, Service, social links, and news. |
| `_layouts/project.html`, `_layouts/with-banner.html`, `_includes/` | Project detail layout, homepage banner shell, and shared cards, galleries, navigation, and list components. Minima supplies the default layout. |
| `assets/images/<slug>/`, `_sass/`, `assets/main.scss` | Project covers and galleries, shared colors, typography, and responsive styles. |
| `redirects/` | Redirects for old category URLs and `/cv/`. Project files redirect their own former root URLs. |
| `downloads/` | Public PDFs, including the CV path configured once as `cv_url` in `_config.yml`. |
| `examples/project.md` | Excluded, copyable project example. Every `_data` file has a commented row example. |
| `TODO.md` | The only source for editorial and launch TODOs; it is excluded from the published site. |

`_includes/header.html` lists the navigation URLs directly: Research, Industry,
Projects, and About. The former
root writeup URLs redirect to their project pages. The old category URLs
redirect to `/projects/`; `/experience/` redirects to `/industry/`; `/cv/`
redirects to the PDF configured by `cv_url`.

## How to add content

Build and preview the affected route locally at desktop and phone width before
pushing. Open every local link and image, check wording and confidentiality,
and use only verified public facts and URLs. Do not change an existing slug
without preserving its old URL.

- **Project:** Copy `examples/project.md` to `_projects/<slug>.md`. Fill
  `title`, `tier`, `order`, and `summary`; use `year` and `context` for Archive.
  The filename sets `/projects/<slug>/`. `featured` appears on the homepage
  (first three by order) and Projects grid; `normal` appears in the grid;
  `archive` appears in the Archive list; `unlisted` has a page but no card or
  Archive row. Lower `order` values appear earlier within the relevant list.
  Write the full article below the front matter. Optional `stack`, `award`,
  and verified `links` appear on the detail page. Set `redirect_from` only
  for a real older URL. A missing cover is skipped.
- **Gallery:** Place files under `assets/images/<slug>/<descriptive-name>/`
  as `01.webp`, `02.webp`, and so on. Add
  `{% raw %}{% include gallery.html dir="descriptive-name" title="Descriptive title" %}{% endraw %}`
  at the desired point in the project's Markdown body. The include uses the
  project filename slug, reads only that folder, and sorts by filename. The
  optional cover lives at `assets/images/<slug>/cover.webp`.
- **Publication or patent:** Copy the commented entry in
  `_data/publications.yml`. Fill `title`, `authors`, `venue`, and `year`; add
  `status` and a verified `links.url` when available. File order controls
  homepage order. No image is needed.
- **Industry role:** Copy the commented entry in `_data/industry.yml`. Fill
  `org`, `role`, `start`, `end`, `location`, and `bullets`; `link` is optional.
  Rows display in file order. Check that every bullet is approved for public
  use. No template or image edit is needed.
- **Service entry:** Copy the commented entry in `_data/service.yml`. Fill
  `role`, `organization`, visible `date`, and sortable `datetime` (`YYYY-MM`).
  Add `writeup` only for a real page or verified external URL. Rows appear
  newest first on About. No image is needed.
- **News item:** Copy the commented entry in `_data/news.yml`. Fill ISO
  `date` (`YYYY-MM-DD`) and `text`; `url` is optional. Rows appear newest
  first on the homepage. The News section stays hidden while the list is
  empty.

## Accuracy and change workflow

- Preserve authored content and public URLs while reorganizing. Use current
  owner-provided material and verified sources for claims; do not infer
  dates, degrees, metrics, awards, publication status, or media. `TODO.md`
  tracks remaining owner decisions, including GE Vernova public wording,
  Rotor LiDAR compression, and ICRA 2027 policy.
- Keep the private résumé, phone number, street address, proprietary work,
  and unpublished patent material out of public output. The public CV is
  `downloads/jinger-chong-cv.pdf`; verify redaction before replacing it.
- Missing media should disappear cleanly. Record the asset needed in
  `TODO.md`; do not add a broken image, dead `href="#"`, or invented media.
- Keep semantic headings, meaningful alt text, keyboard focus, readable
  contrast, responsive layouts, and reduced-motion behavior for future
  autoplay media.
- Inspect `git status` before editing and preserve unrelated changes. After
  editing, build with Ruby 3.3; check `/`, `/research/`, `/industry/`,
  `/projects/`, `/about/`, a project page, a former root URL, and the
  redirects. Check local assets and run `git diff --check`.

`README.md` contains the quick local setup. This is the sole agent-specific
guide in the repository.
