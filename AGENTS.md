# AGENTS.md — jingerchong.com

## Project overview

This repository is a Jekyll portfolio deployed to GitHub Pages at `jingerchong.com`.
It presents Jinger Chong as a robotics researcher and MIT Ph.D. candidate whose primary
interest is perception and whose thesis concerns intent prediction for autonomous navigation.

Preserve the existing visual identity: deep navy and yellow, the robot-arm logo, navy
header/footer bands, yellow text selection, uppercase letter-spaced headings, and the navy
`h2` underline. This is a content and positioning update, not a redesign.

## Stack and local build

- Jekyll 3.10 through `github-pages ~> 232.0`
- Minima `~> 2.5`
- Plugins: `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag`
- Ruby dependencies are declared in `Gemfile` and locked in `Gemfile.lock`.
- Use Ruby 3.3 with the Windows development tools installed. The GitHub Pages
  dependency set requires Ruby below 4. The README gives verified PowerShell
  commands for this machine. Normal local commands are:

  ```sh
  bundle install
  bundle exec jekyll build
  bundle exec jekyll serve
  ```

- `_config.yml` is not hot-reloaded; restart `jekyll serve` after changing it.
- On Windows, use `bundle exec -- C:\Ruby33-x64\bin\jekyll.bat build` (or `serve`)
  if Bundler cannot locate the bare `jekyll` command.
- Build output is `_site/` and is ignored. Never edit generated files.

## Content model

### Deep-dive projects

- `_posts/` contains output pages at root-level `/:title/` URLs.
- Post front matter uses `area`, not `categories` or singular `category`.
- Valid areas and display order are defined by `categories_order` in `_config.yml`:
  `Research`, `Perception & Autonomy`, `Systems & Hardware`, `Teaching`, `Archive`.
- Use `summary` for card descriptions and `featured: true` only for homepage-worthy work.
- A post cover is conventional: `assets/images/<post-slug>/cover.webp`.
- Cover images are guarded in the post/card templates; do not reintroduce unconditional image
  tags.
- Keep post slugs unique and avoid substring-overlapping slugs because gallery matching depends
  on path substrings.

### Lightweight research records

- `_records/` contains non-output records (`output: false`) shown on `/research/`.
- Records use `type` values such as `publication`, `patent`, `research`, `industry`, and
  `teaching`, plus `order` and `show`.
- `page` optionally points to a related deep-dive post. Confidential records must not expose
  links, covers, proprietary detail, or grids; `_layouts/record.html` enforces this.
- Records are rendered by `_layouts/research.html` and their individual HTML partial is
  `_layouts/record.html`.

### Résumé/about content

- `_schools/`, `_jobs/`, and `_skills/` are non-output collections rendered inline by
  `_layouts/about.html`.
- Their layouts are applied through `defaults` in `_config.yml`.
- Organization links use `page.link` in `_layouts/resume.html`.
- Keep sensitive résumé source files out of the published site. The unredacted résumé and
  supplied headshot source are excluded in `_config.yml` and ignored by git.

## Navigation and templates

- `research.markdown` is the first navigation page, followed by Projects and About.
- Archive is an explicit hardcoded link in `_includes/header.html` because archive pages are a
  collection, not normal `site.pages` entries.
- `/projects/` groups posts by `area`; `/projects/<slug>/` is generated from `_archives/` stubs.
- Archive stubs have explicit `title` values. Do not reconstruct category names with
  `page.slug | capitalize`.
- `/` uses `_layouts/home.html`, including the banner, headshot, identity links, and selected
  records/posts.
- `_data/links.yml` is the single source for social links. The custom social include includes an
  inline Google Scholar icon; do not restore Minima's large hardcoded platform switch.
- `site.email` is the primary MIT email; `site.secondary_email` is the durable personal email.

## Safe change and verification rules

- Read `CLAUDE.md` and this file before changing project structure or content.
- Preserve existing user changes and do not reset or checkout unrelated work.
- Use `apply_patch` for text edits. Do not edit `_site/` by hand.
- Do not publish résumé, phone, address, or proprietary internship information without human
  confirmation.
- Do not invent uncertain résumé metrics, graduation dates, authors, course names, patent
  numbers, or publication status. Track them in `TODO.md` until verified.
- After changes, run `bundle exec jekyll build` with Ruby 3.3, then check:
  required routes, local image references, empty `href` values, placeholders, stale links, and
  `git diff --check` where line-ending noise does not obscure existing files.
- Required route smoke checks include `/`, `/about/`, `/research/`, `/projects/`,
  `/projects/archive/`, every category page, and each kept deep-dive post.

