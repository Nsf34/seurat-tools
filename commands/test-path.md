---
description: Generate one survey test path from an existing Survey Map and one test matrix row
---

Generate a single survey test path using the seurat-tools test-path-generator skill.

## Instructions

1. Ask the user for the Survey Map `.md` and the specific matrix row input if not provided as `$ARGUMENTS`.
2. Read the full `skills/test-path-generator/SKILL.md`.
3. Execute the skill exactly as documented, producing one path `.txt` file.
4. Save the path output alongside the Survey Map or matrix inputs unless the user specifies another location.

## Key Details

- Output: one `.txt` path in Seurat Group's exact path format
- This is step 2 of the 3-step survey test plan pipeline
- Use `/seurat-tools:survey-map` first if the Survey Map does not exist yet
- Use `/seurat-tools:test-plan` when the goal is the full multi-path final plan rather than a single path
