#!/bin/bash

languages=("Java" "C#" "PHP" "Visual Basic" "C" "JavaScript")

./PlotGraphics.sh

for language in "${languages[@]}"
do
    python3 EstatisticaLinguagens.py "$language"
    python3 EstatisticaLinguagensRange.py "$language"
    python3 EstatisticaPearson.py "$language"
done

python3 GraficoLinguagens.py
python3 GraficoBoxplot.py
python3 EstatisticaBoxplot.py