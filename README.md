# Seurat Tools — Claude Code Plugin

Seurat Group's consulting toolkit for Claude Code. Automates survey workflows, meeting notes,
and CPG intelligence operations.

## Commands

| Command | What It Does | Output |
|---------|-------------|--------|
| `/test-plan` | Full survey test plan pipeline (map, paths, assemble) | .docx |
| `/survey-outline-wireframe` | Survey outline to client-facing wireframe | .docx |
| `/survey-doc` | Wireframe to programmer-ready survey document | .docx |
| `/daily-brief` | Scan CPG newsletters + Twitter, write daily intelligence brief | .md |
| `/daily-newsletter` | Generate Outlook-ready HTML newsletter from daily brief | .html |

## Install

```
/plugin marketplace add Nsf34/seurat-tools
/plugin install seurat-tools@seurat-tools-marketplace
```

## Usage

After installing, prefix commands with `seurat-tools:`:

```
/seurat-tools:test-plan
/seurat-tools:daily-brief
/seurat-tools:daily-newsletter
```

## Skills

Modular skills that power the commands above. Can be used directly for debugging or custom runs.

| Skill | Purpose | Output |
|-------|---------|--------|
| meeting-notes | Transcript to polished Seurat meeting notes | .docx |
| survey-mapper | Survey doc to structured Survey Map | .md |
| test-path-generator | Survey Map + matrix row to single test path | .txt |
| test-plan-assembler | All paths to final formatted test plan | .docx |
| survey-outline-to-wireframe | Outline to client-facing wireframe | .docx |
| survey-wireframe-to-doc | Wireframe to programmer-ready survey doc | .docx |
| daily-brief | Newsletter inbox + Twitter scan to daily intelligence brief | .md |
| daily-newsletter | Daily brief to branded HTML newsletter (daily or weekly format) | .html |

## Survey Test Plan Pipeline

Three-step pipeline that runs in sequence:

```
survey-mapper -> test-path-generator (x N rows) -> test-plan-assembler
```

1. `survey-mapper` reads the survey and creates the Survey Map
2. `test-path-generator` runs once per matrix row against the Survey Map
3. `test-plan-assembler` collects all paths into the final formatted .docx

## Intelligence Pipeline

Two-step pipeline for CPG monitoring:

```
daily-brief -> daily-newsletter
```

1. `daily-brief` scans newsletter inbox (Gmail MCP) and Twitter (bird CLI), processes and files insights
2. `daily-newsletter` curates the brief into a branded HTML email (Mon-Thu = daily pulse, Friday = weekly digest)

## Requirements

- Claude Code
- python-docx (`pip install python-docx`) for .docx generation
- Gmail MCP server (for daily-brief newsletter scanning)
- bird CLI (for daily-brief Twitter scanning)
- Outlook (for daily-newsletter email delivery)

## Updates

```
/plugin update seurat-tools
```
