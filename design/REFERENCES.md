# NEA portfolio reference sites for deftsuite.com

Research date: 19 Oct 2026. Purpose: find what makes the best NEA-backed B2B / devtools / security / infra marketing sites *distinctive*, so deftsuite.com does not read as a generic AI landing page. This supersedes the genre-average approach of `deft-promo-site/docs/design-brief-source.md` (see section 5).

## 1. Method and evidence

- **NEA backing**: every company below was confirmed in the portfolio JSON embedded in https://www.nea.com/portfolio (fetched 19 Oct 2026; 948 company records parsed). The status field is quoted next to each company. No company is included on reputation alone.
- **Design facts**: for each site I fetched the homepage HTML plus its linked CSS (curl), extracted `@font-face` families, `font-family` usage, hex frequencies, CSS custom properties, and h1/h2/h3 text. I then loaded each page in Chrome at 1179px wide and ran a DOM probe on the computed h1 style (family, size, weight, tracking, alignment, x-position) and h2 alignment, and took screenshots of the hero and one or two scrolls down.
- Anything I did not observe directly is marked **(inferred)**. Hex values are the most frequent values in the fetched CSS/HTML or declared tokens. They are not official brand specs.

Fetched but not shortlisted (still NEA-backed, all "Private" unless noted): Namespace (centred hero on a blue glow; its voice is good, e.g. h3 "Yes, we have Macs*", but the layout is genre-average), Horizon3.ai (centred, with an italic serif accent word; h2 "Evidence, not opinion."), Zania (GRC agents, the closest category neighbour; covered under "do not do"), Datafold, Assembled, Weaviate, Together AI, Ledgy, Coda, Anyscale, Databricks.

## 2. The shortlist (11 references)

