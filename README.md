# deftsuite.com

Marketing site for **DeftSuite**, the lean team's enterprise toolkit.

Pure HTML/CSS/JS, no build step. Served by GitHub Pages from `main` at the repo root,
custom domain in `CNAME`.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Structure

- `index.html` — home page (currently a holding page)
- `assets/css/deft.css` — Deft house style: tokens and shared components, used by every Deft site
- `assets/css/site.css` — this site's page layouts
- `assets/js/deft.js` — shared nav, reveal and footer behaviour
- `docs/STYLE.md` — the house style rules, including the patterns we do not use
- `docs/REFERENCES.md` — reference sites the style is measured against

Positioning, pricing and product lineup: `docs/DEFTSUITE.md` in the deft-platform umbrella.
