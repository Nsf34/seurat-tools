# Client Folder Deep Extraction Plan
## Systematic approach to mining every file for insights

---

## The Problem

The Seurat Brain DB currently stores **survey questions only** — 10 surveys, 414 questions. But client folders contain far more intelligence than just survey docs: strategy decks, sizing models, fieldwork data, deliverable presentations, SOWs, meeting notes, wireframes, and more. Right now, all of that knowledge is locked inside individual files across Dropbox with no way to search, cross-reference, or reuse it.

## The Goal

Build a **complete knowledge extraction system** that processes every file in a client folder and produces:

1. A structured inventory of every file (what it is, what it contains)
2. Extracted insights, findings, and recommendations (tagged and searchable)
3. Survey questions fed into the existing Brain DB
4. Sizing data, market figures, and strategic frameworks captured for reuse
5. A queryable knowledge base that makes past work instantly accessible

---

## Phase 1: Inventory & File Classification

**What:** Recursively scan every file in the downloaded client folder and build a master manifest.

**How:**

1. **Walk the folder tree** and log every file with:
   - Full path, filename, extension, size, modified date
   - Folder depth position (which subfolder level tells us the file's purpose)

2. **Classify by folder convention** — Seurat folders follow a consistent `## Category` numbering pattern:
   - `00 New Business` → pitches, proposals, SOWs
   - `01`–`XX` Project folders → the actual work
   - `02 Wireframe` → survey wireframes and early drafts
   - `03 Discovery` → exploratory research, store visits, secondary data
   - `04 Meetings & Deliverables` → final decks, client presentations
   - `05 Fieldwork` → data collection, tabs, raw data
   - `06 Qual` → qualitative research guides, transcripts
   - `07 Quant` → survey docs, programming specs, data
   - `08`+ → varies by project (Campfire sessions, etc.)

3. **Classify by file type + naming patterns:**
   | Type | Signals | Value |
   |------|---------|-------|
   | Survey Document (.docx) | "Survey Document", "Wireframe", "Screener" in name | Questions, response options, methodology |
   | Deliverable Deck (.pptx) | "v1.0", "Final", in Meetings/Deliverables folder | Key findings, recommendations, sizing |
   | Sizing Model (.xlsx) | "Sizing", "Model", "Analysis" in name | Market data, financial figures, growth projections |
   | Data/Tabs (.xlsx) | "Tabs", "Data", "Crosstabs" in name | Raw survey results, cross-tabulated data |
   | SOW/Proposal (.docx/.pdf) | "SOW", "Proposal", in New Business folder | Scope, objectives, methodology, pricing |
   | Qual Guide (.docx) | "Discussion Guide", "Moderator Guide" in name | Research questions, consumer language |
   | Meeting Notes (.docx) | "Notes", "Recap", "Debrief" in name | Action items, decisions, client feedback |
   | Content/Stimuli (.pptx/.pdf) | "Stimulus", "Concept", "Board" in name | Concepts tested, creative assets |

4. **Output:** `manifest.csv` with columns: `file_path, filename, extension, size_kb, modified_date, folder_category, file_purpose, extraction_priority, status`

**Priority scoring:**
- Deliverable decks = 10 (highest value — these are polished findings)
- Survey documents = 9 (structured questions, feed into Brain DB)
- Sizing models = 9 (quantified insights)
- Data/tabs = 7 (raw data to validate and cross-reference)
- SOWs = 6 (project context and objectives)
- Qual guides = 6 (research framing)
- Other = 3

---

## Phase 2: Tiered Extraction by File Type

Different file types require fundamentally different extraction approaches.

### 2A: PowerPoint Decks (.pptx) — The Gold Mine

Deliverable decks are the single richest source because they contain the team's distilled thinking. Extraction approach:

1. **Extract all slide text + speaker notes** using python-pptx
2. **Classify each slide** by type:
   - Title/divider slide → section structure
   - Findings slide → contains insight text, data points, charts
   - Recommendation slide → strategic guidance
   - Methodology/approach slide → how work was done
   - Appendix → supporting detail
3. **Pull key elements:**
   - Slide titles and subtitles (these often ARE the insights)
   - Bulleted text on findings slides
   - Chart titles and callout boxes (often contain the "so what")
   - Speaker notes (often contain richer context than slide text)
4. **Identify "insight slides"** — look for language patterns:
   - Quantified claims: percentages, dollar figures, growth rates
   - Action language: "should", "opportunity", "recommend", "key finding"
   - Comparative language: "vs.", "compared to", "outperforms"

### 2B: Word Documents (.docx) — Surveys & Reports

1. **Survey Documents** (already partially covered by Brain DB pipeline):
   - Extract using existing `extract_docx_from_tracker.py` approach
   - Parse questions with `draft_question_candidates.py`
   - Normalize with `normalize_question_candidates.py`
   - Feed into Brain DB

2. **Non-survey Word docs** (SOWs, reports, guides):
   - Extract full text
   - Identify document type from content patterns
   - Pull structured elements: objectives, scope, methodology, key findings
   - For qual guides: extract discussion topics, probe areas, stimuli descriptions

### 2C: Excel Files (.xlsx) — Data & Models

1. **Read sheet names** — these reveal the file's structure
2. **Read headers (row 1-3)** of each sheet — reveals what data is captured
3. **For sizing models:**
   - Identify key output cells (often labeled "Total", "Size of Prize", "Opportunity")
   - Capture market size figures, growth rates, share data
   - Note assumptions and methodology
4. **For data tabs/crosstabs:**
   - Identify question labels (these should match Brain DB questions)
   - Capture sample sizes and base descriptions
   - Note any standout data points flagged by the team (colored cells, annotations)
5. **For tracking/admin spreadsheets:**
   - Lower priority, but capture project timelines, team assignments, budgets

### 2D: PDFs — Reports & Forms

1. Extract text using pdfplumber or similar
2. Classify: is this a deliverable report, a vendor document, an external source?
3. For Seurat-authored PDFs: extract like PPTX (these are often exported decks)
4. For external sources: capture title, source, key data points cited

---

## Phase 3: Intelligence Extraction & Structuring

This is where we go beyond raw text to structured, queryable knowledge.

### 3A: Insight Extraction

For each file (especially deliverable decks and reports), extract:

| Field | Description | Example |
|-------|-------------|---------|
| `insight_text` | The actual finding or insight | "67% of grass seed buyers purchase based on seasonal need, not brand loyalty" |
| `insight_type` | Classification | consumer_behavior, market_sizing, competitive, strategic_recommendation |
| `data_point` | Any quantified claim | "67%", "$1.2B", "3x growth" |
| `source_file` | Where this came from | "01 Grass Seed Architecture/04 Meetings/Final Deck v1.0.pptx" |
| `slide_or_page` | Specific location | Slide 14 |
| `client` | Client name | Central Garden & Pet |
| `brand` | Brand if applicable | Pennington |
| `project` | Project name | Grass Seed Architecture |
| `category` | Topic category | lawn_care, grass_seed, seasonal_purchase |
| `date` | When this was produced | 2025-06 |
| `confidence` | How confident is the extraction | high (explicit finding) vs. medium (inferred) |

### 3B: Framework Extraction

Seurat projects often use recurring strategic frameworks. Capture these:
- Category architecture maps
- Consumer segmentation models
- Purchase decision trees (P2P)
- Growth driver frameworks
- Competitive landscape assessments

### 3C: Cross-Project Linkage

Tag insights so they can be found across clients:
- **By category:** lawn care, pet, cleaning, food & bev, personal care
- **By research construct:** awareness, trial, purchase intent, loyalty, satisfaction
- **By methodology:** quant survey, qual interviews, ethnography, store visits
- **By business question:** sizing, segmentation, positioning, innovation, category management

---

## Phase 4: Database Schema Extension

Extend the existing Brain DB with new tables:

```sql
-- New: Store extracted insights from any file type
CREATE TABLE insight (
  insight_id TEXT PRIMARY KEY,
  source_file_path TEXT NOT NULL,
  source_location TEXT,  -- slide number, page, cell reference
  client_name TEXT,
  brand_name TEXT,
  project_name TEXT,
  insight_type TEXT,  -- finding, recommendation, data_point, framework
  insight_text TEXT NOT NULL,
  data_point TEXT,  -- quantified element if any
  confidence TEXT DEFAULT 'medium',
  category TEXT,
  date_produced TEXT,
  extracted_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- New: Store file manifest
CREATE TABLE file_manifest (
  file_id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_path TEXT NOT NULL UNIQUE,
  filename TEXT,
  extension TEXT,
  size_kb REAL,
  modified_date TEXT,
  folder_category TEXT,
  file_purpose TEXT,
  extraction_status TEXT DEFAULT 'pending',
  extraction_priority INTEGER,
  client_name TEXT,
  project_name TEXT,
  notes TEXT
);

-- New: Store sizing/market data specifically
CREATE TABLE market_data (
  data_id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_file_path TEXT,
  client_name TEXT,
  brand_name TEXT,
  metric_name TEXT,  -- e.g., "Category Size", "Brand Share", "Growth Rate"
  metric_value TEXT,
  metric_unit TEXT,  -- $, %, units, etc.
  time_period TEXT,
  geography TEXT,
  data_source TEXT,  -- Nielsen, IRI, survey, etc.
  notes TEXT,
  extracted_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- New: Tag insights for cross-referencing
CREATE TABLE insight_tag (
  insight_id TEXT NOT NULL,
  tag_id INTEGER NOT NULL,
  PRIMARY KEY (insight_id, tag_id),
  FOREIGN KEY (insight_id) REFERENCES insight(insight_id),
  FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
);
```

---

## Phase 5: Execution Plan for Central Garden & Pet (Pennington)

### Step 1: Unzip & Build Manifest (5 min)
- Unzip the downloaded file
- Run folder scan script to produce `manifest.csv`
- Review file counts and types

### Step 2: High-Priority Extraction — Deliverable Decks (30-60 min)
- Process all PPTX files in `04 Meetings & Deliverables` folders
- Extract slide text, notes, and classify slides
- Pull out key insights and recommendations
- This is where 80% of the value lives

### Step 3: Survey Document Extraction (20 min)
- Process all survey docs in `07 Quant / 07 Survey Document` folders
- Run through existing Brain DB pipeline
- Load into survey + question tables

### Step 4: Sizing Model Extraction (20 min)
- Process XLSX files with "Sizing", "Model", "Analysis" in name
- Capture market figures, assumptions, outputs
- Load into market_data table

### Step 5: Supporting Files (15 min)
- SOWs → capture project objectives and scope
- Qual guides → capture research questions
- Meeting notes → capture key decisions

### Step 6: Quality Review & Tagging (15 min)
- Spot-check extracted insights against source files
- Add category tags
- Flag any extraction errors or gaps

### Step 7: Repeat for Next Client
- Move to next client folder alphabetically
- Same process, refining extraction scripts as we go

---

## What Makes This Better Than the Current Approach

| Current State | Proposed State |
|---------------|---------------|
| Only survey questions captured | All file types extracted |
| Manual discovery of past work | Searchable knowledge base |
| 10 surveys, 414 questions | Every insight across every project |
| Text-only extraction | Structured insights with metadata |
| No sizing data captured | Market figures queryable by category |
| No cross-project search | Tagged insights findable across clients |
| Survey-focused pipeline only | Multi-format extraction (pptx, docx, xlsx, pdf) |

---

## Technical Requirements

- **python-pptx** — for extracting slide content
- **python-docx** (or existing zipfile approach) — for Word docs
- **openpyxl** — for Excel files
- **pdfplumber** — for PDF text extraction
- **SQLite** — extend existing Brain DB
- **Claude** — for intelligent classification of slide types, insight extraction, and tagging (the parts that require judgment, not just text extraction)

---

## Key Design Decisions

1. **Claude-in-the-loop for insight extraction:** Raw text extraction is mechanical, but deciding "is this an insight?" requires judgment. The plan uses Claude to classify and extract insights from slide text, rather than relying only on regex/rules.

2. **Preserve source lineage:** Every extracted element traces back to a specific file, slide, or cell. This means anyone can verify or go deeper on any insight.

3. **Build on existing infrastructure:** The Brain DB, its schema, and its pipeline scripts are the foundation. We extend rather than replace.

4. **Client-at-a-time processing:** Process one client folder completely before moving to the next. This allows refinement of extraction quality as we go.

5. **Prioritize deliverable decks:** These contain the team's best thinking and are worth 10x the extraction effort of raw data files. Always process these first within any client folder.
