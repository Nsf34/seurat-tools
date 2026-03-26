# Formatting Standards Reference

Document structure, section headers, table formats, and NEW SCREEN placement conventions.

---

## Document Structure

The survey document follows this top-level structure:

```
[Study Title]
Quantitative Survey Document
[Month Year]

Quant Study Overview
  Research Objectives: [bullet list with sub-bullets]
  Respondent Criteria: [N, demographics, quotas, category engagement, etc.]
  Survey Flow: [section names and brief descriptions]

[Section 1 Name]
  Objectives: [bullet list]
  [Question blocks...]

[Section 2 Name]
  Objectives: [bullet list]
  [Question blocks...]

[...repeat for each section]
```

---

## Section Headers

Each major section gets:
1. A **bold section header** (e.g., "Screener", "Hair Care Priorities", "Usage Deep Dive")
2. An **objectives block** — 2-4 bulleted items restating what the section measures
3. The question blocks

Example:
```
Screener
Objectives:
  - Profile consumers to ensure quotas met / LECs identified
  - Capture engagement with [category] products, including brands
  - Capture inputs to size category growth opportunities
```

All objectives and overview items use **real Word bullets** (interactive list items
with proper numbering definitions), not plain text with manual indentation.

---

## Question Block Format — Merged Table

Every question with response options uses a **single merged table**. The header rows
(R0-R3) are horizontally merged across all columns, and response rows follow below.

```
R0: [TOPIC LABEL]              ← RED on blue, merged across all cols
R1: [QUESTION NUMBER]          ← RED, merged
R2: [Question text] [Italic selection instruction]  ← merged
R3: [Programming note]         ← RED, merged
R4+: [Response rows]           ← format varies by question type
```

After the table:
```
[Logic/programming instructions — RED text, 1-5 sentences]
[blank line]
NEW SCREEN
[blank line]
```

### Question Number + Topic Label
```
S7. Hair Product Category
Q201. SSJ Category Entry Triggers
M1.
D3. Household Size
```

### Programming Notes (one line in R3)

**CRITICAL ordering**: Randomize/Do-not-randomize FIRST, then selection type.

Standard formats:
- `Do not randomize. Single select.`
- `Randomize. Multi-select.`
- `Randomize. Multi-select, max 3.`
- `Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.`
- `Program as a numerical dropdown in increments of 1 (Under 13 – Over 80).`
- `Program as 5-point scale. Randomize. Single select per statement.`
- `Program as a carousel. Pipe through each <qualifying segment> assigned in [Q#].`

**Do NOT repeat programming text**: If a terminate/logic instruction appears in R3,
do NOT also add it as a logic note below the table. Each instruction appears once.

---

## Table Formats

### Simple Response Rows (within merged table)

3 columns. Col 0 is blank but red-formatted. Col 2 is always red-formatted even if empty.

```
Col 0 (blank, red-formatted) | Col 1 (option text, BLACK) | Col 2 (notes, RED)
                             | Option A                   |
                             | Option B                   | Keep R1-R2 together.
                             | Option C                   |
                             | Other, please specify      | Anchor. Open end.
                             | None of the above          | Anchor. Mutually exclusive.
```

### Two-Column Grid (within merged table)

R4 = column header row, R5+ = data rows. 4 total columns.

```
R4: [blank] | [blank] | C1: [Header text] (C1: RED, text BLACK) | C2: [Header text]
R5: [blank] | Option A | [note RED] | [note RED]
R6: [blank] | Option B | |
R7: [blank] | Quality check (Pizza water) | Terminate. | Terminate.
R8: [blank] | None of the above | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
```

### Three-Column Grid (within merged table)

Same pattern, 5 total columns (blank + option + C1 + C2 + C3).

### Scale Grid (Attitude Battery) — Two Separate Tables

**Table 1**: Merged header (R0-R3) + scale rows:
```
R0-R3: [header rows merged across N columns]
R4: 1 (RED) | 2 (RED) | 3 (RED) | 4 (RED) | 5 (RED)
R5: Strongly disagree (BLACK) | Somewhat disagree | Neither | Somewhat agree | Strongly agree
```

Scale labels are BLACK, **no number prefix** (just "Strongly disagree", not "1 Strongly disagree").

**Table 2**: Statement table (separate, immediately below):
```
Col 0 (blank, red-formatted) | Col 1 (statement text, BLACK) [| Col 2 (condition, RED)]
                             | Statement 1
                             | Statement 2
                             | Statement 3                    | Only show if <female>
```

Col 2 only exists if any statement has a conditional display note.

### Bipolar Scale (within merged table)

```
R0-R3: [header rows merged across 3 columns]
R4: [blank] | C1 (RED) | C2 (RED)
R5: [blank] | Left statement (BLACK) | Right statement (BLACK)
R6: [blank] | Left statement (BLACK) | Right statement (BLACK)
```

The programmer builds the numeric scale from the programming note. Do NOT include
inline scale text like "1 — 2 — 3 — 4".

---

## NEW SCREEN Placement

`NEW SCREEN` appears after every question/block — no exceptions. It signals the programmer
to advance to a fresh screen. Place it on its own line in RED, after the logic note.

```
[Logic note]

NEW SCREEN

[Next question's merged table]
```

---

## Hold Terminates Note

Always include this note immediately after the introduction message in the Screener:
```
Hold all terminates until the end of the screener unless otherwise specified.
```

---

## Objective / Rationale → Logic Conversion Guide

The wireframe's "Objective / Rationale" column tells you what logic to build:

| Wireframe Objective Language | Survey Document Output |
|---|---|
| "Ensure respondents meet [criterion]" | Terminate or quota on qualifying response |
| "Min n=X / Max n=Y for [group]" | State quota explicitly after table |
| "Identify [type] consumers" | Create hidden variable; define conditions |
| "Assign [variable] for use in later questions" | Explicit `Create hidden variable` or `Assign` note |
| "Capture inputs to size..." | No logic needed — data capture question only |
| "Ensure quotas are met" | List all quota thresholds explicitly |
| "Flag [type]" | Create hidden variable with conditions |
| "Pipe through selections from [prior question]" | `Pipe through [variable] from [question number]` |
| "Assign based on quotas and least fill" | Least-fill assignment note |

---

## Style Notes

- Use plain, direct language in programming notes — no ambiguity
- Spell out quota thresholds with exact numbers (min n=300, not "at least 300")
- When a response option has conditional display, note it in the right-most column
- Numbered question references use the format: "response in C2 of S14" or "selections in Q201"
- Variable names use angle brackets with underscores: `<qualifying_segment>`, `<LE Consumer>`, `<in-store>`
