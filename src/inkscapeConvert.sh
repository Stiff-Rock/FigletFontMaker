#!/bin/bash

output_dir="./ascii_converted/"

mkdir -p "$output_dir"

for file in ./ascii/*.svg; do
    if [ -f "$file" ]; then
        output_file="${output_dir}$(basename "$file")"
        
        inkscape "$file" --export-type=svg --export-filename="$output_file" --actions="select-all;object-to-path;export-do"
    else
        echo "No SVG files found in the directory."
    fi
done
