# Survey Question Bank

Comprehensive indexed library of every survey question pattern. Each entry includes the exact question text template, programming note, response options, and logic. Variables in `<angle_brackets>` are piped from earlier questions.

Source: Bolton (Personal Care), CCC (Coffee/Whole Bean), Ocean Spray (Hair Accessories), Yerba Madre (Energy Beverages).

---

## How to Use This File

When converting a wireframe row to a survey question:
1. Identify the wireframe topic (e.g., "Age", "Brand purchase", "Shopping difficulty")
2. Find the matching pattern below by category and topic
3. Use the template as-is, substituting `<category>`, `<brand>`, etc. with the study-specific values
4. Apply the programming note and logic from the template
5. Customize response options only where the wireframe explicitly provides study-specific lists

---

## 1. DEMOGRAPHICS & SCREENER GATES

### 1.1 Age
**Question text:** What is your age? Select one.
**Programming note:** Program as a numerical dropdown in increments of 1 (Under 13 – Over 80). Terminate immediately if respondent is <18 or >65.
**Response options:** Numerical dropdown
**Logic:**
```
Terminate immediately respondents outside [age range].
Create hidden variable <generation>:
  18–28 = <Gen Z>
  29–44 = <Millennial>
  45–60 = <Gen X>
  61–65 = <Baby Boomer>
Create hidden variable <next-gen> if respondent is under 35.
Ensure the following quotas are met: [study-specific min/max per generation].
```
**Variations seen:**
- Bolton: 18-65, generation bands 18-29/30-45/46-61/62-65
- CCC: 18-65, <Next Gen> if 18-35
- Ocean Spray: 18-65, bands 18-25/26-40/41-56/57-65
- Yerba Madre: 18-55, bands 18-27/28-43/44-55

### 1.2 Gender
**Question text:** What gender do you identify with? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Male | [quota note if applicable]
| Female | [quota note if applicable]
| Transgender male |
| Transgender female |
| Gender variant / non-conforming |
| Other, please specify | Anchor. Open end.
| Prefer not to answer | Anchor. Mutually exclusive.
```
**Logic:**
```
Create hidden variable <male> if respondent selects R1.
Create hidden variable <female> if respondent selects R2.
Strive for census balance of genders. / [Or hard quota: Min n=X <male>, Min n=Y <female>]
```
**Variation:** Ocean Spray uses "Non-binary" instead of "Gender variant / non-conforming."

### 1.3 Ethnicity
**Question text:** Which best describes your ethnicity? Select all that apply.
**Programming note:** Do not randomize. Multi-select.
**Response options:**
```
| Caucasian / White |
| Black or African American | [quota note]
| Asian or Pacific Islander |
| Native American |
| Eskimo or Aleut |
| Hispanic / Latino | [quota note]
| Other, please specify | Anchor. Open end.
| Prefer not to answer | Anchor. Mutually exclusive.
```
**Variation:** Yerba Madre adds "Middle Eastern / North African" and uses "Native American, Inuit, or Aleut."

### 1.4 Sensitive Industries / Occupation
**Question text:** Have you, your partner, or anyone in your immediate family ever worked in any of these industries? Select all that apply.
**Programming note:** Do not randomize. Multi-select. Terminate immediately respondents who select any sensitive industry.
**Response options:**
```
| Market research or advertising | Terminate.
| [Category]-related manufacturing or distribution | Terminate.
| [Category] service provider (e.g., landscaping, lawn maintenance) | Terminate.
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
**CRITICAL:** Always include non-terminating example occupations alongside the terminating ones so respondents can see what's acceptable. Customize the terminating industries for the specific study category.
**Variation — CCC version adds:** "Student" (assign `<student>`), "Other, please specify" (Anchor).
**Variation — short form:** "Do you, or have you ever, worked in any of these fields?"

### 1.5 Household Income
**Question text:** What is your annual household income? Select one. / What is your total annual household income before taxes? Select one.
**Programming note:** Do not randomize. Single select.
**Response options (standard):**
```
| Less than $25,000 | Terminate. [unless <student> or <retired>]
| $25,000–$39,999 | [Max n note if applicable]
| $40,000–$59,999 |
| $60,000–$79,999 |
| $80,000–$99,999 |
| $100,000–$149,999 |
| $150,000–$199,999 |
| $200,000 or more |
| Prefer not to answer | Anchor. Terminate.
```
**Variation — CCC:** Bottom bracket = "Less than $30,000", second = "$30,000-$49,999", third = "$50,000-$59,999".
**Logic:** Terminate immediately if R1 unless assigned `<student>` or `<retired>`. Monitor distribution across income.

### 1.6 Employment Status
**Question text:** Which best describes your current job status? Select all that apply.
**Programming note:** Do not randomize. Multi-select. / Single select.
**Response options:**
```
| Employed full time (35+ hours per week) |
| Employed part time (<35 hours per week) |
| Student | Assign <student>.
| Retired | Assign <retired>.
| Unemployed |
| Homemaker |
```

