---
name: daily-newsletter
description: >
  Generate Seurat-branded HTML newsletter from daily brief(s). Mon-Thu = daily
  (3-4 signals, clients, building, early signals). Friday = weekly digest (5-6
  signals, counter-signals, data points, what connected, watching next week).
  Opens in Outlook compose mode. Run AFTER daily-brief.
---

Generate today's CPG newsletter for the Seurat team. Open it in Outlook ready to send.

**PREREQUISITE:** Today's daily brief must exist at Intelligence/daily-briefs/[TODAY].md.
If not, STOP and tell the user to run `/daily-brief` first.

**BASE:** C:/Users/NickFisher/Dropbox (Personal)/Nick's Personal Dropbox (Nickfisher518@gmail.com)/seurat-brain

**READS:** daily briefs, _hot-signals.md, _inbox-log.md, active-projects.md, source newsletter emails (Gmail MCP)
**WRITES:** Intelligence/newsletters/[TODAY].html
**OPENS:** Outlook email with HTML body, ready to review + send

---

## Voice (read this first, it governs everything)

You are writing for senior CPG consultants who already read most of these same sources. They are well-informed. The newsletter's value is **curation, connection, and pattern recognition**, not attention-grabbing.

**Write like an analyst briefing a partner before a client call.** Not like a journalist writing for subscribers.

Specific rules:

- **Headlines state what happened.** No narrative framing ("Takes Shape," "Reaches Scale"), no reveal language ("Is Now," "Just Got"), no drama. Lead with the fact or the data point. "Beyond Protein at Expo West" not "The Post-Protein Shelf Takes Shape."
- **Body copy reports facts and lets informed readers draw conclusions.** No sweeping claims ("Scale advantages are eroding"), no urgency manufacturing ("should act now"), no punchy fragments ("Direct competitor, same shelf."). Write complete sentences with measured language.
- **"So what:" lines are analytical observations, not one-liners.** Connect the signal to our work without LinkedIn-style provocation. "Retailers are allocating more shelf space to emerging brands for differentiation" not "Scale advantages are eroding."
- **No jargon-as-drama.** Don't use "table stakes," "game-changer," "unprecedented," or "at scale" unless the data literally requires it.
- **The test:** Would a well-informed partner read this and think the framing is overstated? If yes, tone it down. When in doubt, be more plain.
- **Present tense.** "Nestle sells" not "Nestle has sold."
- **No hedging.** No "it remains to be seen." State what happened, what it connects to.
- **"We" for Seurat connections.** "Relevant to our Koki work" not "Relevant to Seurat's Koki work."

---

## Cadence: Daily Pulse vs. Weekly Digest

This skill produces **two formats** depending on the day.

### Deciding which format to run:

1. **Friday:** Always produce the **Weekly Digest**. It covers Mon-Fri of the current week.
2. **Monday-Thursday:** Produce the **Daily** from today's brief.
3. **Override:** If the user says "weekly" or "daily", follow their instruction regardless of day.

---

## Format A: Daily (Mon-Thu)

**Subject:** `CPG Intelligence Brief // [Day of Week], [Month] [Day]`
**Read time target:** ~2 minutes
**Subtitle in header:** "CPG Intelligence Brief"

### Step D1 - Load intelligence

