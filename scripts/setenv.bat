@echo off
set PROJECT_DIR=%~dp0..
echo Project Root Directory: %PROJECT_DIR%
set SCRIPTS_DIR=%PROJECT_DIR%\scripts
echo Scripts Directory: %SCRIPTS_DIR%
set VENV_DIR=%PROJECT_DIR%\venv\oproof
echo Virtual Environment Directory: %VENV_DIR%
call %VENV_DIR%\Scripts\activate
setx PROJECT_DIR %PROJECT_DIR%
setx SCRIPTS_DIR %SCRIPTS_DIR%
setx VENV_DIR %VENV_DIR%
