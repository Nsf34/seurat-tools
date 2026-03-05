---
name: survey-wireframe-to-doc
description: >
  Converts a survey wireframe Word document (.docx) into a fully-specified, programmer-ready survey
  document (.docx). Use this skill whenever a user has a wireframe and wants to "build out", "expand",
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
| `references/formatting-standards.md` | Document structure, table formats (header table, response table, grid table), NEW SCREEN placement | For output formatting |
| `references/logic-and-piping.md` | Variable assignment, piping notation, terminate/quota/skip logic, anchoring conventions | For logic instructions |
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
| R2 (Question text) | **BLACK** (inherit) | Normal text, no color override needed |
| R2 (Selection instruction) | **BLACK** + **italic** | "Select one.", "Select all that apply." |
| R3 (Programming note) | **RED (FF0000)** | All programming instructions in red |
| Response Col 0 (row numbers) | **RED (FF0000)** | "1.", "2.", "3." etc. |
| Response Col 1 (option text) | **BLACK** (inherit) | Normal text |
| Response Col 2 (notes/actions) | **RED (FF0000)** | "Terminate.", "Anchor.", quota notes |
| Grid header cells (C1, C2, C3) | **RED (FF0000)** | Column headers in grid tables |
| Scale numbers (1, 2, 3, 4, 5) | **RED (FF0000)** | Top row of scale tables |
| Scale labels | **BLACK** (inherit) | "Strongly disagree" etc. |
| Bipolar scale numbers | **RED (FF0000)** | "1 — 2 — 3 — 4 — 5" center column |
| NEW SCREEN | **RED (FF0000)** | Between every question block |
| Logic notes | **RED (FF0000)** | All terminate/variable/quota notes |
| Hold terminates note | **RED (FF0000) + BOLD** | "Please hold all terminations..." |

### Font & Page Setup

- **Document font**: Franklin Gothic Book
- **Font size**: 11pt (139700 EMU) for all body text
- **Page margins**: 1 inch all sides (914400 EMU)
- **Table borders**: All tables use BFBFBF (light gray), size 4, single line
- **Heading 2**: Used for section names (Screener, Plan, Shop, Buy, Use, Demographics)

### Header Table (every question and message)

4 rows × 1 column. All tables use BFBFBF borders.

```
R0: [Topic label]           ← RED text, BLUE (B4C6E7) background
R1: [Question number]       ← RED text (e.g., "S1.", "Q101.", "M3.")
R2: [Question text] [Selection instruction in italic]  ← BLACK text
R3: [Programming note]      ← RED text
```

**R1 is NOT empty.** It always contains the question number (S-prefix for screener, Q-prefix for
body, D-prefix for demographics, M-prefix for messages).

### Simple Response Table

N rows × 3 columns:

```
Col 0 (narrow ~576 dxa): Row numbers in RED — "1.", "2.", "3."
Col 1 (wide ~6031 dxa):  Option text in BLACK
Col 2 (medium ~2748 dxa): Notes/actions in RED — "Terminate.", "Anchor.", quotas
```

### Grid Response Table (2-column: 4 cols; 3-column: 5 cols)

```
Header row: [blank] | [blank] | C1: [Header] RED | C2: [Header] RED [| C3: Header RED]
Data rows:  [blank] | [Option text] BLACK | [note] RED | [note] RED [| note RED]
```

Grid data rows do NOT have row numbers in Col 0.

### Scale (Agreement Battery)

Scale table: 2 rows × N columns (typically 5):
```
R0: [1] RED | [2] RED | [3] RED | [4] RED | [5] RED
R1: [1 Strongly disagree] | [2 Somewhat disagree] | ... | [5 Strongly agree]
```

Statement table: N rows × 3 columns:
```
Col 0: Row number in RED — "1.", "2."
Col 1: Statement text in BLACK
Col 2: Conditional display note in RED (if any)
```

### Bipolar Scale

N rows × 3 columns:
```
Col 0: [Left statement] BLACK
Col 1: [1 — 2 — 3 — 4 — 5] RED
Col 2: [Right statement] BLACK
```

### Spacing Between Question Blocks

