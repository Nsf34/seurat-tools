---
name: daily-brief
description: >
  Run today's CPG intelligence brief for Seurat. Scans newsletter inbox (Gmail MCP)
  and Twitter (bird CLI) for CPG signals. Processes, classifies, and files insights
  to topic files. Writes daily brief to Intelligence/daily-briefs/. Use when asked
  to "run the brief," "scan newsletters," "check the inbox," or "daily brief."
---

Run today's CPG intelligence brief for Seurat — newsletters + Twitter.

**INBOX:** duncanfisherhq@gmail.com via Gmail MCP
**TWITTER:** bird CLI (authenticated via browser cookies)
**WRITES TO:** C:/Users/NickFisher/Dropbox (Personal)/Nick's Personal Dropbox (Nickfisher518@gmail.com)/seurat-brain/Intelligence/
**LOGS TO:** seurat-brain/Intelligence/_inbox-log.md

---

**Step 0 — Check run state**
Read `seurat-brain/Intelligence/_last-run.md`. This file tracks when the brief last ran.

- If `last_run` is today: announce "Brief already ran today at [time]. Switching to late-check mode." In late-check mode, only scan for newsletters arriving AFTER the logged time. Skip Twitter (already scanned).
- If `last_run` is yesterday: normal run. Twitter scan window = last 48 hours.
- If `last_run` is 2+ days ago (weekend/gap): announce "Gap detected — last run was [date]. Expanding scan window." Set Twitter scan window to cover the full gap (all days since last run). Pull extra tweets if needed (--count 30 for Tier 1).
- If `_last-run.md` doesn't exist: first run. Create the file at the end.

---

**Step 1 — Scan newsletter inbox**
Connect to duncanfisherhq@gmail.com via Gmail MCP. Retrieve all unread emails. Keep only emails from known CPG newsletter sources (check seurat-brain/Intelligence/_sources.md for the newsletter list). Skip everything else: account alerts, security notices, product signups, Twitter digests, social notifications.

**Web-fetch fallback:** If a newsletter body is empty, scrambled, or <100 characters after extraction:
1. Check the snippet/headers for a "Read Online" or "View in Browser" URL
2. If found, use `WebFetch` to pull the web version and extract full content
3. Process the web version content instead
4. Log in _inbox-log.md: "(web-fetch fallback)"
This specifically addresses Progressive Grocer's broken HTML template, but applies to any newsletter with rendering issues.

**Missing source detection:** After scanning the inbox, compare today's sources against `_sources.md`. For each SUBSCRIBED source with a daily expected cadence:
- If no edition received today AND none received for 2+ consecutive business days, flag it in the daily brief under "System Health" with suggested action (check spam, re-subscribe, check if cadence changed).
- Update the "Last Received" column in `_sources.md`.

---

**Step 1.5 — Scan Twitter sources**
Using `bird` CLI, pull recent tweets from curated CPG Twitter accounts listed in seurat-brain/Intelligence/_sources.md under the "Twitter Sources" section. **Check the tier assignments and yield notes in _sources.md** — tiers are adjusted after each scan based on signal quality.

**Scan window:** Use the gap calculation from Step 0. Normal run = last 48 hours. Gap run = all days since last_run.

**Tier 1 accounts (scan every day):**
Pull the last 20 tweets from each Tier 1 account using `bird user-tweets @handle --count 20`. (Use --count 30 if gap run.)

**Tier 2 accounts (scan Mon/Wed/Fri only):**
Pull the last 10 tweets from each Tier 2 account using `bird user-tweets @handle --count 10`.

**Tier 3 accounts:** Skip unless user requests or a major industry event is happening (e.g., Expo West, CAGNY, earnings season).

**Filtering rules:**
- Keep only tweets with extractable CPG intelligence: deals, funding rounds, product launches, distribution wins, M&A, category data, strategic commentary with specifics
- Skip: retweets of content already captured from newsletters, personal commentary without CPG substance, event promos without news, political takes, AI/tech commentary not specific to CPG
- When a tweet links to an article that a newsletter also covered, note the overlap but don't double-count the insight
- Attribute Twitter insights as: `**[Twitter @handle — YYYY-MM-DD]**`
- **ALWAYS capture the tweet URL** (the `🔗 https://x.com/...` line from bird output) for every qualifying tweet. Include it in the daily brief and topic files so the newsletter can link directly to the source tweet.

