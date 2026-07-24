#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ -z "${PDFDANCER_TOKEN:-}" ]]; then
    echo "PDFDANCER_TOKEN is required to run the examples." >&2
    echo "Export it first, then run ./run.sh again." >&2
    exit 1
fi

python -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install -r requirements.txt

while IFS= read -r file; do
    echo "Running $file..."
    python "$file"
done < <(find examples -type f -name '*.py' ! -name '__init__.py' -print | sort)
