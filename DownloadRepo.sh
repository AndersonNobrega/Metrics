#!/bin/bash

# languages=("Java" "JavaScript" "C" "C#" "PHP" "Python" "C++" "Visual Basic")
languages=("Java" "C#" "PHP" "Visual Basic" "C" "JavaScript")

for language in "${languages[@]}"
do
    python3 GithubDownload.py "$language" 200
    python3 MergeLineCount.py "$language"
    python3 MergeCSV.py "$language"
done
