@echo off
title Seurat Tools - One-Time Setup
color 0F
echo.
echo  ============================================
echo       Seurat Tools - One-Time Setup
echo  ============================================
echo.
echo  This will set up everything you need.
echo  It only needs to run once.
echo.
pause

:: Check for Node.js
echo.
echo  [1/5] Checking for Node.js...
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  ERROR: Node.js is not installed.
    echo  Please install it from: https://nodejs.org
    echo  Download the LTS version, run the installer, then run this setup again.
    echo.
    pause
    exit /b 1
)
echo         Found Node.js.

:: Check for Python
echo  [2/5] Checking for Python...
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    where python3 >nul 2>nul
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo  ERROR: Python is not installed.
        echo  Please install it from: https://www.python.org/downloads/
        echo  Check "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    )
)
echo         Found Python.

:: Install python-docx
echo  [3/5] Installing python-docx...
pip install python-docx -q 2>nul || pip3 install python-docx -q 2>nul
echo         Done.

:: Install Claude Code CLI
echo  [4/5] Installing Claude Code CLI...
where claude >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    npm install -g @anthropic-ai/claude-code
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo  ERROR: Could not install Claude Code.
        echo  Try running this as administrator.
        echo.
        pause
        exit /b 1
    )
) else (
    echo         Claude Code already installed.
)

:: Install the Seurat Tools plugin
echo  [5/5] Installing Seurat Tools plugin...
call claude /install-plugin Nsf34/seurat-tools 2>nul

:: Create the workspace folder
if not exist "%USERPROFILE%\Seurat Survey Builder" mkdir "%USERPROFILE%\Seurat Survey Builder"

:: Create CLAUDE.md in workspace
echo --- > "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo # Seurat Survey Builder >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo. >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo You are the Seurat Survey Builder. Your job is to convert survey wireframes into >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo programmer-ready survey documents. >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo. >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo When the user provides a wireframe file path: >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo 1. Run the seurat-tools:survey-wireframe-to-doc skill >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo 2. Read ALL reference files before writing anything >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo 3. Save the output to the user's Downloads folder >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo. >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"
echo If the user drags in a file or pastes a path, immediately begin the conversion. >> "%USERPROFILE%\Seurat Survey Builder\CLAUDE.md"

:: Create the desktop shortcut launcher
(
echo @echo off
echo title Seurat Survey Builder
echo color 0F
echo cd /d "%%USERPROFILE%%\Seurat Survey Builder"
echo echo.
echo echo   =============================================
echo echo        Seurat Survey Builder
echo echo   =============================================
echo echo.
echo echo   How to use:
echo echo     1. Paste the path to your wireframe .docx
echo echo     2. Say "build survey doc from this wireframe"
echo echo     3. The finished doc will appear in Downloads
echo echo.
echo echo   Type /quit to exit when done.
echo echo   =============================================
echo echo.
echo claude
) > "%USERPROFILE%\Desktop\Seurat Survey Builder.bat"

echo.
echo  ============================================
echo       Setup Complete!
echo  ============================================
echo.
echo  A shortcut called "Seurat Survey Builder"
echo  has been added to your Desktop.
echo.
echo  Double-click it to start building survey docs.
echo.
echo  IMPORTANT: You will need to log in to Claude
echo  the first time you open it. After that, it
echo  remembers you.
echo.
pause
