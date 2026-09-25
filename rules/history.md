# Durable State Rules

History is an audit trail and feedback dataset, not a blacklist.

Core states: `DISCOVERED`, `VERIFIED_OPEN`, `OPEN_STATUS_UNKNOWN`, `READY_TO_APPLY`, `APPLIED`, `INTERVIEW`, `REJECTED`, `CLOSED`, `WITHDRAWN`.

Never mark `APPLIED` without explicit user confirmation. Keep prior fit judgments separate from later outcomes.