### 1. Sentry: https://sentry.io/welcome/ (NEA: Private, Infrastructure)
- **Type**: display face "Dammit Sans" (custom, h1 88px/700, h2 60px), body Rubik; mono Monaco/Menlo stack. Code blocks use a GitHub-dark syntax palette.
- **Palette** (tokens declared in CSS): `--color-rich-black #1f1633` (the page bg, a purple-black, not neutral), `--color-blurple #6a5fc1`, `--color-dk-blurple #4e2a9a`, plus a warm accent run: `--color-lt-pink #fa7faa`, `--color-md-pink #e1567c`, `--color-lt-orange #ffb287`, `--color-lt-yellow #ffdb4a`, and lime `#c2ef4e`.
- **Hero**: a centred h1 "Code breaks, fix it faster" with "breaks," set in a different weight, colour and baseline. Sub-line: "Application monitoring software considered 'not bad' by millions of developers." Below it is a custom illustrated character, flanked by real product panels (Errors, Replays, Seer root-cause trace).
- **The distinctive move**: a persistent **"Marketing Mode" toggle**. Switching it off goes to https://sentry.io/no-marketing-mode/, a left-aligned page that reads "NO MARKETING. NO VALUE PROPS. NO LOGO RIVERS." with a mono status line `marketing.js disabled`, three short lines of copy, and a `/chat beta` box for asking product questions.
- **Pricing** (https://sentry.io/pricing/): four tiers with real numbers (Free / $26/mo / $80/mo / Custom). Then a comparison table with actual quantities and overage rates ("5k errors", "5GB +$0.50/GB additional") and a separately priced add-on ("$40/active contributor/month").
- **Borrow**: self-aware copy aimed at technical founders who distrust marketing, and a "plain mode" for the page. Show metered numbers, not adjectives.

### 2. Flox: https://flox.dev/ (NEA: Private, Infrastructure)
- **Type**: GeistSans (h1 64px/600, tracking -3.2px, left-aligned at x=77) with GeistMono doing a lot of the work. In the CSS, `var(--font-mono)` is used 73 times vs `var(--font-body)` 40.
- **Palette** (tokens): `--color-black #1b1b1b`, terminal `--term-bg #0c0c0c`, `--color-purple #711aff`, `--color-rose-red #ff4fae`, `--color-orange #ff7c32`, `--color-yellow #ffd02b`, `--green-ink #15803d`. The gradient is confined to two words of the h1 ("developer.", "agent.").
- **Hero**: left text ("One environment. Every developer. Every agent."), right a **terminal** running `curl -fsSL https://get.flox.dev | sh` → `Flox installed`, with a `sha256:9f3c2a` chip and footer chips.
- **The distinctive move**: sections are **demonstrations, not feature cards**. "The drift / One setup, three machines" is a real table of python/nodejs/openssl/rust/go versions across Laptop / CI / Agent, with mismatches in bold, ending in an orange dot and "Nothing matches." Beside it, "The weight / Pinning it by hand" lists Dockerfile, `nvidia/cuda:12.2 3.1 GB` and so on, vs "With Flox: `manifest.toml` 16 lines". The small orange labels (THE DRIFT, THE WEIGHT) name the problem; they are not category eyebrows.
- **Also**: "Ask ChatGPT / Ask Claude / Ask Perplexity" buttons appear in the page source.
- **Borrow**: for each Deft product, draw the before/after as data (an evidence table with stale rows, a policy with an unsigned version). That replaces three icon cards.

### 3. Tiger Data (TimescaleDB): https://www.tigerdata.com/ (NEA: Private, AI)
- **Type**: GeistSans (h1 80px/700), Geist Mono, plus the Geist *Pixel* family (`GeistPixelSquare`, `GeistPixelGrid`, `GeistPixelLine`…) and "Cygnito Mono".
- **Palette**: near-black `#0a0a0c` (the most frequent value by far), zinc greys `#71717a #f4f4f5 #a1a1aa`, a single acid-yellow highlight `#f4ff7d`, and an orange `#fa500f`.
- **Hero**: centred, but the proof under it is specific and mono-set: "Real life scale of a single TimescaleDB Instance: 3 TRILLION METRICS PER DAY · 1 QUADRILLION DATA POINTS STORED · 3 PETABYTES DATA VOLUME". That is a stat strip with a claim boundary ("a single instance"), not vanity totals.
- **The distinctive move**: section labels written as code comments (`// PRIMITIVES`), and an **asymmetric split**: a big left heading ("Built for the hardest machine-data workloads") plus CTAs, with a **ruled list** on the right (Automatic partitioning, Row-columnar storage, Tiered storage…). Each row has a small outlined glyph, a title and one line, separated by 1px rules. There are no cards.
- **Borrow**: the left-heading / right-ruled-list pattern for the suite's capabilities, and mono labels that read like code.

### 4. Metronome: https://metronome.com/ (NEA: Acquired; the header now reads "Metronome a stripe product")
- **Type**: Saans (h1 48px/500, tracking -0.48px, left-aligned at x=37); Fk Grotesk appears too.
- **Palette**: off-white page `#fafbf8`, ink `#0d171a`, slate `#565f5f` (most frequent), deep greens `#003834 #002220`, pale lime `#c3ee8f` (used as the solid "Contact sales" nav block) and `#f1ffd0`.
- **Hero**: left-aligned text with a whitepaper chip above the h1. On the right is a green panel of composed **real product UI**: a Real-time Usage table, a donut and bars.
- **The distinctive move**: each feature section is one wide panel. On the left is a heading ("Ship pricing as fast as you ship product"), a paragraph, a text link, and a **customer quote inside the same panel** (HubSpot). On the right is overlapping product UI with actual data: "LLM pricing (204 customers)", rows "LLM - LG Input Tokens $.050/1M", a "Katie Goodman PAY-AS-YOU-GO PLAN" credit card. Proof sits next to the feature it proves, not in a separate testimonial band.
- **Caveat**: Metronome does use a centred "WHY METRONOME" eyebrow and heading once.
- **Borrow**: pair every product panel with one named proof, and fill mock UI with plausible real values (a DeftQuote line item, a DeftTrust evidence row).

### 5. Pulumi: https://www.pulumi.com/ (NEA: Private, Infrastructure)
- **Type**: Inter (h1 48px/600, tracking -2.4px, left at x=110). This is the counter-example: Inter can work when the content carries the page. Monaspace Neon Var is used for code and labels, and "Vibur" appears in the CSS.
- **Palette**: violet `#5a30c5`, blue `#1e57eb`, green `#1c7d41`; the code palette is GitHub-dark (`#b392f0 #f97583 #79b8ff`).
- **Hero**: left-aligned with a mono "NEW: NATIVE SUPPORT FOR TERRAFORM AND HCL" pill. Below it a typed prompt, "Give me a VPC with a subnet in every AZ.", becomes generated code with language tabs (TS PY GO C# JAVA HCL YAML).
- **The distinctive move**: the logo wall is a **hairline-ruled grid** (6×2 cells with 1px dividers) under a mono caption "TRUSTED BY OVER 4,000 INNOVATIVE COMPANIES". The three-column features have **no icons and no cards**: bold title plus body text on white.
- **Borrow**: hero = an input that becomes an output (a question to DeftAgents → an answer citing a policy, or a SOC 2 control → its evidence). Use ruled grids instead of floating cards.

### 6. Merge: https://www.merge.dev/ (NEA: Private, Infrastructure)
- **Type**: FH Oscar Pro display at **weight 400** (h1 64px/400, tracking -1.92px, left at x=85). Body Inter, with Graphik, IBM Plex Serif and SF Mono also declared.
- **Palette** (tokens): `--colors--charcoal #2c2a25` and `--colors--eggshell #eaebe4`. Warm neutrals `#eaeae9 #faf8f5 #e8e3de` dominate, with `--colors--primary #075ff7` and an orange `#ff6e06` used sparingly.
- **Hero**: left text, a pill "Book a demo" plus a ghost "Start for free", and a dot-matrix illustration field on the right.
- **The distinctive move**: a logo grid where **each logo carries a "Case study →" or "Testimonial" chip**, so the logo wall is a navigable index of proof rather than decoration. The nav exposes "Security SOC 2 · HIPAA · RBAC" as a first-class item.
- **Borrow**: a light-weight display face on warm off-white (not bold Inter on pure white). Every logo or claim links to its evidence.

### 7. Plaid: https://plaid.com/ (NEA: Private, Infrastructure)
- **Type**: fully custom. "Plaid Sans" (preloaded from Hairline to Bold, with obliques) at h1 70px/500, tracking -2.8px, left at x=86. Cern for body, "Bowery Street"/"Bowery Lane" as a display face for big numerals (a "1 in 2" set at 7rem in a gradient), and Inconsolata mono.
- **Palette**: navy `#00172e`, blue `#0a85ea #156ef5`, cyan `#63daff`, mint `#42f0cd #abffdb`, violet `#8358ef`, coral `#f44e66`; teal tokens `#05565c #088181` for card titles and icons.
- **Hero**: left-aligned, a two-tone headline ("Turn data into **revolutionary** financial products"), and a **currency-engraving illustration of Benjamin Franklin** holding a phone, bleeding off the right edge.
- **Product**: 2-up product cards, each a live-looking UI fragment (risk-scored people grid "LOW / HIGH / MEDIUM RISK", the Link onboarding modal). Headings mix weights inside one line ("**Fraud protection** built on millions of data points").
- **Borrow**: one ownable illustration idiom tied to the domain (for Deft, something like a ledger, stamp or registry engraving). Use weight contrast within a headline instead of gradient text.

### 8. Cloudflare: https://www.cloudflare.com/ (NEA: IPO/Public)
- **Type**: STK Bureau Sans (h1 56px/500, body too), FT Kunst Grotesk, Apercu Mono Pro, and "Departure Mono" (a pixel mono).
- **Palette**: near-black page `#151414` (rgb 21,20,20), orange `#ff4801 #ff7038 #ff5e1f`, warm cream `#fffbf5 #f0e3de #e9d1bb`.
- **Hero**: centred on a full-bleed orange slab with a sunrise glow. This is the part *not* to copy.
- **The distinctive moves**: (a) **blueprint framing**: content sits in hairline-ruled cells with small square **corner ticks** at the frame intersections; (b) short, dry headings: "Region: Earth", "Pay only when your code runs" with the aside "(Not to keep servers warm.)", "Fighting infra with 'cloud'"; (c) customer proof as a **tab strip of logos** (Shopify, Character AI, Intercom…), where each tab swaps in a full quote. It is not a static logo river.
- **Borrow**: hairline frames with corner ticks as the structural motif for a suite diagram; parenthetical asides in pricing copy.

### 9. Expel: https://expel.com/ (NEA: Private, Infrastructure)
- **Type**: Alte Haas Grotesk for the h1 (80px/**800**, tracking **-4px**, left at x=35, four short lines). Maison Neue for body and Maison Neue Mono for labels and small h2s (16px), plus a "Digital 7" LCD face for numbers.
- **Palette**: `#181818` (1,128 occurrences), signal green `#5ef784`, warm stone section bg `#e7e3d7`, greys `#5d5d5d #c5c5c5`.
- **Hero**: black, left-aligned, "From detection to done. **Faster.**" (last word in green), with a video panel on the right.
- **Voice**: "Trust isn't built through sales decks. It's earned by doing the work.", "Forrester says we're a Leader. We agree.", "Actually useful resources". The mono label "AI-INTENTIONAL BEATS AI-HYPE" is an eyebrow, but it states an opinion rather than a category.
- **Borrow**: very heavy, very tight display type against a mono label system, and a warm stone neutral instead of grey-50. The voice is confident and slightly wry.

### 10. Metabase: https://www.metabase.com/ (NEA: Private, SaaS)
- **Type**: Lato (h1 60px/700) with Merriweather (Google Fonts) available as a serif, and Fira Code / Roboto Mono.
- **Palette** (tokens): `--base-color-blue-60 #509ee3` (the brand blue), `--base-color-neutral-15 #22242b`, neutrals `#5a6072 #8d93a5 #e2e4e9`.
- **Hero**: centred text, but the visual below is a **working product surface built in the DOM**. A "Total Accounts 1,228" tile, a stacked bar chart "Accounts added per year, by source", and a "Chat with Metabot" panel answering "Which source added the most accounts in 2026?" with an actual answer. I confirmed the tile text is DOM text, not an image. Further down is a "Watch a 1-minute demo" row with a face-cam thumbnail.
- **Caveat**: all five h2s are centred. The page rhythm is genre-average; borrow the hero artefact, not the layout.
- **Borrow**: a static GitHub Pages site can still show the product live. Build the hero as real HTML UI with a scripted question and answer, not a PNG.

### 11. Kong: https://konghq.com/ (NEA: Private) and Factory: https://factory.ai/ (NEA: Private, AI)
These two are grouped because each is worth borrowing for one mechanic only.
- **Kong**: fonts "funnel" (h1 102px/800), League Gothic, Space Grotesk, Roboto Mono. Palette acid `#ccff00` on green-black `#001408`, with `#e7ede5` for light text. Two mechanics worth noting:
  - A vertical **"HUMAN / AGENT" mode switch** fixed on the left edge. The source contains the string "Human Mode to interact with this section", and headings are stored with markdown prefixes ("# AI Connectivity", "## Agentic AI"). **(Inferred)**: Agent mode serves a markdown or plain rendering for LLM readers.
  - A **"WITHOUT KONG / WITH KONG"** segmented toggle that swaps the architecture diagram.
  - The look is too loud for Deft. Borrow the mechanics.
- **Factory**: Geist, Geist Mono, Geist Pixel Square. Monochrome `#f5f5f5` page with ink `#1f1d1c` and a single orange `#ef6f2e`. Mono button labels in caps ("LOG IN / SIGN UP"), and a copyable `curl` install line under the hero CTAs. Feature boxes are numbered in mono ("01 CONTROL", "02 GOVERNANCE", "03 VALUE"), and a heading types in letter by letter on scroll. The hero is centred with a letter-spaced h1 ("MAKE YOUR SOFTWARE IMPROVE ITSELF"). Borrow the restraint of greyscale plus one accent and the numbered mono labels; do not copy the centred hero.

## 3. What actually separates the distinctive sites from the genre

Observed across the 11, versus what the generic template does:

1. **The hero shows a mechanism, not a mood.** Examples: Flox's terminal install, Pulumi's prompt-to-code, Metabase's live dashboard and chat, Metronome's pricing table with real unit prices, Sentry's trace panels. None of the strong sites rely on gradient blobs alone. Cloudflare and Namespace do have glow heroes; they are the weakest part of each page.
2. **Centring is not the tell; content is.** Sentry, Metabase, Factory, Cloudflare, Tiger Data and Kong all have centred h1s. What makes them non-generic is custom display type and a specific artefact under the h1. Seven of 11 (Pulumi, Merge, Metronome, Plaid, Flox, Expel, and Zania among the rejects) left-align, usually in a text-left / artefact-right split.
3. **Custom or uncommon type, almost always paired with a mono.** Dammit Sans + Rubik; Saans; FH Oscar Pro at weight 400; Plaid Sans + Bowery Street; STK Bureau Sans + Apercu Mono; Alte Haas Grotesk + Maison Neue Mono; Geist + Geist Pixel. Only Pulumi uses plain Inter, and it gets away with it through mono labels and code.
4. **Labels are mono and specific when used.** Examples: `// PRIMITIVES`, `THE DRIFT`, `01 CONTROL`, `marketing.js disabled`, "AI-INTENTIONAL BEATS AI-HYPE". They name a problem, a step or a stance, never a section type ("FEATURES", "WHY US").
5. **Structure is drawn with rules, not floating cards.** Pulumi's ruled logo grid, Tiger Data's ruled list, Cloudflare's hairline cells with corner ticks, Merge's logo grid. Cards appear, but with 1px borders and no coloured rails.
6. **Proof is attached to the claim.** Metronome's quote inside the feature panel, Merge's per-logo "Case study" chip, Cloudflare's logo tabs that open quotes, Tiger Data's "single instance" bounded stats.
7. **Copy has a point of view and a sense of humour.** Examples: "considered 'not bad' by millions of developers", "NO LOGO RIVERS.", "(Not to keep servers warm.)", "Trust isn't built through sales decks.", "Yes, we have Macs*", "Nothing matches."
8. **Neutrals are tinted.** Purple-black `#1f1633` (Sentry), green-black `#001408` (Kong), warm off-white `#fafbf8` (Metronome), eggshell `#eaebe4` / charcoal `#2c2a25` (Merge), stone `#e7e3d7` (Expel), cream `#fffbf5` on `#151414` (Cloudflare). Pure `#fff` on slate is the generic default.
9. **The page treats machines and sceptics as readers.** Sentry's no-marketing mode, Kong's Human/Agent switch, Flox's Ask-an-LLM buttons, Kong's markdown-prefixed headings.
10. **Pricing pages are conventional (tier columns), but the numbers are real.** Sentry gives $26/$80, per-GB overages and a per-contributor add-on; Namespace $100/$250 with unit-minute allowances; Flox has three tiers; Cloudflare puts pricing philosophy on the homepage. No reference hides behind "Contact us" for every tier except Enterprise.

## 4. Design principles for deftsuite.com

1. **Type pairing: one characterful grotesk at two weights plus a mono that carries labels.** On a free/static budget, use Geist + Geist Mono (Flox, Tiger Data, Factory precedent) or Space Grotesk / Familjen Grotesk + JetBrains Mono / IBM Plex Mono. For an editorial edge, set display at weight 400–500 with tight tracking (Merge), or a heavy 800 with -4% tracking (Expel); never the default 600/700 Inter. If Inter stays for body, the display and mono must differ from it.
2. **Asymmetric hero: text left, a working artefact right.** The artefact is real HTML/JS. A good choice is a scripted sequence across the suite: a SOC 2 control → the evidence it pulled → the policy page that satisfies it → the trust-portal row a customer sees. It should run in a frame you could mistake for the product (Metabase, Pulumi, Flox).
3. **Show the suite as one ledger with rules, not six icon cards.** Use a ruled list or table, Tiger Data style: each row is a product name in mono (Trust, Docs, Desk, Agents, Quote, Uptime), the one job it does, and a live value (e.g. "42 controls · 3 stale"). Draw connections as hairline lines with corner ticks (Cloudflare) between rows. A "with Deft / without Deft" toggle (Kong) can redraw the tangle of separate vendors into one graph.
4. **Every section demonstrates instead of describing.** Model each section on Flox's "THE DRIFT". Name the problem in a mono label, show it as data (a vendor-questionnaire spreadsheet with 214 rows, an outdated policy PDF, five SaaS invoices), then show the Deft version. One section, one artefact.
5. **Attach proof to the claim it proves.** Put a quote or bounded number inside the product panel (Metronome). Any stat states its boundary ("for a 6-person team", "in a single audit window", like Tiger Data's "a single instance"). If there are few customers, use first-party proof such as "this site's own uptime, live" or "our SOC 2 evidence, public".
6. **Pricing on the page, in numbers, with the arithmetic shown.** Show tiers as a comparison table with real quantities (Sentry): seats, controls, docs, agents and monitors per tier. Frame the price against the stack it replaces, e.g. "Vanta + Notion + Zendesk + PandaDoc + Better Stack ≈ $X/mo; Deft $Y". Add one dry parenthetical (Cloudflare).
7. **Density over air.** Developer and founder audiences reward information. Use tighter section spacing (64–96px rather than 128px) with more per screen: tables, mono metadata and real values. Long whitespace around a single sentence reads as template.
8. **Colour: tinted neutrals plus one signal colour used for state, not decoration.** Pick a warm or tinted base (stone, eggshell or ink-tinted near-black) and one accent that means "attention / changed / live", the way Expel's green, Factory's orange and Tiger Data's acid yellow work. Avoid gradients, except possibly confined to one word (Flox), and better avoided entirely.
9. **A voice that admits it is marketing.** Short, declarative, slightly wry headings written for technical founders, e.g. "Your SOC 2 auditor wants a folder. Here is the folder." Consider a Sentry-style "plain mode" toggle that strips the page to a text spec and price list. That is cheap on a static site and on-brand for "lean team".
10. **Make the page legible to agents.** Since governed AI agents are a product, ship `/llms.txt` and a markdown twin of each page, and say so in the footer or with a Human/Agent switch (Kong, Flox).
11. **Vary the section rhythm on purpose.** Alternate full-bleed artefact, left-heading/right-list, a single wide table, and a quote set large in the display face (Pulumi, Namespace). Two adjacent sections should never share the centred-heading-then-grid pattern.
12. **One ownable visual idiom.** Plaid has currency engraving, Sentry its illustrated characters, Cloudflare blueprint ticks. Deft could own a "registry / ledger" idiom: ruled ledgers, stamp marks, control IDs, sha-style hashes on evidence. It ties to the trust/evidence core and can be built in CSS.

## 5. Conclusions from the old brief (`design-brief-source.md`) to drop

| Old brief said | Drop because |
|---|---|
| "One large sans-serif (Inter-class grotesk)… use Inter everywhere" | Only 1 of 11 strong references uses plain Inter; the rest use custom or uncommon grotesks plus a mono. Inter-only is the clearest AI-template tell. |
| "Quantified stat strip (3–6 metrics)… count-up on scroll" is near-universal / mandatory | The strong sites bound their numbers to a context or embed them in product UI. A free-floating 4-up count-up strip is generic. |
| "Core value pillars (3 cards)… line icon + one-line benefit + Learn more" | Replace with demonstrations (Flox) or ruled lists (Tiger Data, Pulumi without icons). |
| "Eyebrow/overline: 13px 600 uppercase, primary blue" over sections | If labels are used at all: mono, specific, a problem or step name, and not on every section. |
| "Hero… product visual or abstract gradient"; "gentle gradient-mesh drift in hero" | The gradient option produced the blob hero. The hero must show a mechanism. |
| "Final full-width CTA band" | None of the distinctive moves were CTA bands. End on something useful, such as the pricing table or a plain-mode link. |
| "Cards: radius 12px, soft shadow, line icon top-left"; "rounded corners (8–16px) and soft shadows" everywhere | Use rules and hairline frames; cards only where they hold UI. |
| "Healthcare skews blue/teal/navy… `--primary-600 #1E5BCB`, accent teal" | That palette fits a biotech buyer. For technical founders, use tinted neutrals and one state colour. |
| "Logo bar: grayscale at ~60% opacity" directly under the hero | Make logos navigable proof (Merge chips, Cloudflare tabs) or skip them until there are enough. |
| "Alternating feature sections with screenshots in rounded shadowed cards" as the core rhythm | Mechanical left/right alternation is part of the generic rhythm; vary section types instead. |

**Keep from the old brief**: real product UI over abstract art; one disciplined accent; tabular numerals for figures; make security and compliance visible (for Deft it is a product, so show the evidence itself rather than badges).

## 6. Do not do

- Centred h1 over a radial glow or gradient blobs (the weakest part of the Cloudflare and Namespace pages).
- An uppercase eyebrow over every section, or eyebrows that name the section type ("FEATURES", "WHY DEFT").
- Three icon cards with rounded icon tiles; six product cards in a 3×2 grid.
- ✓/✕ bullet comparison lists. Use a real table of what changes, or a with/without toggle.
- A 4-up stat strip with unbounded numbers or count-up animation.
- A dark gradient CTA band before the footer.
- Coloured left or top border rails on cards.
- Inter (or any one sans) at default weights for everything.
- Sub-text that restates the heading. Zania's "Compliance Demands Keep Growing, Your Resources Don't." followed by a paragraph repeating it is the category's own example, and Zania is the nearest GRC neighbour, so differentiate from it directly.
- Title Case on every heading (Zania); sentence case reads more human.
- Screenshots as PNGs where an HTML artefact could run.
- Logo rivers with no link to a story.

## Sources

- NEA portfolio (company records embedded in page JSON): https://www.nea.com/portfolio
- https://sentry.io/welcome/ · https://sentry.io/no-marketing-mode/ · https://sentry.io/pricing/
- https://flox.dev/ · https://flox.dev/pricing/
- https://www.tigerdata.com/
- https://metronome.com/
- https://www.pulumi.com/
- https://www.merge.dev/
- https://plaid.com/
- https://www.cloudflare.com/
- https://expel.com/
- https://www.metabase.com/
- https://konghq.com/
- https://factory.ai/ (redirected to factory.com)
- Also fetched: https://namespace.so/ · https://namespace.so/pricing · https://horizon3.ai/ · https://www.zania.ai/ · https://www.datafold.com/ · https://www.assembled.com/ · https://weaviate.io/ · https://www.together.ai/ · https://ledgy.com/ · https://coda.io/ · https://www.anyscale.com/ · https://www.databricks.com/
