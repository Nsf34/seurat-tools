---
name: survey-mapper
description: >
  Reads a quant survey document (.docx) and produces a structured Survey Map —
  a condensed reference file capturing every question's logic, routing, response
  options, variable assignments, piping dependencies, carousel scope rules,
  category assignment rules, and programming notes.
  This map is the required foundation for the test-path-generator skill.
  Use this skill whenever a user provides a survey .docx and wants to generate
  test paths, or says things like "map the survey," "analyze the survey doc,"
  "read through the survey," or "let's start on the test plan." Always run
  survey-mapper FIRST before test-path-generator.
---

# Survey Mapper

Your job is to thoroughly read a quant survey document and produce a **Survey
Map** — a structured, condensed file that captures every question's logic so
that the test-path-generator can accurately simulate each test path.

Survey documents can be enormous (50–200MB). Never load the whole thing into
context at once. Use Python to extract and parse systematically.

---

## Step 1 — Extract All Survey Text

Use python-docx to pull every paragraph and table cell into a plain text file.

```python
from docx import Document
from docx.oxml.ns import qn

def extract_survey(docx_path, out_path):
    doc = Document(docx_path)
    lines = []
    for el in doc.element.body:
        tag = el.tag.split('}')[-1]
        if tag == 'p':
            text = ''.join(r.text for r in el.findall('.//' + qn('w:t')))
            if text.strip():
                lines.append(text.strip())
        elif tag == 'tbl':
            lines.append('[TABLE]')
            for row in el.findall('.//' + qn('w:tr')):
                cells = [''.join(t.text for t in c.findall('.//' + qn('w:t'))).strip()
                         for c in row.findall('.//' + qn('w:tc'))]
                lines.append(' | '.join(cells))
            lines.append('[/TABLE]')
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Done: {len(lines)} lines → {out_path}")
```

---

## Step 1B — Canonicalize Question IDs

Before building the map, normalize every question ID found in the raw text.
Valid canonical form: uppercase letters + digits + optional single uppercase
letter suffix (e.g., S1, Q205, Q205A, D3, M1).

```python
import re

def canonicalize_id(raw):
    m = re.match(r'^([A-Z]+)(\d+)([A-Z]?)$', raw.strip())
    if m:
        return m.group(1) + m.group(2) + m.group(3)
    return None  # flag for human review
```

Flag any ID that doesn't normalize cleanly:
> ⚠️ ID FORMAT: "[raw]" does not match canonical pattern — verify in survey doc.

---

## Step 2 — Understand Survey Structure

Every quant survey follows a similar high-level architecture:

- **Messages (M1, M2…)**: Informational screens, not questions. Capture text
  and show conditions.
- **Screener (S1, S2…)**: Qualification questions. Each can terminate, route,
  or assign variables.
- **Main modules (Q101–Q199, Q201–Q299…)**: Core questionnaire, often organized
  by topic or module.
- **Demographics (D1, D2…)**: Final standard demographic questions.

**How to identify structure:**
1. Read the survey doc from start to finish in sections.
2. Look for explicit section headers (e.g., "SCREENER", "MODULE 1: ATTITUDES",
   "DEMOGRAPHICS").
