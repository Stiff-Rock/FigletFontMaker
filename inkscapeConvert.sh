#!/bin/bash

# Directory where the converted SVG files will be saved
output_dir="/home/yago/Shared/CodeProjects/TextAsciiArtToSvg/ascii_converted/"

# Make sure the output directory exists
mkdir -p "$output_dir"

# Loop through all SVG files in the specified directory
for file in /home/yago/Shared/CodeProjects/TextAsciiArtToSvg/ascii/*.svg; do
    # Check if files exist before processing
    if [ -f "$file" ]; then
        # Define the output file path
        output_file="${output_dir}$(basename "$file")"
        
        # Convert the text to paths and save the result in the output directory
        inkscape "$file" --export-type=svg --export-filename="$output_file" --actions="select-all;object-to-path;export-do"
    else
        echo "No SVG files found in the directory."
    fi
done


