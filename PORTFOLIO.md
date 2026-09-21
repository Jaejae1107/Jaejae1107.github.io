# Bilingual portfolio

The existing Jekyll / GitHub Pages deployment is retained. The portfolio uses a standalone layout with English at `/` and Korean at `/ko/`. Both languages have project indexes, five project detail pages, résumé landing pages, and Detail pages with a portrait, brief biography, and hobbies. Original English project records remain available in an expandable archive on each English detail page. The existing résumé PDF remains in English and is labeled accordingly.

## Editing

- `_data/portfolio.json`: interface text, biography, experience, and bilingual project summaries.
- `_layouts/portfolio.liquid`: shared page structure and language-specific metadata.
- `assets/css/portfolio.css`: responsive design, including reduced-motion behavior.
- `assets/js/portfolio.js`: progressive-enhancement project filters. Without JavaScript, all projects remain visible.
- `_projects/*.md`: original English project records.
- `_pages/*-ko.md` and `_pages/ko-project-*.md`: Korean route definitions.

The language switch opens the equivalent page in the other language. URLs are explicit, shareable, and work without JavaScript. No automatic language redirect is applied.

## Validation

Use Ruby 3.3.5 and the repository's existing dependencies:

```sh
bundle install
bundle exec jekyll build
python3 bin/check_portfolio.py
bundle exec jekyll serve
```

The check verifies 18 routes, English/Korean content parity, page language, heading structure, alternate-language links, local resources, and the résumé PDF signature. It also runs after the Jekyll build in the existing deploy workflow.

## Presentation and content

The homepage uses a restrained GitHub README-style layout: a name and professional focus, introductory paragraphs, a dated Professional Journey table, interests, and compact project links. System fonts, a white background, simple borders, and print styles keep the page useful for workplace introductions and presentation handouts.

English biography and journey entries follow the supplied professional profile; Korean text is maintained alongside them. Current work is described as semiconductor-industry analytics without naming an unconfirmed employer or job title. The homepage does not display education, graduation dates, or residence. The legacy résumé PDF remains available at its original URL but is no longer promoted in the navigation. `/cv/` and `/ko/cv/` show the updated Professional Journey.
