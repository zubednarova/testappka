#!/bin/bash
set -Eeuo pipefail
cd /app
pip install -r requirements.txt --break-system-packages
