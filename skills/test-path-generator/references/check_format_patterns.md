# Test Path Check Format Patterns

Example patterns for survey testing. When in doubt about how to phrase a
check, find the closest matching pattern here and follow it exactly.

---

## Path Header
```
Path 1
```
(No colon. No extra descriptors. Just "Path N")

---

## Messages

### Standard message checks
```
M1: ensure message appears
M2: Ensure you see the message
M3: Ensure you see the message
M4: Ensure you see the message
Ensure <brand> <category> is piped through in message text
M5: Ensure you see the message text for <category_flag>
```

### Consumer Journey Loop — M1 and M2 placement
M1 and M2 appear INSIDE their respective loop iterations, AFTER Q1.
They NEVER appear before Q1.

```
Q1:
Ensure multi select
Ensure "None of the above" is anchored to the bottom and mutually exclusive
Select R1 "[moment 1 text]" and R3 "[moment 2 text]"
Ensure assigned <moment 1> = "[moment 1 text]"
Ensure assigned <moment 2> = "[moment 2 text]"

M1: ensure message appears
M1: Ensure message reads: "Now, we'd like to understand what influenced your decisions [moment 1 reference]."

Q2:
[checks...]
Select any

Q3:
[checks...]
Select any

Q4:
Ensure you do not see the question

Q5:
[checks...]
Select any

Q6:
Ensure you do not see the question

Q7:
[checks...]
Select any

Q8:
[checks...]
Select any

M2: Ensure you see the message
M2: Ensure message reads: "Now, we'd like to understand what influenced your decisions [moment 2 reference]."

Q2:
[checks — second loop iteration...]
Select any
```

(Q9/Q10 appear AFTER both loop iterations are complete)

---

## Selection Instructions

**Select any:**
```
Select any
```

**Select any within a range:**
```
Select any response 18-55
Select any R5-R9
Select any R1-R2
```

**Select a specific response:**
```
Select R1 "Yes"
Select "[option text]"
Select R4: [description text]
Select R2 "No"
```

**Select specific responses in a grid:**
```
Select C1, C2, and C3 for "[option A]," and "[option B]"
Select C1 & C2 for all priority categories and any others
Select C1 & C2 for [demographic segment]
```

**Select any EXCEPT something:**
```
Select any except R5
Select any except R2
Select any except "I wouldn't be interested in any of these"
Select any except R1 "[option text]"
```

**Select a specific scale value for each statement:**
```
Select the following for each statement:
[Statement A] - 3
[Statement B] - 2
[Statement C] - 2
```

---

## Visibility Checks — Questions

**Question is conditionally shown and IS visible:**
```
Ensure you see the question
Ensure you see question text for <category_flag>
```

**Question is NOT visible for this path:**
```
Ensure you do not see the question
Ensure you don't see the question
```
(Both forms are acceptable — be consistent within a path)

---

## Visibility Checks — Response Options

**See specific response options:**
```
Ensure you see R3, "[option text]"
Ensure you see R5 and R6
Ensure you see R12
Ensure you do see R11, R15, and R16
```

**Do NOT see specific response options:**
```
Ensure you do not see R5 and R6
Ensure you do not see R2, R4, R5, R6, R7, R9, R10, R11, and R13
Ensure you do not see R3, "[option text]"
Ensure you don't see the question
```

---

## Piping Checks

**Piped through in question text:**
```
Ensure <brand><category> is piped through in question text
Ensure <category> is piped through in question text
Ensure "[category A]" is piped through in question text
Ensure "[category A]," "[category B]," "[category C]" are piped
through
Ensure <provider> is piped through in question text
Ensure <moment 1> is piped through in message text
```

**Piped through in response options:**
```
Ensure <brand> is piped through in R14 response option text
Ensure <category> is piped through in R9, R11, and R17 response text
Ensure response options selected in Q1 are piped through
```

**Piped through in columns:**
```
Ensure <brand><category> is piped through in question text and columns
```

**Category piped as bolded headers:**
```
Ensure question pipes through "[category A]," "[category B]," "[category C]"
as bolded headers
```

---

## Format / Question Type Checks

**Scale questions:**
```
Ensure question is a 10 point scale for each category
Ensure question is a 5 point agreement scale
Ensure question is a 4 point scale with one statement all the way to the left /
other all the way to the right
```

**Multi-select / single-select:**
```
Ensure multi select in C1 and C2
Ensure multi select in C1 and C2 and single select in C3
Ensure single select in C1 and C2
Ensure multi select in C1 and single select in C2
```

