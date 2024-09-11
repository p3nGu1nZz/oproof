@echo off
call %~dp0\setenv.bat
echo Current Directory: %cd%
cd %PROJECT_DIR%
echo New Current Directory: %cd%
pip install -e .
timeout /t 0.25 >nul
cls
oproof "What is 2 + 2?" "4" %*
