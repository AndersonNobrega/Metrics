#!/bin/bash

language="$1"
dir="$2"

if [[ "$language" = "VisualBasic" ]]; then
    language="Visual Basic"
fi

search_dir="$language"
dir_path="$search_dir"/"$dir"

if [[ "$language" = "C" ]] || [[ "$language" = "C++" ]]; then
    ./cloc --csv --report-file="$dir_path".csv --include-lang="$language","C/C++ Header" "$dir_path"
else 
    ./cloc --csv --report-file="$dir_path".csv --include-lang="$language" "$dir_path"
fi