3. Note the question ID prefixes used in each section (S, Q###, D).
4. Work section by section, parsing one question at a time.

---

## Step 3 — Build the Survey Map

Write each section's entry into the map immediately as you parse it. Save
incrementally.

Save to: `[ProjectName]_Survey_Map.md` in the project folder.

---

## Survey Map Structure

Use this exact template:

```markdown
# Survey Map: [Project Name]
Source file: [filename]
Date: [today]

---

## Variable Registry

| Variable | Set At | Trigger Condition | Value Assigned |
|----------|--------|-------------------|----------------|
| <variable_1> | [Question ID] | [Condition: which response codes/selections trigger assignment] | [Value assigned to variable] |
| <variable_2> | [Question ID] | [Condition] | [Value assigned] |
| <variable_3> | [Question ID] | [Condition] | [Value assigned] |

# [INSTRUCTIONS FOR POPULATING THIS TABLE]
# 1. Read the survey doc for phrases like "assign <variable>", "create hidden variable",
#    "set <variable> based on", "pipe <variable> into"
# 2. For each variable found, identify:
#    a. Where it's first assigned (which question ID)
#    b. What condition(s) trigger the assignment (which response codes, selections, etc.)
#    c. What value is assigned
# 3. Include BOTH tracking variables (used for piping) and category/segment variables
# 4. Sort by question ID (S1, S2, ... Q101, Q102, ... D1, etc.)
# 5. If a variable is assigned in multiple places, create separate rows for each trigger

---

## Category Assignment Rules

**CRITICAL: Identify category assignment logic from the survey.**

When reading the survey doc, look for patterns like:
- "Respondent's category is determined by..."
- "Priority order: first select X, then Y, else Z"
- "<category> assigned from [question] responses"
- "Categories that CANNOT be assigned" or "exclude from assignment"
- Least-fill logic, qualification restrictions, or "only if eligible" notes

**How to extract:**

1. **Identify the category trigger question** — usually a screener or early question
   where respondent selects one or more categories/products/services.

2. **Extract priority order** — if multiple categories are selected, which takes
   priority? Read for explicit priority numbering (e.g., "1. X → category = X",
   "2. Y → category = Y") or least-fill logic (e.g., "assign to category with
   fewest respondents so far").

3. **Extract exclusions** — note any responses that CANNOT become category
   (e.g., "Other open-end", "None of the above", "Prefer not to answer").

4. **Extract carousel eligibility restrictions** — some carousel questions may
   exclude additional categories. Create a second exclusion list (superset of
   the first) if different from the main category assignment rules.

5. **Extract no-category handling** — what happens if no eligible category
   remains? (e.g., "skip to demographics", "show alternate path", "terminate").

**Template to fill in:**

```
priority_order:
  1. [Response category 1]        → <category> = "[value assigned]"
  2. [Response category 2]        → <category> = "[value assigned]"
  3. [Response category 3 or other pattern] → [assignment logic]
  Note: [additional priority notes, e.g., least-fill, nested conditions]

category_assignment_excluded:
  # These responses can NEVER become <category>:
  - [R#: text]
  - [R#: text]
  - [Other patterns that disqualify]

deep_dive_carousel_excluded:  # (if different from category_assignment_excluded)
  # Carousel questions explicitly exclude these — even if selected earlier:
  - [R#: text]
  - [R#: text]
  - [Additional exclusions specific to carousel scope]

if_no_assignable_category:
  [What happens if no eligible category remains — skip questions, terminate, etc.]
```

---

## Carousel Scope Rules

**A carousel is a rotating set of response options that change based on earlier
selections or conditions.**

When reading the survey doc, look for phrases like:
- "Program as carousel"
- "Show only [selection set] in rotation"
- "Carousel based on [question] responses"
- "Exclude [responses] from carousel"

**How to extract carousel rules:**

For each carousel question in the survey:

1. **Identify the carousel base** — which earlier question/variable determines
   what cycles? (e.g., "carousel based on S17 responses").

2. **Extract include rules** — which specific responses should appear? (e.g.,
   "only R1 and R2", "all S17 selections except...", "all of column C1").

3. **Extract exclude rules** — are any responses explicitly hidden from this
   carousel? (e.g., "exclude R5, R12, Other").

4. **Extract show conditions** — is the carousel itself conditional? (e.g.,
   "only shown if R1 or R2 selected in S17", "only shown if <variable> assigned").

5. **Note any carousel-specific logic** — Gabor-Granger pricing, image rotation,
   scale direction changes, etc.

**Template for each carousel question:**

```
### [Question ID] — [Topic]
carousel_base: [Which earlier question/variable determines carousel content]
carousel_include_only: [[R#] text, [R#] text, ...]  # if explicit include list
carousel_exclude: [[R#] text, [R#] text, ...]       # if explicit exclude list
show_condition: {subject: [Q-ID or variable], operator: [operator], value: [value]}
# [Additional notes on carousel rotation, image anchoring, pricing, etc.]
```

---

## Consumer Journey Loop Structure

**If the survey contains repeating question sets based on earlier selections,
identify the loop structure.**

When reading the survey doc, look for:
- "Respondent will answer the following for each [item]"
- "LOOP: repeat this section for each selection in [question]"
- "For each [selected item], answer Q## through Q##"
- Messages that pipe selected items (e.g., "You selected <item_1>")

**How to extract loop structure:**

1. **Identify the loop trigger** — which question holds the selections that
   determine loop iterations? (e.g., "Q206: Select all that apply → creates
   loop iterations").

2. **Identify loop scope** — which questions repeat? (e.g., "Q207–Q213 repeat
   for each selection", "Questions A–E in loop block").

3. **Identify variable assignments within loop** — are temporary/iteration
   variables assigned? (e.g., "<current_item> = selected item", "<moment_1>,
   <moment_2>" for first and second iterations).

4. **Identify loop messages** — do messages appear at the start of each loop
   iteration, piping the current item? (e.g., M1 pipes <current_item>).

5. **Identify loop-dependent questions** — are some questions within the loop
   only shown on certain iterations? (e.g., "Q209 only if R1 selected in Q208
   within this loop iteration").

6. **Identify post-loop questions** — which questions appear AFTER the loop
   completes? (e.g., "Q214–Q215 after loop finishes").

**Template for loop structure:**

```
sequence:
  [Trigger Question]: [description of selections that create iterations]
  ─── LOOP 1 ─────────────────────────────────────────────────────────
  [Message piping current item/iteration variable]
  [Q1] → [Q2] → [Q3 conditional] → [Q4] → [Q5 conditional] → [Q6] → [Q7]
  ─── LOOP 2 (only if [X] was selected in trigger) ────────────────────
  [Message piping second iteration variable]
  [Q1] → [Q2] → [Q3 conditional] → [Q4] → [Q5 conditional] → [Q6] → [Q7]
  ─────────────────────────────────────────────────────────────────────
  [Post-loop Q1] / [Post-loop Q2]  (source carousel, etc.)

  * [Q3]: only if [condition from Q2 column/response]
  * [Q5]: only if [condition from earlier loop question]
```

---

## Multi-Step Source Resolution Chains

**When the survey pipes sources/recommendations through multiple questions,
document the exact chain.**

When reading the survey doc, look for:
- "Create hidden variable <source> from [multiple question inputs]"
- "Collect from Q1, Q2, Q3 and merge into final set"
- "Deduplicate — [value A] = [value B]"
- "Resolve sub-sources from [conditional questions]"

**How to extract source resolution:**

1. **Identify all source inputs** — which questions contribute to the final
   source set? (e.g., Q204 C1/C2, Q210 C2, Q211 C2, S10 provider).

2. **Identify conditional logic** — are some inputs included only under certain
   conditions? (e.g., "Q211 C2 only if R9–R14 selected in Q210 C1").

3. **Identify deduplication rules** — are any values consolidated? (e.g.,
   "specialist = specialized doctor's office").

4. **Identify exclusion rules** — are any values filtered out? (e.g., "exclude
   R12 from this step").

**Template for source resolution:**

```
## [Final Variable / Question] Source Resolution Chain

Follow this exact multi-step process:

  Step 1: Collect [source 1] from [Question ID]
  Step 2: Collect [source 2] from [Question ID] [column/condition]
  Step 3: Collect [source 3], EXCLUDING [response codes]
  Step 4: For any [special condition responses], resolve to [alternative source]
          (the specific sub-source from [other question])
  Step 5: Deduplicate — [value] = [deduplicated value]
  Step 6: Pipe the resolved, deduplicated set into [final question]
```

---

## Follow-Up Trigger Detection

**Some questions appear only when specific responses are selected earlier.**

When reading the survey doc, look for:
- "Show Q## only if R# selected in Q##"
- "Follow-up to [question] if R1–R3 selected"
- "Trigger: [response codes] → show [question]"

**How to extract trigger rules:**

1. **Identify the trigger question and response codes** — which question and
   which specific response options trigger the follow-up?

2. **Identify the follow-up question** — which question is shown?

3. **Identify any "do NOT trigger" codes** — are there similar responses that
   do NOT trigger the follow-up? (e.g., "if R5 selected, skip this follow-up").

**Template:**

```
## [Follow-Up Question Name]

[Follow-Up Question ID] shows ONLY when these [Trigger Question ID] response
codes are selected:
  trigger_codes: [[R#] [text], [R#] [text], ...]
  [Any codes that do NOT trigger]
[Note any exceptions or special logic.]
```

---

## Always-Shown Questions

**Some questions appear in every survey path, regardless of earlier selections.**

When reading the survey doc, look for:
- No show condition listed
- "Always shown to all respondents"
- "Shown to both [segment A] and [segment B]"

As you map questions, mark them `display_tag: always_shown` if they have no
show condition and no routing logic that skips them.

**Template:**

```
### [Question ID] — [Topic]
display_tag: always_shown
[Standard question details — see below]
```

---

## Structured Show Conditions

For every conditional question, record show conditions as structured logic
triples — NOT as free text. This prevents polarity inversion errors.

format:
  {subject: [question_id or variable_name], operator: [operator], value: [value]}

valid operators:
  includes            subject's selections include this value
  not_includes        subject's selections do NOT include this value
  includes_any_of     subject includes at least one of these values
  equals              subject variable equals this value
  not_equals          subject variable does not equal this value
  is_assigned         variable has any assigned value
  not_assigned        variable has not been assigned

key examples:
  Q209: {subject: Q208_C1, operator: includes, value: R1}
  Q211: {subject: Q210_C1, operator: includes_any_of, value: [R9,R10,R11,R12,R14]}
  Q308: {subject: Q307, operator: includes_any_of, value: [R9,R10,R11,R12,R14]}
  Q407: {subject: Q406, operator: equals, value: R1}
  S20: {subject: S17, operator: not_includes, value: R2}
  S22: {subject: "<variable>", operator: not_assigned}

consistency_checks_to_run:
  - Flag if a show condition references a variable not in the Variable Registry
  - Flag if a show condition forward-references a question with a higher number
    than the current question → likely stale reference
  - Flag if a conditional question's topic doesn't match its show condition
    variable (e.g., RTD question with Protein Powder condition → likely typo)

---

## Messages

**Messages are informational screens with no response collection.**

When reading the survey doc, look for:
- Rows labeled M1, M2, etc.
- "Message:", "Screen:", or similar
- Text without response options
- Show conditions (sometimes messages are conditional)

### M[N] — [Topic / Purpose]
Shown: [always / condition described as structured triple]
Text: "[exact verbatim text — including any piped variables]"

---

## Screener Questions

**Screener questions determine qualification and set up initial variables.**

When reading the survey doc:
1. Look for section labeled "SCREENER"
2. Extract each question's ID (S1, S2, etc.), type, responses, and routing
3. Note any variable assignments and termination conditions

### S[N] — [Topic]
Type: [single-select / multiple-select / open-end / scale / etc.]
Shown: [Always / CONDITIONAL]
display_tag: [always_shown / conditional]
show_condition: [structured triple or null]
Question text: "[full text]"
Response options:
  - R1: [text] — [anchoring notes: ANCHORED TOP / ANCHORED BOTTOM / MUTUALLY EXCLUSIVE / open-end / etc.]
  - R2: [text]
  [...]
Programming notes: [randomization, carousel, scale direction, etc.]
carousel_scope: (fill in if applicable using Carousel Scope Rules above)
Variable assignments:
  - [trigger condition] → <variable> = [value assigned]
  - [other trigger] → <other_variable> = [value]
Routing:
  - TERMINATE IMMEDIATELY if: [condition]
  - TERMINATE END OF SCREENER if: [condition]
  - SKIP to [Q-ID] if: [condition]

---

## Module [N]: [Module Name]

**Main questionnaire modules, organized by topic.**

When reading the survey doc:
1. Identify section headers (e.g., "MODULE 1: ATTITUDES", "PURCHASE INTENT")
2. Extract each question's ID (Q101, Q102, etc.)
3. Note carousel rules, piping, and sub-questions

### Q[N] — [Topic]
Type: [type]
Shown: [Always / CONDITIONAL]
display_tag: [always_shown / conditional]
show_condition: [structured triple or null]
Question text: "[full text]"
Columns: C1=[label], C2=[label]  (if applicable)
Response options:
  - R1: [text] — [anchoring/mutex notes]
  - R2: [text]
  [...]
Piping: [list all <variables> or [Q-IDs] in question text or response options]
Response option visibility:
  - R[N]: {subject: <variable>, operator: is_assigned} → shown
  - R[N]: {subject: <variable>, operator: not_assigned} → hidden
Groupings: [list all grouped response sets, e.g. "R2–R3 together"]
carousel_scope: (if applicable, using Carousel Scope Rules)
Programming notes: [randomization, looping, scale direction, image anchoring, etc.]
Variable assignments:
  - [response selection] → <variable> = [value assigned]
Routing: [skip/terminate conditions]

---

## Demographics

### D[N] — [Topic]
[same structure as Module questions above]

---

## Ambiguity Log

[collected ⚠️ items:]
1. ⚠️ [question_id] — [what is unclear, assumption made]
2. ⚠️ [question_id] — [issue description]

```

---

## Step 4 — Consistency Checks During Mapping

Run these checks as you parse each question:

**1. Negative condition consistency**
If a show condition uses `not_includes` or `not_assigned`, verify the variable
matches the question's semantic meaning. A question about product X with a
condition about product Y variable = flag.
> ⚠️ TYPO: [Q-ID] condition references [variable] but question is about [topic].
> Likely typo for [correct variable]. Using [correct variable].

**2. Forward-reference check**
If [Q-ID] has a show condition referencing [later Q-ID]:
> ⚠️ FORWARD-REF: [Q-ID] condition references [later Q-ID] — likely stale note.
> Ignoring; using programmed logic.

**3. Variable registry check**
Every variable in every condition must exist in the Variable Registry.
> ⚠️ UNDEFINED VAR: `<variable>` used in [Q-ID] condition but not in registry.

**4. Carousel scope check**
For any carousel question without an explicit `carousel_include_only` or
`carousel_exclude` list in the survey doc:
> ⚠️ CAROUSEL SCOPE: [Q-ID] carousel scope not explicitly stated — verify.

---

## Step 4B — Sub-Question Detection

**CRITICAL: Detect and map ALL sub-questions with letter suffixes.**

After parsing each question, check the survey doc for sub-questions:
- S11a, Q302a, Q307a, Q404a–Q404d, etc.
- These are separate questions often embedded in the same table or immediately
  following their parent question.

Detection patterns:
1. Table header contains a question ID with a letter suffix (e.g., "Q302a.")
2. A "NEW SCREEN" or paragraph between tables references a suffixed ID
3. Programming notes say "assign based on response in Q307a"

For each sub-question found, create a FULL map entry — same fields as any
other question (Type, Shown, Response options, etc.).

> ⚠️ SUB-Q MISSING: If a programming note references a suffixed question ID
> (e.g., "assign <temp variable> from Q307a") but no map entry exists for Q307a,
> flag immediately and add the entry.

---

## Step 4C — Merged Cell Handling

When reading survey doc tables, programming notes in the rightmost column
may span multiple rows via merged cells. The mapper MUST apply the note to
ALL response options in the merged range.

Example: A cell containing "Only show if <online>" spanning R8, R9, R10 means
ALL THREE options have this visibility condition, not just R8.

Detection:
- When python-docx reads a merged cell, the same text appears in each row
  that the cell spans. If consecutive rows have identical programming note
  text, treat them as sharing a merged note.
- Alternatively, check the XML for merged cell spans:
  ```python
  tc = cell._element
  vmerge = tc.find(qn('w:tcPr/w:vMerge'))
  ```

For each response option affected by a merged programming note, record the
note on EVERY affected option:
```
Response options:
  - R8: "Option A" — Only show if <condition>
  - R9: "Option B" — Only show if <condition>
  - R10: "Option C" — Only show if <condition>
```

NOT:
```
  - R8: "Option A" — Only show if <condition>
  - R9: "Option B"
  - R10: "Option C"
```

---

## Step 4D — Question Numbering Fidelity

**CRITICAL: Use the exact question IDs from the survey document.**

The survey document's section structure determines question numbering.
Common patterns:
- Screener: S1, S2, S3... (plus S11a, S18, S19, etc. as needed)
- Module 1: Q100, Q101, Q102... (or may start at Q101)
- Module 2: Q201, Q202...
- Module 3: Q301, Q302...
- Demographics: D1, D2, D3...

To determine the starting number for each section:
1. Look for explicit question IDs in table headers (e.g., "Q302a.")
2. Count questions sequentially from the first labeled one
3. Cross-reference programming notes that reference specific Q-IDs

**Do NOT assume sections start at X01 — check the survey doc.** If the first
question in a module is labeled Q100 in any table or note, use Q100.

> ⚠️ NUMBERING: If question IDs cannot be determined from the survey doc,
> flag the ambiguity and state the assumption made.

---

## Step 4E — Specialized Pattern Detection (Gabor-Granger, Etc.)

When the survey doc describes specialized question patterns (e.g., Gabor-Granger
pricing, conjoint matrices, grid randomization), flag them explicitly in the
map so the path generator can handle them.

Detection triggers:
- "Program as carousel" + price/value list
- "First show [median/midpoint]" + stepping logic
- "Create hidden variable <[boundary variable]> based on upper/lower bound"
- "Conjoint matrix — randomize within these rules"
- "Gabor-Granger: if R1–R3 [likely] step higher; if R4–R5 [unlikely] step lower"

For each specialized question, record:
```
### Q[N] — [Topic]
Type: [Specialized pattern name: Gabor-Granger carousel / Conjoint matrix / etc.]
Shown: [condition if applicable]
[Pattern-specific fields]:
  price_list: [[price], [price], ...]
  median_price / midpoint: [value] (entry position in list)
  stepping_logic: "[condition] → [action]; [other condition] → [other action]"
  bound_variable: <[variable name]>
  associated_questions:
    - [Q-ID]: [description]
    - [Q-ID]: [description]
  image_anchoring: "[instructions for images across questions]"
  exclusion_rules: "Do not show [variable/respondent segment]; skip [Q-range]"
```

Also note any global exclusion rules (e.g., "respondents matching [criteria] skip
questions Q[N]–Q[M]").

---

## Step 5 — Gap Detection Pass

After building the full map:

**Numbering gaps**: Flag any gap in question ID sequence:
> ⚠️ GAP: Q204 exists and Q206 exists, but Q205 is absent from the survey doc.
> Verify whether Q205 was omitted from the doc or truly does not exist.

**Referenced-but-undefined**: Any question ID appearing in a condition or
piping note that has no map entry:
> ⚠️ GAP: [Q-ID] is referenced in [context] but has no survey map entry.
> Do not generate paths until this is resolved.

**Variable gaps**: Any `<variable>` in piping or conditions not in the registry:
> ⚠️ UNDEFINED VAR: `<variable>` appears in [Q-ID] but is not defined.

**Do not proceed to path generation if any critical GAP flags exist.**
Present them to the user for resolution first.

---

## Step 6 — Required Questions List

At the end of the map, produce an explicit list used by the path generator
for completeness validation:

```markdown
## Required Questions (always_shown — must appear in every generated path)
[Extract all question IDs with display_tag: always_shown from the map]
[List them as a comma-separated string, ordered by ID]
e.g.: S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, Q101, Q102, Q103,
      Q201, Q202, Q203, Q204, Q301, Q302, D1, D2, D3

## Conditional Questions (may be hidden depending on path state)
[For each question with display_tag: conditional, list its show_condition]
[Example format:]
S18: {subject: S17, operator: includes_any_of, value: [R1, R2]}
S20: {subject: S17, operator: not_includes, value: R2}
Q209: {subject: Q208_C1, operator: includes, value: R1}
Q308: {subject: Q307, operator: includes_any_of, value: [R9, R10, R11]}
Q407: {subject: Q406, operator: equals, value: R1}
[etc.]
```

---

## Step 7 — Save and Report

Save the map as `[ProjectName]_Survey_Map.md`.

Report to the user:
- Total question count by type (M, S, Q, D)
- Total variables in Variable Registry
- Required questions count
- Full list of ⚠️ gaps, typos, and ambiguities
- Whether it's clear to proceed to path generation (list any blockers)