**Bolded/underlined text:**
```
Ensure "[text phrase]" is underlined
Ensure "[text A]," "[text B]," and "[text C]" is bolded
Ensure "[text phrase]?" is bolded
```

**Dropdown:**
```
Ensure "[option text]" is not a dropdown and mutually exclusive
```

---

## Anchoring Checks

**Anchored at bottom, mutually exclusive:**
```
Ensure "None of the above" is anchored at the bottom and mutually exclusive
Ensure "I wouldn't be interested in any of these" is anchored to the bottom and
mutually exclusive
Ensure "Brand does not matter to me" is anchored to the top and mutually exclusive
Ensure "Prefer not to answer" is anchored at bottom and mutually exclusive
Ensure "No one else was there" is anchored to the top and mutually exclusive
Ensure "[option text]" is anchored to the bottom and mutually exclusive
```

**Anchored at bottom, open-end:**
```
Ensure "Other; please specify" is anchored to the bottom and open-end
Ensure "Other, please specify" is anchored at bottom
```

---

## Grouping Checks
```
Ensure R2 and R3 are together
Ensure R4 and R5 are together
Ensure R5 and R6 are together
Ensure R8 and R9 are together
Ensure R11 and R12 are together
```

---

## Variable Assignment Checks
```
Ensure assigned <demographic_flag>
Ensure assigned <exclusion_flag> is assigned
Ensure assigned <category_quota> = "[category name]"
Ensure assigned <brand> = "[brand A]," and "[brand B]"
Ensure assigned <category> = "[category name]"
Ensure <brand_name> is assigned <attribute> = [value]
Ensure assigned <category_list> = "[category A]," "[category B],"
"[category C]"
Ensure not assigned <non_category_1> or <non_category_2>
Ensure assigned <other_category> for all other response options selected
Ensure assigned <awareness_flag>
Ensure assigned <user_type_flag>
Ensure assigned <high_interest_category> based on up to 3 responses
Ensure assigned <category_user_flag>
Ensure assigned <category> = "[category name]"
Ensure assigned <provider> = "[source name]"
Ensure assigned <user_status> = "[status]"
Ensure assigned <moment 1> = "[moment description 1]"
Ensure assigned <moment 2> = "[moment description 2]"
Ensure assigned <brand_category> = "[brand name]"
```

---

## Carousel Scope Checks

### S1/S2 — Category Scoping
S1 and S2 cycle ONLY through included categories (if selected in parent question).
No unselected categories ever appear.

**EXAMPLE PATTERN - Path where multiple categories selected:**
```
S1:
Ensure you see the question
Ensure S1 cycles through [included category A] and [included category B] only
Ensure you do not see any other categories in this carousel
Select any
```

**EXAMPLE PATTERN - Path where single category selected:**
```
S1:
Ensure you see the question
Ensure S1 cycles through [included category A] only
Select any
```

**EXAMPLE PATTERN - Path where no qualifying categories selected:**
```
S1:
Ensure you do not see the question

S2:
Ensure you do not see the question
```

### Q1/Q2 — Deep Dive Carousel with Exclusions
Q1 and Q2 cycle through included categories MINUS the excluded categories
(per survey documentation).

**EXAMPLE PATTERN - Path where specific categories included:**
```
Q1:
Ensure Q1 cycles through: "[category A]," "[category B]," "[category C]"
Ensure you do not see [excluded category A], [excluded category B],
or [excluded category C] in this carousel
Select any
```

**EXAMPLE PATTERN - When a matrix-specified category is in the exclusion list:**
```
Q1:
Ensure Q1 cycles through: "[category A]," "[category B]"
Select any
⚠️ CAROUSEL SCOPE: Matrix includes "[excluded category]" in parent question but it is
excluded from Q1/Q2 per survey doc. Not included in carousel check.
```

---

## Negative Show Condition Checks

These questions show when the respondent does NOT have a particular attribute.
Evaluate each against the path state — show when condition is ABSENT.

**EXAMPLE PATTERN — Shows when [condition] NOT selected:**
(Non-[category] respondent sees the [category] openness question)

Path with NO [condition] selected:
```
Q1:
Ensure you see the question
Ensure single select
Ensure "[negative option]" is anchored to the bottom and mutually exclusive
Select any
```

Path WITH [condition] selected:
```
Q1:
Ensure you do not see the question
```

**EXAMPLE PATTERN — Shows when <variable_flag> NOT assigned:**

Path where <variable_flag> was not assigned:
```
Q2:
Ensure you see the question
Select any
```

Path where <variable_flag> = Yes:
```
Q2:
Ensure you do not see the question
```