### 1.7 Marital Status
**Question text:** What is your marital status? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Single (never married) |
| Living with a significant other |
| Married |
| Separated |
| Divorced |
| Widowed |
| Prefer not to answer | Anchor. Mutually exclusive.
```
**Variation — CCC:** Adds "Engaged" and "Other, please specify." Uses "Living with partner / significant other."

### 1.8 Education Level
**Question text:** What is the highest level of education you have completed? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Some level of high school |
| High school graduate or equivalent |
| Some college (no degree) |
| Associate's Degree |
| Bachelor's Degree |
| Graduate or Professional Degree |
```

### 1.9 Region / State
**Question text:** Where do you live? Select one.
**Programming note:** Single select. Do not randomize. Program as drop-down list of US States.
**Response options:** Dropdown of all 50 US states + DC

### 1.10 Zip Code
**Question text:** What is your zip code? Please type below.
**Programming note:** Program as a numerical open end. Do not accept responses that do not exist as zip codes.
**Response options:** Numerical open-end (validated zip codes).

### 1.11 Urbanicity
**Question text:** How would you describe the area where you live? Select one.
**Programming note:** Randomize. Single select.
**Response options:**
```
| Urban |
| Suburban |
| Rural |
| Other, please specify | Anchor. Open end.
```

### 1.12 Children in Household
**Question text:** Do you have any children under 18 living in your household? Select one in each range.
**Programming note:** Do not randomize. Program R2–R4 as dropdowns from 0–5+. R1 is mutually exclusive.
**Response options:**
```
| No children under 18 living in my household | Mutually exclusive. No dropdown.
| 0–5 years old | Dropdown: 0, 1, 2, 3, 4, 5+
| 6–11 years old | Dropdown: 0, 1, 2, 3, 4, 5+
| 12–18 years old | Dropdown: 0, 1, 2, 3, 4, 5+
```
**Variation — CCC:** Age bands are <1, 1-5, 6-12, 13-17. Creates hidden variable `<kids in HH>` if any dropdown > 0.

### 1.13 Shopping Responsibility
**Question text:** When it comes to buying `<category>`, how much of the shopping are you personally responsible for? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Less than half | Terminate.
| About half |
| More than half |
```
**Logic:** Terminate immediately if respondent selects "Less than half."

### 1.14 Quality Check (Pizza Water)
Insert as a row in a **screener** question (not a body question) so inattentive respondents
are terminated before the main survey begins. Place in an early grid question such as
category purchase or brand grid:
```
| Pizza water | Terminate. | Terminate.
```
Terminate immediately on selection in either column.

---

## 2. CATEGORY ENGAGEMENT

### 2.1 Category Purchase — Simple List (P3M / P6M / P1Y)
**Question text:** Which of the following `<category>` have you purchased in the past [3 months / 6 months / year]? Select all that apply.
**Programming note:** Multi-select. Do not randomize. [Or: Randomize.]
**Response options:** Study-specific product list + anchors:
```
| [Category A] | [Qualify / Min n=X]
| [Category B] | [Qualify / Min n=X]
| [Category C] |
| None of the above | Anchor. Mutually exclusive.
```
**Logic:**
```
Terminate respondents not selecting at least one of R[x]–R[y].
Assign <qualifying category> for qualifying selections.
```

### 2.2 Category Purchase — Two-Column Grid (P6M + P3M / P1Y + P3M)
**Question text:** Which of these [beverages/products] have you purchased in the past year? Select all that apply. / Past 3 months? Select all that apply.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in both columns. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Past year | Select all that apply. | C2: Past 3 months | Select all that apply.
| [Product A] | | Qualify
| [Product B] | |
| None of the above | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
```
**Logic:** Terminate if respondent does not select qualifying item in C2.

