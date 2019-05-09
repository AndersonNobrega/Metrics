#!/bin/bash

# languages=("Java" "JavaScript" "C" "CSharp" "Cpp" "PHP" "Python3" "VisualBasic")
language="$1"

if [[ "$language" = "Python" ]]; then
    language="Python3"
elif [[ "$language" = "C#" ]]; then
	language="CSharp"
elif [[ "$language" = "C++" ]]; then
    language="Cpp"
elif [[ "$language" = "Visual Basic" ]]; then
    language="VisualBasic"
elif [[ "$language" = "PHP" ]]; then
    language="Php"
else
	language="$language"
fi

./DataExtraction.sh "$language"
