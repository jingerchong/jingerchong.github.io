# jingerchong.github.io

Source for Jinger Chong's portfolio, built with Jekyll and GitHub Pages.

## Run locally

Use Ruby 3.3 with the development tools installed. The GitHub Pages gem used by
this site does not support Ruby 4. On Windows, install Ruby+Devkit 3.3 from
[RubyInstaller](https://rubyinstaller.org/downloads/) and select the MSYS2
development toolchain. If another Ruby is also installed, check that `ruby -v`
shows Ruby 3.3 before continuing. For example, if Ruby 3.3 was installed at
`C:\Ruby33-x64`, run this in PowerShell:

```powershell
$env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
ruby -v
gem install bundler -v 2.5.22
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

Open <http://localhost:4000> while the server is running. Press Ctrl+C to stop
it. Restart the server after changes to `_config.yml`. The generated site is in
`_site/`, which is ignored by Git.
