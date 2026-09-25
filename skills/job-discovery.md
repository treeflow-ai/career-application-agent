# Job Discovery

## Goal
Find current roles matching candidate preferences without treating search results as verified openings.

## Procedure
1. Read target roles, geography/work-model constraints, and recent history.
2. Search multiple current sources using the host's web/browser tools.
3. Capture title, company, location, discovery URL, source, discovered timestamp, and short snippet.
4. Prefer official employer/ATS links when surfaced.
5. Normalize obvious tracking parameters and deduplicate by employer/title/canonical posting.
6. Send plausible roles to `job-verification`; do not call them open yet.
7. Avoid rediscovering roles already in terminal state unless the posting materially changed.

## Output
A discovery batch with `DISCOVERED` status, never `OPEN_VERIFIED` by search result alone.
