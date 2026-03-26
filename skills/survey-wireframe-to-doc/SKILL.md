---
name: survey-wireframe-to-doc
description: >
  Converts a survey wireframe Word document (.docx) into a fully-specified, programmer-ready
  survey document (.docx). Use this skill whenever a user has a wireframe and wants to "build out", "expand",
  "draft", or "turn into a survey doc". The wireframe is a strategic blueprint (tables with
  Topic | Questions | Response Options | Objective columns); the output is an executable technical
  specification with question numbering, full response options, programming notes, piping logic,
  terminate/quota rules, and structured formatting. Output must match Seurat survey document formatting
  exactly — no deviations from the examples in the question bank.
---

# Survey Wireframe → Survey Document

You are converting a survey research wireframe into a complete, programmer-ready survey document.
The wireframe is a strategic blueprint; your job is to produce an executable technical specification
that a survey programmer can build from without asking a single follow-up question.

**The output has zero tolerance for formatting errors.** Every question block, every table structure,
every programming note, and every logic instruction must match the patterns in the reference files exactly.

## Reference Files (Read ALL before writing anything)

| File | What it contains | When to consult |
|------|-----------------|-----------------|
| `references/question-bank.md` | **Comprehensive question template library** — every question type indexed by category with exact text, programming notes, response options, and logic | For EVERY question you write |
| `references/formatting-standards.md` | Document structure, table formats (merged header+response table, grid table), NEW SCREEN placement | For output formatting |
| `references/logic-and-piping.md` | Variable assignment, piping notation, terminate/quota/skip logic, anchoring conventions, Keep Rx-Ry together | For logic instructions |
| `references/question-patterns.md` | Standard scale types, demographic response sets, channel/retailer patterns | For standard response option lists |

---

## Exact .docx Formatting Specification

**This section is the single source of truth for all visual formatting.** The `survey_doc_builder.py`
engine implements these rules. Any deviation from this spec is a bug.

### Color Rules (CRITICAL — follow exactly)

| Element | Color | Notes |
|---------|-------|-------|
| R0 (Topic label) | **RED (FF0000)** + **Blue shading (B4C6E7)** | Blue background cell, red text |
| R1 (Question number) | **RED (FF0000)** | "S1.", "Q101.", "M1.", "D1." etc. |
| R2 (Question text) | **BLACK** (inherit) | Normal text |
| R2 (Piped variables) | **RED (FF0000)** | `<brand>`, `<category>`, `<channel>` etc. in question text |
| R2 (Selection instruction) | **BLACK** + **italic** | "Select one.", "Select all that apply." |
| R3 (Programming note) | **RED (FF0000)** | All programming instructions in red |
| Response Col 0 (blank) | **RED (FF0000)** pre-formatted | Empty but red-formatted so manual additions appear red |
| Response Col 1 (option text) | **BLACK** (inherit) | Normal text |
| Response Col 2 (notes/actions) | **RED (FF0000)** pre-formatted | "Terminate.", "Anchor.", quotas — **always red-formatted even if empty** |
| Grid header "C1:", "C2:" prefix | **RED (FF0000)** | Only the "C1:", "C2:", "C3:" label is red |
| Grid header description text | **BLACK** (inherit) | "Aware of. Select all that apply." etc. |
| Scale numbers (1, 2, 3, 4, 5) | **RED (FF0000)** | Top row of scale tables |
| Scale labels | **BLACK** (inherit) | "Strongly disagree" etc. — no number prefix |
| Bipolar column labels | **RED (FF0000)** | "C1" and "C2" header row |
| Bipolar statement text | **BLACK** (inherit) | Left and right statements |
| NEW SCREEN | **RED (FF0000)** | Between every question block |
| Logic notes | **RED (FF0000)** | All terminate/variable/quota notes |
| Hold terminates note | **RED (FF0000) + BOLD** | "Please hold all terminations..." |

### Font & Page Setup

- **Document font**: Franklin Gothic Book
- **Font size**: 11pt (139700 EMU) for all body text
- **Page margins**: 1 inch all sides (914400 EMU)
- **Table borders**: All tables use BFBFBF (light gray), size 4, single line
- **Heading 2**: Used for section names (Screener, Plan, Shop, Buy, Use, Demographics)

### Merged Header + Response Table (CRITICAL — every question with response options)

Questions with response tables use a **single merged table** — the header rows (R0-R3) and
response rows are in ONE table. R0-R3 cells are horizontally merged across all columns.

