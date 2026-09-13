CONTEXT
Repo: personal portfolio at jingerchong.com. Jekyll + GitHub Pages (Ruby).
Owner: Jinger Chong, PhD candidate in Mechanical Engineering at MIT,
advised by Kamal Youcef-Toumi. Applying to Summer 2027 robotics RESEARCH
internships (perception, human motion prediction, uncertainty-aware
autonomy, HRI).

GOAL
Restructure the site so it reads as a robotics researcher's portfolio, not
an undergraduate maker portfolio. Preserve the existing color palette,
logo, and favicon exactly. Reuse the existing card/grid aesthetic; do not
introduce a new design language, CSS framework, or JS build step.

═══════════════════════════════════════════════════════════════════
TASK 0 — SOURCE OF TRUTH AND TODO PROTOCOL  (read before any edit)
═══════════════════════════════════════════════════════════════════

The RESUME at the bottom of this prompt is the newer, authoritative
source for all factual claims. Apply this precedence ladder:

  RULE 1 — DIRECT CONFLICT (same fact, different value):
    Resume wins. Overwrite the site silently. Do NOT stop to ask.
    Append one line per resolution to CONFLICTS.md at repo root:
      `path/to/file` | field | old value → new value | source: resume

  RULE 2 — RESUME OMITS SOMETHING THE SITE HAS:
    Resume silence is NOT deletion. The resume is a compressed 1-2 page
    document; the site is not length-limited. KEEP this content. You may
    relocate or demote it (e.g. to About → "Earlier", or Projects →
    tier: more), but never delete it. Log relocations in CONFLICTS.md
    under a "RELOCATED" heading.
    Non-exhaustive examples that MUST survive: NEET Autonomous Machines
    certificate; Tau Beta Pi; Pi Tau Sigma; coursework not on the resume
    (Computer Vision, Robotic Manipulation, Computational Design &
    Fabrication, Algorithms, Dynamics & Controls); NCTU Computer Games
    and Intelligence Lab research internship (2020); MIT NEET
    Undergraduate Assistant; all existing project pages.

  RULE 3 — SITE OMITS SOMETHING THE RESUME HAS:
    Add it, in the correct new location per the IA below.

  RULE 4 — NEITHER SOURCE HAS IT (media, prose, PDFs, URLs, figures):
    Emit a TODO placeholder. NEVER invent facts, dates, metrics, venues,
    author lists, awards, collaborators, image content, or links. A
    fabricated detail on this site is a worse failure than a visible gap.

KNOWN CONFLICTS — resolve these per RULE 1 without asking:
  - Current degree label → "PhD Candidate in Mechanical Engineering,"
    expected graduation May 2028.
  - SM dates → Sep 2023 – May 2025 (site currently says Sep 2023 – Dec
    2024).
  - BS dates → Sep 2019 – May 2023.
  - BS minors → Computer Science and Chinese.
  - ALL GPAs → omit sitewide (resume 4.8 vs site 4.9 conflict is moot;
    GPA does not belong on a research portfolio). Keep GPA out of every
    page, include, and data file.
  - Footer copyright → auto-generate the year; remove hardcoded 2023.
  - Rotor Technologies → ONE experience entry spanning both terms
    (Graduate Intern Jun–Sep 2023, Undergraduate Intern Jun–Aug 2022).

TODO PROTOCOL — implement this machinery in TASK 1, use it everywhere:
  a) Every page/collection item gets an optional front-matter array:
       todo:
         - level: blocker        # blocker | content | verify | optional
           text: "Add 4s loop of predicted pose distribution."
           owner: jinger
  b) Create _includes/todo.html for inline placeholders:
       {% include todo.html level="content" text="..." %}
     It renders a visible, high-contrast badge ONLY when
     jekyll.environment != "production"; in production it renders
     nothing (or an HTML comment). Placeholders must never leak to a
     live visitor.
  c) Create /todo/ — a noindexed (robots: noindex, sitemap: false)
     dashboard page that iterates site.research, site.experience,
     site.projects, site.pages and every _data file, and renders all
     `todo` entries grouped by level, then by page, with counts and
     direct edit links. This is my launch checklist.
  d) Media placeholders: reference a real committed placeholder asset
     (/assets/placeholder.svg, in brand colors) plus a `todo` entry
     specifying exactly what media is needed, target aspect ratio,
     and file path where I should drop it. Do not use hotlinked or
     stock imagery.
  e) Unknown URLs: use href="#" plus a `todo` entry. Never guess a URL,
     DOI, arXiv ID, or repo path.
  f) Levels: blocker = site should not launch with this; content = prose
     or media I must write/shoot; verify = factual or legal confirmation
     needed (e.g. GE Vernova disclosure wording, ICRA anonymity policy);
     optional = nice-to-have.

