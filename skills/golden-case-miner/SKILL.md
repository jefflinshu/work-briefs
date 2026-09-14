---
name: golden-case-miner
description: Use when mining real user projects, raw agent traces, project summaries, feedback, competitor evidence, and technical materials to build a reusable Golden Case Roster for AI/vibe-coding product evaluation, regression testing, and system improvement.
---

# Golden Case Miner

## Overview

Turn messy real-world product evidence into a maintainable **Golden Case Roster**.

A Golden Case is not a showcase project and not merely a good prompt. It is the smallest meaningful business task that can be:

- reproduced,
- observed,
- scored,
- diagnosed when it fails,
- and rerun after Agent / Skill / Tool / Harness / Template changes.

The final asset should support both product evaluation and engineering regression.

**Canonical package:**

`Spec + Skill + Tool + Expected Trace + Eval`

---

## 0. Scope and Boundary

Golden Case Miner does **not** primarily:

- write PRDs,
- summarize all projects,
- rank users by revenue,
- collect visually impressive demos,
- or convert every user request into a benchmark.

It extracts the tasks that are most valuable for repeatedly testing the product's actual ability to deliver working applications.

Prefer cases that expose real business loops such as:

- create → persist → edit → delete,
- user login → permission check → role-specific action,
- customer booking → availability update → merchant schedule update → notification,
- order → payment/instruction → status transition → inventory update,
- document submission → review → approve/reject/request-new-documents,
- domain/DNS setup → verification → deploy → public access.

A Case should be a **testable business unit**, not a broad industry label.

---

## 1. Inputs

Use any available evidence, but distinguish evidence quality.

### Primary evidence

1. **Raw project trace**
   - user messages,
   - multi-turn corrections,
   - Agent actions,
   - tool calls and tool results,
   - generated/edited files,
   - errors and retries,
   - deployment/testing steps,
   - final user feedback.

2. **Project summary / metadata**
   - user_id,
   - project_id,
   - country/language,
   - project type,
   - project summary,
   - creation/update time,
   - conversation depth where available.

3. **User feedback**
   - explicit complaints,
   - repeated correction requests,
   - requested missing functionality,
   - support tickets,
   - thumbs-down / reason labels.

### Secondary evidence

4. **Commercial signals**
   - paid / unpaid,
   - plan,
   - renewals/upgrades,
   - usage depth.

Use commercial data as a **priority signal**, not as proof that a specific project or feature caused payment or renewal.

5. **Competitor evidence**
   - comparable workflows,
   - benchmark behavior,
   - public product capabilities,
   - reference implementations.

6. **Technical evidence**
   - architecture docs,
   - available Skills/Tools,
   - model/tool limitations,
   - platform capability docs,
   - known incidents and bugs.

---

## 2. Golden Case Definition

A candidate qualifies only when it has most of the following properties.

### Required properties

- **Real demand** — comes from actual user behavior or a clearly justified benchmark.
- **Clear user goal** — success can be expressed as a concrete business outcome.
- **Bounded scope** — the task can be rerun without reproducing an entire company.
- **Observable result** — success/failure can be verified.
- **Reproducibility** — initial state and required inputs can be reconstructed.
- **Diagnostic value** — a failure reveals something useful about the system.
- **Regression value** — rerunning the Case after changes is meaningful.

### Strong positive signals

- paying or high-intent users repeatedly attempted the workflow,
- the same business-loop failure appears across multiple projects,
- a user reaches deep multi-turn usage before failing,
- the Case requires multiple capabilities to work together,
- the failure is easy to mistake for "done" if evaluation only checks generated UI/code,
- competitors complete the same task materially better.

### Negative signals

Do not promote a candidate merely because:

- the UI looks impressive,
- the user paid,
- the project is large,
- the prompt is long,
- one isolated user requested an unusual rule,
- generated code contains an integration skeleton,
- the Agent claimed the task was finished.

---

## 3. Evidence Discipline

