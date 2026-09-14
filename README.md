# Work Briefs

Work Briefs is a living collection of Codex skills for turning messy product context into clear, useful working documents.

This repository is part of my day-to-day work as an agent product manager. It captures repeatable briefing workflows I use when working with AI coding agents, product prototypes, local codebases, screenshots, PRDs, market references, and half-formed ideas. The goal is not to generate more documentation. The goal is to help agents produce the right document for the job.

Writing good documents with AI is still hard. A useful brief needs judgment: what to inspect, what to ignore, what counts as evidence, what belongs in the final output, and what should be left out because it is just template residue or implementation noise. These skills encode that judgment so future agents can do the work more consistently.

## What This Repo Is For

- Extracting product truth from messy evidence.
- Turning local projects into implementation prompts, feature lists, and business briefs.
- Helping agents separate product facts from code facts.
- Keeping reusable document workflows small, inspectable, and easy to update.
- Building a practical operating notebook for agent-assisted product management.

## Current Skills

### `business-feature-list`

Creates customer-facing product feature lists from product evidence such as codebases, docs, screenshots, PRDs, or competitor examples.

Use it when you need:

- A sales-friendly feature list.
- A module or capability matrix.
- A competitor-style product breakdown.
- A business-readable summary of what a product can do.

### `extract-product-prompt`

Reverse-engineers a local app or codebase into a concise product implementation prompt.

Use it when you need:

- An MVP implementation prompt.
- A feature implementation prompt.
- A rebuild or simplification prompt.
- A prompt that captures the product experience without over-specifying technical details.

This skill is especially useful for AI products because it checks the actual generation behavior: user inputs, modes, scenarios, tone rules, output schema, and sample prompt behavior.

### `lovable-details-export`

Exports all Details panels from an existing Lovable conversation into one Markdown file, preserving displayed thoughts, SQL, commands, event order, and code diffs.

- Handles virtualized timelines and repeated event titles.
- Extracts original diff text from the page's copyable code blocks.
- Includes a Python standard-library renderer that checks inventory coverage and missing content.
- Guides targeted credential redaction before saving captures.

Requires an authenticated browser session accessible to the agent. Browser collection follows the skill workflow; the Python script formats already captured JSON. This exports product-visible records, not hidden backend reasoning or orchestration logs.

### `golden-case-miner`

Turns real projects, agent traces, feedback, and supporting evidence into a reusable Golden Case Roster for evaluation and regression testing.

- Defines each case with Spec, Skill, Tool, Expected Trace, and Eval.
- Separates requested, generated, executed, observed, and verified behavior.
- Scores evidence quality, reproducibility, diagnostic value, and coverage.
- Evaluates observable results and actions, with explicit failure attribution.

### `designing-business-app-seo-geo`

Defines SEO/GEO strategy for AI app builders and business-app templates, starting from business jobs and search intent.

- Organizes queries into mature SaaS, build/custom, and AI/no-code intent.
- Connects query validation to template priorities and landing-page architecture.
- Covers category, industry, template, problem, capability, and comparison pages.
- Measures the funnel from discovery through activation and revenue.

## Repository Structure

```text
skills/
  business-feature-list/
    SKILL.md
    agents/openai.yaml

  extract-product-prompt/
    SKILL.md
    agents/openai.yaml

  lovable-details-export/
    SKILL.md
    agents/openai.yaml
    references/browser-capture.md
    scripts/render_details.py

  golden-case-miner/
    SKILL.md
    agents/openai.yaml

  designing-business-app-seo-geo/
    SKILL.md
    agents/openai.yaml
```

Each skill is intentionally small:

- `SKILL.md` contains the workflow and quality gates.
- `agents/openai.yaml` contains UI metadata for skill discovery.
- Optional `references/` and `scripts/` hold capture procedures and reusable processing helpers.

## Design Principles

### Evidence Before Output

A good AI-written brief should be grounded in the material at hand. The skills in this repo push agents to inspect product surfaces before writing: UI, routes, i18n strings, API behavior, prompt files, schemas, docs, screenshots, or user instructions.

### Product Facts Over Code Facts

Files are not features. Routes are not necessarily product requirements. Schemas may describe abandoned work. README files may describe a starter template instead of the current product.

The skills ask agents to distinguish:

- Visible product behavior.
- User-requested target behavior.
- Supporting implementation details.
- Legacy or template residue.
- Speculation.

### Compact, Useful Briefs

The output should help someone act. A brief should be short enough to use, concrete enough to execute, and honest about what is known.

### Positive Requirements First

Good implementation prompts should mostly describe what to build. Scope boundaries matter, but long lists of things not to build often hide the actual product.

### Reusable Judgment

These skills are not tied to one product. They are reusable document workflows that adapt to different product types: AI tools, SaaS apps, mobile apps, developer tools, marketplaces, content products, admin systems, and more.

## How To Use

Copy or install the relevant skill into your Codex skills directory, then ask Codex to use it on a project or source set.

Example prompts:

```text
Use extract-product-prompt on this local project and give me a concise MVP implementation prompt.
```

```text
Use business-feature-list to create a customer-facing feature list from this codebase and README.
```

```text
Use lovable-details-export to save all Details from the current Lovable conversation into one Markdown file.
```

```text
Use golden-case-miner to turn these project traces and feedback into reproducible evaluation cases.
```

```text
Use designing-business-app-seo-geo to plan search-intent clusters, landing pages, and business-app template priorities.
```

The skills are designed to work best when the agent has access to the local project files or the source material you want it to inspect.

## Maintenance Notes

This repo will keep evolving as my product work changes.

When adding or editing a skill:

- Keep the skill focused on a repeatable job.
- Keep `SKILL.md` concise and procedural.
- Add explicit check gates for the failure modes you have seen in real agent work.
- Prefer evidence tables, confidence checks, and clear exclusion rules over vague advice.
- Do not add broad documentation unless it directly improves future agent behavior.

## Why This Matters

AI agents can write quickly, but speed is not the same as understanding. The hard part is often not wording. It is deciding what the document should be about.

This repository is my attempt to turn that decision-making process into reusable working briefs: practical, opinionated, and continuously updated from real product work.
