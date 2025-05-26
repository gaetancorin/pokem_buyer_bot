@echo off
REM Vérifie si python est installé
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python n'est pas installé ou n'est pas dans le PATH.
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

REM Définir l'action
set action=buy

REM Lance le programme principal
echo Commande executee : python start_all.py %action%
python start_all.py  %action%
IF %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite pendant l'exécution.
)

REM Désactive l'environnement virtuel à la fin
deactivate

pause