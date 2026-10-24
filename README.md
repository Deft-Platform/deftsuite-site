# deftsuite.com

Marketing site for **DeftSuite**, the enterprise stack for founder-led teams.

Pure HTML/CSS/JS, no framework. Served by GitHub Pages from `main` at the repo root, custom
domain in `CNAME`.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000   (pages use root-relative paths, so open via the server, not the file)
```

Append `?static` to the home page to jump every animation to its end state (used for screenshots
and by reduced-motion users); `?static&stack` shows the separate-tools view.

## How it is built

`tools/build.py` is the single source of truth for the products, their copy, statuses, prices and the
separate-tools price research. Run it after any change to those:

```bash
python3 tools/build.py
```

It writes:

- `<slug>/index.html`: one page per product (web, marketing, revenue, demo, trust, docs, infra,
  sentinel, desk, agents)
- `assets/js/stack-data.js`: the stack's monthly cost by team size, 1 to 50, read by the home page
- the nav, products section and footer inside `index.html` (between the `<!-- NAME:START -->` markers)
- `sitemap.xml`, `robots.txt`, `llms.txt`

`index.html` is otherwise hand-written: the stack-collapse hero, the Deft MCP section, the
cost-as-you-grow chart and the start-with-one plan picker.

## Structure

- `assets/css/site.css`: shared tokens, nav, footer and product-page styles
- `assets/js/site.js`, `assets/js/stack-data.js` (generated)
- `assets/css/deft.css`, `assets/js/deft.js`: the earlier house-style foundation, kept for DeftBio alignment
- `design/`: style rules, NEA reference research, type specimen (blocked in robots.txt)
- `tools/stack-series.json`: cached copy of the price research series

Positioning, pricing decisions, module copy and licensing live in the private deft-platform umbrella
(`docs/DEFTSUITE.md`, `docs/MODULES.md`, `docs/LICENSING.md`).
