#!/usr/bin/env python3
"""Check bilingual portfolio pages after `bundle exec jekyll build`."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / '_site'
data = json.loads((ROOT / '_data/portfolio.json').read_text())
assert data['en'].keys() == data['ko'].keys(), 'Missing translated interface text'
for project in data['projects']:
    assert project['en'].keys() == project['ko'].keys(), project['id']
    assert len(project['en']['sections']) == len(project['ko']['sections']), project['id']


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.lang = None
        self.h1 = 0
        self.ids = set()
        self.links = []
        self.alternates = {}
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate id: {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.links.append(attrs['href'])
        if tag == 'link' and 'hreflang' in attrs:
            self.alternates[attrs['hreflang']] = attrs['href']


routes = ['/', '/projects/', '/cv/', '/detail/'] + [f'/projects/{p["id"]}/' for p in data['projects']]
for route in routes:
    for lang, prefix in [('en', ''), ('ko', '/ko')]:
        url = prefix + route
        path = OUTPUT / url.lstrip('/') / 'index.html'
        assert path.is_file(), f'Missing page: {url}'
        text = path.read_text()
        assert 'Liquid error' not in text, f'Liquid error: {url}'
        page = Page(text)
        assert page.lang == lang, f'Wrong language: {url}'
        assert page.h1 == 1, f'Expected one h1 in {url}, got {page.h1}'
        for alternate, expected in [('en', route), ('ko', '/ko' + route), ('x-default', route)]:
            assert urlsplit(page.alternates[alternate]).path == expected, f'Wrong hreflang in {url}'
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                assert not parsed.fragment or unquote(parsed.fragment) in page.ids, f'Broken anchor: {url}{link}'
                continue
            target = OUTPUT / unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else path.parent / unquote(parsed.path)
            assert target.exists(), f'Broken local resource: {url} -> {link}'
assert (OUTPUT / 'assets/pdf/Jaewon_Cho_CV.pdf').read_bytes().startswith(b'%PDF'), 'Résumé was overwritten'
print(f'PASS: {len(routes) * 2} pages, bilingual content parity, headings, hreflang, local links, assets, and PDF integrity')
