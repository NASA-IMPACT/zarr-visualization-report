#!/bin/bash

directory='urls'
mkdir -p results

for file in "$directory"/*; do
    if [ -f "$file" ]; then
        echo "Running tests for $file"
        locust -i 1 --urls-file=$file --csv=results/$(basename ${file%.*})
    fi
done