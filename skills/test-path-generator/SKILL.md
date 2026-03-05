---
name: test-path-generator
description: >
  Generates a single complete survey test path in Seurat Group's exact format,
  given a Survey Map (from the survey-mapper skill) and one row from the test
  path matrix. The path is a question-by-question walkthrough of the survey with
  every check, piping verification, response visibility rule, variable assignment
  confirmation, and selection instruction written out precisely.
  Use this skill when the user says "generate path [N]," "write test path [N],"
  "do path [N]," or similar. Requires a completed Survey Map file as input.
  Run survey-mapper first if no map exists yet.
---

# Test Path Generator

> **Before generating any path, read:** `references/check_format_patterns.md`
> Real examples of every check type in exact Seurat Group wording and format.

Your job is to simulate one specific test path through a survey and write out
every check, instruction, and verification in Seurat Group's exact format.

---

## Step 1 — Gather Inputs

You need three things before writing anything:

1. **The Survey Map** (`[ProjectName]_Survey_Map.md`) — produced by survey-mapper.
   Stop and run survey-mapper first if no map exists.
2. **The test matrix row for this path** — the full row from the matrix xlsx,
   defining all variable assignments for this path.
3. **The check_format_patterns.md reference** — read it before writing checks.

Read the full Survey Map before generating anything.

---

## Step 2 — Parse the Matrix Row (Rule 1: Multi-Value Parsing)

Before initializing state, parse ALL matrix fields carefully:

**CRITICAL: Split comma-separated cell values into full lists.**
"Value A, Value B" → ["Value A", "Value B"]
Apply ALL values — never take only the first token.

**Matrix field → question binding:**
Use the Survey Map's Variable Registry to understand which matrix columns
bind to which survey questions. For each matrix column:
1. Find the variable it corresponds to in the Variable Registry
2. Identify which question sets that variable
3. Map the matrix value to the correct response option at that question

Do NOT apply one field's values to another question. Each matrix column maps
to a specific question — the Survey Map defines this binding.

---

## Step 3 — Initialize Path State Register

Extract all variable assignments from the matrix row and write them as an
explicit state register before writing any checks.

```
PATH STATE REGISTER:
<variable_1> = "[value from matrix]"
<variable_2> = "[value from matrix]"
<variable_3> = "[value from matrix]"
<derived_flag_1> = Yes / NOT assigned   ← derived from screener selections
<derived_flag_2> = Yes / NOT assigned
[... list ALL variables from the Survey Map's Variable Registry]
```

Populate each variable using the matrix row. For derived variables (flags
computed from other selections), determine their value by evaluating the
survey map's trigger conditions against the matrix's selections.

Update this register after each selection throughout path generation.

---

## Step 4 — Category / Segment Assignment at Screener (Rule 6)

If the survey has a category or segment assignment question (typically in the
screener), assign the category variable IMMEDIATELY after that question —
do NOT wait for later carousel or deep-dive questions.

Read the Survey Map's **Category Assignment Rules** section to find:
- The priority order for assignment
- The `category_assignment_excluded` list (categories that cannot be assigned)
- The `deep_dive_carousel_excluded` list (stricter exclusion for carousels)

If the matrix's derived flag contradicts the screener selections, surface
a conflict flag and use the survey-derived value:
> ⚠️ CONFLICT: Matrix states [flag]=[value] but screener selections derive
> [derived value]. Using survey-derived value. Verify with project lead.

---

## Step 5 — Walk Through Every Question in Order

Go question by question through the Survey Map. At each question, reason
through these steps before writing output:

**A. Is this question visible?**
Look up the question's `show_condition` in the survey map.
Evaluate the structured triple against current state:
  - `not_includes`, `not_assigned`, `not_equals` → question shows when the
    condition is TRUE (i.e., the thing is absent). Never invert polarity.
  - No condition (null) / display_tag: always_shown → always include.

If hidden, write only:
```
Q[N]:
Ensure you do not see the question
```

**B. Piping checks** (first checks after visibility):
If question text or response options pipe variables, write the piping check
first. See check ordering in Step 6.

**C. Format and structure checks**:
Question type, column types, randomization, scale details.

**D. Path-specific checks** (depend on state register):
Response option visibility, groupings, anchoring, variable assignment.

