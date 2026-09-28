# TODO — human input and verification

This is the single place to track site content and launch work.

## Done

- Projects page restructure (featured / normal / archive tiers, Archive list, Service links),
  the first codebase cleanup pass, and the content architecture refactor are finished.
  Earlier briefs and the cleanup inventory remain in git history (`git log -p -- TODO.md CLEANUP.md`).

## On hold: Edventures (Edgerton Center STEM Mentor)

Wait until Jinger provides articles/media links and the story. Then draft
`_projects/edventures.md` with `published: false` and review it with her. Once it's approved,
point the Edgerton entry in `_data/service.yml` to it. Decide after the draft whether it gets a
Projects card (if the story is about her design work: the ROV workshop, the controller redesign)
or stays Service-only (if it's mostly mentoring/logistics). Source notes so far, copied here
because `_jobs/` is being deleted: scheduled and managed STEM programs; ran an underwater ROV
workshop and interactive physics classes; advised a student-led engineering club on project
design; redesigned a controller to improve ergonomics and simplify fabrication. Jan 2020 and
Jan 2021; Barcelona, Ferrara, remote.

## Content architecture refactor (completed, 2026-09-28)

**Status: implemented and verified.** Decisions 1–4 are Jinger's. Decisions 5–6 used the
recommended option. The 37 baseline HTML routes still render or redirect, except for the
intentionally removed `/todo/`; `/experience/` now redirects and SJCS Robocup has a project
page. All 11 writeups retain their image order. The six content recipes were tested with
temporary entries and the site built successfully. GitHub Pages still generates an empty
`feed.xml` through its bundled `jekyll-feed` plugin, though this site no longer declares the
plugin or advertises a feed link.

### What's wrong now

1. **Every project is split across two files.** `_projects/<slug>` has the card data and
   builds a thin `/projects/<slug>/` page, while `_posts/<date>-<slug>` holds the real writeup
   at `/<slug>/`. For 9 of the 13 projects, the card skips its own project page and links to
   the post (`writeup_url`), so each one has two live URLs and one of them is a placeholder
   page. Title, summary, date and course are typed twice (and `blurb` is usually the same as
   `summary`). SJCS Robocup exists only as a post.
2. **Service-only projects are stubs.** `rf-controllers`, `esp-splash` and `abes-outreach`
   (`in_service: true`) don't show up in any list, but each still builds an empty
   `/projects/<slug>/` page. Their real links are in `_data/service.yml`.
3. **Galleries take three places to set up.** `_grids/` has 22 files that mostly hold only a
   section heading. Adding a gallery means editing the post, adding
   `_grids/<slug>/grid-N.markdown`, and adding `assets/images/<slug>/grid-N/`. The template
   matches them by a partial path match, which can pick up the wrong folder. Galleries always
   show after the writeup, so text can't sit next to its photos. Images aren't zero-padded or
   consistently named (`rf-1-10` sorts before `rf-1-2`; `2048 (2).webp`, `turret (12).webp`).
4. **`_archives/` category pages are orphaned.** There are 5 pages at `/projects/<area>/`.
   Nothing links to them. They use the same `/projects/` URLs as the project pages (so a
   project slug like `research` would clash), and they miss 4 posts that use
   `category`/`categories` instead of `area`. The Projects page's Archive list replaced them.
5. **`_jobs/` (15 files) and `_records/` (10 files) aren't used at all.** No template reads
   `site.jobs` or `site.records`, and neither collection builds pages. The only unique content
   is the Edventures notes (copied above) and `_records/rotor-lidar-compression`, which says
   "up to 50:1" while Industry says 100:1 (see Verify).
6. **`_research/` (3 files) is only read by `/todo/`.** `/research/` is plain text in
   `research.markdown`.
7. **`_experience/` is a list stored as a collection.** `mit-mrl` and `intro-robotics` are
   hidden (`show_industry: false`); Jinger wants them removed, and the Intro Robotics TA role
   is already in Service. The other 4 fill a single list, which is what `_data/` is for.
   The `headline`, `featured` and `confidential` fields are never displayed.
8. **Smaller duplicates and dead config:**
   - The CV link lives in four places: `cv_url`, the CV entry in `_data/links.yml`, the
     homepage text, and a `/cv/` page that isn't in the nav.
   - `social_links` in `_config.yml` isn't used; `_data/links.yml` is the live list.
   - `_sass/colors.scss` Sass variables repeat the CSS variables in `_sass/_tokens.scss`.
   - There are two project card includes: `card.html` (homepage) and `project-grid-card.html`
     (Projects page).
   - TODOs are tracked in three places: `TODO.md`, front-matter `todo:` lists shown on
     `/todo/`, and a hard-coded "What I'd do differently" TODO in `_layouts/project.html`.
     Some items appear in more than one of them (e.g. GE Vernova wording).
   - `redirect_from: /experience/` in `industry.markdown` does nothing, because
     `jekyll-redirect-from` isn't installed.
   - `jekyll-feed` only covers `_posts`, so the feed will be empty once the posts are merged.
   - Leftovers in `_config.yml`: boilerplate comments, `permalink: :title/`,
     `show_excerpts`, `categories_order`, `images`, the `jobs`/`records`/`grids`/`archives`
     collections, and `exclude` entries for files that no longer exist.
   - Image paths are inconsistent: covers are at `assets/images/<slug>/cover.webp`, but
     project TODOs ask for `assets/media/<slug>.webp`.
   - `about`, `experience`, `projects` and `research` layouts are each used by exactly one
     page, so each page is split between an empty root `.markdown` file and a layout.

### Rule for the new structure

- **Has its own page** → one file in a collection, with the metadata and the full text in the
  same file.
- **Is a row in a list** → one entry in a `_data/*.yml` file.
- **Is a nav page** → one root file that contains its own markup.
- Each fact is typed once. Filenames set slugs, and folder conventions set image paths, so
  those don't need front-matter fields.

### Target layout

```
index.html        Home: bio, Highlights (featured projects), publications, news
research.md       Research (prose)
industry.html     Industry     ← _data/industry.yml
projects.html     Projects grid + Archive   ← _projects/
about.html        About        ← _data/education.yml, skills.yml, service.yml
404.html
_projects/<slug>.md      one file per project: card fields + full writeup
_data/            publications, industry, education, skills, service, links, news (.yml)
_layouts/         project.html, plus with-banner.html if the home banner still needs it
_includes/        project-card, gallery, pub-item, industry-item, service, education,
                  head, header, footer, social, banner
_sass/            _tokens.scss (only color source), fonts.scss, layout.scss
assets/images/<slug>/cover.webp  and  assets/images/<slug>/<gallery>/01.webp, 02.webp, …
downloads/        public PDFs
examples/project.md   copy-me template (each _data file keeps its own example in a comment)
```

To be removed: `_posts/`, `_grids/`, `_archives/`, `_jobs/`, `_records/`, `_research/`,
`_experience/`, `_layouts/{post,category,about,experience,projects,research,home}.html`,
`_includes/{card,post-card,project-grid-card}.html`, `_sass/colors.scss`, `cv.markdown`,
`todo.markdown`, `_layouts/todo.html` and `_includes/todo.html`. `CLEANUP.md`
goes too, once this is done.

### One project schema

```yaml
---
title: Granular-Jamming Vise
tier: normal            # featured (home + grid) | normal (grid) | archive (Archive list) | unlisted (page only, e.g. linked from Service)
order: 4                # position within its own list; lower comes first
year: 2021              # text is fine: "2018–2019"
context: 2.009 Product Engineering Processes   # course, lab, or program
summary: A pneumatically actuated vise that uses granular jamming to grip irregular workpieces.
stack: [SolidWorks, Arduino]    # optional
award: Outstanding Project      # optional
links: {video: …, code: …, paper: …}   # optional; missing keys show nothing, never "#"
redirect_from: [/revise/]       # only if the project had an older URL
---
Writeup in Markdown. Galleries go wherever they belong in the text:
{% include gallery.html dir="initial-cad" title="Initial CAD photos and animations" %}
```

- The slug comes from the filename, and the cover is `assets/images/<slug>/cover.webp` if
  that file exists. Remove `slug`, `writeup_url`, `blurb`, `term`, `archive_order`,
  `has_writeup`, `in_service`, `cover` and `problem`/`approach`/`results`.
- `pool-playing-robot` and `water-bottle-quadrotor` keep their text: their
  problem/approach/results become `## Problem` / `## Approach` / `## Results` in the body.
- An Archive row links to its page only if the page has body text. A project with no text
  (Jansen's Linkage) shows as plain text, and its page keeps `sitemap: false`.
- `project.html` shows: title, then context · year · award, the cover, the summary, the body,
  stack chips and links. No hard-coded TODO headings.
- `gallery.html` lists the images in `assets/images/<page slug>/<dir>/` in filename order.

### Decisions

1. **Project URLs (Jinger): `/projects/<slug>/` for every project.** Old `/<slug>/` post URLs
   redirect with `jekyll-redirect-from`. The same plugin redirects the 5 category URLs to
   `/projects/` and `/experience/` to `/industry/`.
2. **TODO tracking (Jinger): `TODO.md` only.** Remove the front-matter `todo:` fields (move any
   item that isn't already in this file), the inline badges (`_includes/todo.html`), the
   `/todo/` page (`todo.markdown`, `_layouts/todo.html`), and the TODO fields in `examples/`
   and the `_data` comments.
3. **`/cv/` page (Jinger): delete it and redirect `/cv/` to the PDF.** `cv_url` is the only
   place the path is stored; `_data/links.yml` and the homepage read it rather than repeating it.
4. **MIT MRL bullets (Jinger): delete them with `_experience/mit-mrl`.** They stay in git
   history. Don't move them anywhere else.
5. **RSS feed (default): remove `jekyll-feed`** and the `feed_meta` tag in `_includes/head.html`.
6. **Galleries (default):** when moving each gallery, rename its folder from `grid-N` to a
   short descriptive name and zero-pad the images (`01.webp`, `02.webp`, …). Keep the order
   the live page shows today.

### Steps (commit after each; the build must pass after every step)

0. **Baseline.** Build (Ruby 3.3 commands are in `AGENTS.md`). Save the list of `_site/`
   routes and, for every writeup, its image count and gallery order. Take screenshots of each
   nav page at desktop width and at ~375px.
1. **Delete unused files (no URL changes).** Delete `_jobs/`, `_records/`, `_research/`
   (move its 3 figure TODOs into `TODO.md` → Content), and `_experience/mit-mrl` and
   `_experience/intro-robotics`. Remove the `_config.yml` leftovers and
   `social_links`. Fold `colors.scss` into `_tokens.scss` without changing any rendered color.
2. **Add redirects.** Add `jekyll-redirect-from` to the Gemfile and `plugins`. Check that
   `/experience/` now redirects.
3. **Merge posts into projects, one slug per commit.** Move the post body into the project
   file. Replace its `_grids/` files with `gallery.html` includes and put the heading/text in
   the body. Apply the new schema and add `redirect_from`. Then delete the post and its grids.
   Create `_projects/sjcs-robocup.md` (`unlisted`). Point the `_data/service.yml` writeup
   links to the new URLs. Afterwards, compare each page's image count and order with step 0.
4. **Templates.** Write the new `project.html`, merge the two cards into `project-card.html`
   (keep the homepage and Projects-page looks with a modifier class if they differ), and
   rebuild the Projects page (grid = featured + normal; Archive = archive, by `order`) and
   the homepage Highlights (featured, by `order`, limit 3).
5. **Industry.** Move the 4 remaining roles to `_data/industry.yml` in display order (no
   `order` or `show_industry` fields). Delete `_experience/` and its `_config.yml` entries.
6. **Remove the old category pages.** Delete `_archives/`, `post.html`, `category.html` and
   `post-card.html`, and redirect the 5 category URLs to `/projects/`. Apply decisions 3 and 5.
7. **One file per nav page.** Move each single-use layout into its root page (`about.html`,
   `industry.html`, `projects.html`, `index.html`). Apply decision 2.
8. **Docs.** Rewrite the `AGENTS.md` codebase map to match the target layout. Rewrite
   "How to add content" with a short recipe for each of: a project, a gallery inside a
   project, a publication, an industry role, a Service entry, and a news item. Each recipe
   says which file to edit or copy, the required fields, where images go, and how to control
   placement and order. Update `examples/project.md` and the example comment at the top of
   each `_data` file. Delete `CLEANUP.md`, and link the recipes from `README.md`.

### Verify

- Every route from step 0 either still renders or redirects to the right new page. Check this
  with a script, and list any exceptions.
- Every writeup has the same images, in the intended order.
- `/projects/` shows the same 4 cards and 6 Archive rows. The homepage shows the same 3
  Highlights. Every About → Service link opens a real writeup.
- Nav pages match the step 0 screenshots, except for intended changes, at desktop width and
  at 375px. No console errors.
- Searching the repo (excluding `_site`) finds no `site.posts`, `site.grids`,
  `site.experience`, `site.jobs`, `site.records`, `site.research`, `writeup_url`, `blurb`,
  `in_service`, `has_writeup` or `archive_order`.
- The build shows no new warnings. Run `git diff --check`.
- Follow each "How to add content" recipe once with a throwaway entry, confirm it appears in
  the right place, then delete it.

## Blockers

- [ ] Add and verify CI: production build, HTML/link checking, blocker-TODO failure, and failure
      when a production-nav page references `assets/placeholder.svg`.
- [x] Redirect legacy project, category, and `/experience/` URLs to their new pages.

## Content

- [ ] Write the four-sentence home research statement using problem class → gap → personal angle
      → trajectory. Do not auto-generate it from résumé bullets.
- [ ] Tighten the three featured-project card headlines.
- [ ] Add sourced figures/media at the paths specified by the TODO badges for the research threads
      and featured projects.
- [ ] Add a 4-second predicted-pose loop for human motion prediction, at
      `assets/images/human-motion-prediction/cover.webp` (16:9 target).
- [ ] Add a sourced figure for perception-aware safety metrics, at
      `assets/images/perception-safety/cover.webp` (16:9 target).
- [ ] Add a verified video URL for the Alfredo project before showing a video link.
- [ ] Add a project figure or 4-second simulation loop for the pool-playing robot at
      `assets/images/pool-playing-robot/cover.webp` (16:9 target).
- [ ] Add a 4-second flip loop or diagram for the water-bottle quadrotor at
      `assets/images/water-bottle-quadrotor/cover.webp` (16:9 target).
- [ ] Add the ICRA 2024 PDF path, DOI, and code link.
- [ ] Add talks and service entries if applicable.
- [ ] Restore the full Jansen’s Linkage writeup/media if that page should be public.
- [ ] Confirm the Jansen’s Linkage blurb wording before making that page public.
- [ ] Expand the restored SJCS Robocup writeup with owner-provided details and review its gallery selection.
- [ ] Add any remaining project-specific “What I’d do differently” retrospectives.

## Verify

- [ ] Confirm ICRA 2027 anonymity and preprint policy before publishing a manuscript or preprint.
- [ ] Confirm GE Vernova’s public wording, metrics, and invention-disclosure language.
- [ ] Confirm the 100:1 Rotor LiDAR compression ratio and final public wording (an old `_records` note said "up to 50:1").
- [ ] Verify all external publication, patent, organization, and social URLs before launch.
- [ ] Run a browser-level accessibility and responsive review; confirm reduced-motion behavior for
      any future autoplay media.

## Optional

- [ ] Decide whether to use a research-specific banner instead of the existing shop photograph.
- [ ] Retain the old sketch as a footer or 404 easter egg if desired.
- [ ] Add the dedicated Publications page after there is more published output.