### 2.3 Category Type / Form — Two-Column Grid
**Question text:** What specific types of `<category>` have you purchased in the past [3/6] months? Select all that apply. / Which have you purchased most recently? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Purchased | Select all that apply. | C2: Most recently | Select one.
| [Type A] | | | <type_a>
| [Type B] | | | <type_b>
| Other, please specify | Anchor. Open end. | Anchor. Open end.
```
**Logic:** Assign `<segment>` or `<form>` based on selection. Respondents can be assigned multiple segments.

### 2.4 Usage Frequency — Standard Scale
**Question text:** How often do you use `<category>`? Select one. / How often do you [purchase / prepare / drink] `<category>`? Select one.
**Programming note:** Do not randomize. Single select.
**Response options (usage):**
```
| Every day |
| Multiple times per week |
| At least once a week |
| A few times per month |
| Once a month |
| Every 2–3 months |
| A few times a year |
```
**Response options (shopping):**
```
| More than once a week |
| Once a week |
| A few times a month |
| Once a month |
| Every 2–3 months |
| A few times a year |
```

### 2.5 Consumption Frequency — Cups / Servings per Week
**Question text:** On average, how many [cups of coffee / servings of `<category>`] do you [drink / consume] in a week? Select one.
**Programming note:** Do not randomize. Single select.
**Response options (CCC coffee example):**
```
| <1 (less than once a week) |
| 1-3 (few days a week) |
| 4-6 (most days of the week) |
| 7 (1 cup per day) |
| 8-14 (1-2 cups per day) |
| 15-21 (2-3 cups per day) |
| 22-28 (3-4 cups per day) |
| 29-35 (4-5 cups per day) |
| 35+ (over 5 cups per day) |
```

### 2.6 Share of Consumption by Segment
**Question text:** In a typical week, what percent of your `<category>` [cups / servings] come from each type? Select one per type.
**Programming note:** Pipe through `<segments>` selected in [prior question]. Program as numerical drop-downs from 0% to 100% in increments of 10%. Randomize.
**Response options:** Dropdown 0%–100% in 10% increments, one per piped segment.

### 2.7 Spend per Trip
**Question text:** How much do you typically spend on `<category>` on a single shopping trip? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:** Study-specific price ranges:
```
| $5–$9.99 |
| $10–$14.99 |
| $15–$19.99 |
| $20–$24.99 |
| $25+ |
```

---

## 3. BRAND & PRODUCT

### 3.1 Brand Awareness/Purchase/Most-Often — Two-Column Grid
**Question text:** Which brands of `<category>` have you [heard of / purchased in the past X months]? Select all that apply. / Which brand do you [purchase / use] most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: [Purchased P3M / P6M] | Select all that apply. | C2: [Purchase most often] | Select one.
| [Brand A] | | [Min n=X]
| [Brand B] | |
| Private label / store branded | | Anchor.
| Other, please specify | | Anchor. Open end.
| None of the above | | Anchor. Mutually exclusive.
```
**Logic:** Assign `<brand>` based on response in C2. Use least-fill assignment if applicable.

### 3.2 Brand Awareness/Purchase/Most-Often — Three-Column Grid
**Question text:** Which of the following `<category>` brands have you heard of? Select all that apply. / Which have you purchased in the past [3/6] months? / Which do you purchase most often? Select one.
**Programming note:** Program as a three-column grid. Randomize. Multi-select in C1 and C2, single select in C3. Must select in C1 to select in C2. Must select in C2 to select in C3.
**Response options:**
```
|  | C1: Heard of | C2: Bought P3M | C3: Buy most often | [variable/tier]
| [Brand A] | | | | <tier_a>
| [Brand B] | | | | <tier_b>
| Other, please specify | | | | Anchor. Open end.
| None of the above | | | | Anchor. Mutually exclusive.
```
**Logic:** Assign `<brand>` based on C3. Assign brand tier variable. Terminate if no qualifying brands in C1.

### 3.3 Brand Form / Type — Two-Column Grid
**Question text:** What specific types of `<brand>` `<category>` have you purchased in the past [3/6] months? Select all that apply. / Most recently? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2. Only show response list for assigned `<category>`.
**Response options:** Category-specific form lists.
**Logic:** Assign `<form>` based on C2.

### 3.4 Brand Carousel — Attribute Association
**Question text:** Which of the [attributes / benefits / words] below do you associate most with the brand below, specifically thinking about `<category>`? Select up to [3].
**Programming note:** Program as a carousel and loop respondent through up to [N] brands selected in [prior question], based on least fill. Multi-select up to [3]. Randomize.
**Response options:** Study-specific attribute list.
**Logic:** Respondent sees one brand per screen, answers for each.

### 3.5 Brand Attitudes — Agreement Battery
**Question text:** On a scale from 1 to 5, how much do you agree with each of the following statements about `<brand>`? Select one per statement.
**Programming note:** 5 pt scale. Randomize statements. Single select per statement.
**Scale:** Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree
**Response options:** Study-specific statement list.

### 3.6 Brand Purchase Drivers
**Question text:** What are the top reasons you would consider purchasing `<brand>`? Select up to [3].
**Programming note:** Randomize. Select up to [3].
**Response options:** Study-specific driver list + anchors:
```
| [Driver A] |
| [Driver B] |
| Other, please specify | Anchor. Open end.
| None of the above | Anchor. Mutually exclusive.
```

### 3.7 Brand Perceptions — Open End
**Question text:** What comes to mind when you think of `<brand>` `<category>`? Please describe in 1-2 sentences.
**Programming note:** Program as open end. Leave space for text entry.

---

## 4. CHANNEL & RETAILER

### 4.1 Channel Selection — Two-Column Grid
**Question text:** Where have you purchased `<brand>` `<category>` in the past [3/6] months? Select all that apply. / Where do you purchase most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Bought P3M/P6M | Select all that apply. | C2: Bought most often | Select one. | <channel>
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
**Logic:** Assign `<channel>` based on C2. Use least-fill for `<retailer>` assignment.

### 4.2 Specific Retailer Selection — Two-Column Grid
**Question text:** Where have you bought `<brand>` `<category>` in the past [3] months? Select all that apply. / Most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.
**Response options:** Study-specific retailer list:
```
|  | C1: Past 3 months | C2: Most often
| [Retailer A] | | Min n=50
| [Retailer B] | | Min n=50
| Online-only stores (e.g., Amazon) | | Assign <online>
| Other, please specify | | Anchor. Open end.
```
**Logic:** Assign `<retailer>` based on C2. Ensure min quotas per retailer.

