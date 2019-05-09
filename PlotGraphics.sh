#!/bin/bash

languages=("Java" "C#" "PHP" "Visual Basic" "C")

for language in "${languages[@]}"
do
    python3 GraficoBar.py "$language"
    python3 GraficoRange.py "$language"
    python3 GraficoHist.py "$language"
done
