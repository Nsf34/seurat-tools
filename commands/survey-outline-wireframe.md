---
description: Convert a survey outline or rough quant planning document into a client-facing survey wireframe
---

Convert a survey outline into a survey wireframe using the seurat-tools survey-outline-to-wireframe skill.

## Instructions

1. Ask the user for the survey outline `.docx` if not provided as `$ARGUMENTS`.
2. Read the full `skills/survey-outline-to-wireframe/SKILL.md`.
3. Execute the skill exactly as documented, producing one final formatted `.docx` wireframe.
4. Save the output `.docx` alongside the input outline unless the user provides an explicit output path.

## Key Details

- Output: one client-facing `.docx` survey wireframe in the current Merck three-column format
- Uses deterministic rendering helpers in `skills/survey-outline-to-wireframe/scripts/`
- Standalone workflow: converts rough outlines, planning docs, and shells into wireframes
