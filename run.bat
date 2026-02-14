@echo off
echo Gerenciando ambiente Python...
python -m venv venv
call venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt --quiet

echo Garantindo motor do navegador (Playwright)...
python -m playwright install chromium

echo Abrindo o app e fechando este terminal...
start pythonw main.py

exit