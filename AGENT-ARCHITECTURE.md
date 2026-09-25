# Agent Architecture

The design pattern is:

**policy -> facts/preferences -> skills -> state -> tools -> outputs -> feedback**

## 1. Orchestrator
`SKILL.md` defines modes, sequencing, precedence, required handoffs, and failure behavior.

## 2. Profile
Candidate identity, evidence, preferences, and canonical resume live in local ignored files under `profile/`. The tracked files provide schemas and fictional examples.

## 3. Rules
Rules are cross-cutting policies: truthfulness, privacy, fit scoring, web verification, state semantics, and document quality.

## 4. Skills
Each skill performs one reusable procedure: discovery, verification, evaluation, evidence mapping, application preflight, resume tailoring, cover-letter drafting, state management, feedback review, and interview prep.

## 5. State
`state/history.csv` is durable memory, not model memory. It records what was seen, how it was evaluated, and what happened later.

## 6. Tools
Web search/browser, files, document renderers, and ATS pages are environment-specific. The skill specifies tool contracts rather than hard-coding one model vendor.

## 7. Deterministic scripts
Exact operations — validation, merge semantics, privacy checks, snapshot heuristics — are code, not free-form reasoning.

## 8. Feedback
Observed hiring/application outcomes are stored separately from prior judgments so the search strategy can learn without rewriting history.

See `docs/architecture.svg` for the visual flow.
