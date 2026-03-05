Clean meeting notes using the seurat-tools meeting-notes skill.

## Instructions

1. Ask the user for the transcript file and any supplementary inputs (raw notes, deck, etc.) if not already provided as $ARGUMENTS.
2. Read the full `skills/meeting-notes/SKILL.md` and all files in `skills/meeting-notes/references/`.
3. Execute the skill exactly as documented — follow every formatting rule, section structure, and learned preference.
4. Generate the output as a .docx file using python-docx, placed in the same directory as the input transcript.

## Key Details
- Output format: .docx with Franklin Gothic Book 11pt, tight spacing
- Sections: Title, Attendees, Next Steps, Key Takeaways, Full Notes
- Always check `skills/meeting-notes/references/learned-preferences.md` for user-refined style rules
