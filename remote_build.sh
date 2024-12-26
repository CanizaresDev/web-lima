python -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://web-lima.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate