@echo off
REM Navigate to the folder where the Python app is located
cd /d "D:\shewana\email generater and sender"

REM Run the Python app
start cmd /k "python app.py"

REM Wait for the server to start (adjust time as needed)
timeout /t 5 > nul

REM Open the server in the default web browser
start http://127.0.0.1:5000
