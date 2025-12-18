#!/bin/bash

output_dir="./ascii_converted/"

mkdir -p "$output_dir"

for file in ./ascii/*.svg; do
    if [ -f "$file" ]; then
        output_file="${output_dir}$(basename "$file")"
        
        "/c/Program Files/Inkscape/bin/inkscape" "$file" --export-type=svg --export-filename="$output_file" --actions="select-all;object-to-path;export-do"
        echo "Processed ${output_file}"
    else
        echo "No SVG files found in the directory."
    fi
done