### 4.3 Fulfillment Method — Two-Column Grid
**Question text:** Thinking about when you shop for `<category>`, do you typically… / Most recently?
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Do not show if assigned `<ecomm>` — auto-assign `<online>`.
**Response options:**
```
|  | C1: Typically shop | C2: Shopped most recently | <fulfillment method>
| At a physical store | | | <in-store>
| Online for delivery | | | <online>
| Online for pick-up at a store | | | <online>
```

---

## 5. ATTITUDES & BELIEFS

### 5.1 Five-Point Agreement Battery
**Question text:** On a scale of 1 to 5, how much do you agree or disagree with each of the following statements? Select one for each statement.
**Programming note:** 5 pt scale. Randomize items. Single select per statement.
**Scale:**
```
Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree
```
**Response options:** Study-specific statement list. Each statement on its own row. Conditional display noted in right column:
```
| [Statement A] |
| [Statement B] | Only show if respondent is <female>
| [Statement C] | Only show for <segment>
```

### 5.2 Bipolar / Slider Scale (4-Point or 5-Point)
**Question text:** Which statement best describes you? / What best describes your attitudes towards `<category>`? Select one per pair of statements.
**Programming note:** Program as a [4/5]-point scale with one statement anchoring each side. Single select per row. Randomize statements.
**Table format:** Merged header (R0-R3) + C1/C2 header row + paired statement rows:
```
R4: [blank] | C1 (RED) | C2 (RED)
R5: [blank] | [Left statement A] (BLACK) | [Right statement A] (BLACK)
R6: [blank] | [Left statement B] (BLACK) | [Right statement B] (BLACK)
```
The programmer builds the numeric scale from the programming note. Do NOT include "1 — 2 — 3 — 4" inline text.
**Variation — Bolton (4-pt):** No midpoint. Arrow starts in middle.
**Variation — CCC (5-pt):** Has midpoint. Arrow starts on left or in middle depending on question.

### 5.3 Journey / Evolution (Then vs. Now)
**Question text:** Think back to when you first started [using/drinking] `<category>` and compare it to today. How would you describe [the experience] then vs. now? Select one in each column.
**Programming note:** Randomize. Single select in both columns. Must select in C1 and C2.
**Response options:**
```
|  | C1: When I first started... | C2: Most recently...
| [State A] | |
| [State B] | |
| [State C] | |
```

---

## 6. SHOPPING JOURNEY

### 6.1 Trip Type
**Question text:** What kind of shopping trip were you on? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Trip specifically to buy [category] |
| Quick trip (2-5 items) |
| Fill in to replace a few needed items (6-10 items) |
| Routine stock-up trip (10+ items) |
| I don't remember |
```

### 6.2 Aisle / Section Engagement
**Question text:** Which best describes how you interacted with the `<category>` section when shopping at `<retailer>`? Select one.
**Programming note:** Randomize. Single select.
**Response options:**
```
| Browsed to see what was new |
| Looked specifically for <brand> |
| Went online on my phone to research products | Only show if not assigned <online>
| Looked for a specific [attribute] |
| Looked at product reviews | Only show if assigned <online>
| Other, please specify | Anchor. Open end.
| None of the above | Anchor. Mutually exclusive.
```

### 6.3 Aisle Perceptions — Bipolar Scale
**Question text:** Which statement best describes the `<category>` section at `<retailer>`? Select one for each pair of statements.
**Programming note:** Program as a 5-point scale with one statement anchoring each side. Randomize statements. Single select per row.
**Table format:** C1/C2 columns:
```
[blank] | C1 (RED) | C2 (RED)
[blank] | Disorganized | Organized
[blank] | Easy to find new items | Difficult to find new items
[blank] | Fun to browse | Boring to browse
[blank] | Has high quality brands | Has low quality brands
[blank] | Has a variety of brands | Has a limited selection of brands
```

### 6.4 Shopping Difficulty / Ease
**Question text:** Overall, how easy or difficult was it for you to find and select the `<category>` products you were looking for at `<retailer>`? Select one.
**Programming note:** Single select. Do not randomize.
**Scale:** 1 (Very difficult) — 2 — 3 — 4 — 5 (Very easy)

### 6.5 Aisle Improvement
**Question text:** What, if anything, would have improved your experience shopping for `<brand>` `<category>` at `<retailer>`? Select up to [3].
**Programming note:** Randomize. Select up to [3].
**Response options:** Study-specific improvement list + anchor:
```
| [Improvement A] |
| [Improvement B] |
| [Improvement C] | Only show if <fulfillment method> is <online>
| None of the above | Anchor. Mutually exclusive.
```

### 6.6 Assortment Gaps
**Question text:** What, if anything, do you wish there were more of in the `<category>` section at `<retailer>`? Select up to [3].
**Programming note:** Randomize. Select up to [3].
**Response options:** Study-specific gap list.

### 6.7 Time Spent
**Question text:** How much time did you spend in the `<category>` section? Select one.
**Programming note:** Single select. Do not randomize.
**Response options:**
```
| Less than 1 minute |
| 1–2 minutes |
| 3–5 minutes |
| 6–10 minutes |
| More than 10 minutes |
```

### 6.8 In-Section Behavior
**Question text:** While in the `<category>` section, which of these did you do? Select all that apply.
**Programming note:** Multi-select. Randomize.
**Response options:** Study-specific behavior list.

### 6.9 Shopping Emotions
**Question text:** Which of the following best describes how you felt while shopping for `<category>` at `<retailer>`? Select up to [3].
**Programming note:** Randomize. Select up to [3].
**Response options:** Study-specific emotion list.

### 6.10 Shopping Comparison
**Question text:** How does shopping for `<category>` compare to shopping for other [beauty / personal care / grocery] products? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Much more enjoyable |
| Somewhat more enjoyable |
| About the same |
| Somewhat less enjoyable |
| Much less enjoyable |
```