---

## Source Carousel Checks

Source carousel questions pipe a resolved, deduplicated set of sources based on
multi-question resolution chains per survey documentation.

**EXAMPLE PATTERN - Multiple sources resolved and deduplicated:**

```
Q1:
Ensure you see the question
Ensure the following sources are piped through: "[source A],"
"[source B]," "[source C - sub-sourced]"
Ensure "[source A]" and "[source B]" are NOT duplicate-piped as separate entries
Select any
```

**EXAMPLE PATTERN - Single resolved source:**
```
Q1:
Ensure the following sources are piped through: "[source A]"
([source resolution logic per documentation] are deduplicated to one entry)
Select any
```

---

## Follow-Up Trigger Check

Follow-up questions show ONLY when specific response options are selected in the
parent question. Other responses do NOT trigger the follow-up.

**EXAMPLE PATTERN - Path where trigger option IS selected:**
```
Q1:
Ensure multi select
Ensure "None of the above" is anchored at the bottom and mutually exclusive
Select R9 "[trigger option]"
Ensure assigned <source_type> includes "[trigger option]"

Q2:
Ensure you see the question
Ensure multi select
Select any
```

**EXAMPLE PATTERN - Path where trigger option is NOT selected:**
```
Q1:
Ensure multi select
Select R3 "[non-trigger option]"

Q2:
Ensure you do not see the question
```

---

## Always-Shown Question Pattern

Certain questions appear for ALL respondents regardless of prior responses.
Never hide them based on user type or prior selections.

**EXAMPLE PATTERN - Current state path:**
```
Q1:
Ensure you see the question
Ensure single select
Select R2 "[option]"
```

**EXAMPLE PATTERN - Alternative state with variable assignment:**
```
Q1:
Ensure you see the question
Ensure single select
Select R1 "[option]"
Ensure assigned <status_flag> = Yes

Q2:
Ensure you see the question
Select any
```

---

## Gabor-Granger Pricing Cascade

Gabor-Granger questions use a carousel that steps price up or down based on
the respondent's likelihood response. The skill auto-detects this pattern and
generates cascading sub-questions.

**EXAMPLE PATTERN - Stepping DOWN from median:**
Starting at $[X] median, target GG = $[Y]:
```
Q1:
Ensure you see the question
Ensure carousel Gabor-Granger format
Ensure 5-point scale from "Very unlikely" to "Very likely"
Ensure price is piped through as <price> in question text
Ensure images are anchored in question
To reach <GG_target> = $[Y].00: starting from $[X], select R1-R3 at initial prices, select R4-R5 at target price; then select R1-R3 when shown higher price again
Ensure assigned <GG_target> = "$[Y].00"

Q2:
Ensure you see the question
Ensure <GG_target> "$[Y].00" is piped through in question text
Ensure open-end response
Ensure 5-second pause after question appears before allowing response
Enter any text response
```

**EXAMPLE PATTERN - Stepping UP from median:**
Starting at $[X] median, target GG = $[Y]:
```
Q1:
Ensure you see the question
Ensure carousel Gabor-Granger format
Ensure 5-point scale from "Very unlikely" to "Very likely"
Ensure price is piped through as <price> in question text
Ensure images are anchored in question
To reach <GG_target> = $[Y].00: starting from $[X], select R4-R5 at initial prices, select R1-R3 at target price; then select R4-R5 when shown lower price again
Ensure assigned <GG_target> = "$[Y].00"

Q2:
Ensure you see the question
Ensure <GG_target> "$[Y].00" is piped through in question text
Ensure open-end response
Ensure 5-second pause after question appears before allowing response
Enter any text response
```

**EXAMPLE PATTERN - When GG section is hidden:**
```
M1:
Ensure you do not see the message

Q1:
Ensure you do not see the question

Q2:
Ensure you do not see the question

Q3:
Ensure you do not see the question
```

---

## Sub-Question Examples (a/b/c/d suffixes)

Sub-questions must never be skipped. Each gets its own block:

**EXAMPLE PATTERN - Q1a — Fulfillment Method:**
```
Q1a:
Ensure <brand> and <retailer> are piped through
Ensure two-column grid
Ensure multi-select in C1 and single select in C2
Select R1 "[option A]" in C1 and C2
Ensure assigned <fulfillment_method> = <[option A]>
```

**EXAMPLE PATTERN - Q2a — Segmentation with options:**
```
Q2a:
Ensure segments are piped through: "[option A]" and "[option B]"
Ensure question uses numerical dropdowns from 0% to 100% in increments of 10%
Select any
```

