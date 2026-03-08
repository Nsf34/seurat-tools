# Seurat Brain v2 — Complete Build Playbook

## Design Principles

These govern every decision in this plan:

1. **Three-layer architecture.** Knowledge (brain folder in Dropbox, syncs to everyone) + Execution (skills in GitHub plugin, installed via Cowork — Claude's desktop app for project-based AI sessions) + Interaction (Cowork sessions pointed at brain folder with plugin installed). Each layer distributes independently.

2. **Provenance tracking.** Every piece of knowledge traces to its source. "Observed in Henkel Hair Care WS1, Feb 2026" beats "Seurat has found that..." Confidence comes from attribution.

3. **Retrieval-first file design.** File names are searchable queries. Headers are Grep-friendly. Content is structured so Claude finds the right file on the first search, not the third.

4. **Anti-hallucination by design.** Every structural choice minimizes Claude making things up: explicit "I don't know" instructions, source citations on factual claims, "Open Questions" sections that mark known unknowns, temporal markers on time-sensitive information.

5. **Cross-referencing as a first-class feature.** Files reference each other explicitly: `see: patterns.md#P12`, `related: clients/henkel.md`, `evidence: clients/unreal-snacks.md, clients/bellring-brands.md`. This creates a navigable knowledge graph, not isolated documents.

   Convention: `see: filename.md#SECTION` references are grep-friendly markers, not clickable links. Claude finds them by searching for the section header (e.g., `### P12` in patterns.md). Use descriptive section headers that Grep can match.

6. **Quality gates between phases.** No phase starts until the previous phase passes validation. Validation = specific test scenarios with expected outcomes.

7. **Skills are detailed specifications, not prompts.** The v1 survey-mapper is 727 lines of exact logic. That's the bar. A skill that says "help the user with surveys" is worthless. A skill that specifies every variable resolution chain, consistency check, and output format is valuable.

---

## Architecture

```
LAYER 1: KNOWLEDGE (Dropbox — syncs automatically)
seurat-brain-v2/
  CLAUDE.md                    ← Routing table (120-150 lines)
  .claude/                          ← NOTE: Dropbox may not sync dotfolders reliably on Windows
    commands/                  ← Slash commands (/daily-brief, /curation, /meeting-notes, /survey-map, /survey-path, /test-plan, /survey-doc)
    settings.local.json        ← Project-level permissions
  knowledge/
    processes/                 ← "How do I do X?"
    project-types/             ← "What is a Category Vision project?"
    patterns.md                ← Cross-client patterns with provenance
    lessons.md                 ← Operational lessons with source engagements
    survey-patterns.md         ← Reusable survey questions, scales, response options, flow templates by type/category
  clients/
    _index.md                  ← Master list (status, projects, themes)
    [client].md                ← Individual profiles
  bd/
    selling-playbook.md        ← Proof points, re-sell patterns, audience angles
    pipeline.md                ← Active prospects
  intelligence/
    themes/                    ← Cross-client strategic clusters
    signals/                   ← Daily brief outputs
    sources.md                 ← Newsletter + Twitter config
  skills/                      ← Skill specs (master copies — Wave 6 writes here, then copied to plugin)
    meeting-notes/             ← SKILL.md + references/
    survey-mapper/             ← SKILL.md + references/
    test-path-generator/       ← SKILL.md + references/
    test-plan-assembler/       ← SKILL.md + references/
    survey-wireframe-to-doc/   ← SKILL.md + references/
  _scripts/                    ← Scanning, extraction, synthesis tools
    digestion_engine.py        ← Dropbox API scanner + extractor + content hash registry
    brain_health.py            ← Cross-reference checker, staleness monitor
    requirements.txt           ← Dependencies (dropbox, python-pptx, python-docx, pdfminer.six, openpyxl)
    .env                       ← DROPBOX_ACCESS_TOKEN (gitignored, not synced)
    output/                    ← Extraction outputs, scan results, progress tracking
      content_registry.db      ← SQLite: content hashes, extraction status, file metadata
  _docs/                       ← Setup guides, architecture spec
  _build/                      ← Build planning (removed after launch)

LAYER 2: EXECUTION (GitHub plugin — installed in Cowork)
seurat-group/seurat-tools/
  .claude-plugin/
    plugin.json                ← Plugin manifest
  skills/
    meeting-notes/             ← SKILL.md + references/
    survey-mapper/             ← SKILL.md + references/
    test-path-generator/       ← SKILL.md + references/
    test-plan-assembler/       ← SKILL.md + references/
    survey-wireframe-to-doc/   ← SKILL.md + references/
  commands/
    meeting-notes.md           ← /seurat:meeting-notes
    survey-map.md              ← /seurat:survey-map
    survey-path.md             ← /seurat:survey-path
    test-plan.md               ← /seurat:test-plan
    survey-doc.md              ← /seurat:survey-doc

LAYER 3: INTERACTION (Cowork pointed at brain folder + plugin installed)
Cowork is Claude's desktop application for project-based AI sessions — think of it as ChatGPT but pointed at a specific folder.
- User opens Cowork → creates project at brain folder path
- Installs seurat-tools plugin
- Claude reads CLAUDE.md, knows what it has, how to behave
- User asks questions or invokes skills
```

---

## Paths

```
Brain (v2):        C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain-v2\
Old brain (ref):   C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\
Firm Dropbox:      C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Client Folder\
Public Drive:      C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Seurat Group -- Public Drive\
```

**NOTE:** All of these paths contain spaces and parentheses. Any shell command referencing them must wrap the path in double quotes, e.g. `cd "C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain-v2\"`. Unquoted paths will break on the spaces and parentheses.

---

## Execution Map

```
PART I: FOUNDATION
  Wave 1   [1 session]    Architecture + CLAUDE.md + .claude/ config + skeleton     SEQUENTIAL
  Wave 1-QG               Quality gate: session start test + routing validation

PART II: KNOWLEDGE MIGRATION
  Wave 2-A [1 session]    Migrate patterns + lessons                    ──┐
  Wave 2-B [1 session]    Migrate BD / selling intel                    ├─ ALL PARALLEL
  Wave 2-C [1 session]    Migrate client profiles (5 priority active)  ──┘
  Wave 2-QG [1 session]   Quality gate: retrieval accuracy + cross-reference integrity

PART III: PROCESS KNOWLEDGE
  Wave 3-A [1 session]    Distill research methods (quant/qual/survey)  ──┐
  Wave 3-B [1 session]    Distill deliverables + discovery + inputs     ├─ ALL PARALLEL
  Wave 3-C [1 session]    Distill PM + project types + close-out       ──┘
  Wave 3-QG               Quality gate: "new analyst" scenario test

PART IV: DATA PIPELINE (Dropbox API)
  Wave 4-A [1 session]    Verify API access + build digestion engine     SEQUENTIAL
  Wave 4-B [1 session]    Content extractor + adaptive depth             (after engine works)
  Wave 4-QG               Quality gate: test scan + extract on 1 client

PART V: DIGESTION
  Wave 5-A [1 session]    Digest active clients batch 1 (5 priority)    SEQUENTIAL
  Wave 5-B [1 session]    Digest active clients batch 2                 ──┐
  Wave 5-C [1 session]    Build theme hubs from emerged data            ├─ PARALLEL (after 5-A)
  Wave 5-QG [1 session]   Cross-client synthesis + theme + survey pattern validation

PART VI: SKILLS & PLUGIN
  Wave 6-A [1 session]    Port meeting notes skill                      ──┐
  Wave 6-B [1 session]    Port survey pipeline (4 skills)               ├─ ALL PARALLEL
  Wave 6-C [1 session]    Build GitHub plugin structure + commands      ──┘
  Wave 6-QG [1 session]   End-to-end skill testing (real inputs → real outputs)

PART VII: AUTOMATION & INTELLIGENCE
  Wave 7-A [1 session]    Daily brief system + source config            ──┐
  Wave 7-B [1 session]    Freshness monitoring + curation process       ├─ PARALLEL
  Wave 7-QG               Quality gate: daily brief + curation + health check validation

PART VIII: TESTING & DEPLOYMENT
  Wave 8-A [1 session]    Comprehensive scenario testing (all user types)
  Wave 8-B [1 session]    Setup guide + training materials + GitHub push
  Wave 8   [human work]   Pilot with 2-3 users → iterate → rollout

ONGOING                   Digestion waves, weekly curation, project close-outs

TOTAL: ~25-28 sessions + quality gates + ongoing
MAX PARALLELISM: 3 simultaneous (Waves 2, 3, 6)
```

---

## Pre-Work (Nick, 15 minutes)

1. Create `seurat-brain-v2` folder in personal Dropbox
2. Keep old `seurat-brain` intact as read-only reference
3. **Set up Dropbox API access** (required for Wave 4+):
   - Go to https://www.dropbox.com/developers/apps
   - Create app → "Scoped access" → "Full Dropbox" → name it "seurat-brain-scanner"
   - Under Permissions tab: enable `files.metadata.read`, `files.content.read`, `sharing.read`
   - Under Settings tab: generate an access token (or set up OAuth refresh token for long-lived access)
   - Save the token — you'll add it to a `.env` file in Wave 4
   - **Why API instead of local sync:** Processing 2TB through local sync requires constant disk space management, is slow to sync, and can be inaccurate. The API lets us download one file at a time, process it, delete the temp copy, and move on — zero disk pressure, content hash tracking to never re-process unchanged files, and full fidelity extraction from the actual file format.
4. Verify you can access firm Dropbox via browser (confirms your account has read access to the shared folders)

---

## Cross-Session Coordination Protocol

When running parallel sessions (up to 3 windows), agents can't talk to each other directly. Instead, they coordinate through two shared files in `_build/`:

### `_build/CONTEXT.md` — Static Context (written in Wave 1, rarely changes)
What the brain is, how it's structured, key paths, design rules. Every session reads this first.

### `_build/decisions.md` — Living Decision Log (written throughout the build)
When any session hits a fork in the road — an unexpected API behavior, a file format it didn't anticipate, a naming conflict, a pattern that changes assumptions for other waves — it writes the decision and rationale here. The next session reads it and adapts.

**Format:**
```
# Build Decisions Log

## [YYYY-MM-DD] Wave [N] — [Short Title]
**Context:** [What was encountered]
**Decision:** [What was decided and why]
**Affects:** [Which future waves or files need to know]
**Action needed:** [none / Wave X needs to adjust Y / Nick should review]
```

**Examples of what gets logged:**
- "Dropbox API namespace requires `with_path_root()` — all API calls must use this pattern"
- "Henkel has 3 separate client folders (Henkel, Henkel Hair Care, Henkel Beauty) — merged into one profile"
- "patterns.md hit 20KB at 42 patterns — splitting into patterns-strategic.md and patterns-operational.md"
- "Old brain's qual-research.md has contradictory cost benchmarks — used most recent numbers, flagged for Nick"
- "PPTX extraction misses SmartArt text — logged as known limitation, affects content depth scoring"

**Rules:**
1. **Read before starting.** Every session reads `_build/decisions.md` before doing any work. If a previous session made a decision that affects your wave, adapt.
2. **Write when you hit a fork.** Don't just silently make a choice — log it so parallel and future sessions can see it.
3. **Never overwrite.** Append only. Newest entries at the bottom.
4. **Tag what's affected.** Always note which waves, files, or sessions need to know.
5. **Flag for Nick.** If the decision is judgment-call territory (not a technical fork), flag it for Nick's review rather than deciding unilaterally.
6. **WRITE BOUNDARIES.** Parallel sessions must only write to their own designated output files. Cross-references to files owned by other parallel sessions should use placeholder format `see: patterns.md#P[TBD]` — these are resolved in the quality gate session that follows. Never edit a file that another parallel session is actively building.

**This replaces inter-agent messaging.** The parallel sessions in this plan are designed to be independent (Wave 2-A doesn't need 2-B's output). But when reality diverges from plan — and it will — `decisions.md` is how sessions stay in sync without needing to talk to each other in real time.

---

## PART I: FOUNDATION

### Wave 1 — Architecture + CLAUDE.md + Configuration (1 session, SEQUENTIAL)

```
You are building "Seurat Brain v2" — a firm-wide knowledge system for Seurat Group, a CPG/retail strategy consulting firm (~15 people). This is the foundational session. Every future session depends on this being right.

FIRM CONTEXT:
- CPG/retail strategy consulting. ~15 people (partners, EMs, analysts).
- Methods: quant surveys, qual interviews, discovery/competitive analysis, category vision, segmentation, brand architecture.
- Clients: large CPG (Henkel, Pepsi, Ocean Spray), growth-stage (Unreal Snacks, Liquid IV), PE-backed (Tropicana, Elida Beauty), non-CPG (Merck, Vizio).
- 545 historical clients, ~20-30 active at any time. ~2TB of project files in firm Dropbox.
- Currently active: Henkel, Merck, Bolton, Pennington, Nielsen-Massey.

SYSTEM DESIGN:
- Three layers: Knowledge (Dropbox folder) + Execution (GitHub plugin with skills) + Interaction (Cowork sessions)
- Knowledge layer = this brain folder. Flat markdown files optimized for Claude to search and read.
- Execution layer = separate GitHub repo with skills (meeting notes, survey pipeline). Installed as Cowork plugin.
- CLAUDE.md at root = routing table telling Claude what exists and how to behave. Auto-loaded on session start.
- Nick Fisher is sole curator. Everyone else reads. Knowledge enters through migration, digestion of Dropbox files, weekly curation, and project close-outs.

PATHS:
- Brain (v2): C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain-v2\
- Old brain (read-only reference): C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\
- Firm Dropbox: C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Client Folder\

BEST PRACTICES TO FOLLOW:
- Provenance: every knowledge file notes its source (which project, which file, when extracted)
- Cross-references: files link to each other explicitly using "see: filename.md" or "related: filename.md" conventions
- Temporal markers: time-sensitive facts include "as of [date]"
- Confidence levels: observations include how many clients they've been seen across
- Anti-hallucination: CLAUDE.md explicitly instructs Claude to say "I don't know" rather than guess
- Retrieval-first naming: file names should be searchable (kebab-case, descriptive)

YOU HAVE FIVE TASKS:

--- TASK 1: Read the old brain's architecture for reference ---

Read these files from the old brain to understand what worked:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\CLAUDE.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\.claude\settings.local.json
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\.claude\commands\daily-brief.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\_meta\AI-INTEGRATION-PLAN.md

Take note of: CLAUDE.md structure (175 lines, trimmed from 300+), permissions model, command format, plugin architecture. Learn from what v1 did well and what it did poorly.

--- TASK 2: Create _build/CONTEXT.md and _build/decisions.md ---

CONTEXT.md — 30-40 lines. Future build sessions read this for context. Contents:
- What the brain is and who it's for (3 lines)
- Three-layer architecture summary (5 lines)
- Folder structure with one-line descriptions (15 lines)
- Three key paths (brain, old brain, firm Dropbox)
- Design rules: no hardcoded paths, all markdown, files under 15KB, provenance on all knowledge, cross-references between files, temporal markers on time-sensitive facts
- Currently active clients: Henkel, Merck, Bolton, Pennington, Nielsen-Massey
- Final line: "IMPORTANT: Also read _build/decisions.md before starting work. It contains decisions made by previous sessions that may affect yours."

decisions.md — Initialize with:
# Build Decisions Log
Entries are appended by each build session. Read this BEFORE starting work. Write here when you encounter unexpected situations, make judgment calls, or discover something that affects other waves.
[empty — entries will be added as the build progresses]

--- TASK 3: Write CLAUDE.md ---

This is the brain's self-awareness. 120-150 lines. Claude reads it at session start and knows everything it has access to and how to behave.

The old brain's CLAUDE.md was 175 lines and included firm terminology, skill maps, folder structure, file naming conventions, and working principles. That's the right scope. But v2 needs to be cleaner and follow these principles:

SECTION 1 — IDENTITY (5 lines)
You are the Seurat Brain — institutional knowledge system for Seurat Group.
Explain what Seurat does (CPG/retail strategy consulting) in 2 sentences.
Explain what the brain contains (process knowledge, client intelligence, cross-client patterns, strategic frameworks, BD intelligence).

SECTION 2 — FIRM TERMINOLOGY (10 lines)
Define terms a new team member wouldn't know:
- Campfire = quarterly all-hands meeting
- WS / Workshop = interim deliverable presentation (WS1, WS2)
- KO = kickoff meeting
- Shareout = internal team presentation
- 5 Cs = Consumer, Category, Company, Competition, Channel/Customer (discovery framework)
- Typing Tool = mechanism to classify new consumers into existing segments
- Demand Space = consumption occasion framework
- PDH = PowerPoint Data Handler (Q Research integration)
- Any other firm-specific terms from the old brain's CLAUDE.md

SECTION 3 — SESSION START (8 lines)
When a user starts a conversation:
- Ask: "Who are you and what are you working on?"
- Read clients/[client].md for their client context
- Read knowledge/project-types/[type].md for engagement type context
- If the client doesn't have a profile: "The brain doesn't have a profile for [Client] yet. I can still help based on general process knowledge. Want me to flag this gap for curation?"
- Never fabricate client details, stakeholder names, project history, or financial data. If you don't know, say so.

SECTION 4 — FOLDER MAP (20 lines, one per folder/key file)
Each line: folder or file path + what's inside + when to search here
Example:
  knowledge/processes/ — Step-by-step guides for every method (quant, qual, survey, discovery, deliverables, PM). Search when someone asks "how do I do X?"
  knowledge/patterns.md — 30-50 cross-client patterns with provenance and evidence. Search when starting new projects, diagnosing problems, or looking for precedent.
  clients/_index.md — Master client list. Search FIRST when someone mentions any client name.
  bd/selling-playbook.md — Proof points, re-sell patterns, audience angles. Search for BD/selling questions.
  intelligence/themes/ — Cross-client strategic clusters. Search when looking for thematic connections across clients.

Cover every folder in the architecture.

SECTION 5 — SEARCH BEHAVIOR (8 lines)
- ALWAYS search before answering questions about clients, processes, or strategy. Use Grep to search file contents and Glob to find files by name.
- Search clients/_index.md FIRST for any client mention — it tells you if a profile exists.
- When citing information, reference the source file: "According to clients/henkel.md..." or "Pattern #12 in patterns.md describes..."
- If you find conflicting information across files, flag it: "patterns.md says X but clients/unreal-snacks.md says Y — which is current?"
- For questions the brain can't answer, check the firm Dropbox for raw project files: C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Client Folder\[Client]\

SECTION 6 — KNOWLEDGE ACCUMULATION (8 lines)
- When a conversation reveals new information (a project update, a new insight, a correction to existing knowledge), flag it:
  "This seems like something the brain should capture. Want me to draft an update for [file]?"
- When someone mentions a project is ending: prompt for close-out capture.
  "Want to do a quick close-out? I'll ask a few questions and draft updates for the client profile and patterns."
- Never write to brain files without user approval. Draft updates, show them, get confirmation.
- For all updates, include provenance: what was the source of this information? When was it current?

SECTION 7 — SKILLS & COMMANDS (10 lines)
List available slash commands and skills with trigger phrases.
For v2 launch, these will be:
- /daily-brief — scan newsletters + Twitter for intelligence signals
- /curation — guided weekly brain curation session
- Skills (via seurat-tools plugin): meeting-notes, survey-mapper, test-path-generator, test-plan-assembler, survey-wireframe-to-doc
- For each: one-line description + trigger phrase ("Use when the user says 'I just got off a call with...' or provides a transcript")

SECTION 8 — WORKING PRINCIPLES (6 lines)
- Specific over generic. Reference actual client examples, pattern numbers, lesson numbers.
- Evidence over opinion. Cite what the brain actually contains, not general consulting advice.
- Honest about gaps. Missing knowledge is better than fabricated knowledge.
- Provenance matters. Always note where information comes from and when it was current.
- The brain grows through use. Every conversation is an opportunity to capture new knowledge.
- Keep individual knowledge files under 15KB. If a file grows beyond this, split it into focused sub-files and update cross-references.

SECTION 9 — PATHS (5 lines)
- Brain root: [this folder]
- Firm Dropbox client work: C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Client Folder\
- Firm Dropbox public drive: C:\Users\NickFisher\Seurat Group Dropbox\Nick Fisher\Seurat Group -- Public Drive\
- Do not modify files outside the brain folder. Read-only access to firm Dropbox.

--- TASK 4: Create .claude/ configuration ---

NOTE: Dropbox on Windows may not sync dotfolders (folders starting with ".") reliably — it may silently skip them or cause sync conflicts. This is fine because .claude/ config is only needed on Nick's machine (the sole curator), not on readers' machines. If Dropbox strips the .claude/ folder, Nick can simply re-add it locally.

Create: .claude/settings.local.json
Base on old brain's permissions, adjusted for v2:
{
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(find:*)",
      "Bash(python:*)",
      "Bash(pip:*)",
      "Bash(MSYS_NO_PATHCONV=1 python:*)",
      "WebSearch",
      "mcp__claude_ai_Gmail__gmail_get_profile",
      "mcp__claude_ai_Gmail__gmail_search_messages",
      "mcp__claude_ai_Gmail__gmail_read_message"
    ]
  }
}

NOTE: Claude Code's built-in tools (Read, Edit, Glob, Grep, Write, Agent) are allowed by default and do not need to be listed here. Only Bash commands (which are sandboxed) and external MCP tools need explicit permission entries.

Create: .claude/commands/ folder (empty — commands added in later waves)

--- TASK 5: Create the folder skeleton ---

Build the complete folder structure. For each folder, create a brief _README.md (2-3 lines) explaining what goes there. This helps Claude understand the structure even when folders are empty.

seurat-brain-v2/
  CLAUDE.md                          [written above]
  _build/
    CONTEXT.md                       [written above]
    decisions.md                     [initialize with header — see Cross-Session Coordination Protocol]
  _scripts/
    _README.md                       "Scanning, extraction, and synthesis scripts for digesting firm Dropbox content."
    output/                          (extraction outputs land here)
  _docs/
    _README.md                       "Setup guides, training materials, architecture documentation."
  .claude/
    settings.local.json              [written above]
    commands/
  knowledge/
    _README.md                       "Process knowledge, project types, patterns, lessons, markets. The 'how we do things' layer."
    processes/
    project-types/
    patterns.md                      [stub with header "# Cross-Client Patterns" + "(populated in Wave 2)" — Wave 2]
    lessons.md                       [stub with header "# Operational Lessons" + "(populated in Wave 2)" — Wave 2]
    survey-patterns.md               [stub with header "# Survey Pattern Library" + "(populated during Wave 5 digestion)" — Wave 5]
  clients/
    _README.md                       "Client profiles and index. The 'who we work with' layer."
    _index.md                        [stub with header "# Client Index" + "(populated in Wave 2)" — Wave 2]
  bd/
    _README.md                       "Business development intelligence. The 'how we sell' layer."
    selling-playbook.md              [stub with header "# Selling Playbook" + "(populated in Wave 2)" — Wave 2]
    pipeline.md                      [stub with header "# BD Pipeline" + "(populated in Wave 2)" — Wave 2]
  intelligence/
    _README.md                       "External intelligence, thematic clusters, and market signals."
    themes/
    signals/
    sources.md                       [empty — Wave 7]

After creating everything, verify: open a fresh Cowork window pointed at the brain-v2 folder. Confirm CLAUDE.md loads. Ask Claude "what do you know?" and verify it routes correctly to the folder map. Report any issues.
```

### Wave 1 Quality Gate

After Wave 1, test these scenarios in a fresh Cowork session pointed at the brain:

| Test | Expected | Pass? |
|------|----------|-------|
| Session start | Claude asks who you are and what you're working on | |
| "What do you have?" | Claude describes the folder structure from CLAUDE.md | |
| "Tell me about Henkel" | Claude searches clients/, finds nothing yet, says so honestly | |
| "How do quant research work?" | Claude searches knowledge/processes/, finds nothing yet, says so | |
| "What patterns exist?" | Claude reads patterns.md, finds it empty, says so | |

All 5 must pass before proceeding to Wave 2.

---

## PART II: KNOWLEDGE MIGRATION

### Wave 2-A — Migrate Patterns + Lessons (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you encounter anything unexpected (contradictions in source data, files too large, naming conflicts, ambiguous content), append a dated entry to _build/decisions.md before proceeding. Tag which waves/files are affected.

YOUR TASK: Migrate cross-client patterns and operational lessons from v1 brain into v2.

SOURCE FILES — read FULLY before writing anything:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Frameworks\patterns.md (~141KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Frameworks\lessons-learned.md (~87KB)

These are the most valuable files in the entire old brain. Handle them with care.

MIGRATION PROCESS FOR PATTERNS:

Review every single pattern. Apply these criteria:

KEEP if:
- Backed by specific client evidence (named engagement, named outcome)
- Observed across 2+ clients (not a single-client anecdote)
- Would change how someone scopes, sells, or executes an engagement
- Contains a "default approach" — what Seurat does when it sees this

SHARPEN if:
- Real insight but vaguely written
- Missing client examples or dates
- "Default approach" is generic

MERGE if:
- Two patterns describe the same dynamic from different angles
- Combining them creates a stronger, more nuanced pattern

CUT if:
- Surface-level observation ("clients like data-driven recommendations")
- Generic consulting advice not specific to Seurat
- Single-client anecdote that doesn't generalize
- Contradicted or retracted

For each surviving pattern, write:

### P[N]: [Descriptive Name]
**Confidence:** strong (5+ clients) | moderate (3-4 clients) | emerging (2 clients)
**First observed:** [Client], [engagement type], [approximate date]
**Also observed in:** [Client 1 — brief context], [Client 2 — brief context]
**What it is:** [2-3 sentences — specific, not generic. What does this dynamic look like in practice?]
**Why it matters:** [How this affects scoping, selling, or execution at Seurat]
**Default approach:** [What Seurat does when it encounters this — specific enough to act on]
**Related:** [Cross-references to other patterns, lessons, client profiles, or themes]
  see: lessons.md#L[N] (if related lesson exists)
  see: clients/[client].md (if detailed example exists)
  see: intelligence/themes/[theme].md (if connects to a theme)

Write to: knowledge/patterns.md

Add a header:
# Cross-Client Patterns
Last curated: [today's date]
Source: Migrated from v1 brain Intelligence/Frameworks/patterns.md, curated during v2 build.
Total patterns: [N]

MIGRATION PROCESS FOR LESSONS:

Same review process. Criteria:

KEEP if:
- Specific post-mortem from a real engagement (named client, named situation)
- Has an actionable fix (not just "be more careful")
- The fix has been validated or at least attempted

CUT if:
- Generic advice
- Unverified (archive-mined without confirmation)
- Retracted (the file already has at least one retraction)

For each surviving lesson:

### L[N]: [Descriptive Name]
**Source:** [Client], [engagement], [approximate date]
**What happened:** [The specific situation — 2-3 sentences with enough detail to recognize it if you see it again]
**What we learned:** [The insight — one sentence]
**The fix:** [What to do differently — specific and actionable enough that a new analyst can follow it]
**Status:** confirmed (fix has been applied successfully) | provisional (fix proposed but not yet tested) | retracted (found to be wrong)
**Related:** see: patterns.md#P[N], see: clients/[client].md

Write to: knowledge/lessons.md

Add header:
# Operational Lessons
Last curated: [today's date]
Source: Migrated from v1 brain Intelligence/Frameworks/lessons-learned.md, curated during v2 build.
Total lessons: [N]

MIGRATION LOG (bottom of each file):

## Migration Log
- Source file: [full path]
- Source count: [N] patterns/lessons in original
- Migrated: [N] (kept or sharpened)
- Merged: [N] — [which ones merged with which]
- Cut: [N] — [1-line reason per cut]
- Flagged for Nick: [anything ambiguous, contradictory, or uncertain]

QUALITY BAR: 35 razor-sharp patterns > 74 mixed ones. Every surviving pattern should pass: "Would reading this change how I approach a new engagement?" If no, cut it.
```

### Wave 2-B — Migrate BD / Selling Intelligence (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you encounter anything unexpected, append a dated entry to _build/decisions.md before proceeding. Tag which waves/files are affected.

YOUR TASK: Migrate business development and selling intelligence from v1 brain into v2.

SOURCE FILES — read ALL before writing:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\BD\BD-dashboard.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\BD\Pipeline.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\BD\target-roster.md
- Search and read everything in: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\BD\Selling\
- Search and read everything in: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\BD\ (all .md files)

Also read for cross-referencing:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Frameworks\patterns.md (selling patterns reference these)

OUTPUT 1: bd/selling-playbook.md

This is what a partner opens before a BD call. It needs to be a weapon, not a document.

Structure:

# Selling Playbook
Last curated: [today's date]
Source: Migrated from v1 brain BD/ folder, curated during v2 build.

## The Seurat Pitch
Preserve EXACT phrasing from old brain — these were refined through real BD conversations.
- **10-second:** [exact line]
- **30-second:** [exact paragraph]
- **2-minute:** [exact script]

## Selling Areas
For each area (~7 in old brain):
### [Area Name]
**What it is:** [1-2 sentences]
**Typical client:** [profile]
**Door openers:** [what triggers the conversation — specific situations, not generic "when they need strategy"]
**Proof points:**
- [Client 1]: [specific outcome — named, with data if available]
- [Client 2]: [specific outcome]
  see: clients/[client].md for full context
**Winning patterns:** [what makes Seurat win vs. competitors in this space]
**Related patterns:** see: patterns.md#P[N]

## Re-Sell Patterns
For each pattern (~7 in old brain):
### [Pattern Name] (e.g., "Segmentation → Category Expansion")
**The pattern:** [what happens and why]
**Client evidence:** [which clients followed this path]
**Timing:** [when to pitch the follow-on — how many months after initial engagement?]
**The line:** [actual pitch language that has worked]
**Related:** see: clients/[client].md, see: patterns.md#P[N]

## Non-Converts (Honest Analysis)
For each (~7 in old brain):
### [Company]
**What happened:** [the situation]
**Why it didn't close:** [honest analysis — not excuses]
**The lesson:** [what to watch for in similar prospects]
**Red flags to recognize:** [specific signals that indicate this type of non-convert]

## Audience Angles
For each buyer type (CMO, CSO, Founder, PE, Insights VP, non-CPG):
### [Audience]
**What they care about:** [their priorities]
**Seurat's angle:** [how to position]
**Proof points to lead with:** [which from above]
**What NOT to say:** [common positioning mistakes for this audience]

OUTPUT 2: bd/pipeline.md

# BD Pipeline
Last updated: [today's date]

| Prospect | Status | Last Touch | Opportunity | Selling Area | Hook | Next Action |
|----------|--------|------------|-------------|--------------|------|-------------|

Status: active / awaiting-response / re-engage / cold / closed-lost
Selling Area: reference selling-playbook.md section names

Consolidate from BD-dashboard.md and Pipeline.md. Remove duplicates. Flag stale (>60 days no response with no clear reason to keep).

Cross-references:
- Each prospect should note: "Related theme: see intelligence/themes/[theme].md" where applicable
- Each prospect should note: "Similar to: [non-convert name]" if the profile matches a known non-convert pattern

QUALITY BAR: A partner reading the selling playbook before a cold call should know exactly what to say, which proof points to drop, which audience angle to use, and what red flags to watch for. If a section doesn't make someone measurably better at selling, cut it.
```

### Wave 2-C — Migrate Client Profiles (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you encounter anything unexpected (duplicate client folders, ambiguous client names, profiles that contradict patterns.md), append a dated entry to _build/decisions.md before proceeding. Tag which waves/files are affected.

YOUR TASK: Build the client index and migrate the most valuable client profiles from v1 into v2.

PRIORITY ACTIVE CLIENTS (must get full profiles regardless of old brain depth):
- Henkel
- Merck
- Bolton
- Pennington
- Nielsen-Massey

STEP 1: Read ALL client profiles from old brain.
Search: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Clients\
Find all _profile.md files. Read each one. Categorize:
- PRIORITY: the 5 listed above — full profile in v2 no matter what
- DEEP (>5KB substantive content): full profile in v2
- THIN (1-5KB, some useful info): condensed entry in index + minimal profile
- EMPTY (<1KB or stub): one-line entry in index only

STEP 2: Build the client index.
Write: clients/_index.md

# Client Index
Last updated: [today's date]
Total clients: [N] | Active: [N] | Lapsed: [N] | Prospect: [N]

| Client | Status | Category | Active Projects | Engagement History | Themes | Profile |
|--------|--------|----------|-----------------|-------------------|--------|---------|

Status: active / lapsed / prospect / archive
Category: Large CPG / Growth-Stage / PE-Backed / Non-CPG
Active Projects: current engagement names or "—"
Engagement History: brief summary (e.g., "3 projects, 2019-2026" or "1 project, 2024")
Themes: tags linking to intelligence/themes/ (e.g., protein, glp-1, channel-fragmentation)
Profile: "yes" with link / "minimal" / "index-only"

Include EVERY client from old brain. This is the brain's answer to "have we ever worked with X?"

STEP 3: Create individual client profiles.
For each PRIORITY and DEEP client, create: clients/[client-name].md

Kebab-case filenames (henkel.md, bellring-brands.md, ocean-spray.md).

Profile structure:

# [Client Name]
Last updated: [today's date]
Source: Migrated from v1 brain, curated during v2 build.
Status: active | lapsed | prospect

## Company
[What they do, size, ownership, category] — 3-4 lines max. Only include what's useful for understanding the strategic context. Don't repeat what anyone could Google.

## Relationship
[When Seurat started working with them. Key milestones. Current relationship status. Who owns the relationship internally.]

## Projects
For each project (current first, then historical):

### [Project Name] ([Type], [Year], [Status])
- **Scope:** What was the strategic question?
- **Methods:** What research methods were used?
- **Key findings:** [2-4 bullets — the actual insights, not generic summaries]
- **Outcome:** What was delivered? What happened next? Did it lead to follow-on work?
- **Team:** [Seurat team members if known]
- **Related:** see: knowledge/project-types/[type].md, see: patterns.md#P[N] if relevant

## Key Stakeholders
[Client-side contacts — name, title, role in decision-making. Only include named people from old brain data.]
[Mark any unconfirmed information: "[unconfirmed]"]

## Strategic Context
[What's driving this client's business RIGHT NOW. Competitive dynamics. Channel situation. Growth tensions. Category trends.]
[Include temporal markers: "As of March 2026, Henkel is..."]

## What We've Learned
[Seurat-specific insights from this relationship. Not generic industry knowledge — things we know BECAUSE of working with this client.]
[Cross-reference to patterns: "This engagement exemplifies Pattern #12 (Post-Integration Corporate — Strategy as Internal Alignment). see: patterns.md#P12"]
[Cross-reference to lessons: "The demand framework iteration on this project led to Lesson #1. see: lessons.md#L1"]

## Themes
[Which thematic clusters this client connects to]
- see: intelligence/themes/[theme-1].md — [why]
- see: intelligence/themes/[theme-2].md — [why]

## Open Questions
[What we don't know. What would be valuable to find out. What gaps exist in our understanding of this client.]

STEP 4: For THIN clients, create minimal profiles with just: Company + Relationship + Projects (1-2 lines each). No stakeholders, strategic context, or learnings sections.

CROSS-REFERENCING:
After creating all profiles, go back and add cross-references:
- If a pattern references a client, add "see: clients/[client].md" to the pattern
- If a client exemplifies a pattern, add "see: patterns.md#P[N]" to the client profile
- If a client connects to a theme, add "see: intelligence/themes/[theme].md" to the client profile
- If a client connects to a BD selling area, add "see: bd/selling-playbook.md#[area]" to the profile

(Note: patterns.md and selling-playbook.md are being created in parallel sessions. Add placeholder cross-references like "see: patterns.md#P[TBD]" and fill them in during the Wave 2 quality gate.)

QUALITY BAR:
- Preserve specific data: revenue figures, market share, named stakeholders, project dates, segment sizes, cost figures
- Preserve strategic intelligence: competitive positioning, channel dynamics, internal organizational tensions
- Cut generic descriptions that anyone could Google
- Mark unconfirmed information clearly: [unconfirmed]
- A new analyst reading a profile should be able to walk into a client call informed and ask good questions
```

### Wave 2 Quality Gate (1 session)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — review ALL entries from Wave 2 sessions. Address any flagged issues or conflicts.

YOUR TASK: Validate the Wave 2 migration and fix cross-references.

STEP 1: Read all migrated files:
- knowledge/patterns.md
- knowledge/lessons.md
- bd/selling-playbook.md
- bd/pipeline.md
- clients/_index.md
- All files in clients/

STEP 2: Cross-reference integrity check
For each "see:" reference in every file:
- Does the target file exist?
- Does the target section/number exist?
- If patterns.md references clients/henkel.md, does henkel.md reference back?
Fix any broken or placeholder references.

STEP 3: Retrieval accuracy test
Open a FRESH Cowork session pointed at the brain folder. Test these queries:

| Query | Expected Behavior | Pass? |
|-------|-------------------|-------|
| "Tell me about Henkel" | Reads clients/henkel.md, summarizes accurately | |
| "What patterns should I know about for a segmentation project?" | Searches patterns.md, finds relevant patterns, cites numbers | |
| "What's in the BD pipeline?" | Reads bd/pipeline.md, summarizes prospects | |
| "Have we ever worked with Albanese?" | Searches clients/_index.md, finds the entry | |
| "What went wrong on the Henkel WS1?" | Finds lesson in lessons.md, cites source | |
| "How do we sell to PE-backed companies?" | Finds selling area in selling-playbook.md | |
| "What do Unreal Snacks and BellRing have in common?" | Cross-references both profiles, identifies shared themes/patterns | |

STEP 4: Content quality spot-check
Pick 5 random patterns and verify:
- Is the client evidence specific (named engagement, named outcome)?
- Is the "default approach" actionable (not generic)?
- Are cross-references valid?

Pick 3 random client profiles and verify:
- Are project scopes specific (not vague)?
- Are key findings actual insights (not summaries of summaries)?
- Are temporal markers present on time-sensitive information?

STEP 5: Report
Write: _build/wave2-quality-report.md
- Cross-reference issues found and fixed
- Retrieval test results (pass/fail per scenario)
- Content quality issues found
- Remaining gaps to address in future curation

Do NOT proceed to Wave 3 until all retrieval tests pass.
```

---

## PART III: PROCESS KNOWLEDGE

### Wave 3-A — Distill Research Methods (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you find contradictions in source docs, ambiguous process steps, or content that exceeds 15KB per file, append a dated entry to _build/decisions.md. Tag which waves/files are affected.

YOUR TASK: Distill Seurat's research methodology documentation from v1 brain source files into clean v2 process guides.

SOURCE FILES — read ALL thoroughly before writing:
NOTE: Large files (100KB+) may exceed the Read tool's default 2000-line window. Use offset/limit parameters to read in chunks, or use Grep to find specific sections. Read the full file even if it takes multiple reads — missing content means missing process knowledge.
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\quant-analytics.md (~100KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\qual-research.md (~108KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\survey-and-field.md (~149KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\supplemental-analytics.md (~73KB)
Also search: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\ for any other research-related docs.

These source files are 100KB+ each and were written stream-of-consciousness. Your job is DISTILLATION — extract the actionable process knowledge, cut the filler, restructure into clear guides.

Create THREE files:

1. knowledge/processes/quant-research.md
   Source: quant-analytics.md + supplemental-analytics.md
   Covering: when to use quant, study design (sample sizes, methodology), questionnaire development, fielding logistics (CINT panel, quotas, weighting), Q Research software (setup, tabs, PDH), analysis techniques, deliverable production

2. knowledge/processes/qual-research.md
   Source: qual-research.md
   Covering: when to use qual vs quant, method selection (IDI, focus group, Dscout diary, AI qual — decision criteria for each), recruitment, discussion/moderator guide creation, moderation principles, analysis frameworks, cost benchmarks by method, SME program

3. knowledge/processes/survey-fieldwork.md
   Source: survey-and-field.md
   Covering: survey design principles, wireframe creation, question type best practices (scales, grids, open-ends, carousels), piping/skip logic, programmer handoff, field management, data cleaning, weighting strategies

FILE STRUCTURE for each:

# [Process Name]
Last updated: [today's date]
Source: Distilled from v1 brain [source file name], curated during v2 build.

## When to Use This
[Decision criteria — when is this the right method? What questions does it answer?]

## The Process (Step by Step)
### Step 1: [Name]
[What to do, who does it, typical timeline, key decisions]
### Step 2: [Name]
[...]
(Continue through all steps from scoping to final deliverable)

## Tools & Vendors
[Specific software, platforms, vendors, with notes on when to use each]
[Include cost ranges where the source docs have them]

## Common Mistakes
[Real mistakes from source docs — not generic warnings. Each should be specific enough to recognize and prevent.]
- **[Mistake]:** [What happens] → **Fix:** [What to do instead]
  Source: [which engagement this lesson came from, if noted in source doc]

## Decision Guides
[Decision trees or comparison tables from the source docs]
[E.g., "IDI vs Focus Group vs Dscout" comparison matrix]

## Related
- see: knowledge/project-types/[type].md (which project types use this method)
- see: knowledge/processes/survey-fieldwork.md (if quant involves a survey)
- see: patterns.md#P[N] (if any patterns relate to this method)

DISTILLATION RULES:
- You're compressing ~430KB of source material into ~45KB (3 files × 15KB max). That's ~10:1 compression.
- KEEP: specific procedures, tool names, vendor details, cost ranges, decision criteria, named mistakes
- KEEP: anything a new analyst would need to execute the method without asking someone
- CUT: repetitive examples, tangential stories, stream-of-consciousness explanations
- CUT: obvious advice ("double-check your work")
- RESTRUCTURE: the source docs meander. Your output should be linear (step 1 → step 2 → ... → done)
- PRESERVE PROVENANCE: if a technique or mistake traces to a specific engagement, keep that attribution

After writing all three files, create a brief summary for Nick:
_build/wave3a-distillation-notes.md
- For each file: source size → output size, what was cut, what was ambiguous or contradictory in the source, what Nick should review
```

### Wave 3-B — Distill Deliverables + Discovery + Inputs (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you encounter anything unexpected, append a dated entry to _build/decisions.md before proceeding.

YOUR TASK: Distill deliverable production, discovery, and inputs review processes from v1 brain into v2 guides.

SOURCE FILES — read ALL before writing:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\pptx-slide-builder.md (~72KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\iteration-review-workflow.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\digital-discovery.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\discovery-automation.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\docx-comment-manipulation.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\docx-formatting-patterns.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Scripts\inputs-review-process.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Scripts\inputs-review-automation.md
Also search Intelligence/Process/ for any other relevant docs.

Create THREE files following the same structure as Wave 3-A (process name, when to use, step-by-step, tools & vendors, common mistakes, decision guides, related):

1. knowledge/processes/deliverable-production.md
   From: pptx-slide-builder.md + iteration-review-workflow.md + docx docs
   Cover: slide structure (headline-evidence-implication), Seurat brand spec (exact colors, fonts, layouts — pull specific values), review chain (analyst → EM → partner), comment conventions, version numbering + Old/ folders, common deck-building mistakes

2. knowledge/processes/discovery.md
   From: digital-discovery.md + discovery-automation.md
   Cover: 5 Cs framework with detail on each C, what to research and where, competitive analysis methodology, how discovery findings feed into strategy, Reddit source requirements (full permalink URL mandatory), common mistakes

3. knowledge/processes/inputs-review.md
   From: inputs-review-process.md + inputs-review-automation.md
   Cover: what inputs are, how they're organized (02 Inputs folder structure), the inputs tracker (12 columns), hero input identification criteria, synthesizing inputs into 5 Cs structure, common mistakes

Same distillation rules and provenance requirements as Wave 3-A.
Write distillation notes to: _build/wave3b-distillation-notes.md
```

### Wave 3-C — Distill PM + Project Types + Close-Out (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: If you encounter anything unexpected, append a dated entry to _build/decisions.md before proceeding.

YOUR TASK: Distill project management, build engagement type guides, and define the project close-out process.

SOURCE FILES:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Process\project-management.md (~59KB)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Frameworks\engagement-types.md (~31KB) (if this file doesn't exist or is named differently, search Intelligence/Frameworks/ and Intelligence/Process/ for any file containing engagement type definitions, project type descriptions, or methodology overviews)

Also read (created in Wave 2 — verify these exist before proceeding):
- knowledge/patterns.md
- clients/_index.md
Search Intelligence/Process/ and Intelligence/Frameworks/ for any other PM or engagement-type related docs.

Create files:

1. knowledge/processes/project-management.md
   From: project-management.md
   Cover: new project setup (Dropbox folders, tracker, team assignments), kickoff prep and execution, status tracking, milestone flow (KO → WS1 → WS2 → Final — what happens at each, what deliverables are expected), analyst development model (trainer → collaborative → trainee), Dropbox folder conventions, common PM mistakes

2. knowledge/project-types/ — ONE FILE PER TYPE
   From: engagement-types.md + patterns.md + client profiles

   For each type found in the source, create: knowledge/project-types/[type-name].md

   Structure per file:
   # [Engagement Type Name]
   Source: Distilled from v1 brain, cross-referenced with patterns and client profiles.

   ## What It Is
   [2-3 sentence definition. What question does this engagement answer?]

   ## When Clients Need This
   [What triggers this type of engagement — specific business situations, not generic "when they need help"]

   ## Typical Scope
   - Duration: [range]
   - Team: [typical composition]
   - Deliverables: [what gets produced]
   - Milestones: [KO → WS1 → WS2 → Final, or different cadence?]
   - Methods: [which from knowledge/processes/ are used]

   ## What Makes It Succeed
   [Specific success factors from Seurat's experience]

   ## What Makes It Fail
   [Specific failure modes — reference lessons.md where applicable]
   see: lessons.md#L[N]

   ## Example Clients
   [Named clients who've done this type — reference profiles]
   see: clients/[client].md

   ## What Comes Next
   [How this engagement type leads to follow-on work — reference re-sell patterns]
   see: bd/selling-playbook.md#[re-sell pattern]

   ## Related Patterns
   see: patterns.md#P[N], #P[N]

   Types to cover (pull from engagement-types.md, expect 8-12):
   - category-vision.md
   - growth-strategy.md
   - consumer-segmentation.md
   - brand-architecture.md
   - challenge-assessment.md
   - innovation-whitespace.md
   - category-expansion.md
   - retail-strategy.md
   - [any others in the source]

3. knowledge/processes/project-close-out.md — NEW PROCESS (no source doc)

   # Project Close-Out Process
   Created: [today's date]
   Status: New process — not yet tested in practice.

   ## Purpose
   Capture project learnings at engagement end so the brain grows with every project.

   ## When
   Within 1 week of final deliverable to client.

   ## Who
   Analyst + EM, 30-minute session with Claude (Cowork pointed at brain).

   ## The Session
   Claude walks through these questions:

   ### 1. Project Summary
   - What was the strategic question?
   - What did we find?
   - What did we recommend?
   - What methods worked well? What didn't?
   → Output: Update to clients/[client].md project section

   ### 2. Pattern Check
   - Read knowledge/patterns.md
   - Does this project add evidence to an existing pattern?
   - Does it reveal a new pattern not yet documented?
   → Output: Draft update to patterns.md (flagged for curation review)

   ### 3. Lessons Learned
   - What went wrong? What would we do differently?
   - What went unexpectedly well? Why?
   → Output: Draft entry for lessons.md (flagged for curation review)

   ### 4. BD Signal
   - Is there a follow-on opportunity with this client?
   - What type of engagement would it be?
   - When should we re-engage? (timing)
   → Output: Draft update to bd/pipeline.md

   ### 5. Theme Connection
   - Which thematic clusters does this project connect to?
   - Does it add evidence to an existing theme?
   → Output: Draft update to intelligence/themes/[theme].md

   All outputs are DRAFTS flagged for Nick's weekly curation review. Nothing writes to the brain automatically.

PRIORITY: If this session runs long, prioritize in this order: (1) project-management.md from source doc, (2) the 5 most common project types (category-vision, growth-strategy, consumer-segmentation, brand-architecture, challenge-assessment), (3) remaining project types, (4) project-close-out.md (can be deferred to a follow-up session since it's a new process with no source doc).

Write distillation notes to: _build/wave3c-distillation-notes.md
```

### Wave 3 Quality Gate

Read _build/decisions.md — review ALL Wave 3 entries. Address contradictions, ambiguities, or content that was flagged for Nick.

Test in a fresh Cowork session:

| Query | Expected | Pass? |
|-------|----------|-------|
| "I'm a new analyst. How do I set up a quant study?" | Reads quant-research.md, walks through steps | |
| "What's the difference between IDIs and focus groups?" | Reads qual-research.md, finds decision guide | |
| "How should I structure a slide?" | Reads deliverable-production.md, explains headline-evidence-implication | |
| "What is a Category Vision project?" | Reads project-types/category-vision.md | |
| "I'm starting a segmentation for a growth-stage snack brand" | Reads segmentation type + searches clients for similar, references patterns | |
| "A project just wrapped up. What should I capture?" | Reads project-close-out.md, initiates the workflow | |

All must pass before proceeding.

---

## PART IV: DATA PIPELINE (Dropbox API)

### Why API Instead of Local Sync

The firm Dropbox is ~2TB. Syncing locally creates three problems:
1. **Disk pressure** — downloading 200GB chunks requires constant space management
2. **Sync reliability** — Dropbox smart sync is slow and sometimes inconsistent; "online-only" files silently fail to read
3. **Change detection** — no way to know which files changed since last scan without downloading everything again

The Dropbox API solves all three:
- **Metadata is free** — list every file across 2TB without downloading a single byte (~5 min for full index)
- **Stream-and-delete** — download one file → extract content → delete temp file. Only ever holding ~50-200MB locally
- **Content hash** — Dropbox provides a `content_hash` per file. Store it in a SQLite registry → never re-process an unchanged file
- **Full fidelity** — downloads the actual .pptx/.docx/.pdf, so python-pptx/python-docx/pdfminer extract everything: slides, notes, tables, headers, grouped shapes, hidden content. No lossy preview rendering.

The old brain already has a working Dropbox API wrapper (`seurat-brain/Scripts/dropbox_utils.py`) that handles pagination, namespaces, and optional dependencies. We'll reference it but build clean for v2.

### Wave 4-Pre — Verify API Access (quick, no session needed)

```
Before building scripts, verify your Dropbox API token works:

1. Confirm you completed Pre-Work step 3 (API app + token)

2. Install dependencies:
   pip install dropbox python-pptx python-docx pdfminer.six openpyxl PyPDF2

3. Quick test — run this in Python:
   import dropbox
   dbx = dropbox.Dropbox("YOUR_TOKEN")
   account = dbx.users_get_current_account()
   print(f"Connected as: {account.name.display_name}")

   # Try listing top-level client folders (this path may need adjustment — see step 4)
   result = dbx.files_list_folder("/Client Folder", limit=10)
   for entry in result.entries:
       print(f"  {entry.name}")

4. If the path "/Client Folder" doesn't work (likely for team Dropbox), try these in order:
   a. Check your namespace: ns = account.root_info; print(ns) — if it's a team namespace, you need with_path_root()
   b. Try: dbx_rooted = dbx.with_path_root(dropbox.common.PathRoot.namespace_id(ns.root_namespace_id))
   c. Then: result = dbx_rooted.files_list_folder("", limit=10) — this lists the true root
   d. Look for the folder that contains client names and note the exact path
   e. Check: result = dbx.sharing_list_shared_folders(limit=5) to see shared folder names
   f. Reference old brain's dropbox_utils.py for working namespace handling patterns:
      C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Scripts\dropbox_utils.py
   g. LOG the working path to _build/decisions.md — Wave 4-A and all future waves depend on it

5. Report: API connection confirmed, exact working client folder path, first 10 client folder names visible.
```

### Wave 4-A — Digestion Engine: Scan Phase (must complete before 4-B)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions from previous sessions that affect your work.
COORDINATION: API integration WILL surface unexpected issues (namespace quirks, permission boundaries, rate limits, folder naming surprises). Log EVERY significant discovery to _build/decisions.md — Wave 4-B and all of Wave 5 depend on this.

Read the old brain's Dropbox utility for reference patterns (namespace handling, pagination):
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Scripts\dropbox_utils.py

YOUR TASK: Build the digestion engine — a single Python script that handles scanning, downloading, extracting, and tracking. This session builds the SCAN phase. Wave 4-B adds the EXTRACT phase.

Write: _scripts/digestion_engine.py
Write: _scripts/requirements.txt
Write: _scripts/.env.template (with placeholder for DROPBOX_ACCESS_TOKEN)
Write: .dropboxignore (add `_scripts/.env` — prevents token from syncing to other team members' machines)

SECURITY NOTE: The brain folder syncs via Dropbox to everyone on the team. The .env file containing your API token MUST be excluded from sync. Create a .dropboxignore file at the brain root with:
  _scripts/.env
  _scripts/output/.tmp/
  _scripts/output/content_registry.db
This prevents your API token, temp downloads, and the SQLite registry from syncing.

DESIGN PRINCIPLES:
- **API-first.** All file access goes through the Dropbox API. No local filesystem assumptions.
- **Stream-and-delete.** Download one file at a time to a temp directory, process it, delete the local copy. Peak disk usage: ~200MB max.
- **Content hash registry.** Every file's Dropbox content_hash is stored in SQLite. If a file hasn't changed since last scan, skip it entirely.
- **Read-only on Dropbox.** Never modify, move, or delete any Dropbox files.
- **Idempotent.** Running twice produces the same results (SQLite registry tracks what's been processed).
- **Resilient.** API errors, rate limits, permission errors, corrupt files — all logged and skipped, never fatal.

DEPENDENCIES: dropbox, python-pptx, python-docx, pdfminer.six, openpyxl, PyPDF2 (in requirements.txt)

CONFIGURATION:
- Token from: .env file (DROPBOX_ACCESS_TOKEN) or --token flag
- Root path from: --root flag or default "/Client Folder"
- Handle team namespace detection automatically:
  - Try direct path first
  - If fails, detect team namespace via users_get_current_account().root_info
  - Use dbx.with_path_root(PathRoot.namespace_id(ns_id)) if needed
  - Reference old brain's dropbox_utils.py for the pattern

SCAN PHASE (this session):

The scan phase uses files/list_folder + files/list_folder/continue to recursively walk the entire client folder tree via API. It extracts metadata WITHOUT downloading any file content.

EXTRACTION per client folder:
- Client name (top-level folder name)
- Dropbox path (for later download)
- Last activity (server_modified of most recent file)
- Total file count
- Total size (bytes)
- Content hash of each file (for change detection)
- Project subfolders: detect numbered folders (regex: ^\d{2}\s+.+) like "01 Project Name"
  For each project:
  - Project name
  - Phase folders detected (match against: KO, Kickoff, WS\d, Workshop, Qual, Quant, Final, Discovery, Fieldwork, Survey, Analysis)
  - Milestone coverage: which phases have v1.0+ files (indicates completion)
  - File count by type (.pptx, .docx, .pdf, .xlsx, other)
  - Most recent file date
  - Files with version numbers: extract version + initials chain from filename
  - **File size per file** — needed for extraction depth planning (see Wave 4-B)
- Old/ subfolder tracking: count files in Old/ separately (these are superseded)
- Conflicted copies: count files matching "conflicted copy" pattern

EXCLUSIONS:
- .DS_Store, Thumbs.db, desktop.ini, ~$* temp files, Icon\r files
- Files < 100 bytes (likely empty/corrupt)

SQLITE REGISTRY (_scripts/output/content_registry.db):
Table: files
  - dropbox_path TEXT PRIMARY KEY
  - client TEXT
  - project TEXT (nullable)
  - filename TEXT
  - extension TEXT
  - size_bytes INTEGER
  - server_modified TEXT (ISO)
  - content_hash TEXT (Dropbox content hash)
  - version TEXT (nullable — extracted from filename)
  - contributors TEXT (nullable — initials from filename, comma-separated)
  - in_old_folder BOOLEAN
  - is_conflicted_copy BOOLEAN
  - scan_date TEXT (ISO — when we last saw this file)
  - extraction_status TEXT DEFAULT 'pending' (pending | extracted | failed | skipped | duplicate)
  - extraction_date TEXT (nullable)
  - word_count INTEGER (nullable — populated after extraction)
  - content_depth TEXT (nullable — thin|standard|rich|dense, populated after extraction)

Table: scan_runs
  - run_id INTEGER PRIMARY KEY AUTOINCREMENT
  - scan_date TEXT
  - root_path TEXT
  - total_clients INTEGER
  - total_files INTEGER
  - total_size_gb REAL
  - new_files INTEGER (files not previously in registry)
  - changed_files INTEGER (known files with new content_hash)
  - duration_seconds REAL

This registry is the foundation of everything. It tells us:
- What exists (full inventory)
- What changed (content_hash comparison)
- What we've already processed (extraction_status)
- What to process next (pending, ordered by priority)

OUTPUT (in addition to SQLite):
1. _scripts/output/scan_results.json
   Same schema as before but populated from API metadata:
   {
     "scan_date": "YYYY-MM-DDTHH:MM:SS",
     "scan_root": "/Client Folder",
     "total_clients": N,
     "total_files": N,
     "total_size_gb": N.N,
     "new_since_last_scan": N,
     "changed_since_last_scan": N,
     "file_type_breakdown": { ".pptx": N, ".docx": N, ... },
     "clients": [
       {
         "name": "Henkel",
         "dropbox_path": "/Client Folder/Henkel",
         "last_activity": "YYYY-MM-DD",
         "file_count": N,
         "size_mb": N,
         "projects": [
           {
             "name": "01 Hair Care Insights",
             "phases": ["KO", "WS1", "WS2"],
             "milestone_coverage": ["KO", "WS1"],
             "file_count": N,
             "last_activity": "YYYY-MM-DD",
             "versioned_files": [
               { "name": "Deck v1.0 TMB.pptx", "version": "1.0", "initials": ["TMB"], "type": ".pptx", "size_mb": 12.3 }
             ]
           }
         ],
         "old_file_count": N,
         "conflicted_copies": N
       }
     ]
   }

2. _scripts/output/scan_summary.md
   Human-readable dashboard:
   - Total: N clients, N files, N.N GB (N new, N changed since last scan)
   - File types: .pptx (N), .docx (N), .pdf (N), .xlsx (N), other (N)
   - Top 20 by file count
   - Top 20 by most recent activity
   - Top 20 by total size
   - Clients with 0 files
   - Projects with full milestone coverage (KO + WS + Final)

3. _scripts/output/digestion_priority.md
   Auto-generated priority order:
   TIER 1 — Active (last activity <6 months):
   [ranked by file count, most → least]

   TIER 2 — Recent (last activity 6-24 months):
   [ranked by file count]

   TIER 3 — Historical (>24 months, >50 files):
   [ranked by file count]

   TIER 4 — Deep archive (everything else):
   [count only]

RATE LIMITING:
- Dropbox API allows ~1000 calls/min for business accounts
- files/list_folder/continue returns up to 2000 entries per call
- Full scan of 545 clients should complete in ~3-8 minutes depending on depth
- Implement exponential backoff on 429 responses (rate_limit_error)

CLI:
  python digestion_engine.py scan                              Full scan
  python digestion_engine.py scan --client "Henkel"            Single client
  python digestion_engine.py scan --depth 3                    Limit folder depth
  python digestion_engine.py scan --dry-run                    Show what would be scanned
  python digestion_engine.py scan --min-files 10               Only output clients with 10+ files
  python digestion_engine.py scan --changed-only               Only report files changed since last scan

Progress: print "Scanning [1/545] Albanese Candy... 47 files (2.3 MB)" to stdout.
Handle: ApiError (log and skip), AuthError (stop and report), RateLimitError (backoff and retry), network errors (retry 3x then skip).

After writing, test: python digestion_engine.py scan --client "Henkel"
Report results: files found, size, projects detected, registry populated correctly.
```

### Wave 4-B — Digestion Engine: Extract Phase + Adaptive Depth (after scan works)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — CRITICAL: Wave 4-A will have logged API quirks, namespace patterns, and folder structure discoveries. Read ALL of them before writing extraction code.
COORDINATION: Log extraction-specific discoveries (file format issues, content depth surprises, deduplication edge cases) to _build/decisions.md. Wave 5 depends on this.

Read: _scripts/digestion_engine.py (understand the scan phase and SQLite registry)
Read: _scripts/output/scan_results.json (first few clients to understand data)

YOUR TASK: Add the EXTRACT phase to the digestion engine. This downloads files one at a time from Dropbox via API, extracts their full content, saves the extract, deletes the temp file, and updates the registry.

CRITICAL DESIGN: STREAM-AND-DELETE PATTERN

For each file to extract:
  1. Query SQLite registry for next pending file (by priority)
  2. Download via Dropbox API → temp file in _scripts/output/.tmp/
  3. Check content_hash matches what we stored in scan phase (file hasn't changed mid-run)
  4. Extract full content using appropriate library
  5. Write extract to _scripts/output/extracts/[client]/[project]/[filename].txt
  6. Update SQLite registry: extraction_status, extraction_date, word_count
  7. DELETE the temp file immediately
  → Peak local disk usage: size of ONE file (typically 5-50MB, rarely >200MB)

Add to: _scripts/digestion_engine.py (extend the existing script)

EXTRACTION LOGIC — FULL FIDELITY:

Nick's core concern: documents must be processed in their ENTIRETY. Some are thin (5 slides, mostly charts), some are deeply rich (100+ slides with strategic narrative, notes, hidden content). The extractor must handle both.

- PPTX (python-pptx) — DEEP EXTRACTION:
  - For each slide: extract ALL text from ALL shapes:
    - TextFrame shapes (paragraphs, runs)
    - Table cells (every row, every column — serialize as "| col1 | col2 |")
    - GroupShape recursion (iterate group.shapes, recurse into nested groups)
    - SmartArt (best effort — extract from underlying XML if python-pptx can't parse)
    - Chart titles and data labels (if accessible)
  - Slide notes (often contain strategic context, presenter talking points, source citations)
  - Slide master/layout text is EXCLUDED (generic branding, not content)
  - Hidden slides: INCLUDE but mark as "[HIDDEN SLIDE]"
  - Output format per slide:
    "=== Slide [N] [of N] ===" (or "[HIDDEN] Slide [N] [of N]")
    [all shape text, preserving rough reading order: title → body → tables → notes]
    "--- Slide Notes ---"
    [notes text]
  - For PPTX files: also extract document properties (title, subject, author, last_modified_by)

- DOCX (python-docx) — DEEP EXTRACTION:
  - Full body text with paragraph structure preserved
  - Heading hierarchy preserved (H1, H2, H3 — useful for section detection)
  - Tables: serialize as markdown tables "| col1 | col2 |"
  - Headers and footers (often contain client name, date, confidentiality)
  - Comments: extract comment text + author + the text they're anchored to (strategic signal)
  - Track changes: extract current text, note that tracked changes exist
  - Text boxes and floating shapes (often contain callouts, key findings)
  - For DOCX files: extract document properties

- PDF (pdfminer.six, fallback PyPDF2) — BEST EFFORT:
  - Extract text preserving rough layout
  - Handle multi-column layouts (pdfminer's LAParams)
  - Page count + per-page extraction
  - Detect scanned/image-only PDFs: if <50 chars extracted per page average, log as "likely scanned — OCR needed" and mark extraction_status='partial'
  - Do NOT attempt OCR in this phase (too slow, requires tesseract) — flag for future

- XLSX (openpyxl) — DATA EXTRACTION:
  - Extract ALL sheet names
  - For each sheet: all rows with data (not just first 100 — data files can be large)
  - BUT: cap at 5000 rows per sheet (data dumps beyond that are raw data, not knowledge)
  - Output as tab-separated values with sheet name headers
  - Named ranges and defined names (often contain key metrics)
  - Note: formulas are extracted as values (openpyxl data_only mode)

ADAPTIVE EXTRACTION DEPTH:
Not all files are equal. A 2MB PPTX with 12 slides of charts is thin. A 45MB PPTX with 90 slides of strategy narrative is rich. The extractor should adapt:

  - **File size** is a rough proxy for content density:
    < 1MB: likely thin (few slides/pages, lots of images)
    1-10MB: typical working document
    10-50MB: likely rich (many slides, embedded content)
    > 50MB: probably media-heavy (video embeds, high-res images) — extract text only

  - **Slide/page count** refines the estimate:
    PPTX: <15 slides = focused, 15-50 = standard, 50+ = comprehensive (WS/Final deck)
    DOCX: <5 pages = memo/brief, 5-20 = standard, 20+ = comprehensive report

  - After extraction, categorize each file:
    THIN (< 500 words extracted): log as thin, still save extract
    STANDARD (500-5000 words): normal processing
    RICH (5000-20000 words): flag for synthesis priority — these contain the most knowledge
    DENSE (> 20000 words): flag as "needs Claude synthesis session" — too much for pattern extraction, needs AI summarization

  - Store depth category in SQLite registry (new column: content_depth TEXT)

DEDUPLICATION (query SQLite before downloading):
- PPTX + PDF same-name pairs → extract from PPTX only (higher fidelity), mark PDF as "skipped: pptx-duplicate"
- "Conflicted copy" files → skip, mark as "skipped: conflicted-copy"
- Files in Old/ subfolders → skip by default, extract if --include-old flag set
- Files with same content_hash as an already-extracted file in different path → skip, mark as "skipped: content-duplicate"

OUTPUT per file:
_scripts/output/extracts/[client]/[project]/[filename].txt

Header block in each extract:
---
source_path: [Dropbox path]
content_hash: [Dropbox content_hash — for verification]
type: pptx | docx | pdf | xlsx
extracted: [ISO timestamp]
file_size_mb: [N.N]
words: [word count]
slides: [count, if pptx]
pages: [count, if pdf]
sheets: [count, if xlsx]
content_depth: thin | standard | rich | dense
version: [if detected from filename]
contributors: [if detected from filename]
has_notes: [true/false, if pptx]
has_comments: [true/false, if docx]
has_hidden_slides: [true/false, if pptx]
---
[extracted text — full content]

PROGRESS TRACKING (all in SQLite registry — no separate JSON):
- extraction_status column tracks: pending → extracted / failed / skipped / partial
- extraction_date tracks when
- word_count tracks density
- content_depth tracks classification
- Query: SELECT COUNT(*) FROM files WHERE extraction_status = 'pending' AND client = 'Henkel'

ERROR HANDLING:
- _scripts/output/extract_errors.log — one line per failure: [timestamp] [dropbox_path] [error_type] [message]
- Common failures:
  - Corrupt ZIP (bad DOCX/PPTX) → mark as 'failed', log error
  - Password-protected → mark as 'failed: password-protected'
  - Dropbox download timeout → retry 3x with exponential backoff, then mark 'failed: download-timeout'
  - Rate limit → backoff and retry (never mark as failed for rate limits)
  - File too large (>200MB) → skip, mark as 'skipped: too-large'
- NEVER stop the batch on a single file failure. Log and continue.

CLI:
  python digestion_engine.py extract --client "Henkel"                Extract all pending for one client
  python digestion_engine.py extract --tier 1                         All Tier 1 priority clients
  python digestion_engine.py extract --type pptx,docx                 Filter by file type
  python digestion_engine.py extract --version-min 1.0                Only v1.0+ (final deliverables)
  python digestion_engine.py extract --limit 50                       Max files per run
  python digestion_engine.py extract --dry-run                        Show plan without executing
  python digestion_engine.py extract --client "Henkel" --project "01" Single project
  python digestion_engine.py extract --changed-only                   Only files changed since last extract
  python digestion_engine.py extract --depth rich                     Only extract files classified as rich/dense
  python digestion_engine.py extract --include-old                    Include Old/ subfolder files

  python digestion_engine.py status                                   Dashboard: files by status, by client
  python digestion_engine.py status --client "Henkel"                 Single client status

STATUS COMMAND output:
  Digestion Engine Status — [date]
  Total files in registry: N
  By status: pending (N) | extracted (N) | failed (N) | skipped (N) | partial (N)
  By depth: thin (N) | standard (N) | rich (N) | dense (N) | unknown (N)
  By type: .pptx (N) | .docx (N) | .pdf (N) | .xlsx (N) | other (N)
  Extraction coverage: [N]% of eligible files processed
  Clients fully extracted: [list]
  Clients partially extracted: [list with %]
  Disk usage (_scripts/output/extracts/): [N MB]

After writing, test:
python digestion_engine.py extract --client "Henkel" --version-min 1.0 --limit 10
Report: files downloaded + extracted, success/fail counts, content depth distribution, sample extract quality (paste first 50 lines of one rich extract), temp files properly cleaned up, disk usage.
```

### Wave 4 Quality Gate

```
Read _build/CONTEXT.md.
Read _build/decisions.md — review ALL Wave 4 entries. API quirks logged here are critical for Wave 5.

Test the digestion engine end-to-end:

1. SCAN TEST:
   python digestion_engine.py scan --client "Henkel"
   - Verify: SQLite registry populated, scan_results.json written, content hashes stored
   - Check: file count matches what you see in Dropbox web UI for Henkel

2. EXTRACT TEST:
   python digestion_engine.py extract --client "Henkel" --version-min 1.0 --limit 5
   - Verify: 5 files downloaded, extracted, temp files deleted
   - Check extract quality: open 2-3 .txt extracts and compare against source documents
   - For a PPTX: are ALL slides extracted? Are notes included? Tables readable?
   - For a DOCX: are headings preserved? Tables formatted? Comments captured?

3. IDEMPOTENCY TEST:
   python digestion_engine.py extract --client "Henkel" --version-min 1.0 --limit 5
   - Should skip all 5 files (already extracted, content_hash unchanged)
   - Verify: "Skipping [file] — already extracted, content unchanged" messages

4. STATUS TEST:
   python digestion_engine.py status --client "Henkel"
   - Verify: shows correct counts for pending/extracted/skipped

5. FULL SCAN TEST (if time allows):
   python digestion_engine.py scan
   - Full scan of all 545 clients
   - Should complete in <10 minutes
   - Report: total clients, total files, total size, scan duration

Write: _build/wave4-quality-report.md
All tests must pass before proceeding to Wave 5.
```

---

## PART V: DIGESTION

### Wave 5-A — Digest Active Clients Batch 1 (SEQUENTIAL — first batch)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — IMPORTANT: Wave 4 will have logged API patterns, extraction quirks, and content depth findings. Adapt your synthesis approach based on what was discovered.
COORDINATION: Log synthesis-level discoveries (unexpected client folder structures, cross-client connections found, pattern candidates that emerged) to _build/decisions.md. Wave 5-B and 5-C need these.

Read: _scripts/output/digestion_priority.md

YOUR TASK: Extract content from the 5 priority active clients and synthesize into brain knowledge.

PRIORITY CLIENTS: Henkel, Merck, Bolton, Pennington, Nielsen-Massey

The 5 clients listed here are the CONFIRMED active clients as of build time. If digestion_priority.md shows different or additional active clients (last activity <6 months), add them to this batch or flag for Nick's decision.

For EACH client:

STEP 1: Extract content (via Dropbox API — stream-and-delete)
python digestion_engine.py extract --client "[Name]" --version-min 1.0 --limit 30
(This downloads each file via API, extracts content, deletes the temp file. No local sync needed.)

STEP 2: Read the extracts
Read files in: _scripts/output/extracts/[client]/

STEP 3: Read the existing client profile (from Wave 2 migration)
Read: clients/[client].md

STEP 4: Synthesize
Compare what's in the extracted project files against what's in the current profile. For each project found in the extracts:

a) PROJECT INTELLIGENCE:
- What was the strategic question? (from the deck titles, executive summaries, KO materials)
- What were the key findings? (from WS and Final deliverables)
- What methods were used? (from survey docs, qual guides, discovery materials)
- What was the timeline? (from file dates)
- Who was on the team? (from contributor initials in filenames)

b) PATTERN EVIDENCE:
Read knowledge/patterns.md. Do any extracted projects:
- Add evidence to an existing pattern? → Note the pattern number and what this project adds
- Reveal a new pattern candidate? → Draft it in pattern format with confidence: emerging

c) LESSON EVIDENCE:
Read knowledge/lessons.md. Do any extracted projects:
- Confirm an existing lesson? → Note confirmation
- Reveal a new lesson? → Draft it in lesson format with status: provisional

d) BD SIGNALS:
- Is there evidence of follow-on opportunity?
- What re-sell pattern might apply? (reference bd/selling-playbook.md)

e) THEME CONNECTIONS:
- Which themes in intelligence/themes/ does this client connect to?
- Any new theme evidence?

f) SURVEY INTELLIGENCE (if project involved quant research):
When extracted content includes survey documents (wireframes, questionnaires, programmer docs, test plans):
- Extract QUESTIONS used: exact question text, question type (scale, grid, open-end, carousel, etc.), what construct it measures
- Extract RESPONSE OPTIONS: scale labels (e.g., "Extremely likely" to "Not at all likely"), grid row/column items, coded answer lists
- Extract CODING LANGUAGE: how variables are named, piping conventions, skip logic patterns
- Extract FLOW/STRUCTURE: section ordering, screening logic, how the survey is organized by topic
- Categorize by: survey type (Usage & Attitude, Concept Test, Segmentation, Brand Tracking, etc.), category (personal care, food & bev, health, etc.)
- Note what's REUSABLE: battery questions that appear across multiple surveys, standard scale formats, demographic blocks, category-specific question patterns
- Write survey patterns to: knowledge/survey-patterns.md (see format below)

This is CRITICAL for powering survey automation tools. The brain should accumulate a library of proven questions, response options, and structural patterns that the survey-mapper and wireframe skills can draw from.

STEP 5: Present synthesis for review
For each client, show me:
1. Proposed updates to clients/[client].md (show new content only, not whole file)
2. Pattern candidates (new or evidence additions) with source extracts cited
3. Lesson candidates with source extracts cited
4. BD signals
5. Theme connections
6. Survey intelligence found (questions, scales, patterns) with source files cited

Wait for my approval before writing ANYTHING into the brain's knowledge files.

PROVENANCE: For every piece of synthesized information, note the source file it came from:
"Source: extracts/henkel/01-hair-care/WS1-Deck-v1.0.txt, slides 12-15"

SURVEY PATTERN LIBRARY FORMAT (knowledge/survey-patterns.md):

# Survey Pattern Library
Last updated: [today's date]
Total patterns: [N questions] | [N scales] | [N flow templates]
Source: Extracted from client survey documents during digestion.

## Question Batteries
Reusable question groups that appear across multiple surveys.

### QB[N]: [Battery Name] (e.g., "Purchase Intent Battery")
**Type:** [scale / grid / open-end / multi-select / single-select]
**Used in:** [Client 1 — survey type], [Client 2 — survey type]
**Category:** [personal care / food & bev / health / general]
**Survey type:** [U&A / Concept Test / Segmentation / Brand Tracking / Custom]
**Question text:** [exact text, preserving piping notation like {BRAND}]
**Response options:**
- [option 1]
- [option 2]
- [...]
**Programming notes:** [variable naming convention, skip logic, any special handling]
**Why it works:** [brief note on what makes this question effective — if discernible from context]

## Standard Scales
Scale formats used consistently across surveys.

### SC[N]: [Scale Name] (e.g., "5-Point Agreement Scale")
**Used in:** [N surveys across N clients]
**Labels:** [Strongly agree / Somewhat agree / Neither / Somewhat disagree / Strongly disagree]
**Coding:** [5 = Strongly agree ... 1 = Strongly disagree] or [as used]
**Variants seen:** [any client-specific modifications]

## Flow Templates
Common survey structure patterns by type.

### FT[N]: [Template Name] (e.g., "Standard U&A Survey Flow")
**Survey type:** [U&A / Concept Test / etc.]
**Typical sections in order:**
1. [Screening]
2. [Category usage/behavior]
3. [Brand awareness & perception]
4. [...]
**Typical length:** [N questions / N minutes]
**Used in:** [Client 1], [Client 2]
**Notes:** [variations by category, common additions]

## Demographic Blocks
Standard demographic question sets.

### DM[N]: [Block Name]
**Questions included:** [list]
**Used in:** [N surveys]
**Notes:** [category-specific additions like "household size" for food, "skin type" for personal care]

IMPORTANT: This file grows over time as more surveys are digested. Each entry must cite the source survey document. The survey-mapper and test-plan-assembler skills should reference this library when building new surveys — it provides proven question language and structure that Seurat has used successfully.
```

### Wave 5-B — Digest Active Clients Batch 2 + Cross-Client Synthesis (after 5-A)

```
Follow the same extraction and synthesis process as Wave 5-A, but for the next 5 clients from digestion_priority.md Tier 1 list.
Use: python digestion_engine.py extract --client "[Name]" --version-min 1.0 --limit 30
The engine's content_hash tracking means re-running on a client already done is safe — it skips unchanged files.

ADDITIONAL STEP — CROSS-CLIENT SYNTHESIS:

After processing this batch, read ALL client profiles updated/created across 5-A and 5-B.
Also read knowledge/patterns.md and knowledge/lessons.md.

Perform cross-client analysis:
1. Which patterns now have 3+ client evidence points? (these are strong — upgrade confidence level)
2. Are there NEW patterns visible only when looking across multiple recently-digested clients?
3. Are there thematic clusters forming that don't yet have theme hub files?
4. Are there common methods or approaches across clients that should strengthen process docs?
5. Are there BD signals that suggest new selling areas or re-sell patterns?
6. SURVEY PATTERNS: Read knowledge/survey-patterns.md. Cross-reference survey content found across clients:
   - Which question batteries appear in 2+ clients? (elevate to standard patterns)
   - Which scales are used consistently? (standardize coding)
   - Do survey flows differ by category in predictable ways? (build flow templates)
   - Are there category-specific demographic questions? (build demographic blocks)
   This cross-client view is where the survey pattern library gets powerful — patterns across surveys reveal Seurat's actual methodology.

Present cross-client synthesis separately from individual client updates.
```

### Wave 5-C — Build Theme Hubs (PARALLEL with 5-B)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — check for cross-client connections and pattern candidates logged during Wave 5-A/5-B. These inform theme hub creation.
COORDINATION: Log theme-level discoveries to _build/decisions.md if themes intersect with ongoing Wave 5-B synthesis.

TIMING: This session reads client profiles and patterns.md which Wave 5-B may be updating concurrently. Read these files at the START of your session and work from that snapshot. If Wave 5-B logs significant updates to decisions.md while you're working, check whether they affect your theme hub construction. The Wave 5 Quality Gate will reconcile any gaps.

Read: clients/_index.md
Read: knowledge/patterns.md
Read all client profiles in clients/
Read old brain theme files for reference:
C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\Themes\
(read all .md files)

YOUR TASK: Build thematic hubs — cross-client strategic clusters that emerge from the data.

Themes emerge from THREE sources:
1. Client profiles — what themes are tagged in each profile?
2. Patterns — which patterns cluster around similar dynamics?
3. Old brain themes — which v1 themes are validated by current v2 data?

For each theme with 3+ connected clients, create:
intelligence/themes/[theme-name].md

# [Theme Name]
Last updated: [today's date]
Source: Built from client profiles, patterns, and v1 brain themes during v2 build.
Connected clients: [N] | BD prospects: [N]

## What This Is
[2-3 sentences. The strategic dynamic, not a generic category definition.]

## Why It Matters for Seurat
[How this theme affects selling, scoping, or execution. Specific.]

## Connected Clients
| Client | Relevance | Evidence Strength | Status |
|--------|-----------|-------------------|--------|
[For each: why they connect, how strong the evidence, active/lapsed]
see: clients/[client].md for each

## Key Insights
[What we've learned from working across multiple clients in this space.]
[NOT generic market facts. Seurat-specific learnings.]
[Example: "Channel fragmentation is structural in personal care — seen across Henkel, Bolton, Beautycounter. The channel question changes the strategy question." ]
[Each insight should cite source: "Observed in Henkel WS1 (Feb 2026) and Bolton fieldwork (Jan 2026)"]

## BD Relevance
[Which prospects in bd/pipeline.md connect? What's the selling angle?]
see: bd/selling-playbook.md#[relevant area]
see: bd/pipeline.md

## Related Patterns
see: patterns.md#P[N], #P[N]

## Cross-Theme Connections
[Which other themes intersect?]
see: intelligence/themes/[other-theme].md

## Open Questions
[What we don't know. What would be valuable to learn.]

Create index: intelligence/themes/_index.md
One-line per theme: name, description, client count, BD prospect count.

QUALITY BAR: A theme hub answers: "If I'm starting a new engagement in this space, what does Seurat already know that gives us an edge?" If a theme can't answer that with specific examples, it's not ready — keep it as a tag in client profiles only.

CUT any theme with fewer than 3 connected clients.
```

### Wave 5 Quality Gate (1 session)

```
Read _build/CONTEXT.md.
Read _build/decisions.md — review ALL entries from Waves 4 and 5. This is where integration issues surface.

YOUR TASK: Validate the digestion outputs and cross-referencing.

0. Check digestion engine status:
   python digestion_engine.py status
   Verify: all priority clients show extraction_status = 'extracted' for v1.0+ files.
   Note content depth distribution: how many rich/dense files were found? Were they all synthesized?

1. Read all updated/created client profiles. For each:
   - Are project summaries grounded in extracted content (not hallucinated)?
   - Are cross-references to patterns, lessons, and themes valid?
   - Are temporal markers present?
   - Is provenance noted for each piece of information?

2. Read patterns.md. Are new evidence additions properly attributed?

3. Read theme hubs. For each:
   - Do all "Connected Clients" entries have profiles?
   - Are "Key Insights" specific to Seurat (not generic)?
   - Are cross-references to patterns and selling-playbook valid?

4. Read knowledge/survey-patterns.md. Are extracted question batteries properly formatted with source attribution? Are scales consistent across entries? Are any patterns seen in 2+ clients appropriately flagged as standard?

5. Run retrieval tests:
| Query | Expected |
|-------|----------|
| "What do we know about protein and sports nutrition?" | Finds theme hub, lists connected clients |
| "Which clients have done category vision projects?" | Cross-references project-types + client profiles |
| "What's the connection between Henkel and Bolton?" | Finds shared themes, patterns |
| "I'm scoping a personal care engagement — what should I know?" | Pulls theme + patterns + client lessons |

Write: _build/wave5-quality-report.md
```

---

## PART VI: SKILLS & PLUGIN

### Wave 6-A — Port Meeting Notes Skill (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions that affect skill porting (path changes, naming conventions, client profile structure).
COORDINATION: Log any skill-level decisions (trigger phrase conflicts, reference file format changes) to _build/decisions.md. Wave 6-B and 6-C are running in parallel.

Read the old brain's meeting notes skill FULLY:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\seurat-meeting-notes\SKILL.md
- Read all files in: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\seurat-meeting-notes\references\

Also read the old brain's AI integration plan for plugin architecture:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\_meta\AI-INTEGRATION-PLAN.md

YOUR TASK: Port the meeting notes skill into v2 brain format.

The v1 skill is detailed and production-tested. Port it with these adjustments:
1. Update file paths to reference v2 brain structure
2. Add integration with client profiles: when processing a meeting, check if clients/[client].md exists and use it for context (attendee background, project history, strategic context)
3. Preserve the learning-feedback loop (learned-preferences.md pattern)
4. Keep all formatting specifications, reference files, and quality rules

Write to: skills/meeting-notes/
- SKILL.md (main specification)
- references/ folder with all reference files (format-guide.md, content-quality.md, example-notes.md, learned-preferences.md)

The SKILL.md should follow the v1 format with YAML frontmatter:
---
name: meeting-notes
description: >
  Convert meeting transcript + optional deck + notes into polished .docx meeting notes.
  Use when user provides a transcript, says "I just had a meeting with...", or asks to process meeting notes.
---

Preserve the v1 skill's detail level. The survey-mapper SKILL.md was 727 lines. Meeting notes should be equally detailed where the specification warrants it.

Also create the slash command:
.claude/commands/meeting-notes.md

This is a markdown file that gets executed when user types /meeting-notes. It should:
1. Ask for inputs (transcript, optional deck, optional notes)
2. Read the SKILL.md
3. Check for client profile context
4. Execute the workflow
5. Save output to appropriate location
```

### Wave 6-B — Port Survey Pipeline (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions that affect skill porting.
COORDINATION: Log any decisions to _build/decisions.md. Wave 6-A and 6-C are running in parallel.

Read the old brain's survey skills FULLY:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\survey-mapper\SKILL.md (727 lines)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\test-path-generator\SKILL.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\test-plan-assembler\SKILL.md (505 lines)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\survey-wireframe-to-doc\SKILL.md
- Read all files in each skill's references/ and scripts/ folders

YOUR TASK: Port the complete survey pipeline (4 skills) into v2 brain format.

These are HIGHLY DETAILED specifications with exact Python code, color values, font specs, and business logic. Preserve ALL of this detail. Do not summarize or simplify the specs.

Port with adjustments:
1. Update file paths for v2 structure
2. Add cross-references to knowledge/processes/survey-fieldwork.md
3. Preserve ALL formatting specifications (Franklin Gothic Book, #0F4761 navy, #E97132 orange, etc.)
4. Preserve ALL consistency checks, gap detection, and quality verification steps
5. Keep any Python code exactly as-is unless paths need updating
6. INTEGRATE WITH SURVEY PATTERN LIBRARY: Add instructions to each skill to READ knowledge/survey-patterns.md at the start of execution:
   - survey-mapper: when mapping a new survey, cross-reference against known question batteries and scales. Flag reusable patterns. After mapping, extract any NEW question patterns not yet in the library and propose additions.
   - test-plan-assembler: when building test plans, reference standard flow templates (FT entries) for the survey type to ensure section coverage is complete.
   - survey-wireframe-to-doc: when converting wireframes, use standard scale labels and coding conventions from the library for consistency.
   This creates a feedback loop: digestion discovers survey patterns → skills use those patterns → new surveys get checked against the library → the library grows.

Write to:
- skills/survey-mapper/SKILL.md + references/
- skills/test-path-generator/SKILL.md + references/
- skills/test-plan-assembler/SKILL.md + references/
- skills/survey-wireframe-to-doc/SKILL.md + references/

Create slash commands:
- .claude/commands/survey-map.md
- .claude/commands/survey-path.md
- .claude/commands/test-plan.md
- .claude/commands/survey-doc.md
```

### Wave 6-C — Build GitHub Plugin Structure (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — Wave 6-A and 6-B may have logged skill naming or path decisions that affect the plugin manifest.
COORDINATION: Log any plugin-level decisions to _build/decisions.md.

Read the old brain's plugin architecture plan:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\_meta\AI-INTEGRATION-PLAN.md

YOUR TASK: Build the GitHub plugin repository structure for distributing skills via Cowork.

This is LAYER 2 of the three-layer architecture: the execution layer distributed via GitHub.

Create the plugin structure in a new folder (this will become a GitHub repo):
_build/seurat-tools-plugin/

Structure:
_build/seurat-tools-plugin/
  .claude-plugin/
    plugin.json                ← Plugin manifest
  skills/
    meeting-notes/             ← Copy from brain skills/meeting-notes/
    survey-mapper/             ← Copy from brain skills/survey-mapper/
    test-path-generator/       ← Copy from brain skills/test-path-generator/
    test-plan-assembler/       ← Copy from brain skills/test-plan-assembler/
    survey-wireframe-to-doc/   ← Copy from brain skills/survey-wireframe-to-doc/
  commands/
    meeting-notes.md           ← Copy from brain .claude/commands/meeting-notes.md
    survey-map.md
    survey-path.md
    test-plan.md
    survey-doc.md
  README.md                    ← Installation and usage instructions

plugin.json:
{
  "name": "seurat-tools",
  "version": "2.0.0",
  "description": "Seurat Group consulting tools — meeting notes, survey pipeline, deliverable automation",
  "skills": [
    { "name": "meeting-notes", "path": "skills/meeting-notes/SKILL.md" },
    { "name": "survey-mapper", "path": "skills/survey-mapper/SKILL.md" },
    { "name": "test-path-generator", "path": "skills/test-path-generator/SKILL.md" },
    { "name": "test-plan-assembler", "path": "skills/test-plan-assembler/SKILL.md" },
    { "name": "survey-wireframe-to-doc", "path": "skills/survey-wireframe-to-doc/SKILL.md" }
  ],
  "commands": [
    { "name": "meeting-notes", "path": "commands/meeting-notes.md" },
    { "name": "survey-map", "path": "commands/survey-map.md" },
    { "name": "survey-path", "path": "commands/survey-path.md" },
    { "name": "test-plan", "path": "commands/test-plan.md" },
    { "name": "survey-doc", "path": "commands/survey-doc.md" }
  ]
}

README.md should include:
1. What this plugin does (one paragraph)
2. Installation (exact Cowork commands)
3. Available skills with trigger descriptions
4. Available slash commands with usage examples
5. Requirements (brain folder must be the Cowork project root)

This folder will be pushed to GitHub as a private repo. For now, build the structure locally.
```

### Wave 6 Quality Gate (1 session)

```
Read _build/CONTEXT.md.
Read _build/decisions.md — review ALL Wave 6 entries. Resolve any cross-skill conflicts before testing.

YOUR TASK: End-to-end skill testing with real inputs.

STEP 1: Test meeting notes skill
- Find a real meeting transcript or create a realistic test transcript
- Run the meeting notes workflow
- Verify: does the output .docx have correct formatting? Are sections complete? Does it reference client context from the brain?

STEP 2: Test survey pipeline
- Find a real survey document or use one from the old brain's test files
  Search: C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Skills\survey-mapper\references\ for example inputs
- Run: survey-mapper → test-path-generator → test-plan-assembler
- Verify: does the pipeline produce a complete test plan? Are formatting specs correct (fonts, colors)?

STEP 3: Verify slash commands
- Test /meeting-notes — does it activate correctly?
- Test /survey-map — does it activate correctly?
- Test /test-plan — does it activate correctly?

STEP 4: Plugin structure validation
- Verify plugin.json is valid JSON
- Verify all skill paths in plugin.json point to existing files
- Verify all command paths point to existing files
- Verify README installation instructions are clear

Write: _build/wave6-quality-report.md with pass/fail for each test.
```

---

## PART VII: AUTOMATION & INTELLIGENCE

### Wave 7-A — Daily Brief System (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions that affect intelligence/signals structure or source configuration.
COORDINATION: Log decisions to _build/decisions.md. Wave 7-B is running in parallel.

Read the old brain's daily brief system:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\.claude\commands\daily-brief.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\_sources.md
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\_last-run.md (if this file doesn't exist, skip it — it was dynamically generated and its absence just means the daily brief system starts fresh)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\_inbox-log.md (if this file doesn't exist, skip it — it was dynamically generated and its absence just means the daily brief system starts fresh)
Read any recent daily brief output for format reference:
C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\Intelligence\daily-briefs\

YOUR TASK: Port the daily intelligence brief system into v2.

Create:
1. intelligence/sources.md — source configuration
   Port from old brain _sources.md:
   - Newsletter inbox (duncanfisherhq@gmail.com)
   - Twitter accounts by tier (Tier 1: daily, Tier 2: Mon/Wed/Fri, Tier 3: weekly)
   - For each source: name, URL/handle, what they cover, which themes they're relevant to

2. .claude/commands/daily-brief.md — slash command
   Port from old brain, adjusted for v2 paths:
   - Check last run state
   - Scan Gmail for unread newsletters from configured sources
   - Scan Twitter accounts per tier schedule
   - Extract signals and classify:
     - Client-relevant: tag to specific client profiles
     - Theme-relevant: tag to specific theme hubs
     - BD-relevant: tag to specific prospects
     - General market: untagged but captured
   - Write brief to: intelligence/signals/[YYYY-MM-DD].md
   - Update state files

3. intelligence/signals/_template.md — brief template
   # Daily Intelligence Brief — [DATE]
   Sources scanned: [N newsletters, N Twitter accounts]
   Signals found: [N]

   ## Client-Relevant Signals
   [For each: source, signal summary, why it matters, tagged client]
   see: clients/[client].md

   ## Theme-Relevant Signals
   [For each: source, signal, tagged theme]
   see: intelligence/themes/[theme].md

   ## BD-Relevant Signals
   [source, signal, tagged prospect]
   see: bd/pipeline.md

   ## General Market
   [signals not tagged to specific clients/themes]
```

### Wave 7-B — Curation Process + Monitoring (PARALLEL)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any decisions that affect monitoring or curation scope.
COORDINATION: Log decisions to _build/decisions.md. Wave 7-A is running in parallel.

Read the old brain's automation infrastructure:
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\_automation\brain_state_weekly.py (if this file doesn't exist, build the health monitoring from scratch based on the requirements below — the v1 versions were prototypes and building fresh may produce better code)
- C:\Users\NickFisher\Dropbox (Personal)\Nick's Personal Dropbox (Nickfisher518@gmail.com)\seurat-brain\_automation\freshness_check.py (if this file doesn't exist, build the health monitoring from scratch based on the requirements below — the v1 versions were prototypes and building fresh may produce better code)

YOUR TASK: Build the weekly curation workflow and basic brain health monitoring.

OUTPUT 1: .claude/commands/curation.md
A slash command for Nick's weekly curation session. When invoked:

1. BRAIN HEALTH CHECK (2 min)
   - Count files by folder, compare to last week
   - Check for files not updated in >30 days
   - Check for broken cross-references (any "see:" pointing to nonexistent files)
   - Report: "Brain has [N] files. [N] updated this week. [N] stale (>30 days)."

2. PROJECT STATUS (10 min)
   - Read clients/_index.md
   - Ask Nick: "Any project status changes this week? New projects? Completions? Milestones?"
   - Update client profiles as directed

3. INTELLIGENCE REVIEW (5 min)
   - Read this week's daily brief signals (intelligence/signals/)
   - "These signals came in this week. Any worth filing to a client profile or theme hub?"
   - File approved signals

4. PATTERN / LESSON CHECK (10 min)
   - "Did anything this week remind you of an existing pattern?"
   - "Did anything go wrong worth documenting?"
   - Draft updates if Nick identifies something

5. BD UPDATE (5 min)
   - "Any BD conversations or updates?"
   - Update pipeline.md as directed

6. SUMMARY (2 min)
   - List all changes made during session
   - Note any items deferred to next week

OUTPUT 2: _scripts/brain_health.py
Simple monitoring script (stdlib only):
- Count files by folder
- Find files not modified in >30 days
- Check all "see:" cross-references resolve to real files
- Output: _scripts/output/brain_health.json + brain_health_summary.md

CLI: python brain_health.py
Can be run by /curation command or standalone.

OUTPUT 3: knowledge/processes/weekly-curation.md
Document the curation process (for reference, not execution — the command handles execution):
- When: weekly, 30-45 minutes
- What it covers (the 5 steps above)
- Why it matters (the brain stagnates without regular feeding)
- How knowledge quality is maintained
```

### Wave 7 Quality Gate

Test the daily brief and curation systems before moving to comprehensive testing:

| Test | Expected | Pass? |
|------|----------|-------|
| `/daily-brief` command | Activates, scans configured sources, writes signal file to intelligence/signals/ | |
| `/curation` command | Activates, runs health check, walks through 5-step workflow | |
| `python _scripts/brain_health.py` | Runs without errors, outputs brain_health_summary.md with accurate file counts | |
| Manually break a cross-reference (add "see: nonexistent.md" to a file) → run health check | Health check detects and reports the broken reference | |
| Check intelligence/sources.md | All newsletter sources and Twitter accounts are configured with correct tiers | |

All must pass before proceeding to Wave 8.

---

## PART VIII: TESTING & DEPLOYMENT

### Wave 8-A — Comprehensive Testing (1 session)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md — review the FULL decision log. This is your record of every fork encountered during the build. Check that all "Action needed" items have been resolved.

YOUR TASK: Run a comprehensive test suite against the completed brain.

SCENARIO TESTS (simulate different user types):

NEW ANALYST SCENARIOS:
1. "I'm Sarah, I just started. I'm working on a project for Henkel."
   → Should: find Henkel profile, describe current projects, suggest relevant patterns
2. "What is a Category Vision project?"
   → Should: find project-types/category-vision.md, explain clearly
3. "How do I build a survey wireframe?"
   → Should: find processes/survey-fieldwork.md, walk through steps
4. "What are common mistakes in quant research?"
   → Should: find processes/quant-research.md, cite specific mistakes with sources
5. "What should I know about the 5 Cs?"
   → Should: find processes/discovery.md, explain framework

EM SCENARIOS:
6. "I'm scoping a segmentation for a growth-stage snack brand. What should I know?"
   → Should: read project-types/consumer-segmentation.md, search patterns for growth-stage, find similar clients
7. "What patterns should I watch for in post-acquisition work?"
   → Should: search patterns.md for post-acquisition, cite multiple patterns with evidence
8. "The Bolton project just wrapped up. Let's capture what we learned."
   → Should: initiate close-out process from processes/project-close-out.md

PARTNER/BD SCENARIOS:
9. "What's in the pipeline?"
   → Should: read bd/pipeline.md, summarize prospects
10. "We have a meeting with a PE-backed personal care company. How do we position?"
    → Should: find selling-playbook.md PE angle + personal care theme, cite proof points
11. "What's our proof point for category vision work?"
    → Should: find selling area, cite specific client outcomes

CROSS-REFERENCING SCENARIOS:
12. "What connects Henkel and Bolton?"
    → Should: cross-reference profiles, find shared themes and patterns
13. "Which clients are in the protein space?"
    → Should: search theme hub + client index, list with relevance
14. "Have we ever worked with [obscure historical client]?"
    → Should: search client index, find entry even if minimal

EDGE CASES:
15. "Tell me about FakeCorp" → Should handle gracefully, say no profile exists
16. "Update the Henkel profile with [new info]" → Should draft update but NOT write without approval
17. "What's our revenue last quarter?" → Should NOT hallucinate, say brain doesn't contain financial data

For each test:
| # | Query | Expected Behavior | Actual Behavior | Pass/Fail | Notes |

Write: _build/wave8-test-results.md

Fix any issues found. Re-test failures after fixes.
```

### Wave 8-B — Setup Guide + Training (1 session)

```
Read _build/CONTEXT.md for project context.
Read _build/decisions.md for any user-facing implications of build decisions.
Read: _build/wave8-test-results.md (to understand what works and what to highlight)

YOUR TASK: Write user-facing documentation.

OUTPUT 1: _docs/setup-guide.md

For a non-technical Seurat team member. Assume they have Dropbox and might need to install Cowork.

# Getting Started with the Seurat Brain

## Step 1: Find the Brain
[Exact folder path in Dropbox. How to verify it's synced.]

## Step 2: Set Up Cowork
[Download link. Installation steps. Account setup.]

## Step 3: Point Cowork at the Brain
[Settings → Projects → Add → path → Save. With screenshots if possible.]

## Step 4: Install the Seurat Tools Plugin
[Exact commands to install the plugin from GitHub.]

## Step 5: Start Using It
[Claude will greet you. Tell it your name and project. Ask questions.]

## What You Can Ask
[Organized by role — see examples from Wave 8 testing that actually worked]

## Slash Commands
- /meeting-notes — process a meeting transcript
- /survey-map — map a survey document
- /test-plan — generate a complete test plan
- /survey-doc — convert wireframe to programmer-ready survey doc

## Troubleshooting
[Common issues and fixes]

## Feedback
[How to report issues or request features — tell Nick]

Keep under 3 pages. No jargon. Someone who's never used AI tools should be able to follow it.

OUTPUT 2: _docs/for-nick-maintenance.md

GITHUB SETUP (Nick, after Wave 8): Create private repo 'seurat-tools' under your GitHub account or a seurat-group org. Initialize with: `cd _build/seurat-tools-plugin && git init && git add . && git commit -m 'Initial seurat-tools plugin' && git remote add origin [repo-url] && git push -u origin main`. Share repo access with team members who need plugin installation.

Nick's maintenance reference:
- How to run weekly curation (/curation command)
- How to run daily briefs (/daily-brief command)
- How to run digestion waves (paste the 'Template: Digestion Wave [N]' prompt from Part IX of the build playbook)
- How to add a new client profile (template + example)
- How to add a new pattern or lesson (format + quality criteria)
- How to update the plugin (push to GitHub)
- How to run brain health checks
- How to handle common issues (stale files, broken cross-refs, missing profiles)
```

---

## PART IX: ONGOING OPERATIONS

### Template: Digestion Wave [N]

```
Read CLAUDE.md.
Read: _scripts/output/digestion_priority.md
Run: python _scripts/digestion_engine.py status

Digest the next batch of clients from the priority list.

NOTE: All script commands below assume working directory is the brain root folder.

First, check for changes since last run:
python _scripts/digestion_engine.py scan --changed-only
(This re-scans and identifies files with new content_hash — even previously digested clients may have new content.)

For each of the next 5 unprocessed clients:

1. Extract: python _scripts/digestion_engine.py extract --client "[Name]" --version-min 1.0 --limit 30
   (Downloads via API, extracts, deletes temp files. Skips files already extracted with unchanged content_hash.)
2. Read the extracts
3. Check if clients/[client].md exists — if yes, read it. If no, prepare to create it.
4. Synthesize:
   - Client profile update/creation
   - Pattern evidence (new or additions to existing)
   - Lesson candidates
   - BD signals
   - Theme connections
5. Present to me for approval. Include provenance for every claim.
6. Write approved content. Update cross-references.

Every 3rd wave, do cross-client synthesis:
- Patterns with strengthened evidence?
- New themes emerging?
- Selling intelligence coalescing?
- Process docs that need updating based on what we're seeing?

Check status: python _scripts/digestion_engine.py status
Update digestion_priority.md with progress notes.
```

### Template: Weekly Curation

```
NOTE: All script commands below assume working directory is the brain root folder.

/curation

[The slash command handles the workflow. Nick just invokes it and responds to Claude's questions.]
```

### Template: Project Close-Out

```
Read CLAUDE.md.
Read: clients/[client].md
Read: knowledge/processes/project-close-out.md

We're wrapping up [Project Name] for [Client].

[Claude follows the close-out process: project summary, pattern check, lessons, BD signal, theme connections. Drafts updates. Shows Nick. Writes approved content.]
```

### Template: Monthly Brain Health Review

```
Read CLAUDE.md.

NOTE: All script commands below assume working directory is the brain root folder.

Run: python _scripts/brain_health.py
Read: _scripts/output/brain_health_summary.md

Monthly review:
1. How many files were updated this month? Which folders grew? Which are stagnant?
2. Are there cross-references that broke since last check?
3. Which client profiles are most stale? Should any be archived?
4. Which patterns have the most/least evidence? Any patterns that should be upgraded or retired?
5. How many digestion waves were run? What's the backlog?
   Run: python _scripts/digestion_engine.py status
   Check: files pending vs extracted, any new files since last scan, any previously-extracted files with changed content_hash
6. Are theme hubs still accurate? Any new themes emerging from recent work?
7. Plugin health: any skill issues reported by users?

Write: _docs/monthly-review-[YYYY-MM].md
```

---

## Execution Summary

| Part | Wave | Sessions | What It Delivers |
|------|------|----------|-----------------|
| I | 1 + QG | 1 + test | Architecture, CLAUDE.md, .claude/ config, skeleton, decisions.md |
| II | 2A-C + QG | 3 + 1 | Patterns, lessons, BD intel, client profiles, cross-refs validated |
| III | 3A-C + QG | 3 + test | Process docs (quant, qual, survey, deliverables, discovery, PM, project types, close-out) |
| IV | 4A-B + QG | 2 + test | Dropbox API digestion engine (scan + extract + content hash registry + .dropboxignore) |
| V | 5A-C + QG | 3 + 1 | Active clients digested, theme hubs built, cross-client synthesis, survey content extraction |
| VI | 6A-C + QG | 3 + 1 | Meeting notes + survey pipeline ported, GitHub plugin built, survey pattern library |
| VII | 7A-B + QG | 2 + test | Daily brief system + curation workflow + health monitoring |
| VIII | 8A-B | 2 | Comprehensive testing + setup guide |
| **Total** | | **~25-28** | **Complete firm-wide knowledge + execution system** |

---

## What's Deliberately NOT In This Plan (And Why)

| Excluded | Why | When to Add |
|----------|-----|-------------|
| YAML front-matter on every file | Single-curator system. Adds maintenance friction without benefit. | If multi-curator model adopted |
| Tag taxonomy | Let tags emerge from content organically. Predefined taxonomies constrain. | After 50+ files exist, extract common tags |
| Market briefs (standalone) | Generic market context Claude can research. Market knowledge lives in theme hubs and client profiles where it's contextual. | If theme hubs prove insufficient |
| Automated curation scripts | Weekly manual curation is simpler and higher quality for v1. | After 6 months of manual curation patterns emerge |
| Survey brain SQLite database | Specialized tool, not part of core knowledge brain. | Reintegrate as a plugin when survey pipeline is stable |
| Workbench UI | Deprecated in v1 in favor of Cowork plugin. Plugin is cleaner. | Never — plugin is the right approach |
| Sizing-replicate skill | Not yet production-tested in v1. Port when validated. | After core 5 skills are stable in v2 |
| seurat-wireframe skill | Not functional end-to-end in v1. | After slide bank is validated |
| Local Dropbox sync for ingestion | API stream-and-delete is faster, uses zero disk, tracks changes via content_hash. Local sync requires disk management and can't detect changes efficiently. | Never — API is strictly better for this use case |
| Web browser automation for Dropbox | Lossy (preview rendering strips notes, formatting, hidden content), fragile at scale, slow, auth complexity. The API gives full-fidelity file access. | Only for sources without APIs (competitor websites, etc.) |
| OCR for scanned PDFs | Too slow for batch processing, requires tesseract install. Scanned PDFs are flagged as 'partial' extraction for future handling. | When a specific scanned PDF contains critical knowledge worth the effort |
| Agent mail / inter-agent messaging (MCP Agent Mail) | Plan is designed with parallel-safe waves + quality gates + `_build/decisions.md` for coordination. Adding an MCP server introduces infrastructure overhead (port management, SQLite locks, message delivery) without proportional value for a single-curator build. | Post-build: when autonomous agents run digestion + curation + intelligence in parallel without Nick pasting prompts |
