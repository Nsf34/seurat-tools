# Seurat Survey Builder — Setup Guide

## What This Does
Converts a survey wireframe (.docx) into a fully formatted, programmer-ready survey document.
You give it a wireframe, it gives you a finished survey doc in your Downloads folder.

## One-Time Setup (5 minutes)

### Prerequisites
You need two things installed first. If you already have them, skip to step 3.

1. **Node.js** — Download from https://nodejs.org (click the big green LTS button, run the installer)
2. **Python** — Download from https://www.python.org/downloads/ (run installer, CHECK the box that says "Add Python to PATH")

### Install
3. Double-click **`install.bat`** in this folder
4. It will install everything automatically
5. When it finishes, you'll have a **"Seurat Survey Builder"** icon on your Desktop

### First Launch
6. Double-click **"Seurat Survey Builder"** on your Desktop
7. It will ask you to log in to Claude — follow the prompts (one-time only)
8. Once logged in, you're ready to go

## Daily Use

1. **Double-click** "Seurat Survey Builder" on your Desktop
2. A chat window opens
3. **Type something like:**
   - `Build a survey doc from this wireframe: C:\Users\YourName\Downloads\My Wireframe v1.0.docx`
   - Or: `Convert this wireframe to a survey document` and then paste the file path when asked
4. **Wait 3-5 minutes** — Claude reads the wireframe, builds the questions, generates the formatted doc
5. **Find your doc** in your Downloads folder

## Tips
- You can drag a file from Explorer into the chat window to paste its path
- If something looks wrong in the output, just tell Claude what to fix — it can re-run
- The chat remembers your conversation, so you can iterate
- Type `/quit` to close when you're done

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "node is not recognized" | Install Node.js and restart your computer |
| "python is not recognized" | Install Python (check "Add to PATH") and restart |
| Claude asks to log in every time | This is normal the first few times |
| The doc looks wrong | Tell Claude specifically what's wrong and ask it to fix it |
| Nothing happens for a long time | The wireframe-to-doc conversion takes 3-5 min — be patient |
