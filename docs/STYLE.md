# Deft house style

The shared visual system for every Deft site: deftsuite.com first, then each product page,
and DeftBio (deftbio.ai) as a vertical on the same base.

**Status (2026-10-19):** foundation only. Tokens and components are adopted from the DeftBio site.
Page and section patterns are on hold until the NEA-portfolio reference review lands in
`docs/REFERENCES.md`.

## Layers

| File | Holds | Shared across Deft sites |
|---|---|---|
| `assets/css/deft.css` | Tokens, base type, buttons, links, nav, forms, footer, reveal motion | Yes |
| `assets/css/site.css` | This site's page and section layouts | No |
| `assets/js/deft.js` | Nav toggle, scroll state, reveal, footer year | Yes |

## Adopted from DeftBio

- **Palette.** One deep blue for brand and action; teal kept for live state and data, never decoration;
  roughly 90% of the page neutral.
- **Type.** Inter for body. Display face is its own token (`--font-display`) and may change after the
  reference review.
- **Components.** Buttons, text links, sticky nav, form fields, footer, 1px borders, soft shadows.

## Not adopted: patterns that read as AI-generated

Banned on every Deft site unless the reference review gives a specific reason to keep one:

- Radial gradient blobs or mesh behind the hero.
- A small uppercase eyebrow over every centred section heading.
- A row of three cards with a rounded icon tile on top.
- ✓ / ✕ bullet lists, and "old way vs new way" two-column compares.
- A 4-up stat strip with count-up numbers.
- A dark gradient call-to-action band closing the page.
- Coloured left or top borders on cards.
- The same centred-heading-then-grid rhythm in every section.
- Sub-text that restates the heading, count lines, or notes explaining the UI.
- Hover lift (translateY) on cards and buttons.

## Copy

Plain sentences, Title Case headings, no invented shorthand. Headline claims must be true of what
ships today; the product readiness table in the DeftSuite brief is the check.
