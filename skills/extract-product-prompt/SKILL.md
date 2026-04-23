---
name: extract-product-prompt
description: Use when converting an existing local app/codebase into a concise product implementation prompt, MVP brief, or feature prompt by reverse-engineering user-facing flows from code, routes, UI text, API prompts, and product behavior.
---

# Extract Product Prompt

## Goal

Reverse-engineer a local coding project into a product implementation prompt.

The output is not a repository summary. The output is the prompt another coding agent should receive to rebuild, simplify, or implement the product from a product-function perspective.

## Core Principle

Extract product facts, not code facts.

Never include a product feature just because a file exists. Include it only when it is visible, requested, strongly implied by product behavior, or necessary for the core product loop.

## Inputs To Inspect

Use the highest-signal local sources first:

- User instruction in the current conversation.
- Homepage or main route: `app/page.*`, `pages/index.*`, route layouts, mobile entry screens.
- Visible components: navigation, primary panels, forms, result views, empty states, modals.
- i18n/message files: `messages/`, `locales/`, `*.json`, localized strings.
- API routes and server actions that reveal product behavior.
- AI prompt files, system prompts, agent/persona definitions, generation schemas.
- Schemas, migrations, storage code, and rate limits only when they reveal product facts.
- README/docs only after checking UI/code, because docs often contain template residue.

For large projects, sample the main product path first instead of enumerating every file.

## Workflow

1. **Inspect**
   - Read product-revealing surfaces.
   - Prefer `rg`, `rg --files`, and focused file reads.
   - Do not trust README alone.

2. **Extract facts**
   - Build an internal evidence table with product facts, evidence, confidence, and include/exclude decision.
   - Resolve conflicts before drafting.

3. **Make adaptive extraction decisions**
   - Identify product type, primary user roles, primary job, output type, feature maturity, MVP boundary, AI prompt depth, and requested artifact type.
   - Use these decisions to choose what facts matter.

4. **Classify facts with adaptive lenses**
   - Start with the universal dimensions below.
   - Choose product-type-specific categories only after inspecting the project.
   - Do not force every project into the same taxonomy.

5. **Resolve conflicts**
   Use this precedence:
   - Current user instruction.
   - Visible product UI.
   - API/prompt behavior.
   - Schemas/data model.
   - README/docs.
   - File names.

6. **Draft the prompt**
   - Write in product language.
   - Prefer what to build over how to implement it.
   - Keep it concise enough for a coding agent to act on.

7. **Check**
   - Run Product Prompt Check.
   - Revise until all included requirements are supported by evidence or current user instruction.

8. **Return**
   - Return a short "Check Passed" note.
   - Then return the final implementation prompt.

## Adaptive Extraction Rules

Before drafting, decide these internally. Use the answers to shape the final prompt. Do not output this analysis unless the user asks for it.

### Product Type

Pick the closest type, or combine types when needed:

- AI tool.
- SaaS workflow app.
- Developer/API product.
- Mobile app.
- Marketplace/e-commerce.
- Content/community product.
- Internal tool/admin system.
- Game/interactive experience.
- Document/report generator.
- Data/analytics dashboard.

### Primary User Roles

Identify the roles the product serves:

- End user.
- Creator.
- Buyer.
- Seller.
- Admin.
- Developer.
- Operator.
- Reviewer/approver.
- Customer/support agent.

If roles have different workflows, do not collapse them into one generic "user".

### Primary Job

State the job the product is hired to do:

- Transform something.
- Create something.
- Manage something.
- Analyze something.
- Sell/buy/book something.
- Automate something.
- Learn/practice/play something.
- Monitor or operate something.

This is the anchor for deciding MVP scope.

### Output Type

Identify what the product produces:

- Generated text, image, video, audio, or code.
- Saved record.
- Report/dashboard.
- Downloadable file.
- Transaction/order/booking.
- API response.
- Game state/progress.
- Notification/message.
- Decision/recommendation.

### Feature Maturity

Classify candidate features:

