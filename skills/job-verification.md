# Job Verification

## Goal
Determine whether a discovered/supplied role currently appears open on an official source.

## Procedure
1. Resolve to the employer's official career page or employer-linked ATS.
2. Check page title/role/company/location and application availability.
3. Look for explicit closed/no-longer-accepting signals.
4. If discovery came from an aggregator, search the employer/ATS independently.
5. Record canonical URL, `verified_at`, source type, and evidence note.
6. Assign `OPEN_VERIFIED`, `CLOSED`, or `OPEN_STATUS_UNKNOWN` according to `rules/web-verification.md`.
7. Only verified/open roles advance automatically to application evaluation.

Never fabricate a successful verification when the host cannot access a dynamic/authenticated page.
