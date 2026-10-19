# Deft house style

The shared visual system for every Deft site: deftsuite.com first, then each product page,
and DeftBio (deftbio.ai) as a vertical on the same base.

**Status (2026-10-19):** foundation adopted from the DeftBio site. The NEA-portfolio reference
review is in `docs/REFERENCES.md` (11 B2B / developer-tool / security sites, all confirmed
NEA-backed).

## Decided (Ethan, 2026-10-19)

1. **Palette — applied in `deft.css`.** Warm off-white page `#F6F4EF`, white surfaces, warm rules
   `#E2DED5`, ink `#14171C`. Deft blue `#12386B` stays as the brand colour, for continuity with
   DeftBio. Teal is dropped. One state accent, stamp vermilion `#D9441C`, for stale, changed or
   needs-attention only — never decoration.
2. **Heading case.** Title Case on every heading and button.
3. **Type — not standard AI.** Rejected as AI-template defaults: Inter, Geist, Space Grotesk,
   DM Sans, Plus Jakarta Sans, Manrope, Outfit, Poppins, Sora, Satoshi, General Sans, Cabinet
   Grotesk. Chosen from `docs/type-specimen.html`: **Schibsted Grotesk** for display and body
   (headings 800 at -0.035em, subheads 700), **IBM Plex Mono** for labels, data and control IDs.

## Still proposed

- **Structure.** Hairline rules and frames instead of rounded cards with soft shadows; cards only
  where they hold product UI.

## Page patterns from the reference review

- **Hero:** text left, a working HTML artefact right that runs across the suite (control → evidence
  → policy → trust-portal row). Never a PNG, never a mood image.
- **The suite:** one ruled ledger of products, each row a name in mono, its one job and a live value;
  connections drawn as hairlines with corner ticks.
- **Sections demonstrate:** a mono label naming the problem, the problem shown as data, then the
  Deft version. One section, one artefact.
- **Proof sits inside the panel it proves,** and every number states its boundary.
- **Pricing on the page** as a comparison table with real quantities, against the cost of the
  separate tools it replaces.
- **Density:** 64–96px section spacing, more information per screen.
- **Vary section types;** no two adjacent sections share a layout.
- **Readable by agents:** `/llms.txt` and a markdown twin of each page; optional plain mode.
- **Ownable idiom:** ruled ledgers, stamp marks, control IDs and short hashes on evidence.

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