---

## 7. PURCHASE DRIVERS

### 7.1 Purchase Drivers — Two-Column Grid (Mattered / Mattered Most)
**Question text:** When you chose `<brand>` at `<retailer>`, which of these things mattered? Select all that apply. / Which mattered most? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Mattered | Select all that apply. | C2: Mattered most | Select one.
| [Driver A] | |
| [Driver B] | |
| None of the above | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
```

### 7.2 Key Attribute Double-Click — Two-Column Grid
**Question text:** Think about [attribute]. Which of these, if any, mattered? Select up to [3]. / Which mattered most? Select one.
**Programming note:** Program as a two-column grid. Randomize. Select up to [3] in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Mattered | Select up to [3]. | C2: Mattered most | Select one.
| [Sub-attribute A] | |
| [Sub-attribute B] | |
| None of these things were important to me | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
```

### 7.3 Considerations — Multi-Select
**Question text:** What did you consider when deciding which `<category>` to purchase? Select all that apply.
**Programming note:** Randomize. Multi-select.
**Response options:** Study-specific consideration list.

### 7.4 Purchase Decision Timing
**Question text:** When did you decide to buy `<brand>` `<category>`? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Before I went to the store |
| While shopping in the store |
| At the shelf |
| I always buy this product |
```

### 7.5 Why Buy
**Question text:** What made you decide to buy `<brand>` `<category>` on this trip? Select all that apply.
**Programming note:** Randomize. Multi-select.
**Response options:** Study-specific driver list + anchors.

---

## 8. OCCASION / USAGE DEEP DIVE

### 8.1 General Activity / Occasion — Two-Column Grid
**Question text:** For which of these [moments / occasions] do you typically use `<category>` products? Select up to [3]. / Most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select (or up to 3) in C1, single select in C2. Must select in C1 to select in C2.
**Response options:**
```
|  | C1: Typically | Select up to [3]. | C2: Most often | Select one.
| [Occasion A] | |
| [Occasion B] | |
| Other, please specify | Anchor. Open end. | Anchor. Open end.
```
**Logic:** Assign `<occasion>` based on C2.

### 8.2 Day of Week
**Question text:** What day of the week was it when you last [used `<category>` / had this experience]? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Weekday |
| Weekend |
| I don't remember |
```

### 8.3 Time of Day
**Question text:** What time of day was it? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Early morning (4am – 7am) |
| Morning (7am – 11am) |
| Midday (11am – 1pm) |
| Afternoon (1pm – 5pm) |
| Evening (5pm – 9pm) |
| Night (9pm – 4am) |
```

### 8.4 Where (Location)
**Question text:** Where were you the last time you [used `<category>` / had this experience]? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| At home |
| At someone else's home |
| At work |
| At school |
| Outside / outdoors |
| In the car / commuting |
| At a gym / sports facility |
| At a restaurant / cafe |
| Other, please specify | Anchor. Open end.
```

### 8.5 Who With
**Question text:** Who were you with the last time you [used `<category>`]? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Alone |
| With family |
| With friends |
| With coworkers |
| With a significant other / partner |
| Other, please specify | Anchor. Open end.
```

### 8.6 Cross-Usage
**Question text:** What other products, if any, did you use when you were `<occasion>`? Select all that apply.
**Programming note:** Multi-select. Randomize.
**Response options:** Study-specific product list. Exclude the respondent's assigned `<category>`:
```
| [Product A] | Do not show if <category> = "[Product A]"
| [Product B] | Do not show if <category> = "[Product B]"
```

### 8.7 Duration
**Question text:** How long did your overall [routine / experience] take? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Less than 15 minutes |
| 15–30 minutes |
| 30–45 minutes |
| 45–60 minutes |
| More than 60 minutes |
```

### 8.8 Occasion Frequency
**Question text:** About how often do you [use `<category>` / have this experience] when `<occasion>`? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:** Standard frequency scale (see 2.4).

### 8.9 Occasion Overlap
**Question text:** When you are [occasion], what other [beverages / products] do you typically have nearby or consume? Select all that apply.
**Programming note:** Multi-select. Randomize.
**Response options:** Study-specific product/beverage list.

