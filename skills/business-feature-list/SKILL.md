---
name: business-feature-list
description: Use when creating or revising customer-facing product feature lists, sales feature tables, module capability matrices, or competitor-style feature breakdowns from any product, docs, screenshots, or codebase.
---

# Business Feature List

## Overview

Create customer-facing business feature lists from product evidence. The goal is to express what buyers can understand, evaluate, and sell, not how the product is implemented.

## Inputs To Inspect

Use the best available sources. Do not assume one source is enough.

- Product identity: explicit user-provided name, product logo/brand text, landing page H1/title, package/app name, repository name, domain, or internal codename.
- Product UI: navigation, sidebars, settings, dashboards, empty states, modals, onboarding, pricing.
- Product docs: README, PRDs, specs, landing pages, FAQ, release notes.
- Codebase signals: route names, page/component names, API modules, constants, feature flags, package boundaries.
- Data/API signals: entity names, endpoints, integration providers, usage/billing models.
- External references: competitor feature lists, customer decks, website copy, screenshots.

## Adaptive Code Scanning

Do not hardcode one scanning recipe. Different products expose features differently.

- Web apps: start with routes/pages/layouts, then navigation and major panels.
- Mobile apps: start with screens/scenes, tab navigation, view models, services.
- Backend/API products: start with API routes/controllers, service modules, OpenAPI/GraphQL schemas, data models.
- SaaS/admin systems: start with menu/sidebar, permissions, resource pages, reports, billing/integrations.
- AI/agent products: start with modes, agent surfaces, tools, runtime services, model/provider usage, eval/logging.
- Marketplaces: start with listing/detail/remix/publish/favorite/share flows and supply/demand roles.

Use fast repo search (`rg`, `find`, `rg --files`) and read representative files. For large repos, sample the highest-signal folders first instead of enumerating everything.

## Core Workflow

1. **Resolve document identity**
   - Product title source priority: user-provided name -> public brand in product UI/landing copy -> docs/README title -> package/app name -> repository/directory name.
   - If a repo codename differs from public brand, use the public brand in the title and mention codename only if useful internally.
   - Add an update date using the current date or source date. Use `更新时间：YYYY-MM-DD`.

2. **Understand the product before extracting features**
   - Infer product type, primary users, core value proposition, business model, and complexity.
   - Infer the best classification method, granularity standard, and exclusion rules for this product.
   - This reasoning guides the feature list but is usually not output unless the user asks.

3. **Inventory raw capabilities**
   - Extract visible actions, modules, integrations, managed services, dashboards, automation, collaboration, controls, and outputs.
   - Keep raw notes messy at first; do not decide final categories too early.

4. **Translate into buyer language**
   - Convert implementation nouns into customer outcomes.
   - Example: `getRuntimeLogs()` -> "运行日志：帮助排查线上报错和服务异常".
   - Example: `upload.ts` + asset panel -> "素材管理：上传和管理图片、文档、视频等业务素材".

5. **Classify by business capability**
   - Choose categories based on how a buyer would evaluate the product, not how the repo is organized.
   - Section headings should carry the category; table columns should usually be `序号 / 功能模块 / 描述`.

6. **Set feature granularity**
   - Merge controls that serve the same buyer outcome.
   - Split only when the buyer would buy, compare, configure, or ask about the capability separately.
   - Prefer a compact executive list by default; expand only if the user asks for exhaustive detail.

7. **Write concrete descriptions**
   - Say what the capability does and why it matters.
   - Include concrete supported objects, file types, providers, workflows, or outputs when they improve clarity.
   - Avoid generic "支持 X" descriptions with no scenario.

8. **Prune low-value items**
   - Remove technical stack, plumbing, legal pages, basic account operations, and UI mechanics unless they are the product being sold.

9. **Gate pricing-sensitive claims**
   - Treat pricing, plans, credits, billing, quotas, limits, usage fees, trial allowances, and upgrade rights as confirmation-sensitive.
   - Only include them when the user provides explicit source material or asks to include pricing/monetization capabilities.
   - If evidence exists but may be unstable or disputed, write “需确认” or move the item to a separate “待确认商业规则” section.
   - Never invent prices, plan names, credit amounts, included quotas, or upgrade rules from code names alone.

