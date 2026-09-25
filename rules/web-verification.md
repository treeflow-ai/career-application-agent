# Job Posting Verification Rules

Openness is time-sensitive.

Prefer evidence in this order:
1. current official employer careers page
2. current employer-linked ATS page
3. employer announcement linking to the role
4. reputable aggregator only as discovery evidence, never final open-status evidence

`OPEN_VERIFIED` requires a current official/ATS source showing a live role or working application path.

Treat as `CLOSED` when an official source explicitly says closed/no longer accepting/filled, the ATS returns a terminal closed state, or the canonical posting is removed and the employer's current listing confirms absence after reasonable re-checking.

Treat as `OPEN_STATUS_UNKNOWN` when evidence conflicts, JavaScript/auth prevents verification, redirects are ambiguous, or only stale/aggregator copies remain.

Record `verified_at`, canonical URL, source type, and a short evidence note. Never claim perpetual openness.
