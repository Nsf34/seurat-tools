---
description: Generate today's CPG newsletter for the Seurat team. Open it in Outlook ready to send.
---

Generate today's CPG newsletter using the seurat-tools daily-newsletter skill.

## Instructions

1. Read the full `skills/daily-newsletter/SKILL.md`.
2. Execute the skill exactly as documented, producing an Outlook-compatible HTML newsletter.
3. Mon-Thu = daily pulse (3-4 signals). Friday = weekly digest (5-6 signals + analysis sections).
4. Save HTML to `Intelligence/newsletters/[TODAY].html` and open in Outlook compose mode.

## Key Details
- Prerequisite: today's daily brief must exist (run `/daily-brief` first)
- Output: .html newsletter + Outlook compose window
- Two formats: daily pulse (Mon-Thu) and weekly digest (Friday)
- User override: say "weekly" or "daily" to force a format
