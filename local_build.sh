#!/bin/bash
source .venv/bin/activate
pip install --upgrade pip
pip install --break-system-packages -r requirements.txt
rm -rf public
reflex init
API_URL=https://linkbio-backend.up.railway.app/ reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