**E. Selection instruction** (last line in block):
Derived from matrix value for this path. "Select any" is NOT acceptable when
a matrix field maps to this question — derive the specific selection.

---

## Rule 2 — Ambiguous Qualifying Criteria

When a question's qualifying response codes are not defined in the survey
document (the matrix says Y/N but the survey doesn't specify which responses
qualify), always flag it:

> ⚠️ AMBIGUOUS QUALIFIER: [Q-ID] qualifying responses are not defined in the
> survey doc. Matrix says [field] = [Y/N]. Select any as a safe default.
> Confirm qualifying response codes with project lead before QA.

Always output this flag and use "Select any."

---

## Rule 3 — Deterministic Selection Enforcement

Whenever a matrix field maps to a specific question, "Select any" is NOT
acceptable. Derive the exact selection from the matrix value.

Key principles:
- If the matrix says a flag = N, do NOT select the response that would
  trigger that flag. Select any other response.
- If the matrix says a flag = Y, select the response that triggers it.
- For specific matrix values (motivation, brand, source, etc.), match to
  the exact response option using Rule 4.

For programming notes (randomization, anchoring): assert the survey doc
behavior, never contradict it. If survey says "Randomize," write
"Ensure randomized." Never write "Ensure do not randomize" if the survey
says randomize.

---

## Rule 4 — Response Label Exact Matching

When selecting a response option from a matrix label:
1. First: exact match against response options in the survey map
2. Second: case-insensitive match
3. If no clean match: flag it, do not silently substitute

> ⚠️ LABEL MISMATCH: Matrix says "[matrix label]" but closest survey option
> is "[survey option]". Verify the correct response before QA.

---

## Rule 5 — Carousel Scope

For any carousel question, read the Survey Map's **Carousel Scope Rules**
section to determine which categories/options should appear.

**Restricted carousels** (carousel_include_only defined):
Only cycle through options matching the include list. If none of the
qualifying options were selected, the carousel question is hidden.
Write: "Ensure you do not see the question."

**Excluded carousels** (carousel_exclude defined):
Take the path's selections and remove excluded options before writing the
carousel check. Write the check using ONLY the remaining eligible options.

If a matrix-specified option is in the exclusion list, drop it and add:
> ⚠️ CAROUSEL SCOPE: Matrix includes [option] but it is excluded from
> [Q-ID] per survey doc. Not included in carousel check.

---

## Rule 7 — Loop Sequencing

If the survey contains loop structures (e.g., questions that repeat for
each assigned moment, segment, brand, etc.), follow the Survey Map's
**Loop Structure** section.

Key rules:
- Messages that open each loop iteration appear INSIDE the loop, not before
  the question that assigns the loop variable.
- If a loop variable has 2+ values, the loop body repeats that many times.
- Conditional questions within loops are evaluated per-iteration against
  the state at that point.
- Post-loop questions (e.g., source carousels that aggregate across loops)
  appear AFTER all loop iterations are complete.

---

## Rule 8 — Negative Show Conditions

When the Survey Map defines a show condition with `not_includes` or
`not_assigned`, the question shows when the condition is TRUE — meaning
the referenced value is ABSENT.

Evaluation pattern:
```
{subject: [question], operator: not_includes, value: [response]}
→ SHOW if [response] was NOT selected in [question]

{subject: "<variable>", operator: not_assigned}
→ SHOW if <variable> was never assigned
```

Common pattern: "openness" or "barrier" questions shown to respondents
who did NOT purchase a particular category. The question about Category A
openness shows when the respondent is NOT a Category A buyer.

**Never invert polarity.** not_includes = SHOW when absent.

---

## Rule 9 — Source Resolution / Piping Chains

If the Survey Map defines a multi-step resolution chain (e.g., sources
piped through from multiple upstream questions), follow the chain exactly:

1. Read the Survey Map's resolution chain section
2. Collect values from each step in order
3. Apply any exclusions or substitutions defined in the chain
4. Deduplicate the final set
5. Pipe the resolved set into the target question

Do NOT pipe raw parent-level labels when the chain specifies sub-sources.

---

## Rule 10 — Always-Shown Questions

Some questions are shown to ALL respondents regardless of path state.
The Survey Map marks these with `display_tag: always_shown`.

Never hide an always_shown question based on path variables like user type,
segment, or category. If the matrix defines a response for an always_shown
question, use it; otherwise, "Select any."

---

## Rule 11 — Follow-Up Trigger Questions

Some questions only appear when specific response codes are selected in
their parent question. The Survey Map defines these trigger conditions.

Read the trigger_codes list from the Survey Map to determine if the
follow-up appears for this path. Do not assume which responses trigger
it — always check the Survey Map.

---

## Rule 12 — Column Direction in Multi-Column Grids

For multi-column grid questions, the Survey Map defines what each column
represents. Use the correct column mapping:

Read the Survey Map entry for the question to find:
- C1 = [what C1 represents]
- C2 = [what C2 represents]

Never swap columns. If the matrix specifies values by column label
(e.g., "Before" = C1, "After" = C2), map them correctly.

---

## Rule 13 — No Termination Logic in Paths

**CRITICAL: Do NOT include any termination checks inside test paths.**

The tester follows a qualifying path — they will never hit a termination
condition. Lines like "Ensure respondents selecting X are terminated
immediately" are noise in a path and must be omitted entirely.

Termination logic belongs ONLY in the Screener Termination Checks section,
which is produced by the test-plan-assembler, not the path generator.

What to write instead:
- For selection: "Select any except R1-R4" (the "except" avoids termination)
- For qualifying selection: "Select R1 in C1 and C2" (just select the
  qualifying option)

---

## Rule 14 — Every Message Must Appear

**CRITICAL: Every message marker (M1, M2, M3, ...) from the survey doc
MUST appear in every path.**

At minimum, each message block must include:
```
M[N]:
Ensure message is shown
```

Additionally, include:
- Piping checks: "Ensure <variable> is piped through" (if applicable)
- Content checks: "Ensure message reads: '...'" (if exact text matters)
- Image anchoring: "Ensure images remain anchored from Q[N]-Q[M]" (if applicable)
- Audience variant: "Ensure message shown to <audience>" (if applicable)

Never skip a message even if it has no piping — the tester still needs to
verify it appears.

---

## Rule 15 — Sub-Questions with Letter Suffixes

**CRITICAL: Never skip questions with letter suffixes (a, b, c, d).**

Questions like S11a, Q302a, Q307a, Q404a are separate questions in the
survey doc and must each have their own block in the test path.

When walking through the survey map, check for sub-questions after every
question. Each sub-question gets its own block with full checks, piping,
and selection.

---

## Rule 16 — Gabor-Granger Pricing Auto-Detection

When the Survey Map flags a question as `Type: Gabor-Granger carousel`,
generate cascading sub-questions.

Read from the Survey Map:
- `price_list`: the available price points
- `median_price`: the starting price
- `stepping_logic`: how R1-R3 and R4-R5 move the price
- `bound_variable`: the GG variable to assign

The direction (up vs down) depends on the path's target GG value relative
to the median price.

Generate one sub-question per price step until the bound is found:
```
Q[N]:
Ensure carousel Gabor-Granger format
Ensure 5-point scale from "Very unlikely" to "Very likely"
Ensure price is piped through as <price> in question text
[stepping instructions to reach target GG value]
Ensure assigned <GG variable> = "[target price]"
```

When a GG section should be hidden (e.g., the respondent is a purchaser
of that brand), write "Ensure you do not see the question" for each
question in the section.

---

## Rule 17 — Formatting and Accuracy Micro-Rules

### 17a. Redundant Selection Instructions
When a format check already states the constraint, the selection instruction
should NOT repeat it:
- WRONG: "Ensure select up to 2" → "Select any up to 2"
- RIGHT: "Ensure select up to 2" → "Select any"

### 17b. Grouping Notation — Use Ranges
For 3+ consecutive response options, use range notation:
- WRONG: "Ensure R2, R3, and R4 are kept together"
- RIGHT: "Ensure R2-R4 are kept together"
For exactly 2 options, comma form:
- RIGHT: "Ensure R6 and R7 are together"

### 17c. Variable Assignment Labels
Always include BOTH the variable name AND value:
- WRONG: "Ensure assigned <some value>"
- RIGHT: "Ensure assigned <variable_name> = '[value]'"

### 17d. Piped Response Option Wording
When response options are piped from a previous question:
- WRONG: "Ensure response options from S16 R5-R12 are piped through"
- RIGHT: "Ensure response options selected in [Q-ID] are piped through"

### 17e. Bolding and Formatting Checks
If the survey doc marks specific words as bold or underlined:
- Include: "Ensure select words in response options are bolded"

### 17f. Anchor/ME Only From Programming Notes
Only write "anchored" or "mutually exclusive" checks when the survey doc
programming notes EXPLICITLY say "Anchor" and/or "Mutually exclusive."
Do NOT fabricate from "Terminate" notes.

### 17g. Question ID Fidelity
Use the exact question IDs from the survey map. Do not renumber questions.

### 17h. Merged Cell Coverage
When a programming note applies to multiple consecutive response options,
apply the note to ALL affected options, not just the first.

---

## Step 6 — Write Output in Exact Format

Follow the format precisely. See check_format_patterns.md for all examples.

### Path header
```
Path [N]
```

### Message blocks
```
M[N]:
Ensure message is shown
Ensure <variable> is piped through
```

### Question blocks
```
Q[N]:
[check line 1]
[check line 2]
[Select instruction — always last]
```

No blank lines between checks within one block. One blank line between blocks.

### Check order within each block (MANDATORY):
1. Question visibility ("Ensure you see the question" — only when conditional)
2. Piping: "Ensure <variable> is piped through in question text"
3. Format: question type, columns, scale, randomization
4. Response option visibility: "Ensure you see/do not see R[N]"
5. Response groupings: "Ensure R[N] and R[M] are together"
6. Response option piping: "Ensure <X> is piped through in response options"
7. Anchored / mutually exclusive options (top anchors first, then bottom)
8. Bolding / formatting: "Ensure select words are bolded"
9. Variable assignment: "Ensure assigned <variable> = 'value'"
10. Selection instruction: "Select [specific response]" — ALWAYS LAST

---

## Step 7 — Update State After Each Selection

After each question with variable assignments, update the state register.
The Survey Map's Variable Registry tells you which questions set which
variables. Key update points are any question listed in the Variable Registry
with a trigger condition.

---

## Step 8 — Completeness Validation Pass

After writing all questions, run this validation:

1. **Required questions check**: Cross-reference the survey map's
   `required_questions` list against your output. Every always_shown question
   must have an entry.
   > ⚠️ MISSING: [Q-ID] is always_shown but not found in path output. Add it.

2. **Sub-question check**: Verify that every "a/b/c/d" sub-question from the
   survey map appears.
   > ⚠️ MISSING: [Q-ID] sub-question exists in survey but not in path. Add it.

3. **Message check**: Every M[N] from the survey map appears in the path output.
   > ⚠️ MISSING: M[N] from survey doc not found in path. Add it.

4. **Variable confirmation check**: Every variable in the state register must
   have at least one "Ensure assigned <variable>" line.

5. **Loop count check**: If loop variables have 2+ values, loop body repeats.

6. **Anchor check**: Every always_shown question's anchored/mutex options have
   a corresponding "Ensure '...' is anchored..." check.

7. **No termination check**: Scan output for "terminated" or "terminate" — if
   found inside a path, remove it per Rule 13.

If validation finds gaps, insert the missing checks before saving.

---

## Step 9 — Conflict Detection Output

When the matrix value conflicts with survey-derived logic, always emit a flag
rather than silently choosing one:

> ⚠️ CONFLICT: Matrix states [field]=[value] but survey logic derives
> [derived value] from [source]. Using [decision: matrix / survey logic].
> Verify with project lead before QA.

Matrix wins for path-definition fields (brand, segment, category, etc.).
Survey logic wins for derived variables (flags computed from selections).

---

## Step 10 — Flag and Note Uncertainties

Inline flag format:
```
Q[N]:
[checks...]
Select any
⚠️ REVIEW: [what is uncertain and why]
```

Collect all flags at the end:
```
--- Path [N] Complete ---
⚠️ Items to review before QA:
1. [Q-ID] — [issue]
2. [Q-ID] — [issue]
```

---

## Output File

Save to: `Path_[N]_[ProjectName].txt`

This file feeds into the test-plan-assembler skill.