═══════════════════════════════════════════════════════════════════

HARD CONSTRAINTS
- Keep Jekyll; keep it deployable on GitHub Pages. If a plugin outside
  the GH Pages allowlist is needed, migrate the deploy to a GitHub
  Actions workflow and say so explicitly in the PR notes.
- No React/Tailwind/Node toolchain. Vanilla Sass + minimal vanilla JS.
- Extract existing brand colors into CSS custom properties in
  _sass/_tokens.scss; every new component consumes those tokens. Do not
  invent new hues; computed tints/shades of existing tokens are fine.
- All existing URLs must keep working via jekyll-redirect-from.
- Accessibility: semantic landmarks, visible focus states, alt text on
  all media, WCAG AA contrast, prefers-reduced-motion honored for
  autoplay media.

TASK 1 — INFORMATION ARCHITECTURE  (+ build the TODO machinery above)
Nav becomes exactly: Research · Experience · Projects · About · CV (PDF,
external-link icon). Create:
  /            home: hero, research statement, 3 selected-work cards,
               publications list, "Now / availability" line
  /research/   research threads with figures, then Publications, then
               Patents, then Talks & Service
  /experience/ industry R&D + teaching, reverse chronological, left
               timeline rail
  /projects/   "Selected projects" (3-4 full cards) + "More work"
               (compact filterable list)
  /about/      bio, education, skills, teaching & service, earlier work,
               contact
  /todo/       noindexed launch checklist (see TASK 0c)

TASK 2 — CONVERT TO COLLECTIONS
Create _research, _experience, _projects collections and _data files
(publications.yml, education.yml, skills.yml, socials.yml). Migrate every
existing project page into _projects with normalized front matter —
migrate all of them, including ones absent from the resume (RULE 2).
Schemas, enforced via _config.yml collection defaults and shared
includes; every schema also accepts the `todo` array from TASK 0a:
  _research:   title, order, status, venue, blurb, metrics[], tags[],
               media, poster, links{paper,code,video,bibtex}
  _experience: org, role, start, end, location, headline, bullets[],
               stack[], featured, confidential
  _projects:   title, tier(selected|more), award, term, tags[], stack[],
               cover, media, links{code,report,video}, teammates
Includes: card.html, card-compact.html, pub-item.html, timeline-item.html,
todo.html, media.html (media.html handles mp4-with-poster, webp, and gif
behind one interface: lazy-loaded, muted, looping, playsinline,
reduced-motion fallback to poster; if no media exists, it renders the
brand placeholder + registers a TODO).

TASK 3 — TAXONOMY
Replace project tags Build/Code/Class/Teach/Fun/Volunteer with:
Robotics, Perception, Controls, Learning, Hardware, Teaching & Outreach.
Every migrated project must land in at least one new tag — if the mapping
is genuinely ambiguous, pick the closest and add a `todo: level: verify`
entry rather than dropping the project. Generate tag index pages from a
single template. Redirect old tag URLs.

TASK 4 — CONTENT (resume is authoritative; TASK 0 ladder governs)
- Research threads, in order: (1) Probabilistic human motion prediction
  for safe HRC; (2) Perception-aware safety metrics; (3) Visual
  localization & mapping for field inspection. Populate Problem/Approach/
  Results from resume bullets; TODO every figure, loop, and diagram.
- Publications: ICRA 2027 (under review — render a status badge, NO PDF
  or preprint link, and add `todo: level: verify` for the venue's
  anonymity/preprint policy before anything is posted); ICRA 2024
  (TODO: PDF path, DOI, code link); U.S. Patent App. 2026/0143604 A1
  (pending). Copy-to-clipboard BibTeX per entry — generate BibTeX only
  from fields present in the resume; TODO any missing field (pages, DOI,
  publisher) rather than inventing it.
