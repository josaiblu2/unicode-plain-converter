@echo off
echo ===================================================
echo      Starting Unicode Converter SaaS
echo ===================================================
echo.

echo [1/2] Starting FastAPI Backend on Port 8003...
:: The 'start' command opens a new command prompt window
start "Unicode Converter - Backend" cmd /k "python -m uvicorn src.main:app --port 8003 --reload"

echo [2/2] Starting Astro Frontend...
cd frontend
start "Unicode Converter - Frontend" cmd /k "npm run dev"

echo.
echo ===================================================
echo All services are starting up in separate windows!
echo.
echo - Your API Backend will run on: http://localhost:8003
echo - Your UI Frontend will run on: http://localhost:4321
echo.
echo You can now open http://localhost:4321 in your browser.
echo ===================================================
pause