- Visible and working.
- Visible but incomplete.
- API exists but not surfaced.
- Schema/model exists only.
- Dead, legacy, or template residue.
- Explicitly requested target behavior.

Prefer visible and working behavior plus explicitly requested target behavior. Treat file-only evidence as weak.

### MVP Boundary

Classify each feature by why it exists:

- Required for core value.
- Helps repeat usage.
- Helps sharing/distribution.
- Helps monetization.
- Operational/admin only.
- Template/noise.

For an MVP implementation prompt, prioritize "required for core value" and include other groups only when the user asks or the product loop needs them.

### AI Prompt Depth

Choose the needed depth:

- No AI: skip AI prompt rules.
- Simple AI transform: include task, constraints, output format.
- Scenario-based AI: include scenario-specific prompt behavior.
- Role/persona-based AI: include role behavior and boundaries.
- Multi-step AI workflow: include stages and handoffs.
- Safety-sensitive AI: include safety, refusal, escalation, and uncertainty handling.

If the product's value depends on AI output quality, include samples.

### Requested Artifact Type

Infer what the user wants now:

- MVP implementation prompt.
- Feature implementation prompt.
- Rebuild prompt.
- Simplification prompt.
- PRD.
- Customer-facing feature list.
- App store or landing page copy.

Shape the final answer for that artifact. Do not reuse the same outline for every request.

## Fact Classification

These are default lenses, not a fixed output taxonomy. Use them to understand the project, then adapt the final prompt structure to the product type.

### Universal Dimensions

Use these for almost every product:

- **Product identity**: name, positioning, primary user value, target user if evident.
- **Primary job**: the main task the user hires the product to do.
- **Core loop**: user input/action -> product processing -> output/result -> next user action.
- **Controls and choices**: user-selectable modes, filters, settings, scenarios, roles, styles, or configuration.
- **Outputs**: generated content, saved records, reports, dashboards, transactions, files, API responses, or notifications.
- **Usage policy**: quotas, limits, account/device/session basis, language behavior, safety rules.
- **States**: empty, loading, success, error, limit reached, offline, permission denied.
- **Noise**: template residue, dead features, unused routes, infrastructure, implementation plumbing.

### Product-Type Lenses

Pick only the lenses that match the inspected project.

#### AI Tool

- User input.
- Context, scenario, role, tone, or style controls.
- AI task and behavior rules.
- Output schema.
- Prompt samples.
- Usage limits and safety handling.

#### SaaS Workflow App

- Onboarding.
- Primary workflow.
- Resource creation/editing.
- Collaboration/review.
- Reporting/analytics.
- Admin/settings only if buyer-visible.

#### Mobile App

- First-run experience.
- Main tabs/screens.
- Daily-use action.
- Local state, sync, notifications, purchases, or permissions if product-facing.

#### Developer/API Product

- Developer goal.
- Authentication/setup.
- Core API resources.
- Request/response behavior.
- SDK/CLI/docs experience.
- Logs, errors, limits, and integration workflow.

#### Marketplace/E-commerce

- Supply-side flow.
- Demand-side flow.
- Listing/detail/checkout or booking path.
- Trust, reviews, payments, fulfillment, support.

#### Content/Community Product

- Create/post/publish flow.
- Browse/discover flow.
- Interaction model.
- Moderation, ranking, notifications, profile/history if product-facing.

### Product Identity

- Product name.
- One-line positioning.
- Primary user value.
- Target user if evident.

### Core User Loop

- What the user inputs.
- What the user chooses.
- What the system produces.
- What the user can do with the result.

### AI Behavior

For AI products, extract or infer:

- AI task.
- User-controllable scenarios, modes, tones, roles, or styles.
- Scenario-specific behavior.
- Tone/style-specific behavior.
- Output shape.
- Sample input/output behavior.

Do not write only "call AI" or "generate response". If generation quality depends on prompting, include concrete prompt rules.

### Usage Policy

- Quotas and limits.
- Login/account requirements.
- Device/session/user basis.
- Language behavior.
- Moderation/safety constraints if visible or requested.

