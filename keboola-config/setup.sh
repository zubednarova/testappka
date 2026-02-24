#!/bin/bash
set -Eeuo pipefail
echo "=== PWD ==="
pwd
echo "=== FIND VENV ==="
find / -name "pyvenv.cfg" 2>/dev/null