- Experience: GE Vernova (featured, confidential: true → suppress all
  imagery, render "invention disclosure under internal review", plus
  `todo: level: verify` on public wording); Microsoft; MIT Intro to
  Robotics TA; Rotor Technologies as one merged entry. NCTU lab and MIT
  NEET assistant → About → "Earlier" one-liners (RULE 2, do not delete).
- Selected projects: Autonomous Pool-Playing Robot (award badge, Fall
  2023), Water Bottle Flipping Quadrotor (Spring 2023), Alfredo. All
  other existing projects → tier: more.
- About: PhD (expected May 2028), SM (Sep 2023 – May 2025), SB (Sep 2019
  – May 2023, minors CS + Chinese), advisor, NEET certificate, honor
  societies, and a coursework line cross-linked to matching project
  pages (resume courses + surviving site courses, deduplicated). No GPAs.
- Home research statement: leave as a TODO placeholder with a
  4-sentences-max instruction comment and a suggested skeleton (problem
  class → gap → my angle → trajectory). Do NOT auto-generate it from
  resume bullets. Same for the three selected-work card headlines: seed
  each from the resume's strongest metric, mark `todo: level: content`
  for me to tighten.
- Delete the line "always on the lookout for any opportunity to learn new
  skills and technologies." Move "I like Japanese food" to About. Keep
  the "pronounced like ginger" line as small hero text or on About.
- Add the availability line: seeking Summer 2027 robotics research
  internships, naming the three focus areas.

TASK 5 — DETAIL PAGE TEMPLATE
One layout for every research/project detail page, sections in order:
hero media → one-sentence TL;DR → Problem → Approach → Results (numbers
bolded) → What I'd do differently → Stack chips → Links → Context (class,
term, collaborators). "What I'd do differently" is always a TODO on
migrated pages. Any section with no sourced content renders a TODO
placeholder, not filler prose.

TASK 6 — SEO, METADATA, PERFORMANCE
jekyll-seo-tag; per-page og:image with a generated brand default; JSON-LD
Person with sameAs (Google Scholar, GitHub, LinkedIn — TODO the Scholar
URL if not in the repo); sitemap excluding /todo/; robots.txt; title
pattern "Page — Jinger Chong". Target Lighthouse ≥95 mobile on the four
top-level pages: compress/resize images, lazy-load below-fold media,
preload the hero font, inline critical CSS if needed.

TASK 7 — DX AND CI
README section documenting: how to add a publication, research thread,
experience entry, and project; the front-matter schema for each; the TODO
protocol and how to clear items; media conventions (formats, dimensions,
naming, paths). CI: build check, html-proofer link check, and a step that
FAILS the production build if any `todo: level: blocker` remains or if
/assets/placeholder.svg is still referenced by a page in the production
nav. Non-blocker TODOs must not fail CI.

DELIVERY
Small, reviewable commits grouped by task. After each task, print:
(1) files added / changed / removed; (2) conflicts auto-resolved via
RULE 1, as a table; (3) content preserved-and-relocated via RULE 2;
(4) new TODOs created, grouped by level. Do not ask me questions
mid-run — resolve via the ladder and record it. At the end, print the
full /todo/ contents as a prioritized checklist, blockers first.

