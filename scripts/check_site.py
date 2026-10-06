"""Check generated Jekyll pages for broken local links and launch placeholders."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
PUBLIC_HOST = "jingerchong.com"
BAD_TEXT = ("TODO:", "Project writeups are coming soon", "Lorem ipsum")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.text = []
        self.accessibility = []
        self.ids = set()
        self.in_anchor = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            if self.in_anchor:
                self.accessibility.append("nested anchor (malformed link)")
            self.in_anchor = True
            href = attrs.get("href", "")
            parsed = urlsplit(href)
            if parsed.scheme in ("http", "https") and parsed.hostname not in (
                PUBLIC_HOST, f"www.{PUBLIC_HOST}"
            ):
                rel = set(attrs.get("rel", "").split())
                if attrs.get("target") != "_blank":
                    self.accessibility.append(f"external link does not open in a new tab: {href}")
                if not {"noopener", "noreferrer"}.issubset(rel):
                    self.accessibility.append(f"external link lacks safe rel attributes: {href}")
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                self.accessibility.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "img" and "alt" not in attrs:
            self.accessibility.append("image without alt text")
        if tag == "iframe" and not attrs.get("title"):
            self.accessibility.append("iframe without a title")
        for name in ("href", "src"):
            if name in attrs:
                self.links.append((name, attrs[name]))

    def handle_endtag(self, tag):
        if tag == "a":
            self.in_anchor = False

    def handle_data(self, data):
        self.text.append(data)


def local_target(page, link):
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc or link.startswith("//"):
        return None
    if not parsed.path:
        return None
    path = unquote(parsed.path)
    if path.startswith("/"):
        target = SITE / path.lstrip("/")
    else:
        target = page.parent / path
    target = target.resolve()
    if not target.is_relative_to(SITE):
        return None
    if target.is_dir() or path.endswith("/"):
        target /= "index.html"
    return target


def main():
    if not SITE.is_dir():
        print(f"Missing build directory: {SITE}", file=sys.stderr)
        return 1

    errors = []
    for name in ("README.md", "AGENTS.md", "TODO.md", "Gemfile", "Gemfile.lock",
                 "scripts", "examples", "Claude outputs"):
        if (SITE / name).exists():
            errors.append(f"development-only content in published output: {name}")
    pages = list(SITE.rglob("*.html"))
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        label = page.relative_to(SITE)
        body = " ".join(parser.text)
        for phrase in BAD_TEXT:
            if phrase.lower() in body.lower():
                errors.append(f"{label}: visible drafting text: {phrase}")
        for issue in parser.accessibility:
            errors.append(f"{label}: {issue}")
        for kind, link in parser.links:
            if link == "#":
                errors.append(f"{label}: empty {kind} target")
            if "assets/placeholder.svg" in link:
                errors.append(f"{label}: placeholder asset: {link}")
            target = local_target(page, link)
            if target is not None and not target.is_file():
                errors.append(f"{label}: missing local target: {link}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(pages)} generated HTML pages and their local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
