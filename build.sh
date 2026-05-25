#!/bin/bash
source .venv/bin/activate
pip install --upgrade pip
pip install --break-system-packages -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip

