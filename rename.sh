#!/bin/bash

# Prompting user for input
read -p "Enter the new base name: " base_name

count=1
for file in Whats*.jpeg IMG*.JPG; do
    if [[ -f "$file" ]]; then
        # Determine the original file's extension
        extension="${file##*.}"  # Gets the extension (JPEG or JPG)

        # Create the new name while preserving the original extension
        new_name="${base_name}_foto_${count}.${extension,,}" 
	mv "$file" "$new_name"
        ((count++))
    fi
done
