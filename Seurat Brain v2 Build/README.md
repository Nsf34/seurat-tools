# Seurat Brain v2 Build

## What's Here

| File | What It Is |
|------|-----------|
| `seurat-brain-v2-build-playbook.md` | **THE PLAYBOOK** — complete build plan with paste-ready prompts for every session (~25-28 sessions, 8 parts) |
| `reference--ai-initiatives-brief.md` | Strategic context — why Seurat is building an AI operating layer |
| `reference--client-folder-extraction-plan.md` | Earlier extraction plan — useful context for Wave 4-5 digestion approach |
| `reference--pepsi-knowledge-example.md` | Example of structured client knowledge capture — shows what client.md files should look like |

## How to Use

1. Read the playbook start to finish (it's long — ~2300 lines — but every line matters)
2. Complete Pre-Work (15 min — create folder, set up Dropbox API token)
3. Open a Claude Code / Cowork window
4. Paste Wave 1 prompt → execute → pass quality gate → proceed to Wave 2
5. Waves marked PARALLEL can run in up to 3 simultaneous windows
6. Quality gates between every major phase — all tests must pass before proceeding

## Key Design Decisions

- **Dropbox API** for file ingestion (not local sync) — zero disk pressure, content hash tracking
- **decisions.md** for cross-session coordination — agents log forks, future sessions adapt
- **Survey pattern library** — digestion extracts reusable questions, scales, flows to power survey tools
- **Single curator (Nick)** — everyone else reads via Dropbox sync

## Dependencies

- Old seurat-brain (personal Dropbox) — read-only reference for migration
- Firm Dropbox — API access for digestion
- Python + packages: dropbox, python-pptx, python-docx, pdfminer.six, openpyxl, PyPDF2
