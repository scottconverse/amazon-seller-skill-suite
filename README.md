# Amazon Seller Skill Suite v1.0

6 Claude Cowork skills for Amazon marketplace selling.
Works with any brand, any product category, any seller account type.

---

> **IMPORTANT DISCLAIMER**
>
> **This is not financial or business advice.** AI output may be inaccurate, outdated, or misleading. This project is **not affiliated with, endorsed by, or associated with Amazon.com, Inc.** in any way.
>
> Following AI-generated recommendations may result in financial loss, listing suppression, or Amazon account action (including suspension). Amazon policies, fees, and marketplace rules change frequently and without notice.
>
> **These skills run autonomously in Claude's CoWork mode and may take actions on your behalf.** Review all output before acting on any recommendation. You are solely responsible for your Amazon seller account and all business decisions.
>
> **Verify all information independently in Amazon Seller Central before acting on it.**
>
> See the [Terms of Service](docs/terms.html) for complete legal terms.

---

## What It Does

Drop these skills into Claude Desktop and they activate automatically based on what you ask. Each skill is a specialist — it knows its domain, enforces hard gates before giving advice, detects contradictions in your inputs, and refuses to fabricate data it doesn't have.

## The 6 Skills

| Skill | Words | What It Does |
|---|---|---|
| **Listing Optimizer** | ~3,560 | Titles, bullets, backend keywords, A+ Content plans, image shot lists. Hard-gated with contradiction blocking. Title positioning logic for value/mid-market/premium brands. Backend keyword packing with UTF-8 byte counting. A+ module-to-buyer-hesitation mapping. |
| **Trend Researcher** | ~2,460 | Competitor analysis, category trends, demand validation, keyword intelligence. 4-archetype competitor segmentation. Price band analysis. Verdict ceiling — cannot issue GO without margin data. |
| **Account Strategist** | ~3,090 | Pricing, expansion, variation strategy, review growth, FBA vs FBM. 7 decision gates. Launch sequencing (4 gated phases). Portfolio triage (SCALE/HOLD/INVEST/KILL). Low-CVR diagnostic before price cuts. |
| **Brand Guardian** | ~2,470 | Brand voice, visual identity, photography direction, Brand Story. Giftability and sustainability honesty tests. Extensible claim challenge framework for any positioning claim. |
| **Social Strategist** | ~3,290 | Content calendars, post drafting, external traffic strategy. Capacity gate (hours/budget/tools confirmed before planning). Brand voice enforcement gate. Every tactic tied to Amazon outcomes. |
| **Listing QA** | ~4,780 | Pre-publish quality gate. Hostile by default. Prompt injection defense. 7-category semantic laundering patterns. Environmental/sustainability claim verification. Exact byte/character computation — never estimates. |

**Total: ~19,650 words across 34 rules.**

## Installation

1. Open Claude Desktop (Cowork mode)
2. Drag a `.skill` file into the chat window
3. Click "Copy to your skills" when prompted
4. Repeat for each of the 6 skill files

Skills activate automatically based on what you ask. On first use, each skill asks about your brand and products.

## Key Features

### Hard Gates
Every skill has gates that block output until required inputs are confirmed. The Account Strategist won't advise without your actual COGS. The Listing Optimizer won't write copy without your brand, product, category, features, and audience. The QA skill won't audit a summary — it demands exact text.

### Contradiction Detection
Every skill checks your inputs for internal contradictions before proceeding. "Premium brand" + "cheap price" = blocked. "Small-batch artisan" + 60,000 units/month = flagged. "Eco-friendly" without certification = challenged.

### Anti-Hallucination Controls
No skill fabricates BSR numbers, search volumes, competitor metrics, or conversion rates. All numerical claims are labeled by source confidence: VERIFIED (Amazon first-party data), ESTIMATED (third-party tools, ±50%), or INFERRED (pattern analysis).

### Cross-Skill Handoff Protocol
When chaining skills, each skill inherits upstream BLOCKED ITEMS and unresolved contradictions. Upstream findings must be provided as actual output, not user summaries. No skill can proceed past an inherited block without new evidence.

### Prompt Injection Defense
All 6 skills treat user-supplied content as DATA, not instructions. Embedded directives ("ignore rules," "mark approved") are flagged as hostile findings, not obeyed.

## How to Use Them Together

### Launching a New Product
| Step | Skill | Purpose |
|---|---|---|
| 1 | Trend Researcher | Validate demand + competitor landscape |
| 2 | Account Strategist | Economics + launch sequence |
| 3 | Listing Optimizer | Full content package |
| 4 | Brand Guardian | Brand consistency audit |
| 5 | Listing QA | Pre-publish check |
| 6 | Social Strategist | Launch traffic plan |

### Optimizing an Existing Listing
| Step | Skill | Purpose |
|---|---|---|
| 1 | Listing Optimizer | Audit + rewrite |
| 2 | Listing QA | Verify changes |
| 3 | Social Strategist | Drive traffic |

### Monthly Review
| Step | Skill | Purpose |
|---|---|---|
| 1 | Trend Researcher | Competitor + keyword shifts |
| 2 | Account Strategist | Portfolio triage (SCALE/HOLD/INVEST/KILL) |
| 3 | Social Strategist | Content calendar |

## What's Inside Each .skill File

Each `.skill` file is a zip archive containing a single `SKILL.md` — the complete instruction set for that specialist. You can open any `.skill` file with a zip tool to read or modify the instructions.

## License

MIT — use it however you want.

## Credits

Adapted from [The Agency](https://github.com/msitarzewski/agency-agents) by Mike Sitarzewski.