### 8.10 Consumption Timing / Daypart
**Question text:** When do you typically [drink / use] each type of `<category>`? Select up to [2].
**Programming note:** Cycle through all segments. Program as carousel. Randomize types, do not randomize response options. Select up to [2] per type.
**Response options:**
```
| Early morning | <early morning>
| Mid-morning | <mid-morning>
| Midday | <midday>
| Afternoon | <afternoon>
| Evening | <evening>
| Nighttime | <nighttime>
```
**Logic:** Assign `<daypart>` based on response, use least fill.

### 8.11 Jobs — Open End
**Question text:** In 1-2 sentences, please describe the role that `<category>` plays for you during `<daypart>`.
**Programming note:** Pipe through 1 random `<segment>` and associated `<daypart>` based on least fill. Program as open-end response. Program a 5 second pause and force response.
**Response options:** Open-end text.

---

## 9. BENEFITS & MOTIVATIONS

### 9.1 Emotional Benefits — Select Up To N
**Question text:** What benefits were most important to you about `<brand>` `<category>` when `<occasion>`? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific benefit list.

### 9.2 Functional Benefits — Select Up To N
**Question text:** Which of the [benefits / functional benefits] below do you associate most with `<brand>`? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific benefit list.

### 9.3 Brand Personality — Select Up To N
**Question text:** Which words best describe how you'd like `<brand>` `<category>` to feel? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific personality trait list.

### 9.4 Underlying Motivations
**Question text:** Thinking more broadly, which of these mattered to you when `<occasion>`? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific motivation list.

### 9.5 Emotions Felt
**Question text:** Which best describes how you felt while [using `<category>` / shopping for `<category>`]? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific emotion list.

### 9.6 Pain Points
**Question text:** What issues, if any, did you experience while [using / shopping for] `<category>`? Select up to [3].
**Programming note:** Randomize. Multi-select up to [3].
**Response options:** Study-specific pain point list + anchor:
```
| [Pain point A] |
| [Pain point B] |
| None of the above | Anchor. Mutually exclusive.
```

---

## 10. FUTURE BEHAVIOR & CHANGE

### 10.1 Change in Consumption
**Question text:** Are you [using / drinking / buying] more or less `<brand>` `<category>` compared to last year? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Significantly more | <increased>
| A little more | <increased>
| The same amount |
| A little less | <decreased>
| Significantly less | <decreased>
```
**Logic:** Create hidden variable `<consumption change>` based on response.

### 10.2 Reason for Increase
**Question text:** You said you're consuming more `<brand>` `<category>` compared to last year. Why is that? Select up to [3].
**Programming note:** Show if respondent assigned `<increased>`. Randomize. Select up to [3].
**Response options:** Study-specific reason list + anchor.

### 10.3 Reason for Decrease
**Question text:** You said you're consuming less `<brand>` `<category>` compared to last year. Why is that? Select up to [3].
**Programming note:** Show if respondent assigned `<decreased>`. Randomize. Select up to [3].
**Response options:** Study-specific reason list + anchor.

### 10.4 Future Intentions
**Question text:** In the coming months, do you anticipate doing any of these? Select all that apply.
**Programming note:** Randomize. Multi-select.
**Response options:** Study-specific intention list + anchors.

### 10.5 Purchase Likelihood — Scale
**Question text:** How likely are you to purchase `<brand>` `<category>` again? Select one.
**Programming note:** Program as a 5-pt scale. Single select. Do not randomize.
**Scale:**
```
| 1 — Definitely will not purchase again |
| 2 |
| 3 — Neutral |
| 4 |
| 5 — Definitely will purchase again |
```

### 10.6 Substitution / Walk Rate
**Question text:** If `<brand>` `<category>` was not available, what would you have done instead? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Another brand of <category> |
| A different product from the same brand |
| A different size of the same product |
| Nothing — I would have left without purchasing |
| Other, please specify | Anchor. Open end.
```

### 10.7 Past Changes — Multi-Select
**Question text:** Which of the following changes have you made to your `<category>` habits in the past [1-2 years]? Select all that apply.
**Programming note:** Randomize. Multi-select.
**Response options:** Study-specific change list.

---

## 11. PRICING (GABOR-GRANGER)

### 11.1 Purchase Likelihood at Price — Adaptive Carousel
**Question text:** Assuming you or someone you were buying for was interested in one of the `<brand>` products shown, how likely would you be to purchase it at the following price? Select one.
**Programming note:** Program as carousel. First show median price [F] and prompt on likelihood of purchase. If respondent replies 1-3 (disagree side), show one price level lower. If respondent replies 4-5 (agree side), show one price level higher. Continue cycling through price points until lower or upper bound is reached. Create hidden variable `<GG[N]>` based on upper/lower bound reached.
**Price ladder:** [Study-specific price points, e.g., $10–$18 in $1 increments]
**Scale:** Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree

### 11.2 Fair Price — Open End
**Question text:** Why do you think `<GG price>` is a fair price for this product?
**Programming note:** Program as open end.
**Response options:** Open-end text.