**Signal yield tracking:** After each scan, mentally note how many tweets from each account produced extractable insights vs. total pulled. If an account consistently yields <15% extractable CPG signal, flag it for demotion in _sources.md at end of run.

---

**Step 2 — Process all sources (newsletters + Twitter)**
For each qualifying newsletter email AND each qualifying Twitter insight:
- Extract all meaningful insights: stats, brand news, trends, retail moves, innovation launches, data points
- Classify each insight by topic: market-trends / category-dynamics / brand-moves / retail-channel / consumer-behavior / innovation / data-points
- Check seurat-brain/Intelligence/active-projects.md for the active client list. Tag any mention of a Seurat client with `[CLIENT BRAND]`
- Append insights to the relevant file in: seurat-brain/Intelligence/topics/[topic].md
- Format: `**[Source Name — YYYY-MM-DD]**` header, then bullet points
- For Twitter: use `**[Twitter @handle — YYYY-MM-DD]** ([tweet link](https://x.com/...))` format — always include the direct tweet URL

**Deduplication rule:** If a Twitter account and a newsletter both report the same story (e.g., @cpgwire tweet + CPG Wire newsletter), file it once under the newsletter source. Only file the Twitter version if it contains additional context, data, or commentary not in the newsletter.

---

**Step 3 — Write the daily brief**
Save to: seurat-brain/Intelligence/daily-briefs/[TODAY'S DATE].md

Structure:
1. **Signal count** — X newsletters processed, Y Twitter accounts scanned, Z total insights extracted
2. **Top stories** — 3-5 highest-signal items with 2-sentence context each (cite source — newsletter or Twitter handle)
3. **Active project connections** — which Seurat client brands appeared today and what was said (label source type: "From newsletters ([Source], [date]): ..." or "From Twitter (@handle, [date]): ...")
4. **Strategic implications** — map today's signals to Seurat opportunities. For each notable signal, identify: relevant clients (from active-projects.md), selling area (Category Vision, Growth Strategy, Brand Strategy, etc.), and a concrete action or question for the team. Also check BD/Pipeline.md for prospect relevance and Intelligence/GrowthPapers/_pipeline.md for paper ideas. This is the "so what" layer — not just what happened, but what Seurat should do about it.
5. **Data points** — specific stats worth keeping, cited with source + date
6. **Emerging patterns** — scan the last 5 daily briefs in seurat-brain/Intelligence/daily-briefs/. What signals are repeating? Note them here.
7. **Open questions** — things worth watching based on today's intel
8. **Twitter-only signals** — insights that appeared on Twitter but NOT in any newsletter (early signals worth watching for newsletter confirmation)
9. **System health** — newsletter delivery status, missing sources, rendering issues, subscription actions needed

---

**Step 4 — Update hot signals**
Check seurat-brain/Intelligence/_hot-signals.md. If any signal from today has appeared 3+ times across recent briefs, add or update its entry. Twitter sources count toward the 3+ threshold the same as newsletters.

---

**Step 5 — Log and update state**
Add one row per processed newsletter to seurat-brain/Intelligence/_inbox-log.md:
| Date | Source | Subject | Insights filed | Client brands flagged | Daily Brief |

Add one summary row for all Twitter sources processed:
| Date | Twitter Scan | [X accounts scanned, Y yield] | [Z insights filed] | [Client brands if any] | Daily Brief |

**Update run state:** Write to `seurat-brain/Intelligence/_last-run.md`:
```
last_run: [ISO timestamp]
newsletters_processed: [count]
twitter_accounts_scanned: [count]
insights_filed: [total count]
brief_file: daily-briefs/[TODAY].md
```

**Update source tracking:** Update the "Last Received" column in `_sources.md` for each newsletter that delivered today.

---

**Step 6 — Calibrate Twitter sources (ongoing)**
After logging, review signal yield from this run:
- Update the "Yield (last scan)" column in _sources.md for each scanned account
- If any account yielded <15% extractable CPG signal for 2+ consecutive scans, demote it one tier
- If any account yielded >50% and is in Tier 2 or 3, flag it for promotion
- Add a dated note to the Signal Quality Notes section with any observations
- Watch for new accounts that appear frequently in QTs/RTs from high-yield sources — flag as candidates to add
