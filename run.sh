#!/usr/bin/env bash

set -e

python -mvenv venv
source venv/bin/activate
pip install -r requirements.txt

for f in $(find examples/ -name '*.py'); do
    echo "Running $f..."
    python "$f"
done