Every question block is separated by:
1. Blank paragraph
2. "NEW SCREEN" paragraph in RED
3. (Next question's header table follows)

---

## The Python Builder

`survey_doc_builder.py` is the formatting engine. It implements all formatting rules above.

```python
import sys
sys.path.insert(0, r"path/to/seurat-brain/Skills/survey-wireframe-to-doc")
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
| `add_overview(objectives, structure, criteria)` | Study overview section |
| `add_section_header(name, objectives)` | Section divider with objectives |
| `add_hold_terminates_note()` | RED bold "hold all terminations" note |
| `add_message(topic, q_number, text, show_condition)` | Message/transition screen |
| `add_question(q_number, topic, ...)` | Full question block |
| `save(filepath)` | Write .docx |

### `add_question()` Parameters

```python
builder.add_question(
    q_number="S1.",                    # Goes in R1 in RED
    topic="Age",                       # Goes in R0 with blue shading, RED text
    question_text="What is your age?", # BLACK text in R2
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

### Question Types

| `question_type` | Table Format | When to Use |
|-----------------|-------------|-------------|
| `"simple"` | 3-col (number \| option \| note) | Single-select, multi-select, select up to N |
| `"2col_grid"` | 4-col with header row | Two-column grids (P3M+Most Often, etc.) |
| `"3col_grid"` | 5-col with header row | Three-column grids (Aware+Bought+Most Often) |
| `"scale"` | 2-row scale + numbered statement table | Agreement batteries |
| `"bipolar"` | 3-col (left \| scale \| right) | Bipolar/slider paired statements |
| `"dropdown"` | No response table | Age dropdown, zip code |
| `"open_end"` | No response table | Open-end text questions |

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
into later questions.

**Quality check**: Insert a "pizza water" row in at least one early grid question.
Mark as `Terminate.` in both columns.

**Anchor options**:
- `Anchor. Mutually exclusive.` for "Prefer not to answer" and "None of the above"
- `Anchor. Leave a space.` for "Other, please specify"

**Terminates**:
- **Immediate**: Sensitive industry, age out of range, quality check failure
- **Held**: Everything else — collect through screener, then terminate

**Hidden variables**: Create explicitly in logic_notes after the question that generates them.

**Randomization**:
- Randomize: attitudes, benefits, brand lists, driver lists, behavior lists
- Do NOT randomize: demographics, income, frequency scales, ordered sequences

**Selection instruction formatting**: Always italic. Exact wording:
- "Select one." — single select
- "Select all that apply." — multi-select
- "Select up to [N]." — bounded multi-select
- "Select one for each statement." — batteries/scales

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
    question_text="What is your gender?",
    selection_instruction="Select one.",
    programming_note="Do not randomize. Single select.",
    response_options=[
        ("Male", ""),
        ("Female", ""),
        ("Non-binary", ""),
        ("Other, please specify", "Anchor. Leave a space."),
        ("Prefer not to answer", "Anchor. Mutually exclusive."),
    ],
    logic_notes=[
        "Monitor Male / Female / Other.",
    ]
)
```

### Example 2: Three-column grid
```python
builder.add_question(
    q_number="S12.",
    topic="Brands Purchased",
    question_text="Which brands of parasiticide <form> are you aware of? Which have you purchased?",
    selection_instruction="Select all that apply.",
    programming_note="Program as a three-column grid. Randomize. Multi-select in C1 and C2, single select in C3.",
    question_type="3col_grid",
    grid_headers=[
        "C1: Aware of | Select all that apply.",
        "C2: Purchased P6M | Select all that apply.",
        "C3: Most recently | Select one.",
    ],
    response_options=[
        ("Bravecto", "", "", ""),
        ("NexGard", "", "", ""),
        ("Other, please specify", "", "", "Anchor. Leave a space."),
        ("None of the above", "", "", "Anchor. Mutually exclusive."),
    ],
    logic_notes=[
        "Assign respondents one <brand> based on their most recent purchase (C3).",
    ]
)
```

### Example 3: Bipolar scale
```python
builder.add_question(
    q_number="Q101.",
    topic="Attitudes Towards Parasiticides",
    question_text="How much do you agree with the following statements about dog parasiticides?",
    selection_instruction="Select one for each statement.",
    programming_note="Program as a 6-point scale with one statement anchoring each side. Single select per row. Randomize statements.",
    question_type="bipolar",
    bipolar_pairs=[
        ("I will stick with my vet recommended brand, regardless of price",
         "I will choose a different brand if the price is lower"),
        ("I typically treat my dog(s) before I see an issue",
         "I typically treat my dog(s) after I see an issue"),
    ],
)
```
