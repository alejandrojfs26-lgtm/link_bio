#!/bin/bash
pip install -r requirements.txt
reflex init
API_URL=https://linkbio-backend.up.railway.app/ reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
desactivate
