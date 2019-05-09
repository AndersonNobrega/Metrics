#!/bin/bash

language="$1"

if [[ "$language" = "VisualBasic" ]]; then
    language="Visual Basic"
fi

search_dir="$language"

for dir in "$search_dir"/*
do
    if [[ -d ${dir} ]]; then
        if [[ "$language" = "C" ]] || [[ "$language" = "C++" ]]; then
            ./cloc --csv --report-file="$dir".csv --include-lang="$language","C/C++ Header" "$dir"
        else 
            ./cloc --csv --report-file="$dir".csv --include-lang="$language" "$dir"
        fi
    fi
done