```
R0: [Topic label]           ← RED text, BLUE (B4C6E7) background — merged across all cols
R1: [Question number]       ← RED text — merged across all cols
R2: [Question text] [Selection instruction in italic]  ← merged across all cols
R3: [Programming note]      ← RED text — merged across all cols
R4+: [Response rows]        ← format varies by question type (see below)
```

**R1 is NOT empty.** It always contains the question number (S-prefix for screener, Q-prefix for
body, D-prefix for demographics, M-prefix for messages).

### Standalone Header Table (messages, dropdowns, open-ends only)

4 rows × 1 column. Used ONLY when there is no response table to merge into.

### Simple Response Rows (within merged table)

Rows below R3 in a 3-column table:

```
Col 0 (narrow ~576 dxa): Blank, red-formatted (for manual coding additions)
Col 1 (wide ~6031 dxa):  Option text in BLACK
Col 2 (medium ~2748 dxa): Notes/actions in RED — "Terminate.", "Anchor.", quotas
                           Pre-formatted as RED even if empty
```

### Grid Response Rows (within merged table)

R4 = column header row, R5+ = data rows.

```
Header row (R4): [blank] | [blank] | C1: [Header] RED prefix, BLACK description | C2: [Header] ...
Data rows (R5+): [blank] | [Option text] BLACK | [note] RED | [note] RED [| note RED]
```

### Scale (Agreement Battery) — TWO tables

**Table 1** (merged header + scale): Header R0-R3 merged, then:
```
R4: [1] RED | [2] RED | [3] RED | [4] RED | [5] RED
R5: [Strongly disagree] BLACK | [Somewhat disagree] BLACK | ... | [Strongly agree] BLACK
```
Scale labels are BLACK text only — **no number prefix** in the label row.

**Table 2** (statements): Separate table immediately below.
```
Col 0: Blank (red-formatted)
Col 1: Statement text in BLACK
Col 2: Conditional display note in RED (only if any statement has a condition)
```

### Bipolar Scale (within merged table)

Header R0-R3 merged across 3 columns, then:
```
R4: [blank] | C1 (RED) | C2 (RED)
R5+: [blank] | Left statement (BLACK) | Right statement (BLACK)
```

The programmer builds the actual numeric scale from the programming note. Do NOT include
"1 — 2 — 3 — 4 — 5" text in the table.

### Spacing Between Question Blocks