### 11.3 Distinctive Attributes
**Question text:** What are the top reasons you would consider purchasing `<brand>`? Select up to [3].
**Programming note:** Randomize. Select up to [3].
**Response options:** Study-specific attribute list + anchors.

### 11.4 Grounding Message (Brand Description)
**Text:** For this activity, please think about the [size] [product type] `<brand>` [packaging] below. [2-4 sentence brand description including founding, key differentiators, certifications, sourcing practices.]
**Programming note:** Show to all respondents. [Include product image if applicable.]

---

## 12. BARRIERS

### 12.1 Category Barriers
**Question text:** Earlier you said you haven't purchased `<category>` in the past [X] months. Why not? Select up to [3]. / Select all that apply.
**Programming note:** Only show to terminated / non-qualifying respondents. Randomize. Multi-select or select up to [3].
**Response options:**
```
| Too expensive |
| Hard to find where I shop |
| Don't have the right [equipment / tools] at home |
| Prefer the ease of other types |
| Not sure how to properly [use / prepare] it |
| Don't think it's different from other types |
| Other, please specify | Anchor. Open end.
| Just haven't thought about it | Anchor. Mutually exclusive.
```

### 12.2 Barrier Overcome — What Would Make You Consider
**Question text:** What, if anything, would make you consider [buying / trying] `<category>` in the future? Select up to [3].
**Programming note:** Only show to non-qualifying respondents. Randomize. Select up to [3].
**Response options:**
```
| None of the below | Anchor. Mutually exclusive.
| More affordable options |
| [Study-specific enabler] |
| Recommendations from family / friends |
| Other, please specify | Anchor. Open end.
```
**Logic:** Terminate all remaining unqualified respondents after this question.

---

## 13. INFORMATION SOURCES

### 13.1 Sources of Information / Inspiration
**Question text:** Where do you find most of your information on `<category>` products? Select all that apply.
**Programming note:** Multi-select. Randomize.
**Response options:**
```
| Medical professional (e.g., General practitioner, dermatologist) |
| Social media (e.g., TikTok, Instagram, Facebook) |
| Friends or family |
| Online search (e.g., Google) |
| In-store (e.g., shelf displays, associates) |
| Magazines / blogs / websites |
| TV / streaming ads |
| Other, please specify | Anchor. Open end.
| None of the above | Anchor. Mutually exclusive.
```

### 13.2 Social Media Sources — Detail
**Question text:** Which social media platforms do you use most for `<category>` inspiration? Select all that apply.
**Programming note:** Only show if respondent selected "Social media" in prior question. Multi-select. Randomize.
**Response options:**
```
| TikTok |
| Instagram |
| YouTube |
| Facebook |
| Pinterest |
| Reddit |
| X / Twitter |
| Other, please specify | Anchor. Open end.
```

### 13.3 Research Behavior
**Question text:** When you research `<category>` products, what information do you look for? Select all that apply.
**Programming note:** Multi-select. Randomize.
**Response options:** Study-specific research info list.

---

## 14. LEADING EDGE / QUALIFICATION

### 14.1 Leading Edge Consumer — Attitude Battery
**Question text:** On a scale from 1 to 5, how much do you agree or disagree with each of the following statements?
**Programming note:** 5 pt scale. Randomize. Single select per statement.
**Scale:** Strongly disagree | Somewhat disagree | Neither agree nor disagree | Somewhat agree | Strongly agree
**Logic:**
```
Create hidden variable <LE Consumer> if respondent meets [N]+ of the following criteria:
  - Selects "Somewhat agree" or "Strongly agree" on [relevant items]
  - AND meets [usage/purchase criteria]
Min n=[X], max n=[Y].
```

### 14.2 Home Barista / Enthusiast — Composite Qualification
**Question text:** Same as 5.1 (agreement battery), but with specific logic:
**Logic (CCC example):**
```
Create hidden variable <Home Barista> if respondent satisfies:
  - Selects "somewhat disagree" or "strongly disagree" for R4 and R5
  - AND selects "somewhat agree" or "strongly agree" for all of R1–R3
```
**Logic (Yerba Madre example):**
```
Create hidden variable <Enthusiast> if respondent satisfies [composite criteria across multiple questions].
```

### 14.3 Triggers to Behavior Change
**Question text:** What prompted you to start [buying/using] `<category>`? Select up to [2].
**Programming note:** Randomize. Multi-select up to [2].
**Response options:** Study-specific trigger list.

---

## 15. MESSAGES & TRANSITIONS

### 15.1 Introduction Message
**Text:** "Thank you in advance for your time. We're excited to hear about your [shopping habits / experiences]!"
**Programming note:** Show to all respondents.
**Format:** 4-row header table, R2 = message text, R3 = "Show to all respondents."
**Followed by:** Hold all terminates until the end of the screener unless otherwise specified.

