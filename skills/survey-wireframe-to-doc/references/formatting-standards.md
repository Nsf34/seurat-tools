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
  Objectives: [bullet list]
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
2. An **objectives block** — 2–4 bullets restating what the section measures
3. The question blocks

Example:
```
Screener
Objectives:
  - Profile consumers to ensure quotas met / LECs identified
  - Capture engagement with [category] products, including brands
  - Capture inputs to size category growth opportunities
```

---

## Question Block Format

Each question follows this exact format:

```
[QUESTION NUMBER]. [TOPIC LABEL]
[blank line]
[Full question text]. [Selection instruction].
[Programming note — one line, plain text]
[blank line]
[TABLE with response options]
[blank line]
[Logic/programming instructions — 1–5 sentences or bullet points]
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

### Programming Notes (one line, follows question wording)
Standard formats:
- `Do not randomize. Single select.`
- `Randomize. Multi-select.`
- `Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.`
- `Program as a numerical dropdown in increments of 1 (Under 13 – Over 80).`
- `5 pt scale. Randomize. Single select per statement.`
- `Program as a carousel. Pipe through each <qualifying segment> assigned in [Q#].`
- `Randomize groups, but keep each group of retailers together.`

---

## Table Formats

### Simple Single-Select List
```
[TABLE]
| Option A |
| Option B |
| Option C |
| Other, please specify | Anchor. Leave a space.
| None of the above | Anchor. Mutually exclusive.
[/TABLE]
```

### Response Table with Quota/Action Column
```
[TABLE]
| Option A | [quota note or action, e.g., "Min n=300" or "Terminate"]
| Option B | Max n=500
| Option C |
| Prefer not to answer | Anchor. Terminate.
[/TABLE]
```

### Response Table with Variable Assignment Column
```
[TABLE]
| Option A | [quota note] | <variable_a>
| Option B | | <variable_b>
| Other, please specify | | Anchor. Leave a space.
[/TABLE]
```

### Two-Column Grid
```
[TABLE]
|  | C1: [Column 1 header] Select all that apply. | C2: [Column 2 header] Select one.
| Option A | | |
| Option B | | |
| Quality check (e.g., "Pizza water") | Terminate. | Terminate.
| None of the above | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
[/TABLE]
```

### Two-Column Grid with Variable Assignment (3 columns)
```
[TABLE]
|  | C1: [Header] Select all that apply. | C2: [Header] Select one. | <variable>
| Option A | | | <label_a>
| Option B | | | <label_b>
| Other, please specify | | | Anchor. Leave a space.
[/TABLE]
```

### Three-Column Grid (C1/C2/C3)
```
[TABLE]
|  | C1: [Header] | C2: [Header] | C3: [Notes column]
| Option A | | | [Note or variable]
| Option B | | | [Note or variable]
[/TABLE]
```

### Scale Grid (Attitude Battery)
```
[TABLE]
Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree
[/TABLE]

[TABLE]
| Statement 1 |
| Statement 2 |
| Statement 3 | Only show if respondent is <female>
[/TABLE]
```

### Conditional Sub-Groups (e.g., Retailer Lists by Channel)
Use multiple tables with headers for each group:
```
[TABLE]
| Grocery (only show if selected R1 in [question]) | | |
| Kroger | Min n=300 | |
| Safeway | | |
| Other grocery store, please specify | | | Anchor. Leave a space.
[/TABLE]

[TABLE]
| Mass (only show if selected R3 in [question]) | | |
| Target | Min n=300 | |
| Walmart | Min n=300 | |
[/TABLE]
```

---

## NEW SCREEN Placement

`NEW SCREEN` appears after every question/block — no exceptions. It signals the programmer to advance to a fresh screen. Place it flush left, on its own line, after the logic note and before the next question.

```
[Logic note]
NEW SCREEN

[Next question number]. [Next topic]
```

For transition messages, NEW SCREEN appears before the message that starts the next section:
```
[Last question of previous section logic]
NEW SCREEN

M2.
[Transition message text]
Show to all respondents.
NEW SCREEN
```

---

## Conditional Intro Messages Within Question Tables

When a section begins with a message mid-survey (not a standalone M-number screen), format it as a table row spanning all columns:

```
[TABLE]
Message: [Text piping in <variables> as appropriate] | Message: [same] | Message: [same] | Message: [same]
[/TABLE]

[First question in this section]
```

This indicates the message is shown before the block of questions in that section, not as a separate screen.

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
- When a response option has conditional display (by gender, segment, etc.), note it in the right-most column of the table
- Numbered question references use the format: "response in C2 of S14" or "selections in Q201"
- Variable names are always lowercase with underscores or single words in angle brackets: `<qualifying_segment>`, `<LE Consumer>`, `<in-store>`
