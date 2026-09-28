# TODO — human input and verification

Development-only TODOs are rendered at [/todo/](/todo/). Production hides inline TODO badges.

## Projects page restructure (approved by Jinger, 2026-09-27; updated after review)

Decisions were final for the implementation. Ask Jinger before changing the agreed structure.
Rule: **every item appears in exactly one list** (Projects grid, Archive, or
About → Service). A Service entry may link to a writeup page; that is not a repeat.

### Target state

| List | Items |
|---|---|
| Projects grid (4) | Pool-Playing Robot · Autonomous Racecar Stack (`alfredo`) · Water Bottle Flipping Quadrotor · Granular-Jamming Vise (`revise`) |
| Archive (6) | Minibot · TD Learning for 2048 · Modular Play Instrument · Rubber Band Turret · Soccer Robot · Jansen's Linkage (no link) |
| About → Service | existing entries (incl. RF Controllers via 16.632, ABES, ESP Splash, Edgerton Mentor) + SJCS Robocup linked to its restored writeup |
| Removed | Home Upgrades · Iron Man · Flashlight · Segway Robot |
| On hold | Edventures page: draft only, not listed anywhere (see step 6) |

### Steps

1. **Replace the tiers with three values** in `_projects/*.markdown` front matter:
   - `tier: featured`: shown on the homepage **and** as a card in the Projects grid.
   - `tier: normal`: card in the Projects grid only.
   - `tier: archive`: no card anywhere. Listed in Archive, unless the project
     also has `in_service: true`, in which case it's listed only via its About → Service entry
     (no repeats).
   - Remove the old `selected` / `more` values completely; nothing should reference them.
   - `_layouts/projects.html`: grid combines `featured` and `normal` entries,
     then sorts by `order` (the locked Liquid version rejects `or` in `where_exp`).
   - `_layouts/home.html`: change `where: 'tier', 'selected' | sort: 'title'` to
     `where: 'tier', 'featured' | sort: 'order'` (keep `limit:3`).
1b. **Remove tags, filters, and the tag line on cards.**
   - Delete the `tags:` key from **every** `_projects/*.markdown` file (Jinger: the tags
     aren't accurate). Leave `stack:` as is.
   - `_layouts/projects.html`: delete the `.project-filters` toolbar, the
     `project_tags` Liquid loop, the "Showing N projects" status line, the
     `project-filters.js` script tag, and the `data-project-browser` / `data-project-grid` hooks.
   - `_includes/project-grid-card.html`: remove the tag line (`.project-card-tags`) and the
     `data-project-card` / `data-tags` attributes. Show the short description as
     `summary | default: blurb` so every card has one (`revise` has only a `blurb`).
   - Delete `assets/js/project-filters.js` and the unused `.project-filter*` /
     `.project-card-tags` rules in `_sass/layout.scss` (recoverable from git).
   - Grep the repo (excluding `_site`) for `tags`, `project-filter`, `selected`, `more`
     (tier context) to confirm nothing still depends on them.
2. **Retier existing projects**

   | tier | projects |
   |---|---|
   | featured (order 1–3) | `pool-playing-robot` (1), `alfredo` (2), `water-bottle-quadrotor` (3) |
   | normal | `revise` (order 4) |
   | archive | `minibot`, `rl-in-2048`, `toy-for-toddlers`, `rubber-band-turret`, `soccer-robot`, `jansens-linkage` |
   | archive + `in_service: true` | `rf-controllers`, `abes-outreach`, `esp-splash` |

3. **Add an "Archive" section** below the grid in `_layouts/projects.html`, built from
   `tier == 'archive'` projects **without** `in_service: true`.
   - Reuse the Service markup and classes from `_includes/service.html`
     (`.service-list`, `.service-entry`, `.service-title-row`, `.service-role`,
     `.service-organization`, `time`). Add no new CSS unless it's needed.
   - Each row reads `Title, *context*`, with the year right-aligned in grey. The
     whole title-and-context line links to `writeup_url` (fall back to `item.url`), and is plain text when the
     project has no writeup (`jansens-linkage`). Always expanded, not collapsible.
   - Add a `context:` field to each archive project, and sort newest first by an
     explicit `archive_order` (lower = higher):

     | archive_order | slug | context | year shown |
     |---|---|---|---|
     | 1 | minibot | 16.632 Intro to Autonomous Machines | 2021 |
     | 2 | rl-in-2048 | NCTU Computer Graphics and Intelligence Lab | 2020 |
     | 3 | toy-for-toddlers | Early Childhood Cognition Lab | 2019–2020 |
     | 4 | rubber-band-turret | Freshman engineering seminar | 2019 |
     | 5 | soccer-robot | Discover Mechanical Engineering pre-orientation | 2019 |
     | 6 | jansens-linkage | IB Extended Essay | 2018–2019 |

   - `jansens-linkage`: set `year: 2018–2019`, `term: 2018–2019`, blurb "IB Extended
     Essay on the kinematics of Jansen's linkage." (confirm wording with Jinger),
     remove its `todo:` entry, and add `sitemap: false`. Its `/projects/jansens-linkage/`
     page still builds, but nothing links to it and it isn't indexed.
4. **Remove projects**: `home-upgrades`, `iron-man`, `flashlight`, `segway-robot`.
   Delete for each: `_projects/<slug>.markdown`, the matching `_posts/*-<slug>.markdown`,
   `_grids/<slug>/`, and `assets/images/<slug>/`. First grep the repo (excluding
   `_site`) for each slug and remove any remaining references; none were found on
   2026-09-27. Everything stays recoverable from git history. Do **not** add redirects
   for these four; Jinger wants their old URLs to 404.
5. **Service updates** (`_data/service.yml`)
   - SJCS Robocup is listed in Service and links to its restored root-level
     writeup from `main`. Its existing `_grids/sjcs-robocup/` and
     `assets/images/sjcs-robocup/` supply the gallery.
   - Fix the writeup links: RF Controllers, ESP Splash, and ABES currently link to
     `/projects/<slug>/`, which is the scaffold page with TODO placeholders. Point each
     to its real post writeup instead: `/rf-controllers/`, `/esp-splash/`, `/abes-outreach/`
     (the `writeup_url` values).
6. **Edventures (Edgerton Center STEM Mentor): hold**. Do not add a card or a live page yet.
   Jinger will provide articles/media links and the story. Then draft
   `_projects/edventures.markdown` with `published: false` and review it with her.
   Once approved, point the Edgerton Service entry's `writeup` at it. Whether it
   becomes a grid card is decided after the draft (a card if the story centers on
   her design work, such as the ROV workshop or controller redesign; Service-only
   if it's mostly mentoring/logistics). Source material so far: `_jobs/edventures-stem.markdown`.
7. **Verify**
   - `bundle exec jekyll build` completes with no errors (see `AGENTS.md` for the
     Ruby 3.3 commands).
   - `/projects/`: 4 cards, each with a short description and no tags; no filter bar,
     no count line, no console errors; Archive lists 6 rows in the order above; Jansen
     row has no link; all other rows open a real writeup.
   - Homepage shows Pool Robot, Racecar, Quadrotor, in that order.
   - No project page, card, or historic writeup displays category badges.
   - `/about/` Service: RF/Splash/ABES/SJCS Robocup links resolve to posts.
   - Removed slugs appear nowhere in `_site/`.
   - Check at phone width (~375px): Archive rows stack like Service.
   - The `_archives/` category pages (`/projects/archive/`, etc.) still list the old
     `_posts`. Don't redesign them in this task; note any now-empty or broken ones
     under Blockers so they're handled with the redirect work.

### Later (not in this task)

- Jinger plans to add stronger projects to the grid soon. A 4-card grid leaves one
  orphan card in the 3-column layout, which is acceptable for now.
- Edventures writeup (step 6).

## Blockers

- [ ] Add and verify CI: production build, HTML/link checking, blocker-TODO failure, and failure
      when a production-nav page references `assets/placeholder.svg`.
- [ ] Add `jekyll-redirect-from` redirects for every legacy project/tag URL once the final
      collection URLs are approved; the legacy root pages currently remain as compatibility pages.

## Content

- [ ] Write the four-sentence home research statement using problem class → gap → personal angle
      → trajectory. Do not auto-generate it from résumé bullets.
- [ ] Tighten the three featured-project card headlines.
- [ ] Add sourced figures/media at the paths specified by the TODO badges for the research threads
      and featured projects.
- [ ] Add the ICRA 2024 PDF path, DOI, and code link.
- [ ] Add talks and service entries if applicable.
- [ ] Restore the full Jansen’s Linkage writeup/media if that page should be public.
- [ ] Confirm the Jansen’s Linkage blurb wording before making that page public.
- [ ] Expand the restored SJCS Robocup writeup with owner-provided details and review its gallery selection.
- [ ] Add any remaining project-specific “What I’d do differently” retrospectives.

## Verify

- [ ] Confirm ICRA 2027 anonymity and preprint policy before publishing a manuscript or preprint.
- [ ] Confirm GE Vernova’s public wording, metrics, and invention-disclosure language.
- [ ] Confirm the 100:1 Rotor LiDAR compression ratio and final public wording.
- [ ] Verify all external publication, patent, organization, and social URLs before launch.
- [ ] Run a browser-level accessibility and responsive review; confirm reduced-motion behavior for
      any future autoplay media.

## Optional

- [ ] Decide whether to use a research-specific banner instead of the existing shop photograph.
- [ ] Retain the old sketch as a footer or 404 easter egg if desired.
- [ ] Add the dedicated Publications page after there is more published output.
