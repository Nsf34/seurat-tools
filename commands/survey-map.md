---
description: Map a survey document to produce a structured Survey Map
---

Map a survey document using the seurat-tools survey-mapper skill.

## Instructions

1. Ask the user for the survey document (.docx) if not provided as $ARGUMENTS.
2. Read the full `skills/survey-mapper/SKILL.md`.
3. Read the entire survey document — every question, every response option, every routing instruction.
4. Execute the skill exactly as documented, producing a complete Survey Map (.md).
5. Save the Survey Map to the same directory as the input survey document.

## Key Details
- Output: Structured .md Survey Map with variable registry, categories, routing, show conditions
- This is step 1 of the 3-skill survey test plan pipeline
- Next step: Use `/seurat-tools:test-path` to generate one path from this map, or `/seurat-tools:test-plan` for the full pipeline
