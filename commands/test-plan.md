Run the full survey test plan pipeline using seurat-tools skills.

## Instructions

This command orchestrates the 3-skill survey test plan pipeline:

1. **Survey Mapper** — Ask the user for the survey document (.docx). Read `skills/survey-mapper/SKILL.md`, execute it, produce the Survey Map.
2. **Test Path Generator** — For each row in the test matrix, read `skills/test-path-generator/SKILL.md` and generate a test path. Repeat N times (once per matrix row).
3. **Test Plan Assembler** — Collect all generated test paths, read `skills/test-plan-assembler/SKILL.md`, and assemble the final .docx test plan.

If $ARGUMENTS includes a Survey Map that already exists, skip step 1 and start from step 2.

## Key Details
- Full pipeline: survey-mapper -> test-path-generator (xN) -> test-plan-assembler
- Final output: Complete Survey Test Plan (.docx) with navy blue/orange formatting
- Time saved: 6-10 hours per survey test plan
