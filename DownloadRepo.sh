#!/bin/bash

# languages=("Java" "JavaScript" "C" "C#" "PHP" "Python" "C++" "Visual Basic")
languages=("C")

for language in "${languages[@]}"
do
    #python3 GithubDownload.py "$language" 200
    #python3 MergeLineCount.py "$language"
    ./ExtractionRunner.sh "$language"
done