Read these files:
1. `Intelligence/daily-briefs/[TODAY].md`
2. `Intelligence/_hot-signals.md`
3. `Intelligence/_inbox-log.md` (today's entries)
4. `Intelligence/active-projects.md`

### Step D2 - Mine source emails for links

Via Gmail MCP, for every newsletter processed today:
1. Search for and read each source email
2. Extract article URLs (tracking links, "View in browser" URLs). Match to stories in today's brief. Every headline must link to its source.
3. For footer, every source needs a link. Use "View Online" URL if available, publication homepage as fallback.
4. For Twitter signals, use tweet URLs from the daily brief directly.

**If an email body is empty or mangled** (Progressive Grocer known issue), use publication homepage. Don't block the newsletter.

### Daily sections (top to bottom):
1. **Header** (logotype + date)
2. **Hook** (2-3 sentences, ~200-230 characters, filling 3 lines. The day's most notable development.)
3. **TOP SIGNALS** (3-4 stories with circle number badges)
4. **FOR OUR CLIENTS** (client brands that appeared today)
5. **BUILDING** (the pattern with most momentum, tracked across days)
6. **EARLY SIGNALS** (3 Twitter-only signals with tweet URLs, X badge next to section header)
7. **Footer** (logotype + all sources linked)

### Daily deduplication rules (critical):

Before writing, read the last 2-3 newsletters in `Intelligence/newsletters/` to see what was already sent. The daily must feel like **new news**, not a repeat.

- **TOP SIGNALS must be new.** If a story ran as a signal yesterday, do NOT run it again today even if new sources covered it. Find a different angle or a different story. Exception: a genuinely new development on the same topic (e.g., "Target bans synthetic colors" Monday is different from "Target expands grocery 50%" Tuesday, even though both are Target).
- **BUILDING can repeat the same trend** but the narrative MUST advance. Add the new data point, name the new source, note the velocity change. Never copy yesterday's BUILDING text. If nothing new was added to the trend today, pick a different building signal.
- **FOR OUR CLIENTS only includes today's new mentions.** If BellRing appeared yesterday AND today, only include today's mention with today's specific signal. Do not repeat yesterday's client line.
- **EARLY SIGNALS must rotate.** Never repeat a Twitter signal that appeared in a previous daily. If the tweet was already featured, it is spent. Pick a different one.
- **If today is thin on new signals** (e.g., only 1-2 newsletters delivered), it is better to send 2-3 strong unique signals than to pad with repeats. Reduce to 3 TOP SIGNALS rather than recycling.

### Daily content rules:

**TOP SIGNALS (3-4)**
- Headline: 8 words max. State the fact. Link to source article.
- Body: 2-3 sentences with specific numbers. Inline-link key claims.
- "So what:" one analytical sentence connecting to our work.
- Source line: linked source names
- 4 signals on full days (5+ newsletters). 3 signals on light days (1-2 newsletters).

**FOR OUR CLIENTS** (only if client brands appeared today with new signals)
- One line per brand. `**ClientName:** [signal + implication, linked to source]`
- Use colons after client name, not dashes

**BUILDING (1)**
- Descriptive title, not dramatic
- 2-3 sentence narrative. How the pattern built across recent days. Must include at least one NEW data point from today.
- Strength/appearances/tracking-since metadata line

**EARLY SIGNALS (3)** - Twitter-only, not yet in newsletters
- Section header: "EARLY SIGNALS" label with X logo badge (black 20x20 rounded square with &#120143; character) and subtitle "From accounts we track on X. Click to explore."
- Each = exactly 3 full lines of text. @handle at end of line 3.
- Linked bold headline (to tweet URL) + 2-3 sentence context + @handle link at end
- ~200-210 total characters per signal
- Must not repeat any signal from a previous daily newsletter

---

## Format B: Weekly Digest (Friday)

**Subject:** `CPG Intelligence Weekly // Week of [Month] [Day]`
**Read time target:** 4-5 minutes
**Subtitle in header:** "CPG Intelligence Weekly"

The weekly is NOT a longer daily. A daily sees one day and reports what happened. A weekly sees five days and provides **perspective**: cross-signal synthesis, velocity, counter-signals, and forward-looking context. ~40% of the weekly should be analysis that doesn't exist in any daily.

### Design principle: weekly-only readers miss nothing, daily readers get new value

- **Weekly-only readers** get every client mention from the week, all top signals, and the synthesis. They never feel out of the loop.
- **Daily readers** get genuinely new analysis they haven't seen: What Connected, Counter-signals, signal velocity, strategy implications, and the data reference table.

### Step W1 - Load the full week

Read ALL daily briefs from this week: Monday through Friday.
Also read:
- `Intelligence/_hot-signals.md`
- `Intelligence/_inbox-log.md` (full week)
- `Intelligence/active-projects.md`
- `BD/Pipeline.md` (for prospect relevance)
- `Intelligence/GrowthPapers/_pipeline.md` (for paper ideas)
- The last 2 weekly digests in `Intelligence/newsletters/` for pattern continuity
- `Intelligence/topics/` files for cross-week context

### Step W2 - Mine source emails for links

Via Gmail MCP, for the week's key stories:
1. Search for and read source emails from the week
2. Extract article URLs (tracking links, "View in browser" URLs)
3. For Twitter signals, use tweet URLs from the daily briefs
4. For footer, link every source (publication homepage as fallback)

### Step W3 - Curate the weekly

Select the **best 5-6 signals from the entire week** (not just Friday). Combine related signals from different days into richer, more complete stories. A signal that appeared Tuesday and got follow-up data Thursday becomes one deeper weekly story, not two separate entries.

### Weekly sections (top to bottom):
1. **Header** (logotype + "Week of [date]")
2. **Hook** (3-4 sentences, ~280-320 characters. The week's defining theme with supporting evidence.)
3. **THIS WEEK** (5-6 signals with circle number badges)
4. **FOR OUR CLIENTS** (ALL client mentions from the week, consolidated. No one should feel they missed a client signal.)
5. **BUILDING** (the pattern with most momentum, with velocity data and cross-week narrative)
6. **EARLY SIGNALS** (3-4 best Twitter-only signals from the week, with X logo badge in section header)
7. **COUNTER-SIGNALS** (1-2 things that contradict the prevailing narrative. What didn't happen, or where buzz and shelf reality diverge.)
8. **DATA POINTS** (5-8 specific stats, formatted as a scannable reference)
9. **WHAT CONNECTED** (3-4 sentences of cross-signal synthesis)
10. **WATCHING NEXT WEEK** (2-3 things coming up: earnings calls, events, expected launches)
11. **Footer** (logotype + all sources linked)

### Weekly content rules (where it differs from daily):

**THIS WEEK (5-6 signals)**
- Same format as daily signals, but:
- Body: 3-4 sentences (longer than daily's 2-3). Room to include context from multiple days.
- "So what:" can be 2 sentences if the signal warrants deeper connection to our work. Connect to specific Seurat selling areas (Category Vision, Growth Strategy, Brand Strategy, etc.) or BD prospects where relevant.
- If a signal appeared across multiple days, note how it developed: "Flagged Tuesday when [X]. By Thursday, [Y] confirmed the direction."

**FOR OUR CLIENTS**
- **Include ALL client mentions from the week.** A partner who only reads the weekly must not miss a client signal.
- Consolidate across the week: if Koki appeared Monday and Thursday, combine into one richer entry.
- Can be 2 lines per brand if warranted (vs. 1 in the daily).
- Note which day signals appeared: "Flagged Tuesday" helps weekly-only readers gauge urgency.

**BUILDING (1)**
- Same format, but the narrative covers the full week and references prior weeks.
- 3-4 sentences instead of 2-3.
- **Include velocity:** "X mentions last week, Y this week" or "first appeared [date], now [N] sources covering it."
- Connect to specific client opportunities or Seurat selling areas if applicable.

**EARLY SIGNALS (3-4)** — one more than daily
- Same format as daily (3 full lines each, @handle at end)
- Pick the best from the full week, not just Friday's scan

**COUNTER-SIGNALS (weekly only)**
- 1-2 items. What contradicts the prevailing narrative this week?
- Example: "Despite heavy social media buzz around seed-oil-free, actual Expo West launches were still overwhelmingly protein-focused. The gap between online conversation and shelf reality is worth watching."
- This is what makes the newsletter feel like analysis, not aggregation. Informed readers value the contrarian check.
- If nothing genuinely contradicts the week's signals, omit the section.

**DATA POINTS (weekly only)**
- 5-8 bullet points. Each is a specific stat with source.
- Format: `[Stat] — [Source, Date]`
- Example: "116K daily price changes at Amazon — Retail Brew, Mar 6"
- These are the numbers someone would paste into a deck or reference on a client call. Design for screenshot-ability.

**WHAT CONNECTED (weekly only)**
- 3-4 sentences. No bullets.
- What themes ran through multiple signals this week? What's the "so what" across the whole week, not just individual stories?
- This is the analysis that makes the weekly worth reading even if you read every daily.
- Example: "Three separate signals this week point to the same shift: seed-oil-free claims at Kroger, Non-UPF Verified reaching 118 products, and Target dropping artificial colors. Ingredient scrutiny is moving from natural/specialty into mainstream retail simultaneously across multiple chains. For clients with a clean-ingredient story, the positioning window is open. For those without one, the competitive pressure is building."

**WATCHING NEXT WEEK (weekly only)**
- 2-3 bullet points. What's coming up that the team should be aware of.
- Earnings calls, industry events, expected product launches, regulatory deadlines, client milestones.
- Gives the weekly a forward-looking element and gives daily readers a reason to pay attention next week.
- Example: "Kroger Q4 earnings Thursday — watch for comments on natural/organic set expansion. CAGNY presentations continue — PepsiCo and Mondelez both presenting."

---

## Content rules (both formats)

### Cut - never include:
- M&A, deal valuations, financial restructuring (not our work)
- Processing stats, signal counts, system metadata
- `[CLIENT BRAND]` tags, seurat-brain references, infrastructure language
- Filler stories included just to fill a slot

### Content focus:
Seurat is a **consumer insights firm**, not a bank. Prioritize:
- Consumer behavior shifts, shopper dynamics, trip patterns
- Category dynamics: share shifts, format changes, shelf trends
- Innovation: product launches, ingredient trends, format evolution
- Retail channel: retailer strategy, format competition, pricing
- Brand strategy signals relevant to our clients

Do NOT lead with: M&A deals, PE moves, earnings, financial restructuring, stock performance.

### Typography rules (non-negotiable):
- **No em dashes.** Never use `&mdash;` or `—` anywhere. Use colons, periods, commas, or restructure.
- **Headlines must fit one line.** Max ~35 characters (accounting for badge column width).
- **No hanging orphans.** #1 editorial rule. Never leave 1-3 words dangling on a final line. Estimate ~60 chars/line in badge column, ~67 chars/line full width. If the last line would be just a word or two, rewrite to pull them back or add enough to fill the line.
- **Balance link density.** Never stack two linked sentences back-to-back without unlinked text between them. Readers should see a mix of linked claims and plain context.
- **Straight quotes.** Use regular `"` and `'`.
- **`&middot;`** for inline separators.

---

## Outlook-compatible HTML

The newsletter renders in **Outlook's Word-based HTML engine**.

### Outlook rules (non-negotiable):
- **Tables only for layout.** No `<div>`, flexbox, grid.
- **All styles inline.** Outlook strips `<style>` blocks.
- **`border-radius:50%`** for non-Outlook; VML `<v:roundrect arcsize="50%">` inside `<!--[if mso]>` for Outlook circle badges.
- **No `opacity` or `rgba()`** - pre-calculated solid hex colors only.
- **No `max-width`** - explicit `width="600"` on tables.
- **`mso-line-height-rule:exactly`** alongside every `line-height`.
- **`padding` only on `<td>`** - not on `<p>`, `<span>`.
- **MSO XML declaration** in `<html>` tag and `<head>`.

### Font stacks and weight rules:
- **Headlines (19px), building/hot signal title (17px):** `'Franklin Gothic Demi','Franklin Gothic Medium',Calibri,Arial,sans-serif` — do NOT add `font-weight:bold` (Demi is already medium-bold; doubling looks too heavy)
- **Section labels (11px uppercase):** `'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif` with `font-weight:bold`
- **Body text, source lines:** `'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif`
- **VML circle badge text:** `Calibri,sans-serif` only inside VML `<center>` tags. `font-size:14px` + `line-height:32px` for vertical centering.
- **Logotype:** Franklin Gothic Demi, 28px header / 18px footer

### Brand colors:

| Name | Hex | Use |
|------|-----|-----|
| Navy | `#1B2E59` | Header, headlines, "So what" prefix |
| Body | `#424242` | All body text |
| Blue | `#28A8E0` | Section labels, links, number badges |
| Orange | `#F49221` | Client section label, client names, logotype "group" |
| Teal | `#397778` | Building signal border + label |
| Soft BG | `#F4F5F7` | Outer wrapper, footer |
| White | `#FFFFFF` | Content area, logotype "seurat" |
| Muted | `#999999` | Source lines |
| Header subtitle | `#8DA3C0` | Subtitle text on navy |
| Header date | `#6B82A3` | Date text on navy |

### Logo:
Text-based logotype in Franklin Gothic Demi.
- Header: `<span style="color:#FFFFFF;">seurat</span><span style="color:#F49221;">group</span>` (white+orange on navy)
- Footer: `<span style="color:#1B2E59;">seurat</span><span style="color:#F49221;">group</span>` (navy+orange on light)

### HTML template skeleton

Use this structure. Adjust sections based on daily vs. weekly format.

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--[if mso]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body style="margin:0; padding:0; background-color:#F4F5F7; width:100%;">

<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#F4F5F7;">
<tr><td align="center" style="padding:24px 10px;">

<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" style="background-color:#FFFFFF;">

<!-- ========== HEADER ========== -->
<tr>
<td style="background-color:#1B2E59; padding:32px 40px 28px 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td style="font-family:'Franklin Gothic Demi','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:28px; mso-line-height-rule:exactly; line-height:34px; letter-spacing:1px;"><span style="color:#FFFFFF;">seurat</span><span style="color:#F49221;">group</span></td></tr>
  <tr><td style="font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:14px; color:#8DA3C0; padding-top:6px; mso-line-height-rule:exactly; line-height:20px;">[CPG Pulse -or- CPG Intelligence Weekly]</td></tr>
  <tr><td style="font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:12px; color:#6B82A3; padding-top:2px; mso-line-height-rule:exactly; line-height:18px;">[Date or Week of date]</td></tr>
  </table>
</td>
</tr>

<!-- ========== HOOK ========== -->
<tr>
<td style="padding:28px 40px 20px 40px;">
  <p style="margin:0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:16px; color:#424242; mso-line-height-rule:exactly; line-height:24px;">[2-3 sentences, ~200-230 chars. Week's defining theme. Facts, not framing.]</p>
</td>
</tr>

<!-- ========== SECTION LABEL ========== -->
<tr>
<td style="padding:0 40px;">
  <p style="margin:0 0 12px 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; font-weight:bold; color:#28A8E0; letter-spacing:2px; text-transform:uppercase; mso-line-height-rule:exactly; line-height:14px;">[TODAY -or- THIS WEEK]</p>
  <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E0E0E0; font-size:1px; line-height:1px;">&nbsp;</td></tr></table>
</td>
</tr>

<!-- ========== SIGNAL (repeat per story) ========== -->
<tr>
<td style="padding:16px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td width="36" valign="top" style="padding-right:14px;">
      <table cellpadding="0" cellspacing="0" border="0"><tr>
        <td width="32" height="32" align="center" valign="middle" style="background-color:#28A8E0; border-radius:50%; font-family:Calibri,Arial,sans-serif; font-size:14px; font-weight:bold; color:#FFFFFF; mso-line-height-rule:exactly; line-height:32px;"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:32px;v-text-anchor:middle;width:32px;" arcsize="50%" fillcolor="#28A8E0" stroke="f"><w:anchorlock/><center style="color:#ffffff;font-family:Calibri,sans-serif;font-size:14px;font-weight:bold;line-height:32px;">1</center></v:roundrect><![endif]--><!--[if !mso]><!-->1<!--<![endif]--></td>
      </tr></table>
    </td>
    <td valign="top">
      <a href="[URL]" style="font-family:'Franklin Gothic Demi','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:19px; color:#1B2E59; text-decoration:none; mso-line-height-rule:exactly; line-height:25px;">[Headline]</a>
      <p style="margin:6px 0 0 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:15px; color:#424242; mso-line-height-rule:exactly; line-height:22px;">[Body: 1-2 sentences daily, 2-3 weekly]</p>
      <p style="margin:4px 0 0 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:15px; color:#424242; mso-line-height-rule:exactly; line-height:22px;"><strong style="color:#1B2E59;">So what:</strong> [One analytical sentence.]</p>
      <p style="margin:4px 0 0 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:12px; color:#999999; mso-line-height-rule:exactly; line-height:16px;"><a href="[URL]" style="color:#999999;">[Source]</a></p>
    </td>
  </tr>
  </table>
</td>
</tr>

<!-- Signal divider -->
<tr><td style="padding:16px 40px 0 40px;"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #F0F0F0; font-size:1px; line-height:1px;">&nbsp;</td></tr></table></td></tr>

<!-- ========== FOR OUR CLIENTS ========== -->
<tr>
<td style="padding:24px 40px 0 40px;">
  <p style="margin:0 0 12px 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; font-weight:bold; color:#F49221; letter-spacing:2px; text-transform:uppercase; mso-line-height-rule:exactly; line-height:14px;">FOR OUR CLIENTS</p>
  <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E0E0E0; font-size:1px; line-height:1px;">&nbsp;</td></tr></table>
</td>
</tr>
<tr>
<td style="padding:10px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding:6px 0; border-bottom:1px solid #F5F5F5;">
      <p style="margin:0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:14px; color:#424242; mso-line-height-rule:exactly; line-height:21px;"><strong style="color:#F49221;">[Client]:</strong> [Signal + implication. Link to source.]</p>
    </td>
  </tr>
  </table>
</td>
</tr>

<!-- ========== BUILDING ========== -->
<tr>
<td style="padding:24px 40px 0 40px;">
  <p style="margin:0 0 12px 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; font-weight:bold; color:#397778; letter-spacing:2px; text-transform:uppercase; mso-line-height-rule:exactly; line-height:14px;">BUILDING</p>
</td>
</tr>
<tr>
<td style="padding:0 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td width="4" style="background-color:#397778;"></td>
    <td style="background-color:#F5F9F9; padding:16px 20px;">
      <p style="margin:0; font-family:'Franklin Gothic Demi','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:17px; color:#1B2E59; mso-line-height-rule:exactly; line-height:22px;">[Descriptive title]</p>
      <p style="margin:8px 0 0 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:14px; color:#424242; mso-line-height-rule:exactly; line-height:21px;">[2-3 sentences showing how the pattern built.]</p>
      <p style="margin:6px 0 0 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:12px; color:#999999; mso-line-height-rule:exactly; line-height:16px;">[Building/Strong] &middot; [N] appearances &middot; Since [date]</p>
    </td>
  </tr>
  </table>
</td>
</tr>

<!-- ========== EARLY SIGNALS (both formats) ========== -->
<tr>
<td style="padding:24px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td valign="middle" style="padding:0 0 4px 0;">
      <p style="margin:0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; font-weight:bold; color:#1B2E59; letter-spacing:2px; text-transform:uppercase; mso-line-height-rule:exactly; line-height:14px;">EARLY SIGNALS</p>
    </td>
    <td width="24" valign="middle" style="padding:0 0 4px 8px;">
      <table cellpadding="0" cellspacing="0" border="0"><tr>
        <td width="20" height="20" align="center" valign="middle" style="background-color:#000000; border-radius:4px; font-family:Calibri,Arial,sans-serif; font-size:12px; font-weight:bold; color:#FFFFFF; mso-line-height-rule:exactly; line-height:20px;"><!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="height:20px;v-text-anchor:middle;width:20px;" arcsize="20%" fillcolor="#000000" stroke="f"><w:anchorlock/><center style="color:#ffffff;font-family:Calibri,sans-serif;font-size:12px;font-weight:bold;line-height:20px;">&#120143;</center></v:roundrect><![endif]--><!--[if !mso]><!-->&#120143;<!--<![endif]--></td>
      </tr></table>
    </td>
  </tr></table>
  <p style="margin:0 0 10px 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:12px; color:#999999; mso-line-height-rule:exactly; line-height:16px;">From accounts we track on X. Click to explore.</p>
  <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E0E0E0; font-size:1px; line-height:1px;">&nbsp;</td></tr></table>
</td>
</tr>
<tr>
<td style="padding:8px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding:6px 0; border-bottom:1px solid #F5F5F5;">
      <p style="margin:0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:14px; color:#424242; mso-line-height-rule:exactly; line-height:21px;"><a href="[TWEET_URL]" style="color:#1B2E59; font-weight:bold; text-decoration:none;">[Headline.]</a> [Context, ~200-210 chars total for 3 full lines.] <a href="[TWEET_URL]" style="color:#28A8E0;">@handle</a></p>
    </td>
  </tr>
  </table>
</td>
</tr>

<!-- ========== WHAT CONNECTED (weekly only) ========== -->
<tr>
<td style="padding:24px 40px 0 40px;">
  <p style="margin:0 0 12px 0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; font-weight:bold; color:#1B2E59; letter-spacing:2px; text-transform:uppercase; mso-line-height-rule:exactly; line-height:14px;">WHAT CONNECTED</p>
  <table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E0E0E0; font-size:1px; line-height:1px;">&nbsp;</td></tr></table>
</td>
</tr>
<tr>
<td style="padding:10px 40px 0 40px;">
  <p style="margin:0; font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:14px; color:#424242; mso-line-height-rule:exactly; line-height:21px;">[2-3 sentences. What themes linked across this week's signals. The proprietary analysis layer.]</p>
</td>
</tr>

<!-- ========== FOOTER ========== -->
<tr>
<td style="padding:28px 40px; background-color:#F4F5F7;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td align="center" style="font-family:'Franklin Gothic Demi','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:18px; mso-line-height-rule:exactly; line-height:22px; padding-bottom:6px;"><span style="color:#1B2E59;">seurat</span><span style="color:#F49221;">group</span></td></tr>
  <tr><td align="center" style="font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; color:#BBBBBB; mso-line-height-rule:exactly; line-height:15px;">[N] newsletters + [N] Twitter accounts &middot; [Date]</td></tr>
  <tr><td align="center" style="font-family:'Franklin Gothic Book','Franklin Gothic Medium',Calibri,Arial,sans-serif; font-size:11px; color:#BBBBBB; mso-line-height-rule:exactly; line-height:15px; padding-top:2px;"><a href="[URL]" style="color:#BBBBBB;">[Source]</a> &middot; ...</td></tr>
  </table>
</td>
</tr>

</table>
</td></tr></table>
</body>
</html>
```

### Link rules:
- Every headline links to its source article
- Every footer source links to newsletter web archive or publication homepage
- Twitter signals link to actual tweet URL (https://x.com/handle/status/ID)
- Link colors: body `#28A8E0`, headlines `#1B2E59` (no underline), footer `#BBBBBB`
- No source URL? Plain text headline (no fake links)

---

## Save and deliver

### Save:
Write HTML to `Intelligence/newsletters/[TODAY].html`

### Open in Outlook:

```python
import win32com.client

html_path = r"[FULL_PATH]/Intelligence/newsletters/[TODAY].html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

outlook = win32com.client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.Subject = "[CPG Pulse // Day, Month Day] -or- [CPG Intelligence Weekly // Week of Month Day]"
mail.HTMLBody = html_content
mail.Display()
```

Nick adds recipients and sends.

**If Outlook COM fails:** Tell user the HTML is saved, they can open in browser, Ctrl+A, Ctrl+C, paste into Outlook.

---

## Report

Tell the user:
1. Format sent (daily pulse or weekly digest) and why
2. Signals included
3. Archive saved at `Intelligence/newsletters/[TODAY].html`
