# Seurat Tools — Claude Cowork Plugin

Seurat Group's consulting toolkit for Claude. Automates meeting notes, survey test plans, survey outline to wireframe generation, and survey document generation.

## What's Inside

| Skill | What It Does | Output | Time Saved |
|-------|-------------|--------|------------|
| **meeting-notes** | Transcript -> polished Seurat meeting notes | .docx | 45-60 min/meeting |
| **survey-outline-to-wireframe** | Survey outline -> client-facing wireframe | .docx | 1-3 hrs/study |
| **survey-mapper** | Survey doc -> structured Survey Map | .md | 1-2 hrs/survey |
| **test-path-generator** | Survey Map + matrix row -> test path | .txt | 30-60 min/path |
| **test-plan-assembler** | All test paths -> complete test plan | .docx | 1-2 hrs/plan |
| **survey-wireframe-to-doc** | Wireframe -> programmer-ready survey doc | .docx | 2-4 hrs/survey |

## Install

```
/plugin marketplace add Nsf34/seurat-tools
/plugin install seurat-tools@seurat-tools-marketplace
```

## Usage

After installing, use the slash commands:

- `/seurat-tools:meeting-notes` — Clean meeting notes from a transcript
- `/seurat-tools:survey-outline-wireframe` — Convert a survey outline into a client-facing wireframe
- `/seurat-tools:survey-map` — Map a survey document (step 1 of test plan pipeline)
- `/seurat-tools:test-path` — Generate one path from an existing Survey Map + matrix row
- `/seurat-tools:test-plan` — Run the full survey test plan pipeline (all 3 steps)
- `/seurat-tools:survey-doc` — Convert wireframe to programmer-ready survey doc

## Requirements

- Claude Pro/Team plan with Cowork access
- python-docx (`pip install python-docx`) for .docx output generation

## Survey Test Plan Pipeline

The test plan is a 3-step pipeline that runs in sequence:

```
survey-mapper -> test-path-generator (x N rows) -> test-plan-assembler
```

1. Feed your survey .docx to survey-mapper to get the Survey Map
2. test-path-generator runs once per matrix row against the Survey Map
3. test-plan-assembler collects all paths into the final formatted .docx

## Survey Outline Wireframe Workflow

Use `/seurat-tools:survey-outline-wireframe` when the input is not yet a survey wireframe.

This workflow:

1. Reads the survey outline or rough quant planning document
2. Preserves the study-specific section architecture
3. Drafts missing questions aggressively
4. Renders one final client-facing `.docx` wireframe in the Merck three-column format

## Updates

This plugin syncs from GitHub. When skills are updated, run:

```
/plugin update seurat-tools
```