### UI Surface

- Homepage behavior.
- Main controls.
- Result states.
- Empty/loading/error states.
- Copy/save/share actions.

### Out-of-Scope Noise

Identify but usually exclude:

- Template residue.
- Demo agents or starter-kit docs.
- Dead or legacy features not visible in the current product.
- Framework plumbing and infrastructure.
- Basic auth/admin/legal pages unless central to the requested product prompt.

## Fact Extraction Check

Before writing the final implementation prompt, build an internal evidence table.

Example:

| Product fact | Evidence | Confidence | Include? |
| --- | --- | --- | --- |
| Product name is Trazy | User instruction, app assets, product UI | High | Yes |
| Core function is communication rewrite | User instruction, rewrite/translate UI or API | High | Yes |
| Needs login | Auth components exist, but user says no login | Low | No |
| Daily quota is 30 per device | User instruction | High | Yes |
| Official template page is required | README template residue only | Low | No |

Rules:

- Include a feature only if it is visible, strongly implied, or explicitly requested.
- Exclude features that are only template residue, unused code, old routes, infrastructure, or speculation.
- If code and current user instruction conflict, the current user instruction wins.
- If evidence is weak but useful, omit it from a direct implementation prompt unless the user asks for options.

## Product Prompt Check

Run this checklist before returning the final prompt.

### 1. Fact Coverage

- Every included requirement has evidence or was explicitly requested.
- Low-confidence features were removed.
- README claims were verified against UI/code before inclusion.
- Product type, user roles, output type, feature maturity, and MVP boundary were considered.

### 2. Product Loop

- The prompt has one clear user value loop.
- Input, choices, output, and result action are explicit.
- The generated result contents are concrete.

### 3. AI Prompt Quality

If AI generation exists:

- General AI role/task is specified.
- Scenario prompts are included when scenarios exist.
- Tone/style rules are included when tone choices exist.
- Output format is specified.
- At least one sample input/output is included when useful.

### 4. Scope Cleanliness

- The prompt is not a repo summary.
- The prompt avoids framework, database, route, and component details unless requested.
- Template residue and unused features are excluded.
- The prompt avoids long "do not build" lists; it states intended product behavior positively.

### 5. Implementation-Agent Usability

- A coding agent can implement from the prompt without asking what the product is.
- Product terms, options, limits, and states are concrete.
- Acceptance checks are included when helpful.
- The structure matches the requested artifact type instead of a fixed template.

## Hard Gate

Do not return the final implementation prompt until Product Prompt Check passes.

If any check fails:

1. Inspect the missing project surface.
2. Revise the extracted product prompt.
3. Run the check again.
4. Only then return the final prompt.

## Output Rules

- Write what to build, not how to implement it.
- Keep the final prompt compact and executable.
- Use the user's language unless they request another language.
- Prefer positive requirements over negative scope.
- Mention implementation details only when they are product-facing or explicitly requested.
- Include a short "Check Passed" note before the prompt.

## Output Template

```text
Check Passed:
- Inspected [surfaces].
- Identified core loop: [input] -> [choice] -> [output] -> [action].
- Verified [quota/language/state/prompt facts].
- Excluded [noise category] as non-core or unsupported.

实现 [Product] MVP。

[Product] 是一个 [one sentence product definition]。

核心功能：

1. [Primary input]
- ...

2. [User choices]
- ...

3. [Generated output]
- ...

4. [Basic operations]
- ...

5. [Usage limits]
- ...

6. [Language support]
- ...

AI 生成规则：

通用 prompt：
...

场景 prompt：
...

示例：
...

验收标准：
- ...
```

## Common Mistakes

- Summarizing the repository instead of extracting the product prompt.
- Including login, official templates, dashboards, admin, community, or history features as core MVP when they are not required for the primary loop.
- Treating old routes or existing files as product requirements.
- Writing only "call AI" without describing the actual generation behavior.
- Over-specifying technology choices when the user asked for product functionality.
- Repeating long lists of exclusions instead of stating the intended product positively.
