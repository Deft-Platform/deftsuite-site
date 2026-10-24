"""Build the generated parts of deftsuite.com.

One source of truth for the products, their copy and the price research. Writes:

- assets/js/stack-data.js   monthly cost of the separate-tools stack by team size (1..50)
- <slug>/index.html         one landing page per product
- sitemap.xml, robots.txt, llms.txt

The home page (index.html) is hand-written and reads stack-data.js.

Run from the repo root:  python3 tools/build.py
"""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://deftsuite.com"
CONTACT = "hello@deftsuite.com"
SUITE_PRICE = (99, 249, 499)
PRODUCT_PRICE = (39, 99, 199)

# ---------------------------------------------------------------------------
# The separate-tools stack. Published list prices checked 19 Oct 2026
# (docs/research/stack-prices.md in the deft-platform umbrella), plus WP Engine
# checked 24 Oct 2026. Vanta and Conveyor publish no price: Vendr estimates.
# ---------------------------------------------------------------------------
STACK = [
    # key, category, vendor, rate label, estimate?, glyph, Deft product slug
    ("WPEngine", "Website Hosting", "WP Engine Essential", "$28 / month", False, "globe", "web"),
    ("Vanta", "SOC 2 Automation", "Vanta", "about $12,000 / year", True, "shield", "trust"),
    ("Conveyor", "Trust Center And Questionnaires", "Conveyor", "about $15,000 / year", True, "list", "trust"),
    ("Atlassian Confluence", "Wiki And Policies", "Confluence", "$7.15 / user after 10 free", False, "doc", "docs"),
    ("Dropbox Sign", "E-Signature", "Dropbox Sign", "$17.50 / user, 2 minimum", False, "pen", "docs"),
    ("Zendesk", "Help Desk", "Zendesk", "$19 / agent", False, "chat", "desk"),
    ("GitBook", "Public Docs Site", "GitBook", "$65 / site + $12 / user", False, "book", "desk"),
    ("Atlassian Statuspage", "Status Page", "Statuspage", "free, then $29 / month", False, "pulse", "sentinel"),
    ("Better Stack", "Uptime Monitoring", "Better Stack", "$29 / responder", False, "clock", "sentinel"),
    ("PandaDoc", "Proposals And Quotes", "PandaDoc", "$49 / user", False, "quote", "revenue"),
    ("Arcade", "Interactive Demos", "Arcade", "$49 / month", False, "play", "demo"),
    ("beehiiv", "Email Newsletters", "beehiiv", "$49 / month", False, "mail", "marketing"),
]
WPENGINE_MONTHLY = 28.0
RESEARCH = Path("/Users/ethand320/.claude/jobs/21bd52cf/tmp/stack-prices.json")
SERIES_CACHE = ROOT / "tools" / "stack-series.json"

# ---------------------------------------------------------------------------
# Products. Status: Available, Early Access, In Build.
# Stories are told as "we", without naming the company they were built for,
# and without customer impact or security specifics (decided 24 Oct 2026).
# ---------------------------------------------------------------------------
STAGES = [
    ("win", "Win", "Send us a proposal."),
    ("review", "Pass Review", "Send your SOC 2 and security questionnaire."),
    ("keep", "Keep", "Where is your support portal?"),
    ("work", "Do The Work", "Across every stage."),
]