Every question block is separated by:
1. Blank paragraph
2. "NEW SCREEN" paragraph in RED
3. (Next question's merged table follows)

---

## The Python Builder

`survey_doc_builder.py` is the formatting engine. It implements all formatting rules above.

```python
import sys
sys.path.insert(0, r"path/to/seurat-tools/skills/survey-wireframe-to-doc")
from survey_doc_builder import SurveyDocBuilder

builder = SurveyDocBuilder()
builder.set_study_info(title="...", date="Month Year")
builder.add_overview(objectives=[...], structure=[...], criteria=[...])
builder.add_section_header("Screener", objectives=[...])
builder.add_message("Introduction Message", "", "Thank you...", "Show to all respondents.")
builder.add_hold_terminates_note()
builder.add_question(q_number="S1.", topic="Age", question_text="...", ...)
builder.save("output.docx")
```

### API Reference

| Method | Purpose |
|--------|---------|
| `set_study_info(title, date)` | Title page |
| `add_overview(objectives, structure, criteria)` | Study overview with proper Word bullets |
| `add_section_header(name, objectives)` | Section divider with bulleted objectives |
| `add_hold_terminates_note()` | RED bold "hold all terminations" note |
| `add_message(topic, q_number, text, show_condition)` | Message/transition screen (standalone header) |
| `add_question(q_number, topic, ...)` | Full question block (merged header + response table) |
| `save(filepath)` | Write .docx |

### `add_question()` Parameters

```python
builder.add_question(
    q_number="S1.",                    # Goes in R1 in RED
    topic="Age",                       # Goes in R0 with blue shading, RED text
    question_text="What is your age?", # BLACK text in R2 (piped <vars> auto-red)
    selection_instruction="Select one.",# Italic BLACK in R2
    programming_note="Program as...",  # RED text in R3
    response_options=[                 # Tuples — format varies by question_type
        ("Option A", "note"),          # simple: (text, note)
        ("Option B", ""),              # 2col_grid: (text, c1_note, c2_note)
    ],                                 # 3col_grid: (text, c1, c2, c3)
    grid_headers=["C1: Header", ...],  # For grid types only
    logic_notes=["Terminate if.."],    # RED paragraphs after the table
    question_type="simple",            # See table below
    scale_labels=["Strongly disagree", ...],  # For "scale" type
    bipolar_pairs=[("left", "right")], # For "bipolar" type
)
```

### `add_overview()` Parameters

```python
builder.add_overview(
    objectives=[
        "Size the consumer opportunity...",                    # Simple bullet
        ("Profile each archetype...", [                        # Bullet with sub-bullets
            "How will we do this? We'll send the survey...",
        ]),
    ],
    structure=[
        ("Screener", [                                         # Section name + sub-bullets
            "Qualify respondents on demographics",
            "Assign archetypes based on motivators",
        ]),
    ],
    criteria=[
        ("N = 1,500 U.S. consumers", [                        # Nested lists
            "Age: all 18+",
            "Income: <$20k (max = 150)",
            ("Category engagement", [                          # 3rd level
                "Grass seed (min n = 1200)",
                "Fertilizer (monitor)",
            ]),
        ]),
    ],
)
```

### Question Types

| `question_type` | Table Format | When to Use |
|-----------------|-------------|-------------|
| `"simple"` | Merged: R0-R3 header + 3-col response rows | Single-select, multi-select, select up to N |
| `"2col_grid"` | Merged: R0-R3 + header row + 4-col data rows | Two-column grids (P3M+Most Often, etc.) |
| `"3col_grid"` | Merged: R0-R3 + header row + 5-col data rows | Three-column grids (Aware+Bought+Most Often) |
| `"scale"` | Merged header+scale table + separate statement table | Agreement batteries |
| `"bipolar"` | Merged: R0-R3 + C1/C2 header + paired statements | Bipolar/slider paired statements |
| `"dropdown"` | Standalone 4x1 header | Age dropdown, zip code |
| `"open_end"` | Standalone 4x1 header | Open-end text questions |

---

## Workflow

### Step 1: Parse the wireframe

Read the wireframe .docx. Extract:
- **Study overview**: title, date, objectives, N, respondent criteria, quotas
- **Survey flow**: section names and what each section covers
- **Each question row**: Topic | Question text | Sample Response Options | Objective/Rationale

The wireframe may have 4 or 5 columns. Column order varies. Pay close attention to the
**Objective/Rationale** column — it encodes the logic you must build.

### Step 2: Plan section numbering

Assign question numbers before writing:
- **Screener**: S1, S2, S3...
- **Body Section 1**: Q101, Q102, Q103...
- **Body Section 2**: Q201, Q202, Q203...
- **Body Section 3**: Q301, Q302, Q303...
- **Body Section 4**: Q401, Q402...
- **Demographics/Profiling**: D1, D2, D3...
- **Messages**: M1, M2, M3... (independent numbering)

### Step 3: Write the build script

Create a Python script that calls the builder for every question. The script is the
"source of truth" for the survey document — it can be re-run to regenerate the .docx
at any time.

For every wireframe row:
1. **Match the topic to the question bank** — find the closest pattern
2. **Use the bank's template** for question text, programming note, and response options
3. **Customize with study-specific content** from the wireframe
4. **Expand abbreviated lists** — if wireframe says "Etc." or "(e.g., ...)", use the
   standard response set from the question bank
5. **Generate logic notes** from the objective column

### Step 4: Key rules (apply to EVERY question)

**Piping**: Use `<angle_bracket_variables>`. Variables assigned in screener get piped
into later questions. Piped variables in question text are automatically rendered in RED.

**Quality check (pizza water)**: Insert a "pizza water" row in a **screener** question
(not a body question) so inattentive respondents can be terminated before the main survey.
Place it in an early grid question (e.g., category purchase or brand grid).

**Anchor options**:
- `Anchor. Mutually exclusive.` for "Prefer not to answer" and "None of the above"
- `Anchor. Open end.` for "Other, please specify" (NOT "Leave a space")

**Keep related options together**: When response options within a list form a sub-category
or are closely related (e.g., two options both mapping to the same archetype), add
`Keep Rx-Ry together.` coding in Col 2 so randomization doesn't separate them.

**Terminates**:
- **Immediate**: Sensitive industry, age out of range, quality check failure
- **Held**: Everything else — collect through screener, then terminate

**No duplicate programming text**: If a terminate or logic instruction appears in R3
(the programming note), do NOT repeat it in the logic_notes below the table. Each
instruction should appear in exactly one place.

**Hidden variables**: Create explicitly in logic_notes after the question that generates them.

**Randomization**:
- `Randomize.` — that's it. Do NOT add "except anchored items" or "except Other" —
  anchored items are already excluded by their anchor coding in Col 2.
- Do NOT randomize: demographics, income, frequency scales, ordered sequences

**Instruction ordering in R3**: Always put randomize/do-not-randomize FIRST, then
selection type. Example: `Randomize. Multi-select, max 3.` NOT `Multi-select, max 3. Randomize.`

**Selection instruction formatting**: Always italic. Exact wording:
- "Select one." — single select
- "Select all that apply." — multi-select
- "Select up to [N]." — bounded multi-select
- "Select one for each statement." — batteries/scales

**Do NOT add qualifying/non-qualifying dividers**: When a response list contains both
qualifying and non-qualifying categories, list them all together. Do not separate them
with a visual divider or label rows as "Qualifying" vs "Non-qualifying" — the programmer
handles this via the notes in Col 2.

**Occupation/industry screener**: Always include non-terminating example occupations
alongside the terminating ones, so respondents can see what's acceptable. Examples:
healthcare, technology, finance, education, service industry, student, etc.

### Step 5: Generate & save

Run the build script. Save as: `[Study Name] Survey Document v0.1.docx`

Output goes to:
- Working folder for review
- `seurat-brain/Outputs/survey/` for permanent storage

---

## Transformation Examples

### Example 1: Simple question
```python
builder.add_question(
    q_number="S2.",
    topic="Gender",
    question_text="What gender do you identify with?",
    selection_instruction="Select one.",
    programming_note="Do not randomize. Single select.",
    response_options=[
        ("Male", ""),
        ("Female", ""),
        ("Non-binary", ""),
        ("Other, please specify", "Anchor. Open end."),
        ("Prefer not to answer", "Anchor. Mutually exclusive."),
    ],
    logic_notes=[
        "Monitor Male / Female quotas.",
    ]
)
```

### Example 2: Two-column grid
```python
builder.add_question(
    q_number="Q102.",
    topic="Sources of Influence",
    question_text="Which sources influence what products you buy for your lawn?",
    selection_instruction="Select all that apply.",
    programming_note="Randomize. Multi-select in column 1, single select in column 2.",
    question_type="2col_grid",
    grid_headers=[
        "C1: Influences. Select all that apply.",
        "C2: Most influential. Select one.",
    ],
    response_options=[
        ("Social media (Facebook, Instagram, TikTok)", "", ""),
        ("Family / friend recommendations", "", ""),
        ("Brand websites", "", ""),
        ("Other, please specify", "Anchor. Open end.", "Anchor. Open end."),
        ("None — I don't use any outside sources", "Anchor. Mutually exclusive.", "Anchor. Mutually exclusive."),
    ],
)
```

### Example 3: Scale battery
```python
builder.add_question(
    q_number="Q303.",
    topic="Innovation Interest",
    question_text="How interested would you be in these new product ideas?",
    selection_instruction="Select one for each statement.",
    programming_note="Program as 5-point interest scale. Randomize. Single select per row.",
    question_type="scale",
    scale_labels=[
        "Not at all interested",
        "Slightly interested",
        "Moderately interested",
        "Very interested",
        "Extremely interested",
    ],
    response_options=[
        "A personalized grass seed blend created for your soil and climate",
        "A lawn health diagnostic kit that tests your soil and recommends products",
        "A drought-tolerant grass seed blend that stays healthy with minimal water",
    ],
)
```

### Example 4: Bipolar scale
```python
builder.add_question(
    q_number="Q103.",
    topic="Lawn Values",
    question_text="Which best describes your approach to lawncare?",
    selection_instruction="Select one per row.",
    programming_note="Program as 4-point scale with one statement anchoring each side. Single select per row. Randomize statements.",
    question_type="bipolar",
    bipolar_pairs=[
        ("Maintaining my yard is enjoyable and relaxing",
         "Maintaining my yard is an annoying chore I'd prefer to skip"),
        ("I tend to stick with what I know works",
         "I frequently experiment with new products and/or methods"),
    ],
)
```
