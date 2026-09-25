# Web / Browser Tool Contract

The agent is vendor-neutral. The host environment should provide current web search and page/browser access.

## Discovery tool expectations
- search by role family, location/work model, employer, and recency
- return source URL and source type
- allow follow-up navigation to official employer/ATS pages

## Verification tool expectations
- open the official employer/ATS posting
- inspect current page content and application path
- capture canonical URL and verification timestamp
- distinguish inaccessible/dynamic/authenticated pages from confirmed closure

## Safety / honesty
A tool failure is not evidence that the job is closed. An aggregator result is not evidence that the job is open. If the official source cannot be verified, use `OPEN_STATUS_UNKNOWN`.

The included snapshot verifier is a deterministic helper for saved HTML and CI fixtures; live verification should use the host browser/web capability.
