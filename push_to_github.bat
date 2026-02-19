@echo off
echo checking for git...
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git is not installed or not in your PATH.
    echo Please install Git from https://git-scm.com/downloads and try again.
    pause
    exit /b
)

echo Initializing Git repository...
git init
git add .
git commit -m "Initial commit: Selenium to Playwright Converter"
git branch -M main
REM Remove origin if it exists to avoid errors on re-run
git remote remove origin >nul 2>nul
git remote add origin https://github.com/saurabh4004/SeleniumToPlaywrightConverterLocalLLM.git

echo Pushing to GitHub...
git push -u origin main

if %errorlevel% neq 0 (
    echo Failed to push. You might need to authenticate or check prompt.
) else (
    echo Successfully pushed code to GitHub!
)
pause
