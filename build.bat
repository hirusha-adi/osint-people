@echo off
REM Set the script name (change if your script filename is different)
set SCRIPT_NAME=osint_people
set PYTHON_FILE=osint_people.py

echo Building executable...
pyinstaller --onefile --name=%SCRIPT_NAME% %PYTHON_FILE%

echo Cleaning up unnecessary files...
REM Remove the build directory
rmdir /s /q build

REM Remove the .spec file
del %SCRIPT_NAME%.spec

echo Build complete. The executable is located at: dist\%SCRIPT_NAME%.exe
