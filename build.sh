#!/bin/bash
uv pip install -r requirements.txt
uv run reflex init
API_URL=https://linkbio-backend.up.railway.app/ uv run reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
