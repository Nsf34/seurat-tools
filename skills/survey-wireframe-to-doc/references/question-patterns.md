# Question Patterns Reference

Standard question types, response option sets, programming notes, and scale formats.
Use this to build full response option lists from wireframe shorthand like "(e.g., …)".

---

## Standard Scale Types

### 5-Point Agreement Scale
Use for attitude/belief statements ("How much do you agree with…")
```
Programming note: Program as 5-point scale. Randomize. Single select per statement.

| Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree |
```
Scale labels are BLACK, no number prefix.

### 4-Point Two-Sided Scale (Bipolar / Slider)
Use for paired opposing statements ("Which better describes you…")
```
Programming note: Program as a 4-point scale with one statement anchoring each side.
Single select per row. Randomize statements.

Col 0: blank | C1: Left statement (BLACK) | C2: Right statement (BLACK)
```
Example pairs:
- "Hair care is just another part of my daily hygiene routine" vs. "Hair care is a critical part of my overall self-care / wellness routine"
- "I prefer to stick to the same products I trust" vs. "I enjoy trying new products and brands"
- "I shop quickly and grab what I need" vs. "I enjoy taking time to explore the aisle"

### 5-Point Satisfaction / Ease Scale
```
1 (Very difficult / Challenging) — 2 — 3 — 4 — 5 (Very easy / Seamless)
```

### Frequency Scale (Standard)
Use for "How often do you use / purchase…"
```
Do not randomize. Single select.

| Every day |
| Multiple times per week |
| At least once a week |
| A few times a month |
| Once a month |
| Every 2–3 months |
| A few times a year |
```

### Frequency Scale (Shopping-specific)
Use for "How often do you shop at / purchase from…"
```
Do not randomize. Single select.

| A few times a week |
| Once a week |
| A few times a month |
| Once a month |
| Every 2–3 months |
| A few times a year |
```

---

## Standard Demographic Response Sets

### Age
```
Program as a numerical dropdown in increments of 1 (Under 13 – Over 80).
Terminate <18 or >65 (adjust based on study criteria).
```
Standard generational bands:
- 18–28 = `<Gen Z>`
- 29–44 = `<Millennial>`
- 45–60 = `<Gen X>`
- 61–65 = `<Baby Boomer>`

### Gender
```
Do not randomize. Single select.

| Male | [quota note if applicable]
| Female | [quota note if applicable]
| Transgender male |
| Transgender female |
| Gender variant / non-conforming |
| Other, please specify | Anchor. Open end.
| Prefer not to answer | Anchor. Mutually exclusive.
```

### Ethnicity
```
Do not randomize. Multi-select.

| Caucasian / White |
| Black or African American | [quota note]
| Asian or Pacific Islander |
| Native American |
| Eskimo or Aleut |
| Hispanic / Latino | [quota note]
| Other, please specify | Anchor. Open end.
| Prefer not to answer | Anchor. Mutually exclusive.
```

### Household Income
```
Do not randomize. Single select.

| Less than $25,000 | [Terminate unless <student> or <retired>]
| $25,000–$39,999 | [Max n note if applicable]
| $40,000–$59,999 |
| $60,000–$79,999 |
| $80,000–$99,999 |
| $100,000–$149,999 |
| $150,000–$199,999 |
| $200,000 or more |
| Prefer not to answer | Anchor. Terminate.
```

### Employment Status
```
Do not randomize. Single select.

| Employed full time (35+ hours per week) |
| Employed part time (<35 hours per week) |
| Student | Assign <student>
| Unemployed / Retired | Assign <retired>
| Homemaker |
```

### Marital Status
```
Do not randomize. Single select.

| Single |
| In a relationship / partnered |
| Married |
| Divorced / Separated |
| Widowed |
| Prefer not to answer | Anchor. Mutually exclusive.
```

---

## Sensitive Industry / Occupation Screener (Standard)

Always included early in screener. Terminate immediately on select of sensitive industries.
**CRITICAL: Include non-terminating example occupations** so respondents can see what's acceptable.

```
Do not randomize. Multi-select.

| Market research or advertising | Terminate.
| [Category]-related manufacturing or distribution | Terminate.
| [Category] service provider (e.g., landscaping) | Terminate.
| [Category] retail | Terminate.
| Home improvement or hardware retail |
| Finance and/or consulting |
| Service industry |
| Technology |
| Healthcare |
| Leisure and hospitality |
| Student |
| None of the above | Anchor. Mutually exclusive.
```
*Terminate immediately if any sensitive industry is selected.*

---

## Channel / Retailer Questions

### Channel (Where they shop)
```
Randomize. Multi-select in C1, single select in C2.

|  | C1: Bought in past 6 months | C2: Bought most recently | <channel>
| Grocery store (e.g., Safeway, Kroger, Albertson's) | | | <grocery>
| Natural foods store (e.g., Whole Foods, Sprouts) | | | <natural>
| Mass merchant (e.g., Target, Walmart) | | | <mass>
| Club/warehouse store (e.g., Costco, Sam's Club) | | | <club>
| Online only retailer (e.g., Amazon.com) | | | <ecomm>
| Drugstore (e.g., CVS, Walgreens) | | | <drug>
| Specialty beauty store (e.g., Sephora, Ulta) | | | <specialty beauty>
| Dollar store (e.g., Dollar General) | | | <dollar>
| Other, please specify | | | Anchor. Open end.
| None of the above | | | Anchor. Mutually exclusive.
```

### Fulfillment Method
```
Program as a two-column grid. Randomize. Multi-select in C1, single select in C2.
Do not show if assigned <ecomm> — auto-assign <online>.

|  | C1: Typically shop | C2: Shopped most recently | <fulfillment method>
| At a physical store | | | <in-store>
| Online for delivery | | | <online>
| Online for pick-up at a store | | | <online>
```

---

## Shopping Behavior / Attitude Questions

### Shopping Responsibility
```
Do not randomize. Single select.

| Less than half | Terminate.
| About half |
| More than half |
```
*Terminate immediately if respondent selects "Less than half."*

### Walk Rate / Substitution
Standard for path-to-purchase sections:
```
Do not randomize. Single select.

| Another brand of <segment> |
| A different product from the same brand |
| A different size of the same product |
| Nothing — I would have left without purchasing |
| Other, please specify | Anchor. Open end.
```

---

## Product / Brand Grid Questions

### Two-Column Brand Grid (P6M + Most Frequently)
```
Program as a two-column grid. Randomize. Multi-select in C1, select up to 3 in C2.
Must select in C1 to select in C2.

|  | C1: Bought in past 6 months | C2: Use most frequently (up to 3) | Shown to:
| [Brand A] | | | Show for all
| [Brand B] | | | Show for <shampoo> only
| Private label / store branded | | | Anchor.
| Other, please specify | | | Anchor. Open end.
```

---

## Ranking Questions
Use for priority/importance ranking.
```
Rank list from 1 to [N]. Randomize.

Respondent drags/ranks items in order of most to least important.
```

## Greatest Hits / Pay-For Priority
When asking what respondents are most willing to pay for (piping prior selections):
```
Respondent will see responses piped through from [prior question numbers].
Rank top 5. Randomize piped items.
```

---

## Open-End Questions
```
Open end.
[Character limit if applicable, e.g., max 500 characters]
```

---

## Quality Check (Pizza Water)

**Place in a screener question** (not a body question) so inattentive respondents
are terminated before the main survey begins.

Include in an early grid question (e.g., category purchase grid or brand grid):
```
| Pizza water | Terminate. | Terminate.
```
This is a nonsensical option used to identify inattentive respondents.
Terminate immediately on selection in either column.
