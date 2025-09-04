@echo off
:: ==========================================
::   Py++ Setup Script with UAC Elevation
:: ==========================================

:: Check for admin rights
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo Installing Py++...

:: Get current folder (where setup.bat + pypp folder is)
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "PYPP_INTERPRETER=%SCRIPT_DIR%\pypp\cli.py"

:: Make sure cli.py exists
if not exist "%PYPP_INTERPRETER%" (
    echo ERROR: Could not find interpreter at %PYPP_INTERPRETER%
    pause
    exit /b
)

:: Create registry keys
reg add "HKCR\.pypp" /ve /d "PyppFile" /f
reg add "HKCR\PyppFile" /ve /d "Py++ Source File" /f
if exist "%SCRIPT_DIR%\logo.ico" (
    reg add "HKCR\PyppFile\DefaultIcon" /ve /d "\"%SCRIPT_DIR%\logo.ico\"" /f
)
reg add "HKCR\PyppFile\shell\open\command" /ve /d "\"cmd.exe\" /k \"python \"%PYPP_INTERPRETER%\" \"%%1\"\"" /f

echo.
echo Association complete! .pypp files will now open in a cmd window using Py++.
echo.

pause
