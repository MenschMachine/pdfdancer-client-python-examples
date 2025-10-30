#!/usr/bin/env bash

set -e
for f in $(find examples/ -name '*.py'); do
    echo "Running $f..."
    python "$f"
done
