# TODO — portfolio launch and application season

This is the single place to track site work. The list reflects the current source files as of
2026-09-28. A missing cover is intentionally omitted by the templates; hidden drafts have
`published: false` and are not launch blockers.

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
| Water Bottle Flipping Quadrotor | `bottle-flip` | Published; needs evidence | Cover, individual contribution, comparison or failure cases |
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

- [ ] **Review outreach photos before displaying them.** The K–12 outreach images are excluded
      from the published site because they include identifiable students. Confirm public-use
      approval before removing `assets/images/abes-outreach` from `_config.yml`'s exclude list.
- [ ] Add strong, rights-cleared covers to the three featured projects. The racecar has a cover;
      pool and quadrotor do not. Consider whether a research-specific banner would better signal
      the current work than the shop photograph.
- [ ] Add a short teaching writeup for the Spring 2023 2.00B Lab Instructor role if there are
      approved photos and useful detail (Fusion 360 and Illustrator workshops for 70+ students;
      coached a six-member team). Optionally add Rotor 2022's subscale-helicopter CAD/SAS and
      procurement work after public wording is approved.
- [ ] Add talks or a News section when there are verified items. Revisit a dedicated Publications
      page once the list grows. Keep the old sketch only if it adds value as a footer or 404 detail.

## Editorial decisions already made

- The 2026-09-29 `revamp` GitHub Actions production build and local-link check passed after
  locking native gems for Windows and Linux and excluding `vendor/` from Jekyll output.
- The project URLs now use `struct-gp`, `safety-metrics`, `pool-robot`, `bottle-flip`, and
  `2048-rl`; the hidden drafts use `novel-view-sythesis`, `infant-gaze`, and `ur5-lego`.
  Former project URLs have no redirects. The 2048 images moved with its slug.
- Jinger approved the public GE Vernova bullets, metrics, deployment and invention-disclosure
  wording and Rotor's 100:1 LiDAR compression claim on 2026-09-28.
- Jinger confirmed that the ICRA 2027 anonymity policy permits the current arXiv link. Keep the
  publication status current; on 2026-09-28 she confirmed it is still under review.
- Jinger confirmed the arXiv link points to the updated ICRA manuscript.
- Jinger confirmed the public CV's Sep 2022–Present MIT Mechatronics Research Lab timeline.
  Research → NOW uses the same timeline and role title. The public CV contains no phone number or
  street address.
- Hide Jansen’s Linkage until its blurb or writeup is approved. External links were checked on
  2026-09-28; the dead ReVise team-page link was removed and its webcast uses a direct Vimeo link.
  The four Alfredo YouTube videos resolve.
- The 2026-09-28 production build and local HTML/link check passed. The main routes and redirects
  were previewed at desktop and phone widths; mobile image and navigation layout was adjusted.
- Orange and Bronze Software Labs stays off the site (CV only).
- 2026-09-28: Edgerton K-12 Mentor stays unlinked in Service until `/projects/edventures/` is
  published. Keep a mix of community and outreach roles for personality; sort Service newest first.
  Keep the current 2.00B teaching titles. Segway Robot, Flashlight, Iron Man, Home Upgrades, and the Photography
  page from the old site stay retired.
- 2026-09-28: Service lists one Student Project Lab (4-409) row (Shop Mentor, 2019 – 2021);
  the separate Assistant Shop Manager row was removed. Banana Lounge stays.
- 2026-09-28: Keep Andres Bonifacio Elementary School Robotics Outreach and Banana Lounge in
  Service. Remove the Filipino Students Association and Women's Independent Living Group rows
  to focus the section on impact and personality.
- Keep the Skills list robotics-focused. Do not add Java, HTML/CSS, SQL, LaTeX, OpenSCAD, or
  Illustrator just to mirror the old résumé.
