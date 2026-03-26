@echo off
:: Syncs the latest seurat-tools from the git repo to the Claude Code plugin cache.
:: Run this after any git push, or set it as a pre-launch step.

set REPO=C:\Users\NickFisher\seurat-tools
set MARKETPLACE=%USERPROFILE%\.claude\plugins\marketplaces\seurat-tools-marketplace
set CACHE=%USERPROFILE%\.claude\plugins\cache\seurat-tools-marketplace\seurat-tools

:: Pull latest from git
cd /d "%REPO%"
git pull origin master 2>nul

:: Sync to marketplace
xcopy /E /Y /Q "%REPO%\skills" "%MARKETPLACE%\skills\" >nul 2>nul
xcopy /E /Y /Q "%REPO%\commands" "%MARKETPLACE%\commands\" >nul 2>nul
xcopy /E /Y /Q "%REPO%\.claude-plugin" "%MARKETPLACE%\.claude-plugin\" >nul 2>nul
xcopy /E /Y /Q "%REPO%\setup" "%MARKETPLACE%\setup\" >nul 2>nul
copy /Y "%REPO%\README.md" "%MARKETPLACE%\README.md" >nul 2>nul

:: Sync to all cached versions
for /d %%v in ("%CACHE%\*") do (
    xcopy /E /Y /Q "%REPO%\skills" "%%v\skills\" >nul 2>nul
    xcopy /E /Y /Q "%REPO%\commands" "%%v\commands\" >nul 2>nul
    xcopy /E /Y /Q "%REPO%\.claude-plugin" "%%v\.claude-plugin\" >nul 2>nul
)

echo [seurat-tools] Plugin synced to latest.