Always separate:

1. **Requested** — what the user asked for.
2. **Generated** — what the Agent/code appears to implement.
3. **Executed** — what tools/tests actually ran.
4. **Observed** — what the user/system could demonstrably do.
5. **Verified** — what the evaluator can reproduce and assert.

Never collapse these into one status.

Examples:

- "Payment API code exists" does not mean a real payment succeeded.
- "Calendar page exists" does not mean bookings correctly block future availability.
- "Admin login UI exists" does not mean a merchant can log in with correct permissions.
- "Deployment succeeded" does not mean the public workflow works end-to-end.

When raw Trace is unavailable, mark the evidence gap instead of inventing the missing behavior.

---

## 4. Workflow

### Step 1 — Normalize the evidence

Join sources around the smallest reliable unit, normally:

`user_id + project_id`

Create a normalized record containing:

- project identity,
- scenario,
- user goal,
- explicit requirements,
- relevant Trace spans,
- corrections/failures,
- commercial/context signals,
- final observable state,
- evidence confidence.

Do not use project summaries as substitutes for Trace when diagnosing a blocker.

---

### Step 2 — Extract Jobs and business loops

Map each project to one or more concrete Jobs.

Examples:

- Restaurant → reservation, QR ordering, kitchen workflow.
- Fleet company → driver review, rental contract, payment tracking.
- Salon → service booking, availability, WhatsApp confirmation.
- Retail → catalog, cart, PIX/payment, stock deduction.

Then rewrite the Job as a stateful loop:

`Initial state → User action → System action → State transition → External/role effect → Verification`

Prefer loops over feature lists.

---

### Step 3 — Mine failure patterns

Scan repeated Trace behavior and user corrections.

Cluster failures by the **same broken loop**, not merely by shared keywords.

Good clusters:

- booking is created but does not appear in merchant schedule,
- reserved slot remains available to another customer,
- email/WhatsApp action is rendered but never actually sends,
- merchant cannot enter the generated admin,
- CRUD visually succeeds but data is not persisted,
- deletion removes UI state but not database state,
- role permissions exist in UI but are not enforced,
- integration code exists but credentials/runtime are never validated.

Do not treat every failure in the same industry as one problem.

---

### Step 4 — Generate candidate Cases

For each recurring/high-value loop, create a candidate with:

- user goal,
- actors,
- initial state,
- main workflow,
- business rules,
- required capabilities,
- expected end state,
- known historical failure,
- source evidence.

Reduce broad projects into independently evaluable tasks where possible.

---

### Step 5 — Score candidates

Score each dimension from **0–3**.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Real-user evidence | hypothetical | weak | clear single-user | repeated/strong |
| Business value | cosmetic | useful | important workflow | blocks real operation |
| Reproducibility | unclear | heavy manual setup | mostly reproducible | deterministic fixture |
| Observability | subjective | partial | clear assertions | fully machine-verifiable |
| Capability coverage | trivial | one capability | multi-step | cross-system/stateful |
| Diagnostic value | vague failure | some signal | localized | maps clearly to system layer |
| Regression value | unlikely to recur | occasional | likely | core recurring capability |
| Representativeness | edge case | niche | common segment | repeated core pattern |

Use the score to prioritize investigation, not to manufacture false precision.

### Hard gates

A Golden Case should normally have:

- a defined initial state,
- an explicit success condition,
- a reproducible verification path,
- enough evidence to explain why the Case matters.

If these are missing, keep it as `candidate` rather than `golden`.

---

## 5. Build the Golden Case Package

Every promoted Case should be stored as:

### A. Spec

Defines:

- user / business context,
- actors and roles,
- initial data,
- required workflow,
- business rules,
- constraints,
- expected final state.

### B. Skill

The reusable domain/process knowledge that the Agent may legitimately use.

The Skill should help solve the class of task without encoding the hidden answer.

### C. Tool

The allowed tools/integrations/runtime available to the Agent.

