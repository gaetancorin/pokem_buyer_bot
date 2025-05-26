@echo off
REM Vérifie si python est installé
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python n'est pas installe ou n'est pas dans le PATH.
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
echo Liste des fichiers disponibles dans le dossier config :
for %%f in (config\*.ini) do (
    echo   %%~nxf
)

REM === Demande à l'utilisateur d'en choisir un ===
echo.
echo --- --- --- ---
set /p config_number="Entrez le numero d un fichier config.ini a utiliser (ex: 2 pour config2.ini) : "

REM Construit le nom du fichier à partir du numéro
set "config_file=config%config_number%.ini"

REM Vérifie si le fichier existe
if not exist "config\%config_file%" (
    echo Le fichier "config\%config_file%" n'existe pas.
    pause
    exit /b 1
)

REM Définir l'action
set action=choose_pickup_point

REM Lance le programme principal
echo Commande executee : python start_one.py %config_number% %action%
python start_one.py %config_number% %action%
IF %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite pendant l'exécution.
)

REM Désactive l'environnement virtuel à la fin
deactivate

pause