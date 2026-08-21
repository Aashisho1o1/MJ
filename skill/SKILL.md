---
name: applyops
description: "Network-first job-search workflow. Use when a candidate asks to find fresh roles, evaluate a posting, check whether they already applied, identify a referral path, tailor application materials, draft outreach, or prepare for interviews. Start from the candidate's connections and use official employer or ATS sources."
---

# ApplyOps

Use ApplyOps as a candidate-owned job-search workflow. Load the candidate's private working files, not the generic files in `templates/`, before making candidate-specific decisions.

## Required private inputs

Ask the candidate to provide or maintain:

- Resume or resume baselines
- `connections.md` or an exported connections file
- `preferences.json`
- `application-registry.jsonl`
- `profile.md`

Use the matching files in `templates/` only as starter formats.

## Core workflow

1. Check the duplicate registry before researching or drafting.
2. Start with companies where the candidate has a plausible connection.
3. Open the official employer career page or official ATS posting.
4. Verify the job link, location, and posting date from the employer or ATS record.
5. Treat search results and aggregators as discovery only.
6. Read the full posting before judging fit.
7. Rank roles, but do not silently discard candidates based on inferred meaning.
8. Explain the fit, referral path, uncertainty, and next action.
9. Draft outreach only for the connections the candidate selects.
10. Record completed screens and application packages explicitly.

## Hard rules

- Never fabricate a candidate fact, metric, contact, or job detail.
- Never represent an inferred posting date as verified.
- Do not submit applications or send messages without explicit approval.
- Do not treat a company-level match as a duplicate when the requisition is different.
- Preserve candidate data and application history locally and privately.

## Freshness

Use the employer or ATS date field whenever possible. A listing without a verifiable date should be labeled as unverified and should not be presented as fresh.

## Referral path

A connection is a possible path, not proof of willingness to refer. Present the person's name, current relationship context if known, and a concise editable outreach draft. Let the candidate decide whether to contact them.

## Templates

- `templates/profile-template.md`
- `templates/connections-template.md`
- `templates/preferences-template.json`
- `templates/application-registry-template.jsonl`
- `templates/resume-template.md`
- `templates/writing-style-template.md`

## Scripts

- `scripts/voicecheck.py` checks basic document issues.
- `scripts/preflight.py` provides delivery checks. Treat warnings as prompts for human review, not automatic truth.
