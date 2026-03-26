# Logic, Piping & Variable Assignment Reference

How to translate wireframe objectives into survey programming logic.

---

## Piping Notation

All dynamic text uses `<angle_bracket_variables>`. Variables are assigned during the screener and referenced throughout the survey body. **Piped variables in question text are rendered in RED automatically.**

### Standard Variable Names
| Variable | What it holds | Typically assigned in |
|---|---|---|
| `<brand>` | Brand respondent bought/uses most | Brand question in screener |
| `<segment>` | Product category (shampoo, conditioner, styling, treatment) | Usage frequency + quota assignment |
| `<qualifying segment>` | Segments respondent qualifies in (can be multiple) | Category purchase screener |
| `<form>` | Product form (mousse, spray, serum…) | Brand form question |
| `<retailer>` | Store/site where they shopped | Retailer assignment in screener |
| `<channel>` | Channel type | Channel question |
| `<fulfillment method>` | `<in-store>` or `<online>` | Fulfillment question |
| `<occasion>` | Usage occasion (before work, special event…) | Occasion question in usage section |
| `<factor>` | External factor impacting routine | Impact factors question |
| `<generation>` | Gen Z, Millennial, Gen X, Baby Boomer | Derived from age |
| `<hair type>` | straight, wavy, curly, coiled | Hair type question |
| `<male>` / `<female>` | Gender flag | Gender question |
| `<student>` / `<retired>` | Employment status flag | Employment question |
| `<LE Consumer>` | Leading Edge Consumer flag | LEC attitude battery |

### Piping in Question Text
Always pipe variables into question and message text using angle brackets:
- "Which brands of `<segment>` have you bought in the past 6 months?"
- "You said you use `<brand>` `<segment>` for `<occasion>`."
- "Think about the last trip you made to `<retailer>` where you bought `<brand>` `<segment>`."
- "We will now ask you about your experience shopping for products at `<retailer>`."

When piping `<styling>` into question text, pipe as "styling products".
When piping `<treatment>` into question text, pipe as "treatment products".

---

## Hidden Variable Creation

Always write variable creation as an explicit instruction after the question logic:

```
Create hidden variable <variable_name> if [condition]:
  [Value 1] = <label1>
  [Value 2] = <label2>
```

Examples:
```
Create hidden variable <generation>:
  18–28 = <Gen Z>
  29–44 = <Millennial>
  45–60 = <Gen X>
  61–65 = <Baby Boomer>

Create hidden variable <male> if respondent selects "Male" in S2.
Create hidden variable <female> if respondent selects "Female" in S2.

Create hidden variable <LE Consumer> if respondent meets 3+ of the following criteria:
  - Selects "Somewhat agree" or "Strongly agree" on [relevant attitude items]
  - AND meets usage criteria [specify]
  Min n=1,000, max n=1,500 (adjust per study).
```

---

## Termination Logic

### Immediate Terminates (fire right away, don't wait for screener end)
- Sensitive industry selection
- Age out of range
- Quality check failure (pizza water)
- Gender quota exceeded (when hard quota)

### Held Terminates (hold until end of screener)
All other terminates — collect data through the screener, then terminate:
- Insufficient category engagement
- Low usage frequency
- Shopping responsibility below threshold
- All quotas filled for a demographic cell

**Standard instruction:** "Hold all terminates until the end of the screener unless otherwise specified."

### Terminate Syntax

In response option tables:
```
| Less than half | Terminate.
| Prefer not to answer | Anchor. Terminate.
```

After table (logic instructions):
```
Terminate immediately if respondent selects R1 in [question].
Terminate immediately if respondent does not select at least [N] responses across R[x]–R[y] in C1 of [question].
Skip to S21 and then terminate immediately.
```

**Do NOT repeat**: If the terminate instruction is already in R3 (programming note),
do not also add it as a logic note below. Each instruction appears once.

For quota-based terminates:
```
Terminate if quota for [cell] is met.
Monitor [demographic] and soft-terminate once max n=[X] is reached.
```

---

## Assignment Logic

### Least-Fill Assignment
When assigning a respondent to one of multiple possible values, use least-fill:

```
Assign <variable> based on response in [question], prioritizing filling quotas and then
assigning based on least fill to ensure balanced representation across [brands / retailers / segments / occasions].
```

### Conditional Assignment from Multi-Select
When a respondent selects multiple qualifying options:
```
If respondent selects R1 "[Option A]", assign <variable_a>.
If respondent selects R2 "[Option B]", assign <variable_b>.
Respondent can be assigned multiple <variable> values.
Final <segment> assignment will prioritize quota completion.
```

### Carousel / Loop Instructions
When asking the same question for multiple assigned values:
```
Program as a carousel. Pipe through each <qualifying segment> assigned in [question].
Respondent answers once per assigned segment.
```

---

## Quota Management

### Min/Max Quotas
State quotas explicitly after questions that determine them:
```
Ensure the following quotas are met:
  Min n=[X] <variable>
  Max n=[Y] <variable>
  At each [retailer] except [exception], min n=[A] <female> and min n=[B] <male>
```

### Cross-Segment Quotas
```
Within <styling>, ensure:
  Min n=750 are <male> and <styling>
  Min n=750 are <female> and <styling>
```

### Monitor Language
For soft targets (strive for, not enforce):
```
Monitor distribution across [regions / income bands] and strive for census balance.
Strive for readable sample across [secondary retailers].
```

---

## Skip Logic

### Skip to Question
```
If respondent is assigned <variable>, skip Q[X].
If respondent does not select [option] in [question], skip to Q[Y].
```

### Conditional Show
In question headers:
```
Only show if respondent is <female>.
Only show to respondents assigned <styling>.
Do not show question if respondent is assigned to channel = <ecomm> — auto-assign <online>.
```

In response option tables (right column):
```
| Statement about beauty trends | Only show if respondent is <female>
| Statement about wellness trends | Only show if respondent is non-<female>
| Got2b | Only show for <styling> and <treatment>
```

### Selective Retailer Display
```
Show sets of retailers based on <channel shopped> in [question].
Only show [Grocery retailers] if respondent selected "Grocery" in [channel question].
Keep each grouping of response options together.
```

---

## Message Transitions

Between major sections, include a transition message screen:
```
M[N].
[Message text setting context for the next section]
Show to all respondents. / Show to [specific segment only].
```

Example patterns:
- "Thank you in advance for your time. We're excited to hear about your shopping habits!"
- "Thanks for taking the time to complete our study. First, we're going to ask you some questions about your attitudes towards [topic]."
- "We'd now like to focus more on your overall routine and the moments when you're using `<brand>`."

---

## Anchoring Conventions

Standard anchor options always appear at the bottom of response lists:
```
| Other, please specify | Anchor. Open end.
| None of the above | Anchor. Mutually exclusive.
| Prefer not to answer | Anchor. Mutually exclusive. [/ Terminate if applicable]
```

**Use "Anchor. Open end."** (not "Anchor. Leave a space.") for open-end anchor items.

### Keep Related Options Together
When response options form a sub-category or are closely related, add grouping coding:
```
| Option A | Keep R1-R2 together.
| Option B | Keep R1-R2 together.
| Option C | Keep R3-R4 together.
| Option D | Keep R3-R4 together.
```

This tells the programmer to keep grouped items adjacent during randomization.

### Randomize Convention
Write `Randomize.` — that's all. **Do NOT write** "Randomize (except anchored items)."
or "Randomize (except 'Other')." — anchored items are already excluded by their
`Anchor.` coding in Col 2.

To lock randomized items relative to each other but allow group to randomize:
```
Randomize groups, but keep items within each group together.
```
