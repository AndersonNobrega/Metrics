#!/bin/bash

language="$1"
language_dir=""

if [[ "$language" = "Python3" ]]; then
    language_dir="Python"
elif [[ "$language" = "CSharp" ]]; then
	language_dir="C#"
elif [[ "$language" = "VisualBasic" ]]; then
    language_dir="Visual Basic"
elif [[ "$language" = "Cpp" ]]; then
    language_dir="C++"
elif [[ "$language" = "Php" ]]; then
    language_dir="PHP"
else
	language_dir="$language"
fi

search_dir="$language_dir"

for dir in "$search_dir"/*
do
	if [[ -d "$dir" ]]; then
		path=$( basename "${dir}" )
		java -Xss32m -Xms1024m -Xmx8192m -jar VocabularyExtractor_Generic.jar -lang "$language" -n "$path" -d "$language_dir"/"$path"/ -f Project_Metrics/"$language"/
		python3 Tokenize.py Project_Metrics/"$language"/Tokens/"$path"
		rm -rf "$language_dir"/"$path"/
	fi
done 
