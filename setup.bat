@echo off
:: Run as Administrator!

echo Installing Py++...

:: Create folder for PyPP
set PYPP_DIR=%~dp0pypp
if not exist "%PYPP_DIR%" mkdir "%PYPP_DIR%"

:: Copy cli.py and interpreter.py into System32\pypp
xcopy /Y "%~dp0cli.py" "%PYPP_DIR%\"
xcopy /Y "%~dp0interpreter.py" "%PYPP_DIR%\"

:: Detect Python path
for /f "tokens=*" %%i in ('where python') do set PYTHON_PATH=%%i
echo Python found at: %PYTHON_PATH%

:: File association
assoc .pypp=PyPPFile
ftype PyPPFile="%PYTHON_PATH%" "%PYPP_DIR%\cli.py" "%%1"

echo Association complete! .pypp files will now open with Py++.
pause
