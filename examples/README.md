# Content examples and layout reference

Copy `project.md` into `_projects/<slug>.md`, keep `published: false` while drafting,
and replace all example content before publishing. Use the commented YAML examples
at the top of each `_data/*.yml` file for publications, industry, research, education,
skills, teaching, service, and social links.

## Current labels and behavior

| Page | Sections |
| --- | --- |
| Home | Publications, Projects (first three featured), Experience |
| Projects | Featured (featured + normal tiers), More (archive tier) |
| About | Off the clock, Education, Skills, Teaching, Service |
| Research | Now, Before |
| Industry | Experience |

The More list places title/context on the left and dates at the right edge,
including on phones.

Home links use All projects and All experience. Navigation remains Research,
Industry, Projects, About. Contact shows the configured email as a mailto link.
Home has one bio paragraph ending with View my CV; internship availability
appears only in the banner. Banner tagline and status are configured in `_config.yml`.

Publication `paper` links to PDFs display PDF, while non-PDF paper targets display
Paper. Other PDF links retain their descriptive label and a (PDF) suffix.
CITE is a button that copies the entry's `bibtex` value to the clipboard; patents
have no citation button. The public site uses HTTPS for clipboard access.

Project links belong in front matter when they should appear above the hero.
Missing metadata and media are omitted; missing covers use blueprint tiles in
listings. Select pool, quadrotor, prediction, or safety with `placeholder`.
Use the shared gallery and video includes shown in `project.md`.

## Design references

`design/site-style-mockups-final.html` and `design/logo.svg` are preserved design
references. The mockup is historical: its citation dropdowns and some labels were
superseded by the choices above. Do not copy its dummy links, placeholder facts,
embedded images, or scripts into production. Use the live Liquid/Sass components
and the current `AGENTS.md` for implementation and validation.