PRODUCTS = [
    {
        "slug": "web", "name": "DeftWeb", "stage": "win", "status": "Early Access",
        "job": "Your website, rebuilt on Deft, edited by your AI and published by a person.",
        "headline": "A Website Your AI Edits And A Human Approves",
        "title": "DeftWeb: A Website Your AI Edits And A Human Approves",
        "cta": ("Request A Free Rebuild", "Free rebuild of my site"),
        "cta_note": "Send us your URL. We rebuild your site on DeftWeb at the same addresses, and you run it from chat or your own Claude before you decide.",
        "story": [
            "Our marketing site was agency-built WordPress that outlived the agency. It ran 41 plugins, its content delivery network cached nothing, and its \"Publish Staging to Live\" button would have deleted live pages.",
            "People edited production in the admin screen, which broke the subscribe form, and nothing told us when they did.",
        ],
        "short": [
            "An agency-built site outlives the agency, and then nobody knows what a button will delete.",
            "When anyone can edit production in the admin screen, nothing tells you when they do.",
            "A plugin stack that slows every page is a cost you pay on every visit.",
        ],
        "asks": [
            ("Change the pricing headline to \"One Flat Price\" and show me a preview.", "web.update_section(\"pricing\", hero)", "draft build 42 on preview"),
            ("Publish build 42.", "web.request_publish(42)", "awaiting your approval"),
        ],
        "with": [("marketing", "Forms on your pages feed your own list."), ("demo", "Walkthroughs embed on any page.")],
    },
    {
        "slug": "marketing", "name": "DeftMarketing", "stage": "win", "status": "Early Access",
        "job": "Your list, newsletter and sign-up funnels, without automation spaghetti.",
        "headline": "A Newsletter Without The Automation Spaghetti",
        "title": "DeftMarketing: A Newsletter Without The Automation Spaghetti",
        "cta": ("Request Early Access", "DeftMarketing early access"),
        "story": [
            "We ran our newsletter on an email marketing platform whose automations, tags and conditional rules grew into a system nobody wanted to touch.",
            "Meanwhile the sign-up boxes on our site stopped reaching the list in July, and nothing told us. So we built something simpler: one form feeds one funnel, and each email reaches a person once.",
        ],
        "short": [
            "A sign-up box that silently stops syncing costs every subscriber since the day it broke.",
            "Automations, tags and conditions grow into a system only one person understands.",
            "A send that cannot be traced to an approved version is a send nobody can explain.",
        ],
        "asks": [
            ("Draft this month's newsletter from our three latest posts.", "marketing.draft_campaign(posts=3)", "draft ready for review"),
            ("Send it to the main list.", "marketing.request_send(campaign)", "awaiting your approval"),
        ],
        "with": [("web", "Your site's forms feed the list directly.")],
    },
    {
        "slug": "revenue", "name": "DeftRevenue", "stage": "win", "status": "Early Access",
        "job": "Quotes, contracts, renewals and the customer record, after the deal closes.",
        "headline": "Everything After Closed-Won, In One Place",
        "title": "DeftRevenue: Everything After Closed-Won, In One Place",
        "cta": ("Request Early Access", "DeftRevenue early access"),
        "story": [
            "Our CRM knew a deal had closed. It did not know the subscription renewed in 30 days, the invoice was 60 days late, or the customer's support queue was full, and every system called the same customer something different.",
            "Onboarding ran on a board automation that stopped picking up work when someone left one word out of a ticket title, and contracts changed state without anyone being told.",
        ],
        "short": [
            "A CRM models the sale, not the subscription that follows it.",
            "An automation keyed on a naming convention stops silently when one word is missing.",
            "Separate tools with no shared customer key cannot answer who renews next month and is overdue.",
        ],
        "asks": [
            ("Who renews in the next 30 days and is overdue?", "revenue.renewals(days=30, overdue=True)", "3 accounts"),
            ("Turn the Halden deal into an order form and send it for signature.", "revenue.create_quote(\"Halden\")", "awaiting your approval"),
        ],
        "with": [("desk", "Each account shows its support tickets."), ("docs", "Order forms use your approved legal language.")],
    },
    {
        "slug": "demo", "name": "DeftDemo", "stage": "win", "status": "In Build",
        "job": "Product walkthroughs buyers can skim, search and question.",
        "headline": "A Walkthrough Buyers Can Skim, Search And Question",
        "title": "DeftDemo: A Walkthrough Buyers Can Skim, Search And Question",
        "cta": ("Join The Waitlist", "DeftDemo waitlist"),
        "story": [
            "The best explanation of our product happened on live calls, and it was gone when the call ended. A recorded video scaled, but nobody could skim it, search it or ask it a question.",
            "Click-through tours were too rigid: viewers clicked to the end to get it over with. So we record the real app as page events, not pixels, and let the viewer ask it anything.",
        ],
        "short": [
            "A live demo does not scale, and the good explanation is lost when the call ends.",
            "A video cannot be skimmed, searched or questioned.",
            "A click-through tour trades a line of text for every click, so viewers race to the end.",
        ],
        "asks": [
            ("Does it support single sign-on?", "demo.answer(question)", "jumps to 03:42, shown"),
            ("What did prospects ask that the walkthrough did not show?", "demo.unanswered()", "5 questions"),
        ],
        "with": [("web", "Embed a walkthrough on any page.")],
    },
    {
        "slug": "trust", "name": "DeftTrust", "stage": "review", "status": "Early Access",
        "job": "SOC 2 controls with their evidence collected and attached every week.",
        "headline": "SOC 2 Evidence That Files Itself Every Week",
        "title": "DeftTrust: SOC 2 Evidence That Files Itself Every Week",
        "cta": ("Request Early Access", "DeftTrust early access"),
        "story": [
            "Our SOC 2 lived in a wiki: policies and control reports with statuses set by hand, and evidence gathered as monthly screenshots.",
            "A Type II observation window does not forgive a missed week, because evidence for a past week cannot be collected later. So DeftTrust collects it on schedule, hashes it, and keeps it where the auditor can read it.",
        ],
        "short": [
            "A wiki full of policies cannot collect evidence, and every forgotten week is a permanent hole.",
            "A screenshot request with no instructions gets a screenshot of the wrong screen.",
            "A ticket marked Resolved is not proof the work happened.",
        ],
        "asks": [
            ("What evidence is overdue this week?", "trust.overdue()", "2 controls"),
            ("Answer the auditor's request list from evidence we already hold.", "trust.answer_requests(\"PBC list\")", "41 of 44 answered"),
        ],
        "with": [("docs", "Each control cites the policy it enforces."), ("sentinel", "Uptime checks become availability evidence."), ("infra", "Deploy records become change-management evidence.")],
    },
    {
        "slug": "docs", "name": "DeftDocs", "stage": "review", "status": "In Build",
        "job": "Policies and procedures, approved, versioned and signed, that your AI can edit safely.",
        "headline": "Policies Your AI Can Edit One Section At A Time",
        "title": "DeftDocs: Policies Your AI Can Edit One Section At A Time",
        "cta": ("Join The Waitlist", "DeftDocs waitlist"),
        "story": [
            "We maintain our policies and procedures with AI agents. Through our wiki's connector, an agent could not change one sentence: the update call takes the whole page, with no version check.",
            "To fix section 4.2 it rewrote everything, and anything it did not understand disappeared behind a version bump that looked like a normal edit. With two editors, the last one won and nobody was told.",
        ],
        "short": [
            "An agent editing a wiki page rewrites the whole page, and comments it did not understand vanish.",
            "With two editors, the last write wins without an error.",
            "A wiki's connector often cannot reach its own databases at all.",
        ],
        "asks": [
            ("Update section 4.2 of the incident response policy to add the new on-call rota.", "docs.update_section(\"IR-01\", \"4.2\", rev=7)", "draft, other sections untouched"),
            ("Show the access control policy as it read on 12 March.", "docs.get_version(\"IT-02\", \"2026-03-12\")", "v3.1, signed"),
        ],
        "with": [("trust", "Controls cite the policy and its version."), ("desk", "Publish public docs to your customer portal.")],
    },
    {
        "slug": "infra", "name": "DeftInfra", "stage": "review", "status": "In Build",
        "job": "One record of every server, app and setting, and of who changed what.",
        "headline": "Every Server, App And Setting, With Who Changed What",
        "title": "DeftInfra: Every Server, App And Setting, With Who Changed What",
        "cta": ("Join The Waitlist", "DeftInfra waitlist"),
        "story": [
            "The inventory we had written down was not the estate we ran: one server ran six apps, not two.",
            "When an upgrade destroyed every app on a test server, we rebuilt from our configuration record, and every setting that had lived only on the box was gone. The first version of our own tool had one shared admin key, so nobody could say who changed what.",
        ],
        "short": [
            "A setting that lives only on the server dies with the server.",
            "The inventory you wrote down is not the estate you run.",
            "One shared admin key means no record of who changed anything.",
        ],
        "asks": [
            ("Which apps run on the production host, and what changed this week?", "infra.inventory(host=\"prod-1\")", "6 apps, 3 changes"),
            ("Add the STRIPE_WEBHOOK_SECRET reference to staging.", "infra.set_variable(\"staging\", ...)", "recorded, not restarted"),
        ],
        "with": [("trust", "Every change becomes change-management evidence.")],
    },
    {
        "slug": "sentinel", "name": "Sentinel", "stage": "review", "status": "Available",
        "job": "Uptime monitoring that runs somewhere other than the thing it watches.",
        "headline": "Know It Broke Before Your Customer Does",
        "title": "Sentinel: Know It Broke Before Your Customer Does",
        "cta": ("View On GitHub", None),
        "cta_href": "https://github.com/ethandrower/sentinel",
        "cta_note": "Sentinel is open source under the MIT licence. Run it yourself, or let Deft run it with the rest of the suite.",
        "story": [
            "Our monitoring ran inside the application. When a background worker died, it took every scheduled task with it, including the alarm meant to report the failure.",
            "Nothing told us for two days. Sentinel runs on a separate host, so the thing that breaks cannot silence the thing that reports it.",
        ],
        "short": [
            "Monitoring inside the app dies with the app.",
            "Checking that a process exists is not checking that work is flowing.",
            "An alert channel full of test-server noise trains people to ignore production.",
        ],
        "asks": [
            ("Is anything down right now?", "sentinel.status()", "all 14 checks passing"),
            ("When does the API certificate expire?", "sentinel.check(\"api-tls\")", "in 41 days"),
        ],
        "with": [("trust", "Daily uptime records become availability evidence.")],
    },
    {
        "slug": "desk", "name": "DeftDesk", "stage": "keep", "status": "Available",
        "job": "One login where enterprise customers read your docs, raise tickets and exchange files.",
        "headline": "One Login For Your Customers' Docs, Tickets And Files",
        "title": "DeftDesk: One Login For Your Customers' Docs, Tickets And Files",
        "cta": ("Request Access", "DeftDesk access"),
        "story": [
            "Enterprise customers expect a portal. Ours started as a wiki space and email to a help-desk inbox.",
            "Email lost the record: a failed send disappeared, and a notification sent to nobody looked exactly like one that worked. Deliverables went out as attachments with no versions, no approval and no signature trail.",
        ],
        "short": [
            "An email form loses the submission when the send fails.",
            "A notification that silently goes to nobody looks the same as one that worked.",
            "An email attachment has no version history, approval or signature trail.",
        ],
        "asks": [
            ("Which enterprise customers have open tickets older than three days?", "desk.tickets(older_than=3)", "2 tickets"),
            ("Send the Q3 report to Halden for approval.", "desk.send_deliverable(\"Halden\", \"Q3 report\")", "awaiting their approval"),
        ],
        "with": [("docs", "Publish approved docs to the portal."), ("revenue", "Tickets appear on the customer's account.")],
    },
    {
        "slug": "agents", "name": "DeftAgents", "stage": "work", "status": "Early Access",
        "job": "AI agents that do real work, with limits, approvals and a record of every action.",
        "headline": "AI Agents With Limits, Approvals And A Record Of Every Action",
        "title": "DeftAgents: AI Agents With Limits, Approvals And A Record Of Every Action",
        "cta": ("Request Early Access", "DeftAgents early access"),
        "story": [
            "We run sales, product and support work through AI agents. Our first code review bot never ran, and reported \"no PRs needed review\" every time.",
            "An agent with shell access can reach far more than its job needs, so we took that away. And when an agent got something wrong, only a developer could fix it.",
        ],
        "short": [
            "A bot that silently stops looks exactly like a quiet day.",
            "An agent with a shell can rewrite its own instructions.",
            "If the only ways to correct an agent are chat and code, only developers can correct it.",
        ],
        "asks": [
            ("Post today's pipeline and demo count to the sales channel.", "agents.run(\"piper\", \"daily-pipeline\")", "posted, logged"),
            ("The agent got the renewal date wrong. Fix it.", "agents.propose_correction(...)", "awaiting review"),
        ],
        "with": [("trust", "Every agent action is part of the audit record."), ("docs", "Agents follow the policies in DeftDocs.")],
    },
]

