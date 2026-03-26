---
description: Convert a survey wireframe to a programmer-ready survey document
---

Convert a survey wireframe to a programmer-ready survey document using the seurat-tools survey-wireframe-to-doc skill.

## Instructions

1. Ask the user for the wireframe (.docx with Topic | Questions | Response Options | Objective table) if not provided as $ARGUMENTS.
2. Read the full `skills/survey-wireframe-to-doc/SKILL.md`.
3. Execute the skill exactly as documented, producing a formatted .docx survey document.
4. Save the output .docx to the user's Downloads folder.

## Key Details
- Output: .docx with Seurat formatting, numbering, piping, logic, programming notes
- Uses survey_doc_builder.py engine for generation
- Standalone skill — not part of the test plan pipeline
