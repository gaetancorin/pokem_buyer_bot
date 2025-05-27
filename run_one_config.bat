@echo off
REM Vérifie si python est installé
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed or not in the PATH.
    pause
    exit /b 1
)

REM Crée l'environnement virtuel (si pas déjà créé)
if not exist ".venv" (
    python -m venv .venv
)

REM Active l'environnement virtuel
call .venv\Scripts\activate.bat

REM Installe les dépendances depuis requirements.txt
pip install --upgrade pip
pip install -r requirements.txt


REM === Affiche tous les fichiers .ini du dossier config ===
echo.
echo List of files available in the config folder:
for %%f in (config\*.ini) do (
    echo   %%~nxf
)

REM === Demande à l'utilisateur d'en choisir un ===
echo.
echo --- --- --- ---
set /p config_number="Enter the number of a config.ini file to use (ex: 2 for config2.ini). The example file is not allowed:"

REM Construit le nom du fichier à partir du numéro
set "config_file=config%config_number%.ini"

REM Vérifie si le fichier existe
if not exist "config\%config_file%" (
    echo The file "config\%config_file%" does not exist.
    pause
    exit /b 1
)

REM Définir l'action
set action=buy

REM Lance le programme principal
echo Command executed: python start_one.py %config_number% %action%
python start_one.py %config_number% %action%
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during execution.
)

REM Désactive l'environnement virtuel à la fin
deactivate

pause