# Agent guide for this portfolio

## Purpose and audience

This is Jinger Chong's personal website, a public portfolio for robotics research and engineering opportunities, including summer internships. Make it easy for a recruiter or researcher to understand Jinger's current focus, strongest technical work, specific contributions, and how to get in touch. Keep the voice personal and direct. Preserve the owner's facts and writing style; do not invent credentials, results, publications, dates, affiliations, availability, or project details. The existing content is a historical snapshot, so verify time-sensitive claims with the owner or a supplied source before changing them. Do not silently turn old dates or a past "Present" role into a current claim.

## Stack and build

- Static Jekyll site hosted with GitHub Pages at `jingerchong.com` (`CNAME`). No JavaScript app or package manager is used.
- Dependencies are pinned in `Gemfile` and `Gemfile.lock`; the site uses GitHub Pages gem 232, Jekyll 3.10, Minima 2.5.1, Liquid templates, Markdown, and Sass. Use Ruby 3.3 with the development tools installed; this dependency set does not support Ruby 4. Prefer compatible Jekyll and GitHub Pages features over adding plugins or a new frontend stack.
- From the repository root, run `bundle install` if needed, then `bundle exec jekyll build` to validate changes. Use `bundle exec jekyll serve` for visual checks. `_config.yml` changes require restarting the server.
- Generated `_site/`, Jekyll caches, and `vendor/` are ignored. Do not edit generated output. If Ruby/Bundler is unavailable, say that the build could not be run; still check changed front matter, Liquid references, local links, and image paths manually.

## Where things live

- `_config.yml`: site identity, domain/base URL, social links, navigation order, project category order, collection definitions, and default layouts.
- `index.markdown`, `about.markdown`, `projects.markdown`, `photography.markdown`: top-level pages. The home introduction is in `index.markdown`; the About and Projects pages are assembled mainly by their layouts.
- `_posts/YYYY-MM-DD-slug.markdown`: individual project stories. `_layouts/home.html` selects posts with `featured: true`; `_layouts/projects.html` groups posts by `categories_order`; `_layouts/category.html` renders category archives. The post filename/slug also determines the image directory expected by templates.
- `_archives/*.markdown`: category landing pages. A new category needs a matching archive and, if it should appear on the Projects overview, an entry in `categories_order`.
- `_schools/`, `_jobs/`, `_skills/`: About page data, rendered by `_layouts/about.html` and `_layouts/resume.html`. Entries with `show: true` appear; `order` controls display order (schools and jobs are reversed after sorting; skills are not). Keep hidden entries unless asked to remove them.
- `_grids/<post-slug>/grid-N.markdown`: optional named sections beneath a post. `_layouts/post.html` finds grid files whose path contains the post slug, sorts by slug, and collects matching static images from `assets/images/<post-slug>/grid-N/`.
- `assets/images/<post-slug>/cover.webp`: cover image convention used on project cards and post pages. Other images live under the matching grid directory. `assets/` also holds branding and icons; `downloads/` holds downloadable documents.
- `_includes/` and `_layouts/`: shared Liquid/HTML. `with-banner.html` wraps the home page, while the Minima theme supplies the default layout and head include. `assets/main.scss` imports `_sass/colors.scss`, `_sass/fonts.scss`, and `_sass/layout.scss`, then Minima.

## Content and design rules

- Prioritize the robotics/perception story and evidence of research or engineering impact when updating the home page, About page, featured projects, or experience. Lead project descriptions with the problem, Jinger's own role, technical approach, and a concrete result when documented. Distinguish individual work from team work.
- Keep claims accurate and specific. Existing project posts and job entries are source material, not proof that information is still current. Ask for missing facts rather than guessing metrics, internship dates, thesis topics, or availability.
- Preserve valid YAML front matter (`---` delimiters). For a new post, set `title`, `date`, `categories` as a list, and `featured` deliberately. Use category spelling that matches `_config.yml` and `_archives/`. Check that the slug and image paths match before featuring a post.
- A new post normally needs `assets/images/<slug>/cover.webp`. Add `_grids/<slug>/grid-N.markdown` only when a section has useful content or images, and put its images in the matching `assets/images/<slug>/grid-N/` directory. Avoid committing huge originals when a web-sized image will do.
- Keep internal links and asset paths working with the site's `url`/`baseurl` settings and existing Liquid filters. Check rendered links rather than assuming a Markdown source path is correct. Do not change established permalinks casually; external links and search results may depend on them.
- Maintain readable, responsive pages and semantic HTML. Give new images descriptive alt text, ensure links and controls work by keyboard, and check desktop and narrow mobile layouts. Existing Sass breakpoints are 800px, 600px, and 480px; follow the existing palette and typography unless a redesign is requested.
- Do not replace the portfolio with generic recruiting copy or bury contact information. The header navigation and footer contact/social links are shared across pages.

## Before finishing a change

1. Review the rendered home, About, Projects, affected post/category, and mobile layout as applicable.
2. Run `bundle exec jekyll build` when the toolchain is available and resolve build warnings or errors introduced by the change.
3. Check new or changed links, image paths, front matter, category pages, and `featured`/`show` visibility. Confirm each public claim against supplied facts.
4. Report what changed and what was verified, including any build or visual check that could not be completed.
