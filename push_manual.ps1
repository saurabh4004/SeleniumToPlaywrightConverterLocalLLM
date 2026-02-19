$GIT = "C:\Program Files\Git\cmd\git.exe"

Write-Host "Initializing Git..."
& $GIT init

Write-Host "Adding files..."
& $GIT add .

Write-Host "Committing..."
& $GIT commit -m "Initial commit: Selenium to Playwright Converter"

Write-Host "Setting main branch..."
& $GIT branch -M main

Write-Host "Adding remote..."
# Remove existing remote if any to avoid errors
& $GIT remote remove origin
& $GIT remote add origin https://github.com/saurabh4004/SeleniumToPlaywrightConverterLocalLLM.git

Write-Host "Pushing to GitHub..."
& $GIT push -u origin main
