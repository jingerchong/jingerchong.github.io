# Codebase cleanup inventory

Phase 1 baseline and review list. No files were deleted or content sources merged. `TODO.md` was already modified when this inventory began; those edits were preserved. The baseline is the successful Ruby 3.3 Jekyll build in the current working tree. The build showed the existing Faraday retry middleware notice and no errors.

## Resolution after owner review

Jinger authorized removal of files confirmed duplicate or obsolete. The initial
inventory below remains a record of the pre-cleanup state.

| Decision | Paths | Reason |
| --- | --- | --- |
| DELETE | `Gemfile.bak`, `Gemfile.lock.bak`, `_includes/card-compact.html`, `_includes/timeline-item.html`, `assets/arrow-right-solid.svg` | Unused backups, include fragments, and icon. |
| DELETE after moving useful metadata | `_includes/custom-head.html` | The active head now contains its favicon and theme links. |
| DELETE duplicate | `_data/socials.yml` | `_data/links.yml` is the live social source and contains the same entries. |
| DELETE unused renderers | `_layouts/record.html`, `_layouts/resume.html`, `_layouts/research-item.html`, `_layouts/experience-item.html` | Their collections do not output pages; unused layout defaults were removed. |
| DELETE unused style assets | `assets/calendar-alt-regular.svg`, `assets/map-marker-alt-solid.svg` | Their only callers were removed résumé styles. |
| DELETE unused media | `assets/placeholder.svg` | Cards and details now skip missing images; no renderer references the placeholder. |
| KEEP | `_jobs/`, `_records/`, `_research/`, hidden `_experience/` entries | Distinct authored writing, draft research, or TODO data; no silent merge into public pages. |
| KEEP | `assets/headshot@2x.webp`, `assets/images/sjcs-robocup/map (1).webp`, `assets/images/sjcs-robocup/map (2).webp` | Authored media that may be reused; ownership makes deletion uncertain. |
| KEEP | `_posts/`, `_grids/`, `_archives/` | Historic root and category URLs remain live. |

The post-cleanup build has the same 37 HTML routes. No route was removed. A
temporary project, publication, and experience entry each appeared in its
documented location; all were removed after the check. The Faraday notice is
unchanged from the baseline.

Tracked files inventoried: **342** (296 KEEP, 5 DELETE candidates, 41 CONFIRM). Generated HTML routes: **37**. Every tracked file appears once in the full inventory below.

## Review before deletion

- **DELETE candidates:** `Gemfile.bak`, `Gemfile.lock.bak`, `_includes/card-compact.html`, `_includes/timeline-item.html`, and `assets/arrow-right-solid.svg`. Each has no live route or call site.

- **CONFIRM:** all `_jobs/` and `_records/` entries, three `_research/` drafts, the two hidden `_experience/` entries, `_data/socials.yml`, the four legacy layouts, `_includes/custom-head.html`, three image/icon assets, and two SJCS map images. The per-file reasons and overlap checks are below. These hold authored material, affect future work, or have an ambiguous dependency.

- `_posts/`, `_grids/`, and `_archives/` are KEEP for now because they supply historic root and category URLs. Review any future pruning together with the redirect task in `TODO.md` → Blockers.

## Baseline generated routes

These are generated HTML paths, including the 404 page. Later phases must compare against this list.