STATUS_NOTE = {
    "Available": "Available now.",
    "Early Access": "Early access: we onboard each team by hand.",
    "In Build": "In build: join the waitlist and we will tell you when it ships.",
}

BY_SLUG = {p["slug"]: p for p in PRODUCTS}

GLYPH = {
    "globe": '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/>',
}

E = html.escape


def mailto(subject):
    return f"mailto:{CONTACT}?subject={subject.replace(' ', '%20')}"


def nav(active=None):
    return f"""<header class="nav">
  <a class="brand" href="/">DeftSuite</a>
  <nav class="links" aria-label="Primary"><a href="/#suite">Products</a><a href="/#ai">Your AI</a><a href="/#pick">Pricing</a></nav>
  <a class="btn" href="{mailto('DeftSuite early access')}">Request Early Access</a>
</header>"""


def footer():
    groups = []
    for key, label, _ in STAGES:
        links = "".join(f'<a href="/{p["slug"]}/">{p["name"]}</a>' for p in PRODUCTS if p["stage"] == key)
        groups.append(f'<div class="fcol"><h4>{label}</h4>{links}</div>')
    return f"""<footer class="foot">
  <div class="foot__inner">
    <div class="fcol fcol--brand"><a class="brand brand--ink" href="/">DeftSuite</a><p>The enterprise stack for founder-led teams.</p></div>
    {''.join(groups)}
    <div class="fcol"><h4>Company</h4><a href="mailto:{CONTACT}">{CONTACT}</a><a href="/llms.txt">llms.txt</a></div>
  </div>
  <div class="foot__base mono"><span>© 2026 Deft</span><span>deftsuite.com</span></div>
</footer>"""


