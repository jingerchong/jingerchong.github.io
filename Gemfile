source "https://rubygems.org"

# Match the GitHub Pages dependency set; it pins Jekyll 3.10 and Minima 2.5.1.
gem "github-pages", "~> 232.0", group: :jekyll_plugins
gem "minima", "~> 2.5"
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Windows and JRuby need time zone data.
platforms :windows, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Ruby 3 no longer bundles WEBrick for local serving.
gem "webrick", "~> 1.8"