**EXAMPLE PATTERN - Q3a — Single select with piped variable:**
```
Q3a:
Ensure <variable_description> is piped through as [option description]
Ensure single select
Select any
```

---

## Loop Checks
```
Ensure all possible questions in Q1 – Q10 are looped up to two times for all
assigned <brand>
Ensure Q11 - Q12 is looped up to two times for all assigned <brand>
```

---

## Non-Buyer Question Checks
```
Ensure you see the question
Ensure <category_1> and <category_2> is piped through in
question text and the question cycles through twice
Ensure you see R20 and R21
```

---

## Conflict and Ambiguity Flag Format

### Matrix vs. survey-derived value conflict
```
⚠️ CONFLICT: Matrix states [attribute]=[value] but question includes [option],
which assigns <variable>. Using survey-derived value. Verify with project lead before QA.
```

### Matrix vs. official plan conflict (matrix wins)
```
⚠️ CONFLICT: Official plan selects R[N] at Q[ID] but matrix says R[M] "[option text]."
Using matrix value. Official plan may contain an error.
```

### Label mismatch flag
```
⚠️ LABEL MISMATCH: Matrix says "[expected label]" but closest survey
option is "[actual option]." Verify the correct response before QA.
```

### Qualifying condition flag (always emit when uncertain)
```
Q1:
Ensure you see the question
Ensure 5 point agreement scale
Select any
⚠️ QUALIFIER: Q1 qualifying responses are not defined in the survey doc.
Matrix says [flag] = Y. Select any as a safe default.
Confirm qualifying response codes with project lead before QA.
```

### Missing question flag
```
⚠️ MISSING: Q[ID] is referenced in the survey but has no map entry.
Verify whether Q[ID] exists in the programmed survey before using this path in QA.
```

### Required question gap (completeness pass)
```
⚠️ MISSING: Q[ID] is always_shown but not found in this path output. Add it.
```

---

## Key Formatting Rules

1. Question number on its own line with colon: `Q1:`
2. Each check on its own line — no blank lines between checks within one question
3. Blank line between question blocks
4. Selection instruction always LAST within a block (before any ⚠️ flags)
5. Variable names always in angle brackets: `<brand>`, `<category>`
6. Response options in double quotes when referenced: `"None of the above"`
7. Response numbers as R1, R2, R3... and column numbers as C1, C2, C3...
8. "Ensure" capitalized in all checks except the M1 message line (lowercase "ensure")
9. Scale descriptions use numbers separated by dashes: `3`, `5 point`
10. Never bullet-point the check lines — plain text only
11. Conflict/flag lines (⚠️) go AFTER the selection instruction, never before it
12. Path ends with: `--- Path [N] Complete ---` followed by ⚠️ review items list

### Check Order Within a Question Block (MANDATORY)
1. Question visibility: "Ensure you see the question" (only if conditional)
2. Piping: "Ensure <variable> is piped through in question text"
3. Format: question type, columns, scale, randomization
4. Response option visibility: "Ensure you see/do not see R[N]"
5. Response groupings: "Ensure R[N] and R[M] are together"
6. Response option piping: "Ensure <X> is piped through in response options"
7. Anchored / mutually exclusive options
8. Bolding / formatting: "Ensure select words are bolded"
9. Variable assignment: "Ensure assigned <variable> = 'value'"
10. Selection instruction — ALWAYS LAST

### Formatting Micro-Rules
- **No termination in paths**: Never write "Ensure terminated if..." in a path
- **Redundant selection**: When format says "Ensure select up to 2," write
  "Select any" NOT "Select any up to 2"
- **Grouping ranges**: 3+ consecutive → "Ensure R2-R4 are kept together"
  (not "R2, R3, and R4"). Two items → "Ensure R6 and R7 are together"
- **Variable labels**: Always include variable name AND value:
  "Ensure assigned <segment>: <[value]>" not just "Ensure assigned <[value]>"
- **Piped response wording**: "Ensure response options selected in Q1 are
  piped through" (not "from Q1 R5-R12")
- **Anchor/ME only from notes**: Only assert anchor/ME when the survey doc
  programming notes explicitly say "Anchor" or "Mutually exclusive." Do not
  fabricate these attributes from "Terminate" notes.
- **Question ID fidelity**: Use exact IDs from survey map. If survey starts at
  Q100, write Q100 — not Q101.
- **Sub-questions**: Never skip a/b/c/d suffixed questions (Q1a, Q2a, Q3a, etc.)
- **Messages**: Every M[N] MUST appear with at minimum "Ensure message is shown"