def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}" />
<link rel="canonical" href="{SITE}{path}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{E(title)}" />
<meta property="og:description" content="{E(desc)}" />
<meta property="og:url" content="{SITE}{path}" />
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
<link rel="alternate" type="text/plain" href="/llms.txt" title="Plain text for agents" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/site.css" />
</head>"""


def status_pill(status):
    cls = {"Available": "is-live", "Early Access": "is-early", "In Build": "is-build"}[status]
    return f'<span class="pill {cls} mono">{status}</span>'


def stage_label(key):
    return next(label for k, label, _ in STAGES if k == key)


def product_page(p):
    stage = stage_label(p["stage"])
    cta_text, subject = p["cta"]
    href = p.get("cta_href") or mailto(subject)
    note = p.get("cta_note") or STATUS_NOTE[p["status"]]
    asks = "".join(
        f"""<div class="ask"><span class="who mono">YOU</span>{E(q)}</div>
        <div class="call mono"><span>{E(call)}</span><span class="st{' wait' if res.startswith('awaiting') else ''}">{E(res)}</span></div>"""
        for q, call, res in p["asks"])
    story = "".join(f"<p>{E(s)}</p>" for s in p["story"])
    short = "".join(f'<li><span class="n mono">{i:02d}</span><span>{E(s)}</span></li>' for i, s in enumerate(p["short"], 1))
    withs = "".join(
        f'<a class="link-row" href="/{slug}/"><span class="mono">{BY_SLUG[slug]["name"]}</span><span>{E(why)}</span><span class="arrow">→</span></a>'
        for slug, why in p["with"])
    preview = ' <span class="mono preview-tag">Preview</span>' if p["status"] == "In Build" else ""
    desc = f'{p["name"]}: {p["job"]} Part of DeftSuite, the enterprise stack for founder-led teams.'
    return f"""{head(p["title"], desc, f'/{p["slug"]}/')}