## Classification Methods

Use one or combine several depending on the product.

### How to Pick a Classification

Prefer the classification that makes the fewest categories while preserving how customers evaluate the product.

- If the product sells an end-to-end workflow, start with **Value Chain**.
- If the product has a clear user path, start with **User Journey**.
- If the product is a platform/devtool/AI/cloud product, start with **Capability Domain**.
- If the buyer groups have clearly different needs, use **Buyer Persona**.
- If the user provides a competitor feature list, mirror its style with **Competitor-Style**, but only where it fits real capabilities.

Default heuristic: choose 6-10 top-level sections; each section should usually contain 3-6 feature rows. If a section has more than 6 rows, merge subfeatures or split the section. If a section has 1 row, merge it into a neighboring section unless it is a major standalone product pillar.

### 1. Value Chain Classification

Best for platforms and end-to-end tools.

Typical order:

1. Discover / Plan
2. Create / Build
3. Edit / Configure
4. Run / Test
5. Deploy / Publish
6. Operate / Monitor
7. Analyze / Optimize
8. Monetize / Bill
9. Govern / Secure

### 2. User Journey Classification

Best for consumer apps, SaaS workflows, marketplaces, and internal tools.

Group by the customer journey:

- Onboarding
- Core workflow
- Collaboration/review
- Delivery/output
- Management
- Reporting
- Expansion/upgrade

Drop basic login/logout unless identity itself is a business capability.

### 3. Capability Domain Classification

Best for technical products, AI platforms, cloud tools, and developer-facing products.

Common domains:

- Creation/building
- Design/content/assets
- Data/storage
- Runtime/hosting
- Integrations
- Automation/AI
- Observability/logs
- Security/governance
- Analytics/billing
- Marketplace/ecosystem

### 4. Buyer Persona Classification

Best when different buyers care about different things.

Examples:

- Founder/PM: idea-to-launch, templates, analytics.
- Developer: code visibility, logs, environments, integrations.
- Operator: billing, monitoring, permissions, support.
- Marketer: landing pages, SEO, assets, sharing.
- Enterprise buyer: SSO, audit, data controls, governance.

Use this when the output needs sales messaging or buyer-specific decks.

### 5. Competitor-Style Classification

Best when the user provides a competitor feature list and wants similar structure.

Steps:

- Mirror the competitor's top-level categories when they fit.
- Do not copy their features blindly; map only real capabilities.
- Keep unmatched but important product strengths as extra categories.
- Avoid forcing a product into categories it does not actually support.

## Internal Inference Checklist

Before writing the table, decide internally:

- Product type: SaaS platform, AI tool, devtool, marketplace, enterprise system, consumer app, etc.
- Main buyers/users: business user, developer, operator, marketer, enterprise admin, platform owner.
- Classification method: business domain, user journey, page/view, user role, value chain, competitor-style, or hybrid.
- Granularity: capability-level for complex/AI/platform products; feature-level for traditional SaaS; page-level only when pages map directly to buyer-visible modules.
- Exclusion rules: what this product's customers would not pay attention to.

Do not output this analysis by default. Output only the final feature list unless the user asks for rationale.

## Feature Granularity Rules

Default granularity:

- 3-6 feature rows per section.
- 25-45 rows for a normal sales/executive list.
- One row should describe a buyer-recognizable capability, not a UI control.
- A row may include several sub-capabilities in its description when they serve the same user goal.

### Keep As Standalone Feature

Use standalone rows when the capability is:

- A buyer-visible product promise.
- A paid-plan differentiator.
- A workflow stage customers ask about.
- An integration/provider customers recognize.
- A managed service: database, storage, hosting, secrets, logs, LLM runtime.
- A governance/security/compliance capability customers evaluate.
- A dashboard or report used for business decisions.

### Merge Into A Broader Feature

Merge when the item is a UI affordance or sub-control:

- search boxes, filters, pagination, sorting, row counts.
- copy buttons, refresh buttons, tabs, collapses, empty states.
- route guards, 404 pages, loading spinners.
- logs clear, auto-scroll, line counts.
- field-level forms unless the provider/configuration is the feature.

### Usually Drop

- Frameworks, SDK internals, state management, build tools, package names.
- Legal pages, privacy policy, refund policy, terms page.
- Login/logout/session persistence unless authentication is part of the product's sold capability.
- Internal API wrappers, interceptors, token storage mechanics.
- One-off implementation details not visible to customers.
- Pricing, credits, billing, quotas, and plan entitlements unless confirmed by current product/pricing source or explicitly requested by the user.

## Pricing-Sensitive Content

Pricing and commercial entitlements are high-risk because they change often and can create customer-facing disputes.

Default handling:

- Do not include pricing rows in the main feature list unless the user explicitly wants them.
- If included, describe the capability without amounts unless the source is explicit.
- Use “需确认” for any uncertain plan, quota, credit, billing, or price claim.
- Prefer “用量与成本可视化” over detailed “套餐与升级” unless pricing is confirmed.

Examples:

| Evidence | Safer phrasing |
|---|---|
| Code has `CreditsLedger` | “支持查看 Credits 使用流水（具体计费规则需确认）。” |
| Pricing UI has plan names but no confirmed commercial copy | “提供套餐展示与升级入口（套餐权益和价格需确认）。” |
| Current official pricing page provided by user | “按用户提供的价格页整理套餐和额度。” |

## Description Writing Pattern

Use this sentence shape:

`支持/提供 [capability], 用于 [business scenario/outcome], 可包含 [specific examples].`

Good:

- "支持上传 Markdown、Word、PDF、Excel、PPT、图片和视频等资料，作为应用生成上下文。"
- "提供构建日志和运行日志，帮助定位发布失败、页面报错、接口异常和服务启动异常。"
- "支持 Stripe Checkout、订阅、Webhook、客户门户等支付配置，适合付费工具、会员订阅和 SaaS 收费场景。"

Weak:

- "支持文件上传。"
- "有日志功能。"
- "使用 React 和 Vite 构建。"

## Output Format

Default output:

```markdown
# [产品名] 业务功能清单

更新时间：[YYYY-MM-DD]　　分类方式：[业务域 / 用户旅程 / 页面视图 / 用户角色 / 混合分类等]

## 一、[业务能力域]

| 序号 | 功能模块 | 描述 |
|---:|---|---|
| 1 | [功能名] | [业务描述] |
```

Rules:

- Title must use the best available public product name. Do not invent a brand name.
- Include update date and classification method unless the user explicitly asks for a bare table.
- Do not include source metadata by default; users usually do not need it in the deliverable.
- Use section headings for categories; omit a repeated category column.
- Keep numbering continuous across all sections.
- Default target: 25-45 rows for a sales/executive feature list, with 3-6 rows per section.
- If the user asks for exhaustive inventory, add more rows but still avoid UI trivia.
- If competitor comparison is needed, create a separate document or section, not inside the core feature list.

## Quality Checklist

Before finalizing, check:

- Could sales explain every row to a customer?
- Does every row describe buyer value, not implementation?
- Are categories mutually understandable and not just repo folders?
- Are broad platform capabilities represented: data, runtime, integrations, observability, analytics, billing, security if applicable?
- Are pricing/plan/credits/billing claims either confirmed or marked as “需确认”?
- Are examples concrete where ambiguity would hurt?
- Did you remove padding and low-sales-value basics?

## Common Corrections

- If the user says "太泛了": add supported types/providers/scenarios to descriptions.
- If the user says "太细了": merge UI subfeatures into capability rows.
- If the user says "这不是功能": remove plumbing/legal/basic account operations.
- If the user flags pricing, plans, credits, or billing as disputed: remove from the main list or mark "需确认".
- If the user provides a competitor list: learn its category style, then adapt to the product's actual capabilities.
- If source evidence is code-heavy: translate routes/API/components into business nouns before writing the table.
