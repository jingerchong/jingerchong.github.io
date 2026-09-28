# jingerchong.github.io

Source for Jinger Chong's portfolio, built with Jekyll and GitHub Pages.

Agent guidance and the current codebase map are in [AGENTS.md](AGENTS.md).

## Run locally on Windows

Use Ruby+Devkit 3.3 with the MSYS2/MINGW development toolchain. The current
GitHub Pages dependency set requires Ruby below 4. If Ruby 3.3 is installed at
`C:\Ruby33-x64`, run these commands in PowerShell from a new terminal:

```powershell
$env:Path = 'C:\Ruby33-x64\bin;' + $env:Path
ruby -v
cd 'C:\Users\Jinger\Documents\jingerchong.github.io'
gem install bundler -v 2.5.22
bundle install
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat build
bundle exec -- C:\Ruby33-x64\bin\jekyll.bat serve
```

`ruby -v` must report Ruby 3.3 before installing the gems. Open
<http://localhost:4000> after the server starts, and press Ctrl+C to stop it.
Restart the server after changing `_config.yml`. The generated `_site/`
directory is ignored by Git.