<body class="product">
<div class="top">
  {nav()}
  <section class="phero">
    <div>
      <div class="crumbs mono"><a href="/#suite">DeftSuite</a> / {stage} / {p["name"]}</div>
      <h1>{E(p["headline"])}</h1>
      <p class="sub">{E(p["job"])}</p>
      <div class="cta"><a class="btn" href="{href}">{E(cta_text)}</a><a class="ghost" href="#price">See Pricing</a></div>
      <p class="note">{status_pill(p["status"])} {E(note)}</p>
    </div>
    <div class="console" aria-label="Asking your AI to use {p['name']}">
      <div class="console__bar mono"><span>Your AI · connected to {p["name"]}</span>{preview}</div>
      {asks}
    </div>
  </section>
</div>

<section class="story">
  <div class="wrap split">
    <h2>Why We Built It</h2>
    <div class="story__body">{story}</div>
  </div>
</section>

<section class="short">
  <div class="wrap split">
    <h2>Where The Alternatives Fall Short</h2>
    <ol class="short__list">{short}</ol>
  </div>
</section>

<section class="with">
  <div class="wrap split">
    <h2>Works With The Rest Of Deft</h2>
    <div>{withs}</div>
  </div>
</section>

<section class="price" id="price">
  <div class="wrap split">
    <h2>Pricing</h2>
    <div>
      <table class="ptable">
        <thead><tr><th></th><th>1–9 People</th><th>10–19 People</th><th>20+ People</th></tr></thead>
        <tbody>
          <tr><th>{p["name"]} on its own</th><td>${PRODUCT_PRICE[0]}</td><td>${PRODUCT_PRICE[1]}</td><td>${PRODUCT_PRICE[2]}</td></tr>
          <tr><th>The whole suite</th><td>${SUITE_PRICE[0]}</td><td>${SUITE_PRICE[1]}</td><td>${SUITE_PRICE[2]}</td></tr>
        </tbody>
      </table>
      <p class="aside mono">Per month. Not per user. Three products cost about the same as the suite. <a href="/#pick">Build your plan</a></p>
    </div>
  </div>