### 15.2 Section Transition Message
**Text:** "[Context-setting text for the next section, piping variables as needed.]"
**Programming note:** Show to all respondents. / Show to [specific segment only].
**Examples:**
- "Thanks for taking the time to complete our study. First, we're going to ask you some questions about [topic]."
- "We'd now like to focus more on your overall routine and the moments when you're using `<brand>`."
- "You said you use `<brand>` `<category>` for `<occasion>`. Now, we want to ask you more about the last time you used `<brand>` `<category>` for `<occasion>`."
- "Keep thinking about the last trip you made to `<retailer>` to buy `<brand>` `<category>`."
- "You're doing great! For the next few questions, we're going to ask you about [topic]."

### 15.3 Qualifying / Congratulations Message
**Text:** "Congratulations, you have qualified for this study! We appreciate your thoughtfulness and honesty."
**Programming note:** Show message to respondents based on their qualification.

### 15.4 Grounding Message (Brand/Product Description)
**Text:** See 11.4 above.

### 15.5 Closing Message
**Text:** "Thank you for your answers so far! We look forward to reading your responses. Before we complete the survey, we have just a couple remaining questions."
**Programming note:** Show to all respondents.

---

## 16. PRODUCT-SPECIFIC PATTERNS

### 16.1 Appliances / Equipment Owned — Two-Column Grid
**Question text:** Which of the following [appliances / tools] do you currently own? Select all that apply. / Which do you use most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2.
**Response options:**
```
|  | C1: Currently own | C2: Use most often
| [Appliance A] | |
| [Appliance B] | |
| Other, please specify | Anchor. Open end. | Anchor. Open end.
| None of the above | Anchor. Mutually exclusive. | Anchor. Mutually exclusive.
```

### 16.2 Brew Method / Preparation — Two-Column Grid
**Question text:** What are all the different ways that you typically prepare `<brand>` `<category>`? Select all that apply. / Most often? Select one.
**Programming note:** Program as a two-column grid. Randomize. Multi-select in C1, single select in C2.
**Response options:** Study-specific preparation method list.

### 16.3 Drink / Product Type — Single Select with Variable
**Question text:** What type of [drink / product] do you [prepare / use] most with `<brand>`? Select one.
**Programming note:** Randomize. Single select.
**Response options:**
```
| [Type A] | <type_a>
| [Type B] | <type_b>
| Other, please specify | Anchor. Open end.
```
**Logic:** Create hidden variable `<product type>` based on response.

### 16.4 Additives / Customization
**Question text:** What, if anything, do you add to your `<category>`? Select all that apply.
**Programming note:** Randomize. Multi-select.
**Response options:** Study-specific additive list. Use "Keep R[x] and R[y] together" for related items.

### 16.5 Gifting vs. Personal Purchase
**Question text:** How often do you purchase `<category>` as a gift vs. for yourself? Select one.
**Programming note:** Do not randomize. Single select.
**Response options:**
```
| Always for myself |
| Mostly for myself, sometimes as a gift |
| About equally for myself and as gifts |
| Mostly as gifts |
| Always as gifts |
```

### 16.6 Hair Type / Physical Attribute (Category-Specific)
**Question text:** What is your [hair type / skin type / etc.]? Select one.
**Programming note:** Single select. Do not randomize.
**Response options:** Category-specific (e.g., straight, wavy, curly, coiled for hair).

---

## 17. SUGAR / INGREDIENT ATTITUDES (Specialty Module)

### 17.1 Ingredient Importance — Bipolar Scale
**Question text:** How important is [sugar / sweetener / ingredient] to you when choosing `<category>`? Select one per pair.
**Programming note:** Program as a 5-point scale. Single select per row. Randomize.

### 17.2 Ingredient Preferences — Agreement Battery
**Question text:** How much do you agree with each statement about [sugar / ingredients]? Select one per statement.
**Programming note:** 5 pt scale. Randomize. Single select per statement.

### 17.3 Desired Ingredient Type
**Question text:** Which type of [sweetener / ingredient] do you prefer in your `<category>`? Select one.
**Programming note:** Single select. Do not randomize.
**Response options:** Study-specific ingredient list.

---

## Quick Reference: Table Format by Question Type

| Question Type | Header Table | Response Table Cols | Notes |
|---|---|---|---|
| Simple single-select | 4×1 | 3 (blank, option, note) | "Single select" |
| Simple multi-select | 4×1 | 3 (blank, option, note) | "Multi-select" |
| Multi-select up to N | 4×1 | 3 (blank, option, note) | "Select up to [N]" |
| 2-column grid | 4×1 | 4 (blank, option, C1 note, C2 note) | R0 = column headers |
| 3-column grid | 4×1 | 5 (blank, option, C1, C2, C3/note) | R0 = column headers |
| 5-pt agreement | 4×1 (scale row) + 4×1 (statements) | 3 (blank, statement, condition) | Scale in separate table above |
| Bipolar/slider | 4×1 | 3 (left statement, scale, right statement) | Per-row format |
| Dropdown | 4×1 | N/A | "Program as dropdown" |
| Open-end | 4×1 | N/A | "Open end. Leave space." |
| Message | 4×1 | N/A | R0=topic, R2=text, R3=show condition |
| Carousel | 4×1 | 3 | Loop instruction in logic |
| Gabor-Granger | 4×1 | Adaptive carousel | Price ladder + scale |
