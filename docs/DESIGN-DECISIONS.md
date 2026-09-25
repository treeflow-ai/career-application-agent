# Design Decisions and Trade-offs

This document explains the main engineering choices in Career Application Agent. It is intended to help a reviewer understand why the repository is structured as an agent workflow rather than a single resume prompt.

## 1. Why separate discovery from verification?

Search results and job-board cards are useful discovery signals, but they are not proof that a role is still open. The agent separates discovery from verification so a cached listing, repost, aggregator card, or copied job description cannot silently become an `OPEN_VERIFIED` target. Verification prefers a current employer or ATS source and may return `OPEN_STATUS_UNKNOWN` when the evidence is not strong enough.

## 2. Why use an evidence bank?

Job descriptions create pressure for a language model to mirror the employer's terminology. Without an evidence boundary, a desired skill in the job description can turn into an implied candidate claim. The evidence bank creates a one-way rule: the JD can influence selection and wording, but candidate facts must come from verified or user-confirmed evidence.

## 3. Why are procedures stored as `skills/*.md`?

Some work requires language-model judgment: interpreting role requirements, mapping transferable experience, writing concise resume bullets, and identifying gaps. These procedures are easier to inspect and revise as declarative skills. Hard invariants are not left to prompts; they are enforced by scripts, tests, and release gates.

## 4. Why maintain durable state?

A job-search agent needs memory across runs: which roles were seen, which were verified, which were skipped, which materials were generated, and what later happened. Durable state supports deduplication, auditability, and market feedback without rewriting historical decisions after the fact.

## 5. Why mix LLM review with deterministic validation?

The deterministic layer checks things that should never depend on model judgment: evidence IDs, private-file leakage, placeholder text, explicit hyperlinks, and state transitions. Semantic review is still needed for judgment-heavy issues such as scope inflation, relevance, tone, and whether a transferable claim is worded carefully enough.

## 6. Why keep human approval in the loop?

The agent prepares reviewable application artifacts; it does not auto-submit applications. The user remains responsible for final submission, factual acceptance, and any sensitive self-identification decisions.

## 7. What does the system deliberately not automate?

It does not ship credentials, bypass authentication, scrape private systems, infer sensitive identity information, guarantee every posting can be verified, or submit applications automatically. If a posting, qualification, claim, or link cannot be verified, the expected behavior is to record a gap or fail the release gate.