RESUME — AUTHORITATIVE SOURCE OF TRUTH
Jinger Chong
jinger@mit.edu | 617-710-0511 | Cambridge, MA | jingerchong.com | linkedin.com/in/jingerchong | github.com/jingerchong 
EDUCATION
Massachusetts Institute of Technology	Cambridge, MA
PhD Candidate in Mechanical Engineering | Advisor: Kamal Youcef-Toumi | GPA: 5.0/5.0	Expected Graduation May 2028
•	Courses: Underactuated Robotics, Visual Navigation for Autonomous Vehicles, Algorithmic Human-Robot Interaction
MS in Mechanical Engineering | GPA: 5.0/5.0	Sep 2023 – May 2025
BS in Mechanical Engineering, Minors in Computer Science and Chinese | GPA: 4.8/5.0	Sep 2019 – May 2023
EXPERIENCE
MIT Mechatronics Research Lab, Research Assistant	Sep 2022 – Present
•	Outperformed baselines including Motron (CVPR 2022) by 50 nats (KDE NLL) with 8× fewer parameters on probabilistic full-body motion prediction (Human3.6M), enabling real-time human intent estimation for safe human-robot collaboration
•	Built a structured multitask variational Gaussian process with joint-dimension factorization and continuous 6D rotation representation, validated by empirical coverage analysis and ablations over kernel, inducing points, and latent dimensionality
•	Designed and deployed an adjustable UR5 camera rig adopted lab-wide for validating perception and manipulation algorithms
GE Vernova Advanced Research Center, Computer Vision Research Intern	Jun 2026 – Aug 2026
•	Reduced inspector review volume by ~50% by consolidating redundant detections into unique defects on wind turbine blades
•	Developed visual localization for an inspection crawler along 50–75 m blades, chunked into overlapping windows, using COLMAP SfM with sequential ALIKED + LightGlue matching on perspective views rendered from equirectangular imagery
•	Scaled matching to 10⁴–10⁶ candidate defect polygon pairs per blade with a cascaded coarse-to-fine geometric verification filter 
•	Delivered 2–5 hour per blade single-node pipeline slated for deployment, with invention disclosure under internal patent review 
Microsoft, Mechanical Engineering Intern	Jun 2024 – Aug 2024
•	Owned end-to-end design and prototyping of a custom hinge mechanism from concept through alpha, translating benchmarking and user-study findings into specifications and first-order models for spring selection, material choice, and friction tuning
•	Honed in on target torque profile through iterative fabrication and measurement of 3D-printed and CNC-machined prototypes
MIT Introduction to Robotics, Teaching Assistant	Jan 2024 – May 2024
•	Built embedded C++ and ESP32-S3 platforms for labs in motor control, kinematics, computer vision, ML, and sensor interface
•	Revamped curriculum and lab handouts for 50+ student graduate robotics course, collaborating with 8 instructional staff
Rotor Technologies, Graduate Engineering Intern	Jun 2023 – Sep 2023
•	Achieved 100:1 LiDAR compression via H.265 encoding, enabling low-latency streaming for remotely-piloted helicopters
•	Streamlined sensor testing without flight hardware by emulating onboard sensors from recorded video and packet captures
•	Reduced real-time bandwidth by up to 3x via azimuth-level decimation and adaptive bitrate control
Rotor Technologies, Undergraduate Engineering Intern	Jun 2022 – Aug 2022
•	Expanded subscale helicopter testing infrastructure for perception, flight controls, and data logging from 1 to 3 units 
•	Integrated onboard power and data systems and bridged EKF and airspeed data from PX4 to proprietary flight software 
PUBLICATIONS & PATENTS
J. Chong, X. Zhang, K. Youcef-Toumi, “Towards Scalable Probabilistic Human Motion Prediction with Gaussian Processes for Safe Human-Robot Collaboration,” ICRA, 2027, under review.
X. Zhang, J. Chong, K. Youcef-Toumi, “How Does Perception Affect Safety: New Metrics and Strategy,” ICRA, 2024.
J. Chong, et al., “Multi-Function Hinge,” U.S. Patent Application Publication No. US 2026/0143604 A1, 2026, pending.
PROJECTS
Autonomous Pool-Playing Robot (Outstanding Project, Robotic Manipulation) – Drake, Python	Sep 2023 – Dec 2023
•	Developed a physics-based simulation of a single-shot pool-playing robot, modeling cue dynamics, ball motion, and collisions
•	Sank target balls consistently in randomized simulations using a heuristic task planner with IK and inverse dynamics control
Water Bottle Flipping Quadrotor – Drake, Python	Feb 2023 – May 2023
•	Demonstrated robust bottle-flipping across 4 fill levels (25–100%) using direct-collocation hybrid trajectory optimization 
•	Modeled quadrotor–bottle dynamics; formulated constraints for transitions, collisions, contact and impulse forces, and states
TECHNICAL SKILLS 
Languages: Python, C++, MATLAB, Julia, LaTeX
Tools: PyTorch, GPyTorch, OpenCV, COLMAP, hloc, ROS, Drake, Eigen, NumPy, SciPy, scikit-learn, Libpcap, FFmpeg, Git
Hardware: Solidworks, Fusion 360, 3D printing, laser cutting, CNC, machining, soldering, electronics and sensor integration
