@echo off
chcp 65001 > nul
cd /d %~dp0

:: 1. venv (仮想環境) のチェックと自動作成
if exist venv\Scripts\activate.bat (
    echo Virtual environment found. Activating...
    call venv\Scripts\activate.bat
) else (
    echo [Info] Windows compatible venv not found.
    echo Creating new virtual environment...
    python -m venv venv
    
    echo Activating new environment...
    call venv\Scripts\activate.bat
    
    echo Installing Flask...
    pip install flask
)

:: 2. 環境変数の設定
set FLASK_APP=flaskr
set FLASK_ENV=development

:: 3. ブラウザを自動で開く
start "" http://127.0.0.1:5000

:: 4. アプリの起動
echo Starting Flask App (flaskr)...
python -m flask run

:: エラーで落ちたときに画面を残す
if %errorlevel% neq 0 (
    echo.
    echo [Error] The application crashed. Please check the logs above.
    pause
)