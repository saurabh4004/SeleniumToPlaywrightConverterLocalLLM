@echo off
echo Starting Selenium to Playwright Converter...

echo [1/2] Starting Backend Server (Port 8000)...
start "Backend Server" cmd /k "python -m uvicorn backend.server:app --reload --port 8000"

echo [2/2] Starting Frontend Server (Port 8080)...
start "Frontend Server" cmd /k "python -m http.server 8080 --directory frontend"

echo.
echo ===================================================
echo   🚀 Application is running!
echo   👉 Open your browser at: http://localhost:8080
echo ===================================================
echo.
pause