Record:

- required tools,
- credentials/fixtures,
- permissions,
- network/runtime assumptions,
- mocked vs real external services.

### D. Expected Trace

Describe expected behavioral checkpoints, not a single exact chain of thought.

Examples:

- inspect existing schema before destructive migration,
- establish persistence before building dependent CRUD,
- test role permissions with different users,
- validate external API/tool response instead of assuming success,
- verify state after mutation,
- run the relevant user flow after implementation.

Avoid requiring one exact implementation if multiple valid solutions exist.

### E. Eval

Each Case should contain:

**Result Eval + Trace Eval**

Result Eval checks the delivered application behavior.

Trace Eval checks whether the Agent reached the result through valid, robust actions.

---

## 6. Eval Design

### 6.1 Result Eval

Prefer deterministic assertions.

Examples:

- record persists after refresh,
- second device/session sees the same record,
- unauthorized role cannot perform restricted action,
- deleted record is actually absent from storage,
- approved document changes the review status correctly,
- booked slot is no longer offered,
- notification is recorded/sent through the expected channel,
- payment/order status transition is consistent,
- deployment URL serves the expected application.

Cover four layers where relevant:

1. **Data lifecycle**
2. **Business rules / state machine**
3. **Permissions**
4. **UI behavior / end-to-end workflow**

---

### 6.2 Trace Eval

Inspect observable Agent/tool behavior such as:

- instruction following,
- planning/decomposition,
- schema decisions,
- tool selection,
- tool invocation correctness,
- error handling,
- permission handling,
- state verification,
- test execution,
- deployment verification,
- security/integrity.

Trace Eval should help localize failure to a stage such as:

`planning → schema → implementation → tool → permission → UI/action → verification`

Do not score private chain-of-thought. Evaluate observable actions and tool traces.

---

### 6.3 Hidden Evaluation

Keep critical assertions hidden from the Agent under test.

Use hidden evaluation to prevent:

- hard-coded expected values,
- reading evaluator fixtures/answers,
- editing tests instead of solving the task,
- bypassing required workflows,
- accidental one-time passes.

Where appropriate, randomize fixture values and entity IDs.

---

### 6.4 Forbidden Shortcuts

A passing final screen is insufficient if the Agent cheated the intended workflow.

Detect or forbid, when relevant:

- direct database mutation when the user flow must work through the application,
- hard-coding fixture-specific IDs/values,
- modifying test files/evaluator state,
- deleting failing assertions,
- reading hidden-answer files,
- bypassing permission/business-rule layers,
- claiming external success without a tool/API result.

Use environment isolation so the evaluated Agent cannot access hidden evaluator material.

---

## 7. Failure Localization

When a Case fails, classify the root layer.

Default taxonomy:

- **Model** — reasoning/coding capability failure.
- **Skill** — missing or misleading reusable instructions/domain knowledge.
- **Harness** — context assembly, orchestration, memory, execution-loop problem.
- **Tool** — tool unavailable, malformed invocation, bad integration contract, unreliable result.
- **Template** — starter architecture/schema/component pattern makes the task fail or expensive.

Optionally add:

- **Platform** — deployment/runtime/storage/auth capability.
- **Eval** — evaluator itself is wrong, flaky, or over-constrained.

Do not patch a Golden Case to make one run pass. Use repeated failures to identify the system layer.

---

## 8. Golden Case Roster

Maintain a roster instead of a flat prompt list.

Recommended fields:

| Field | Meaning |
|---|---|
| `case_id` | Stable identifier |
| `name` | Short business-task name |
| `status` | candidate / golden / retired |
| `priority` | P0 / P1 / P2 |
| `scenario` | Business context |
| `job` | Concrete Job-to-be-done |
| `actors` | Customer / merchant / admin / manager / etc. |
| `source_refs` | Project/Trace/feedback references |
| `evidence_confidence` | high / medium / low |
| `initial_state` | Reproducible fixture |
| `spec` | Required behavior and rules |
| `required_capabilities` | Auth / CRUD / payments / integrations / deploy / etc. |
| `tools` | Allowed/required tools |
| `expected_trace` | Observable checkpoints |
| `result_eval` | End-state assertions |
| `trace_eval` | Process/action assertions |
| `hidden_eval` | Hidden checks |
| `forbidden_shortcuts` | Invalid ways to pass |
| `historical_failure` | Why this became a Case |
| `failure_layer` | Model / Skill / Harness / Tool / Template / Platform |
| `difficulty` | L1–L4 or project-specific scale |
| `last_regression_result` | latest benchmark result |

---

## 9. Roster Coverage

A strong roster should cover different failure surfaces, not only different industries.

Track coverage across:

- CRUD and persistence,
- auth/session,
- roles and permissions,
- state machines,
- data lifecycle,
- file upload/storage,
- email/notification,
- payments,
- calendar/availability,
- third-party integrations,
- custom domains/deployment,
- responsive/mobile interaction,
- migration/change requests,
- repair of an existing broken application.

Also balance:

- build-from-scratch vs iterate/fix,
- short vs long tasks,
- single-role vs multi-role,
- internal system vs public customer flow,
- deterministic local workflow vs external integration.

---

## 10. Output Contract

When asked to mine Golden Cases, return in this order:

1. **Dataset/evidence coverage**
   - sources used,
   - sample size,
   - missing evidence,
   - important limitations.

2. **Candidate clusters**
   - Job/business loop,
   - repeated user evidence,
   - recurring failure pattern.

3. **Golden Case Roster**
   - prioritized table,
   - normally select only the strongest cases requested by the user.

4. **Case Cards**
   - one complete package per selected Case:
   - `Spec + Skill + Tool + Expected Trace + Eval`.

5. **Capability Coverage Matrix**
   - Case × capability/failure surface.

6. **Failure-layer hypotheses**
   - Model / Skill / Harness / Tool / Template / Platform,
   - clearly label hypotheses vs verified causes.

7. **Evidence gaps / next collection**
   - what additional Trace/test is required before promotion.

If the user asks for only N cases, return the best N rather than expanding into a broad report.

---

## 11. Regression Loop

Golden Cases are living evaluation assets.

Use this loop:

`Collect repeated failures`
→ `Cluster failure patterns`
→ `Identify Model / Skill / Harness / Tool / Template layer`
→ `Fix the systemic issue`
→ `Run the full Golden Case regression`
→ `Compare Result Eval + Trace Eval`
→ `Promote/update/retire cases`

Do not optimize a single Case in isolation if the change degrades the wider roster.

---

## 12. Guardrails

- Never invent Trace evidence, user behavior, payment outcomes, or production success.
- Paid/renewal data is a prioritization signal, not proof of causality for one project.
- Do not infer a blocker from a project summary when the raw Trace does not support it.
- Do not confuse generated code with an executed business workflow.
- Do not promote a one-off exotic rule as a platform-wide capability without repeated evidence.
- Do not make a benchmark pass by weakening evaluation.
- Keep hidden evaluation and evaluator fixtures unavailable to the tested Agent.
- Prefer deterministic checks over subjective visual impressions.
- When visual quality matters, separate visual evaluation from functional success.
- Mark uncertainty explicitly.
- Preserve source references so every Case can be audited back to real evidence.

---

## Quick Reference

| Decision | Default |
|---|---|
| Unit of analysis | User project → concrete Job/business loop |
| Golden Case asset | Spec + Skill + Tool + Expected Trace + Eval |
| Eval | Result Eval + Trace Eval |
| Selection | Real demand + reproducibility + observability + diagnostic/regression value |
| Root-cause layers | Model / Skill / Harness / Tool / Template |
| Anti-overfit | Hidden eval + environment isolation + forbidden-shortcut detection |
| Main purpose | Repeatable product capability evaluation and regression |
