#!/bin/bash
set -Eeuo pipefail
cd /app
pip install -r requirements.txt
echo "=== VENV LOCATION ==="
find / -name "uvicorn" -type f 2>/dev/null