| Route | Source |
| --- | --- |
| `/404.html` | `404.html` |
| `/abes-outreach/index.html` | `_posts/2019-01-16-abes-outreach.markdown` |
| `/about/index.html` | `about.markdown` |
| `/alfredo/index.html` | `_posts/2022-03-20-alfredo.markdown` |
| `/cv/index.html` | `cv.markdown` |
| `/esp-splash/index.html` | `_posts/2019-11-24-esp-splash.markdown` |
| `/index.html` | `index.markdown` |
| `/industry/index.html` | `industry.markdown` |
| `/minibot/index.html` | `_posts/2021-01-30-minibot.markdown` |
| `/projects/abes-outreach/index.html` | `_projects/abes-outreach.markdown` |
| `/projects/alfredo/index.html` | `_projects/alfredo.markdown` |
| `/projects/archive/index.html` | `_archives/archive.markdown` |
| `/projects/esp-splash/index.html` | `_projects/esp-splash.markdown` |
| `/projects/index.html` | `projects.markdown` |
| `/projects/jansens-linkage/index.html` | `_projects/jansens-linkage.markdown` |
| `/projects/minibot/index.html` | `_projects/minibot.markdown` |
| `/projects/perception-autonomy/index.html` | `_archives/perception-autonomy.markdown` |
| `/projects/pool-playing-robot/index.html` | `_projects/pool-playing-robot.markdown` |
| `/projects/research/index.html` | `_archives/research.markdown` |
| `/projects/revise/index.html` | `_projects/revise.markdown` |
| `/projects/rf-controllers/index.html` | `_projects/rf-controllers.markdown` |
| `/projects/rl-in-2048/index.html` | `_projects/rl-in-2048.markdown` |
| `/projects/rubber-band-turret/index.html` | `_projects/rubber-band-turret.markdown` |
| `/projects/soccer-robot/index.html` | `_projects/soccer-robot.markdown` |
| `/projects/systems-hardware/index.html` | `_archives/systems-hardware.markdown` |
| `/projects/teaching/index.html` | `_archives/teaching.markdown` |
| `/projects/toy-for-toddlers/index.html` | `_projects/toy-for-toddlers.markdown` |
| `/projects/water-bottle-quadrotor/index.html` | `_projects/water-bottle-quadrotor.markdown` |
| `/research/index.html` | `research.markdown` |
| `/revise/index.html` | `_posts/2021-12-20-revise.markdown` |
| `/rf-controllers/index.html` | `_posts/2020-03-05-rf-controllers.markdown` |
| `/rl-in-2048/index.html` | `_posts/2020-08-31-rl-in-2048.markdown` |
| `/rubber-band-turret/index.html` | `_posts/2019-12-30-rubber-band-turret.markdown` |
| `/sjcs-robocup/index.html` | `_posts/2018-04-19-sjcs-robocup.markdown` |
| `/soccer-robot/index.html` | `_posts/2019-08-25-soccer-robot.markdown` |
| `/todo/index.html` | `todo.markdown` |
| `/toy-for-toddlers/index.html` | `_posts/2020-01-07-toy-for-toddlers.markdown` |

## Configuration and rule-level findings

| Area | Finding | Next action |
| --- | --- | --- |
| `_config.yml` | `_schools`, `_skills`, `_jobs`, and `_records` defaults/collection declarations outlive their current output. `_jobs/` and `_records/` contain authored content. | Wait for CONFIRM decisions before removing declarations or files. |
| Industry | `_layouts/experience.html` filters by organization string; two authored entries never appear. | Replace with a display flag/order field in Phase 3. |
| Social links | `_data/socials.yml` duplicates three entries in live `_data/links.yml`; only `links.yml` also has CV. | Confirm whether to remove the duplicate. |
| Favicons | `_includes/custom-head.html` is not called by the current `_includes/head.html`. Icon files are retained, but head metadata needs review. | Confirm whether to fold favicon links into the live head. |
| Sass | `.resume*`, `.record-*`, `.timeline*`, `.duration`, and `.location` styling may be dead or tied to legacy layouts. | Review selectors against rendered markup before deletion. |
| Media | `assets/headshot@2x.webp` and two `sjcs-robocup/map (*.webp)` images have no current render reference; gallery images under `grid-N/` are dynamically included. | Keep owner images pending review. |
| Brochure link | The ReVise post links to `/downloads/revise-product-sheet.pdf/` with a trailing slash; the file exists without the slash. | Fix the link in Phase 3 and verify it resolves. |
| Content overlap | Legacy Rotor graduate/job and record sources say 50:1 LiDAR compression, while the live experience entry says 100:1; `TODO.md` already requests owner verification. | Do not merge this claim until verified. |
| Authoring | Projects, publications, Service, and experience currently have no copyable unpublished examples; news has no live source/template. | Design examples and news path in Phase 3 after source decisions. |

## Full tracked-file inventory

`Referenced by` names the actual route/template, a dynamic convention, or the overlapping live source. `CONFIRM` means preserve until Jinger decides.

| Path | Group | Reason | Referenced by / overlap |
| --- | --- | --- | --- |
| `.gitignore` | KEEP | repository hygiene | site configuration / repository workflow |
| `404.html` | KEEP | Generated public route | /404.html |
| `AGENTS.md` | KEEP | agent guide required by TODO.md | site configuration / repository workflow |
| `CNAME` | KEEP | custom domain | site configuration / repository workflow |
| `Gemfile` | KEEP | Jekyll dependencies | site configuration / repository workflow |
| `Gemfile.bak` | DELETE | Old dependency backup; active Gemfile/lock supersede it | No live references |
| `Gemfile.lock` | KEEP | locked GitHub Pages dependencies | site configuration / repository workflow |
| `Gemfile.lock.bak` | DELETE | Old dependency backup; active Gemfile/lock supersede it | No live references |
| `README.md` | KEEP | local build instructions | site configuration / repository workflow |
| `TODO.md` | KEEP | launch checklist and cleanup plan | site configuration / repository workflow |
| `_archives/archive.markdown` | KEEP | Public legacy category URL | _layouts/category.html -> /projects/archive/ |
| `_archives/perception-autonomy.markdown` | KEEP | Public legacy category URL | _layouts/category.html -> /projects/perception-autonomy/ |
| `_archives/research.markdown` | KEEP | Public legacy category URL | _layouts/category.html -> /projects/research/ |
| `_archives/systems-hardware.markdown` | KEEP | Public legacy category URL | _layouts/category.html -> /projects/systems-hardware/ |
| `_archives/teaching.markdown` | KEEP | Public legacy category URL | _layouts/category.html -> /projects/teaching/ |
| `_config.yml` | KEEP | Jekyll routing, collections, defaults, navigation | site configuration / repository workflow |
| `_data/education.yml` | KEEP | Live data source | _includes/education.html -> /about/ |
| `_data/links.yml` | KEEP | Live data source | _includes/social.html -> footer |
| `_data/publications.yml` | KEEP | Live data source | _layouts/home.html -> / and _layouts/todo.html |
| `_data/service.yml` | KEEP | Live data source | _includes/service.html -> /about/ |
| `_data/skills.yml` | KEEP | Live data source | _layouts/about.html -> /about/ |
| `_data/socials.yml` | CONFIRM | Duplicate authored social links; links.yml is live | _data/links.yml (same three links plus CV) |
| `_experience/gev.markdown` | KEEP | Rendered industry entry | _layouts/experience.html -> /industry/ |
| `_experience/intro-robotics.markdown` | CONFIRM | Authored experience omitted by current organization filter; TODO may use it | _layouts/todo.html; _data/service.yml or future industry listing |
| `_experience/microsoft.markdown` | KEEP | Rendered industry entry | _layouts/experience.html -> /industry/ |
| `_experience/mit-mrl.markdown` | CONFIRM | Authored experience omitted by current organization filter; TODO may use it | _layouts/todo.html; _data/service.yml or future industry listing |
| `_experience/rotor-graduate.markdown` | KEEP | Rendered industry entry | _layouts/experience.html -> /industry/ |
| `_experience/rotor-undergraduate.markdown` | KEEP | Rendered industry entry | _layouts/experience.html -> /industry/ |
| `_grids/abes-outreach/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-abes-outreach.markdown |
| `_grids/abes-outreach/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-abes-outreach.markdown |
| `_grids/abes-outreach/grid-3.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-abes-outreach.markdown |
| `_grids/abes-outreach/grid-4.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-abes-outreach.markdown |
| `_grids/abes-outreach/grid-5.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-abes-outreach.markdown |
| `_grids/esp-splash/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-esp-splash.markdown |
| `_grids/minibot/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-minibot.markdown |
| `_grids/revise/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-revise.markdown |
| `_grids/revise/grid-3.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-revise.markdown |
| `_grids/rf-controllers/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rf-controllers.markdown |
| `_grids/rf-controllers/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rf-controllers.markdown |
| `_grids/rf-controllers/grid-3.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rf-controllers.markdown |
| `_grids/rf-controllers/grid-4.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rf-controllers.markdown |
| `_grids/rl-in-2048/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rl-in-2048.markdown |
| `_grids/rubber-band-turret/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rubber-band-turret.markdown |
| `_grids/rubber-band-turret/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rubber-band-turret.markdown |
| `_grids/rubber-band-turret/grid-3.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rubber-band-turret.markdown |
| `_grids/rubber-band-turret/grid-4.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-rubber-band-turret.markdown |
| `_grids/sjcs-robocup/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-sjcs-robocup.markdown |
| `_grids/sjcs-robocup/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-sjcs-robocup.markdown |
| `_grids/sjcs-robocup/grid-3.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-sjcs-robocup.markdown |
| `_grids/soccer-robot/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-soccer-robot.markdown |
| `_grids/toy-for-toddlers/grid-1.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-toy-for-toddlers.markdown |
| `_grids/toy-for-toddlers/grid-2.markdown` | KEEP | Historic post gallery document | _layouts/post.html -> _posts/*-toy-for-toddlers.markdown |
| `_includes/banner.html` | KEEP | Live include | _layouts/with-banner.html |
| `_includes/card-compact.html` | DELETE | No include call from live layout | No live references |
| `_includes/card.html` | KEEP | Live include | _layouts/home.html |
| `_includes/custom-head.html` | CONFIRM | Not included by current head override; holds favicon markup | Potential head/favicons work |
| `_includes/education.html` | KEEP | Live include | _layouts/about.html |
| `_includes/footer.html` | KEEP | Live include | Minima default and _layouts/with-banner.html |
| `_includes/head.html` | KEEP | Live include | Minima default and _layouts/with-banner.html |
| `_includes/header.html` | KEEP | Live include | Minima default and _layouts/with-banner.html |
| `_includes/industry-item.html` | KEEP | Live include | _layouts/experience.html |
| `_includes/media.html` | KEEP | Live include | _layouts/project.html |
| `_includes/post-card.html` | KEEP | Live include | _layouts/category.html |
| `_includes/project-grid-card.html` | KEEP | Live include | _layouts/projects.html |
| `_includes/pub-item.html` | KEEP | Live include | _layouts/home.html |
| `_includes/service.html` | KEEP | Live include | _layouts/about.html |
| `_includes/social.html` | KEEP | Live include | _includes/footer.html |
| `_includes/timeline-item.html` | DELETE | No include call from live layout | No live references |
| `_includes/todo.html` | KEEP | Live include | _layouts/project.html, _includes/pub-item.html, _includes/media.html |
| `_jobs/200b-labua.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _data/service.yml (lab instructor); distinct workshop and team details |
| `_jobs/200b-mentor.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _data/service.yml (undergraduate assistant); distinct mentoring detail |
| `_jobs/4409-shop.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | No live counterpart; shop-management details |
| `_jobs/edventures-stem.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _data/service.yml names Edgerton; unique workshop and controller details; TODO.md future Edventures source |
| `_jobs/eecl-urop.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _projects/toy-for-toddlers.markdown and root post; distinct attachment detail |
| `_jobs/eecs-600-la.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | No live counterpart; Python-course teaching details |
| `_jobs/gev-intern.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/gev.markdown; wording and disclosure details differ |
| `_jobs/intro-robotics-ta.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/intro-robotics.markdown and _data/service.yml; fuller teaching details |
| `_jobs/microsoft-intern.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/microsoft.markdown; older patent and project wording |
| `_jobs/mrl-urop.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/mit-mrl.markdown; extra YOLOv7 and camera-rig detail |
| `_jobs/nctu-cgi-2048.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _posts/2020-08-31-rl-in-2048.markdown; distinct 2,000/20,000-round figures |
| `_jobs/neet-ua.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _data/service.yml and RF Controllers post; detailed controller counts |
| `_jobs/onb-swe.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | No live counterpart; software-internship details |
| `_jobs/rotor-grad-intern.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/rotor-graduate.markdown; conflicting 50:1 versus 100:1 compression claim |
| `_jobs/rotor-ugrad-intern.markdown` | CONFIRM | Authored legacy résumé entry; content may not be fully migrated | _experience/rotor-undergraduate.markdown; fuller systems detail |
| `_layouts/about.html` | KEEP | Live layout | about.markdown -> /about/ |
| `_layouts/category.html` | KEEP | Live layout | _archives/*.markdown -> /projects/:slug/ |
| `_layouts/experience-item.html` | CONFIRM | _config.yml default for non-output experience entries; no live page renders it | _config.yml defaults or legacy content |
| `_layouts/experience.html` | KEEP | Live layout | industry.markdown -> /industry/ |
| `_layouts/home.html` | KEEP | Live layout | index.markdown -> / |
| `_layouts/post.html` | KEEP | Live layout | _posts/*.markdown -> root post URLs |
| `_layouts/project.html` | KEEP | Live layout | _projects/*.markdown -> /projects/:slug/ |
| `_layouts/projects.html` | KEEP | Live layout | projects.markdown -> /projects/ |
| `_layouts/record.html` | CONFIRM | _config.yml default for non-output records; contains legacy record presentation | _config.yml defaults or legacy content |
| `_layouts/research-item.html` | CONFIRM | _config.yml default for non-output research entries; draft presentation | _config.yml defaults or legacy content |
| `_layouts/research.html` | KEEP | Live layout | research.markdown -> /research/ |
| `_layouts/resume.html` | CONFIRM | _config.yml default for non-output jobs; legacy résumé presentation | _config.yml defaults or legacy content |
| `_layouts/todo.html` | KEEP | Live layout | todo.markdown -> /todo/ |
| `_layouts/with-banner.html` | KEEP | Live layout | _layouts/home.html |
| `_posts/2018-04-19-sjcs-robocup.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /sjcs-robocup/ |
| `_posts/2019-01-16-abes-outreach.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /abes-outreach/ |
| `_posts/2019-08-25-soccer-robot.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /soccer-robot/ |
| `_posts/2019-11-24-esp-splash.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /esp-splash/ |
| `_posts/2019-12-30-rubber-band-turret.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /rubber-band-turret/ |
| `_posts/2020-01-07-toy-for-toddlers.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /toy-for-toddlers/ |
| `_posts/2020-03-05-rf-controllers.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /rf-controllers/ |
| `_posts/2020-08-31-rl-in-2048.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /rl-in-2048/ |
| `_posts/2021-01-30-minibot.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /minibot/ |
| `_posts/2021-12-20-revise.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /revise/ |
| `_posts/2022-03-20-alfredo.markdown` | KEEP | Public historic writeup and root URL | _layouts/post.html; _archives/*; /alfredo/ |
| `_projects/abes-outreach.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/alfredo.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/esp-splash.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/jansens-linkage.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/minibot.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/pool-playing-robot.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/revise.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/rf-controllers.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/rl-in-2048.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/rubber-band-turret.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/soccer-robot.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/toy-for-toddlers.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_projects/water-bottle-quadrotor.markdown` | KEEP | Public project URL, card, Archive or Service source | _layouts/project.html; _layouts/projects.html; _layouts/home.html |
| `_records/eccl-toddler-toy.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _projects/toy-for-toddlers.markdown and root post; alternate summary |
| `_records/gev-blade-inspection.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _experience/gev.markdown; confidential wording and timing differ |
| `_records/icra2024-perception-safety.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _data/publications.yml and research-page narrative; alternate summary |
| `_records/microsoft-hinge-patent.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _data/publications.yml and _experience/microsoft.markdown; extra links/status |
| `_records/mit-robotics-ta.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _experience/intro-robotics.markdown and _data/service.yml; alternate summary |
| `_records/mrl-icra2027.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _data/publications.yml and _research/human-motion-prediction.markdown; fuller methods/claims |
| `_records/mrl-ur5-rig.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _experience/mit-mrl.markdown; distinct rig and YOLOv7 detail |
| `_records/nctu-2048.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _posts/2020-08-31-rl-in-2048.markdown; alternate summary |
| `_records/rotor-lidar-compression.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _experience/rotor-graduate.markdown; conflicting 50:1 versus 100:1 compression claim |
| `_records/rotor-subscale-heli.markdown` | CONFIRM | Authored non-output record; content may not be fully migrated | _experience/rotor-undergraduate.markdown; alternate summary |
| `_research/field-localization.markdown` | CONFIRM | Draft research content; TODO arrays feed /todo/ | _layouts/todo.html; research-page future work |
| `_research/human-motion-prediction.markdown` | CONFIRM | Draft research content; TODO arrays feed /todo/ | _layouts/todo.html; research-page future work |
| `_research/perception-safety.markdown` | CONFIRM | Draft research content; TODO arrays feed /todo/ | _layouts/todo.html; research-page future work |
| `_sass/_tokens.scss` | KEEP | Sass build input; some selectors need rule-level review | assets/main.scss -> /assets/main.css |
| `_sass/colors.scss` | KEEP | Sass build input; some selectors need rule-level review | assets/main.scss -> /assets/main.css |
| `_sass/fonts.scss` | KEEP | Sass build input; some selectors need rule-level review | assets/main.scss -> /assets/main.css |
| `_sass/layout.scss` | KEEP | Sass build input; some selectors need rule-level review | assets/main.scss -> /assets/main.css |
| `about.markdown` | KEEP | Generated public route | /about/ |
| `android-chrome-192x192.png` | KEEP | Icon/manifest compatibility asset | site.webmanifest |
| `android-chrome-512x512.png` | KEEP | Icon/manifest compatibility asset | site.webmanifest |
| `apple-touch-icon.png` | KEEP | Icon/manifest compatibility asset | favicon compatibility; named in _includes/custom-head.html |
| `assets/arrow-right-solid.svg` | DELETE | No template, CSS, content, or manifest reference | No live references |
| `assets/banner.webp` | KEEP | Site identity image | _config.yml; header, home or banner layout |
| `assets/calendar-alt-regular.svg` | CONFIRM | Only referenced by CSS for legacy .duration/.location classes | _sass/layout.scss; no live markup uses those classes |
| `assets/headshot.webp` | KEEP | Site identity image | _config.yml; header, home or banner layout |
| `assets/headshot@2x.webp` | CONFIRM | Unreferenced high-resolution owner photo | Potential future responsive headshot |
| `assets/images/abes-outreach/cover.webp` | KEEP | Post/project cover image | _posts/*-abes-outreach.markdown or _projects/abes-outreach.markdown |
| `assets/images/abes-outreach/grid-1/abes-1-1.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-1/abes-1-2.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-1/abes-1-3.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-1/abes-1-4.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-1/abes-1-5.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-1/abes-1-6.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-1.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-2/abes-2-1.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-2.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-2/abes-2-2.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-2.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-2/abes-2-3.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-2.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-2/abes-2-4.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-2.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-2/abes-2-5.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-2.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-1.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-2.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-3.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-4.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-5.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-3/abes-3-6.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-3.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-1.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-10.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-11.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-12.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-2.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-3.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-4.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-5.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-6.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-7.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-8.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-4/abes-4-9.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-4.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-1.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-10.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-11.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-12.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-2.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-3.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-4.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-5.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-6.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-7.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-8.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/abes-outreach/grid-5/abes-5-9.webp` | KEEP | Rendered historic gallery image | _grids/abes-outreach/grid-5.markdown; _layouts/post.html |
| `assets/images/alfredo/cover.webp` | KEEP | Post/project cover image | _posts/*-alfredo.markdown or _projects/alfredo.markdown |
| `assets/images/esp-splash/cover.webp` | KEEP | Post/project cover image | _posts/*-esp-splash.markdown or _projects/esp-splash.markdown |
| `assets/images/esp-splash/grid-1/esp-1.webp` | KEEP | Rendered historic gallery image | _grids/esp-splash/grid-1.markdown; _layouts/post.html |
| `assets/images/esp-splash/grid-1/esp-2.webp` | KEEP | Rendered historic gallery image | _grids/esp-splash/grid-1.markdown; _layouts/post.html |
| `assets/images/esp-splash/grid-1/esp-3.webp` | KEEP | Rendered historic gallery image | _grids/esp-splash/grid-1.markdown; _layouts/post.html |
| `assets/images/minibot/cover.webp` | KEEP | Post/project cover image | _posts/*-minibot.markdown or _projects/minibot.markdown |
| `assets/images/minibot/grid-1/minibot-1.webp` | KEEP | Rendered historic gallery image | _grids/minibot/grid-1.markdown; _layouts/post.html |
| `assets/images/minibot/grid-1/minibot-2.webp` | KEEP | Rendered historic gallery image | _grids/minibot/grid-1.markdown; _layouts/post.html |
| `assets/images/minibot/grid-1/minibot-3.webp` | KEEP | Rendered historic gallery image | _grids/minibot/grid-1.markdown; _layouts/post.html |
| `assets/images/revise/cover.webp` | KEEP | Post/project cover image | _posts/*-revise.markdown or _projects/revise.markdown |
| `assets/images/revise/grid-2/assembly_3.png` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-2/bladder_exp.gif` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-2/bladder_real_2.png` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-2/bladder_screw.gif` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-2/control_box_exp.gif` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-2/control_box_side.gif` | KEEP | Rendered historic gallery image | _grids/revise/grid-2.markdown; _layouts/post.html |
| `assets/images/revise/grid-3/hd_view_1.png` | KEEP | Rendered historic gallery image | _grids/revise/grid-3.markdown; _layouts/post.html |
| `assets/images/revise/grid-3/hd_view_2.png` | KEEP | Rendered historic gallery image | _grids/revise/grid-3.markdown; _layouts/post.html |
| `assets/images/revise/grid-3/hd_view_3.PNG` | KEEP | Rendered historic gallery image | _grids/revise/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/cover.webp` | KEEP | Post/project cover image | _posts/*-rf-controllers.markdown or _projects/rf-controllers.markdown |
| `assets/images/rf-controllers/grid-1/rf-1-1.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-1.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-1/rf-1-2.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-1.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-1/rf-1-3.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-1.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-1/rf-1-4.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-1.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-2/rf-2-1.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-2.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-2/rf-2-2.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-2.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-2/rf-2-3.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-2.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-1.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-2.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-3.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-4.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-5.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-3/rf-3-6.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-3.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-1.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-2.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-3.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-4.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-5.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rf-controllers/grid-4/rf-4-6.webp` | KEEP | Rendered historic gallery image | _grids/rf-controllers/grid-4.markdown; _layouts/post.html |
| `assets/images/rl-in-2048/cover.webp` | KEEP | Post/project cover image | _posts/*-rl-in-2048.markdown or _projects/rl-in-2048.markdown |
| `assets/images/rl-in-2048/grid-1/2048 (2).webp` | KEEP | Rendered historic gallery image | _grids/rl-in-2048/grid-1.markdown; _layouts/post.html |
| `assets/images/rl-in-2048/grid-1/2048 (3).webp` | KEEP | Rendered historic gallery image | _grids/rl-in-2048/grid-1.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/cover.webp` | KEEP | Post/project cover image | _posts/*-rubber-band-turret.markdown or _projects/rubber-band-turret.markdown |
| `assets/images/rubber-band-turret/grid-1/turret-1-1.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-1.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-1/turret-1-2.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-1.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-1/turret-1-3.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-1.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-1.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-2.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-3.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-4.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-5.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-6.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-2/turret-2-7.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-2.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-1.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-2.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-3.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-4.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-5.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-6.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-3/turret-3-7.webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-3.markdown; _layouts/post.html |
| `assets/images/rubber-band-turret/grid-4/turret (12).webp` | KEEP | Rendered historic gallery image | _grids/rubber-band-turret/grid-4.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/cover.webp` | KEEP | Post/project cover image | _posts/*-sjcs-robocup.markdown or _projects/sjcs-robocup.markdown |
| `assets/images/sjcs-robocup/grid-1/prep-1.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-2.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-3.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-4.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-5.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-6.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-1/prep-7.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-1.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-1.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-10.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-11.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-12.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-13.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-14.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-15.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-16.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-17.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-2.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-3.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-4.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-5.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-6.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-7.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-8.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-2/robocup-1-9.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-2.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-1.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-10.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-11.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-12.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-13.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-14.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-2.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-3.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-4.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-5.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-6.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-7.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-8.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/grid-3/robocup-2-9.webp` | KEEP | Rendered historic gallery image | _grids/sjcs-robocup/grid-3.markdown; _layouts/post.html |
| `assets/images/sjcs-robocup/map (1).webp` | CONFIRM | Owner image outside cover/gallery conventions; not rendered | No current HTML reference; SJCS Robocup source asset |
| `assets/images/sjcs-robocup/map (2).webp` | CONFIRM | Owner image outside cover/gallery conventions; not rendered | No current HTML reference; SJCS Robocup source asset |
| `assets/images/soccer-robot/cover.webp` | KEEP | Post/project cover image | _posts/*-soccer-robot.markdown or _projects/soccer-robot.markdown |
| `assets/images/soccer-robot/grid-1/soccer-robot-1.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-2.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-3.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-4.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-5.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-6.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-8.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/soccer-robot/grid-1/soccer-robot-9.webp` | KEEP | Rendered historic gallery image | _grids/soccer-robot/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/cover.webp` | KEEP | Post/project cover image | _posts/*-toy-for-toddlers.markdown or _projects/toy-for-toddlers.markdown |
| `assets/images/toy-for-toddlers/grid-1/toy-1-1.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-10.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-2.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-3.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-4.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-5.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-6.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-7.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-8.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-1/toy-1-9.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-1.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-1.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-10.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-2.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-3.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-4.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-5.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-6.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-7.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-8.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/images/toy-for-toddlers/grid-2/toy-2-9.webp` | KEEP | Rendered historic gallery image | _grids/toy-for-toddlers/grid-2.markdown; _layouts/post.html |
| `assets/logo.webp` | KEEP | Site identity image | _config.yml; header, home or banner layout |
| `assets/main.scss` | KEEP | Sass build input; some selectors need rule-level review | assets/main.scss -> /assets/main.css |
| `assets/map-marker-alt-solid.svg` | CONFIRM | Only referenced by CSS for legacy .duration/.location classes | _sass/layout.scss; no live markup uses those classes |
| `assets/placeholder.svg` | KEEP | Current project media fallback | _includes/media.html, card.html, project-grid-card.html |
| `browserconfig.xml` | KEEP | Windows tile configuration | site configuration / repository workflow |
| `cv.markdown` | KEEP | Generated public route | /cv/ |
| `downloads/jinger-chong-cv.pdf` | KEEP | Public CV | _config.yml cv_url; footer /cv/ |
| `downloads/revise-product-sheet.pdf` | KEEP | Public brochure | _posts/2021-12-20-revise.markdown (URL needs repair) |
| `favicon-16x16.png` | KEEP | Icon/manifest compatibility asset | favicon compatibility; named in _includes/custom-head.html |
| `favicon-32x32.png` | KEEP | Icon/manifest compatibility asset | favicon compatibility; named in _includes/custom-head.html |
| `favicon.ico` | KEEP | Icon/manifest compatibility asset | browser conventional /favicon.ico request |
| `index.markdown` | KEEP | Generated public route | / |
| `industry.markdown` | KEEP | Generated public route | /industry/ |
| `mstile-150x150.png` | KEEP | Icon/manifest compatibility asset | browserconfig.xml |
| `projects.markdown` | KEEP | Generated public route | /projects/ |
| `research.markdown` | KEEP | Generated public route | /research/ |
| `robots.txt` | KEEP | crawler rules for /todo/ | site configuration / repository workflow |
| `safari-pinned-tab.svg` | KEEP | Icon/manifest compatibility asset | favicon compatibility; named in _includes/custom-head.html |
| `site.webmanifest` | KEEP | site/app identity and Android icons | site configuration / repository workflow |
| `todo.markdown` | KEEP | Generated public route | /todo/ |
