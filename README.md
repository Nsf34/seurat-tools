# Seurat Tools — Claude Cowork Plugin

Seurat Group's consulting toolkit for Claude. Automates survey test plans, survey outline to
wireframe generation, survey document generation, and supporting internal research workflows.

## Core Commands

| Command | What It Does | Output |
|---------|-------------|--------|
| **test-plan** | Run the full survey test plan pipeline | .docx |
| **survey-outline-wireframe** | Survey outline -> client-facing wireframe | .docx |
| **survey-doc** | Wireframe -> programmer-ready survey doc | .docx |

## Install

```
/plugin marketplace add Nsf34/seurat-tools
/plugin install seurat-tools@seurat-tools-marketplace
```

## Usage

After installing, use these top-level slash commands:

- `/seurat-tools:test-plan` — Run the full survey test plan pipeline (all 3 steps)
- `/seurat-tools:survey-outline-wireframe` — Convert a survey outline into a client-facing wireframe
- `/seurat-tools:survey-doc` — Convert wireframe to programmer-ready survey doc

## Internal Skills

The plugin still contains modular internal skills so multi-step workflows remain reliable:

| Skill | Purpose | Typical Output |
|-------|---------|----------------|
| **meeting-notes** | Transcript -> polished notes workflow | .docx |
| **survey-mapper** | Survey doc -> structured Survey Map | .md |
| **test-path-generator** | Survey Map + matrix row -> path | .txt |
| **test-plan-assembler** | All paths -> final test plan | .docx |
| **survey-outline-to-wireframe** | Outline -> client-facing wireframe | .docx |
| **survey-wireframe-to-doc** | Wireframe -> programmer-ready survey doc | .docx |

These skills support the main commands and can still be used directly for debugging or custom runs.

## Requirements

- Claude Pro/Team plan with Cowork access
- python-docx (`pip install python-docx`) for .docx output generation

## Survey Test Plan Pipeline

The test plan is a 3-step pipeline that runs in sequence:

```
survey-mapper -> test-path-generator (x N rows) -> test-plan-assembler
```

1. `survey-mapper` reads the survey and creates the Survey Map
2. `test-path-generator` runs once per matrix row against the Survey Map
3. `test-plan-assembler` collects all paths into the final formatted .docx

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