</section>

{footer()}
<script src="/assets/js/site.js"></script>
</body>
</html>
"""


def stack_series():
    """Monthly stack cost by team size, 1..50, per tool and in total."""
    if RESEARCH.exists():
        rows = json.loads(RESEARCH.read_text())["monthly_total_by_team_size"]
        SERIES_CACHE.write_text(json.dumps(rows))
    else:
        rows = json.loads(SERIES_CACHE.read_text())
    out = []
    for r in rows:
        row = {"n": r["team_size"]}
        for key, *_ in STACK:
            row[key] = WPENGINE_MONTHLY if key == "WPEngine" else round(r[key], 2)
        row["total"] = round(r["total"] + WPENGINE_MONTHLY, 2)
        out.append(row)
    return out


def write_stack_data():
    tools = [
        {"key": k, "cat": cat, "vendor": vendor, "rate": rate, "est": est, "glyph": glyph,
         "deft": BY_SLUG[slug]["name"], "slug": slug}
        for k, cat, vendor, rate, est, glyph, slug in STACK
    ]
    products = [{"slug": p["slug"], "name": p["name"], "job": p["job"], "status": p["status"], "stage": p["stage"]}
                for p in PRODUCTS]
    js = ("/* Generated by tools/build.py. Do not edit by hand. */\n"
          f"var STACK_TOOLS = {json.dumps(tools)};\n"
          f"var STACK_SERIES = {json.dumps(stack_series())};\n"
          f"var DEFT_PRODUCTS = {json.dumps(products)};\n"
          f"var SUITE_PRICE = {list(SUITE_PRICE)}, PRODUCT_PRICE = {list(PRODUCT_PRICE)};\n")
    (ROOT / "assets/js/stack-data.js").write_text(js)


def write_meta_files():
    urls = ["/"] + [f'/{p["slug"]}/' for p in PRODUCTS]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nDisallow: /design/\nDisallow: /concepts/\nSitemap: {SITE}/sitemap.xml\n")
    lines = ["# DeftSuite", "",
             "> The enterprise stack for founder-led B2B teams that sell to enterprise and run their company through AI.",
             "", "## Products", ""]
    for key, label, _ in STAGES:
        lines.append(f"{label}:")
        for p in (q for q in PRODUCTS if q["stage"] == key):
            lines.append(f'- [{p["name"]}]({SITE}/{p["slug"]}/): {p["job"]} Status: {p["status"]}.')
        lines.append("")
    lines += ["## Pricing", "",
              "Flat monthly price by team size. Not per user. No add-ons.", "",
              f"- The whole suite: ${SUITE_PRICE[0]} (1 to 9 people), ${SUITE_PRICE[1]} (10 to 19), ${SUITE_PRICE[2]} (20 or more).",
              f"- Any one product: ${PRODUCT_PRICE[0]}, ${PRODUCT_PRICE[1]} or ${PRODUCT_PRICE[2]} by the same tiers. The suite price caps the bill.",
              "", "## Your AI", "",
              "Each product has its own agent connection over MCP, with human approval enforced on the server for publish, send, sign and approve. One connection across the whole suite (Deft MCP) is in build.",
              "", "## Contact", "", CONTACT, ""]
    (ROOT / "llms.txt").write_text("\n".join(lines))


def suite_section():
    cols = []
    for key, label, ask in STAGES:
        rows = []
        for p in (q for q in PRODUCTS if q["stage"] == key):
            cls = {"Available": "is-live", "Early Access": "is-early", "In Build": ""}[p["status"]]
            rows.append(f'<a class="plink" href="/{p["slug"]}/"><b>{p["name"]}<span class="mono {cls}">{p["status"]}</span></b>'
                        f'<span class="j">{E(p["job"])}</span></a>')
        quote = f'"{ask}"' if key != "work" else ask
        cols.append(f'<div class="stage"><div class="stage__h"><b>{label}</b><span class="mono">{E(quote)}</span></div>{"".join(rows)}</div>')
    return f"""<section class="suite" id="suite">
  <div class="suite__inner">
    <div class="suite__head">
      <h2>One Product For Each Thing An Enterprise Buyer Asks For</h2>
      <p>Buy one, add the next, or take the whole suite. Every product stands alone, and they share one record when you use them together.</p>
    </div>
    <div class="suite__grid">{"".join(cols)}</div>
  </div>
</section>"""


def fill(text, name, content):
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    a, b = text.index(start) + len(start), text.index(end)
    return text[:a] + content + text[b:]


def write_home():
    path = ROOT / "index.html"
    text = path.read_text()
    text = fill(text, "NAV", nav())
    text = fill(text, "SUITE", suite_section())
    text = fill(text, "FOOTER", footer())
    path.write_text(text)


def main():
    write_stack_data()
    for p in PRODUCTS:
        d = ROOT / p["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(product_page(p))
    write_meta_files()
    write_home()
    print(f"built {len(PRODUCTS)} product pages, stack data, sitemap, robots, llms.txt")


if __name__ == "__main__":
    main()
