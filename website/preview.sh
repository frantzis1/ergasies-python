#!/usr/bin/env bash
# Simple helper script to preview the static site locally.
# Usage: ./preview.sh [port]
set -euo pipefail
PORT="${1:-8000}"
echo "Starting local preview server on http://localhost:${PORT}" 
python3 -m http.server "${PORT}" --directory "$(dirname "$0")"

