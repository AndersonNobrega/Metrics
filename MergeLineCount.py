from os import listdir, remove, stat
from os.path import isfile, join, expanduser, splitext
from sys import argv
import csv

code_line_values = []
comment_line_values = []
projects = []
languages = []
language = argv[1]

home_path = expanduser("~")
path = language
quant_projetos = 0

only_csv_files = [f for f in listdir(path) if isfile(join(path, f)) and join(path, f).endswith(".csv") and 
                f != (language.replace(" ", "") + "GitMetrics.csv") and f != (language.replace(" ", "") + "Metrics.csv") and
                f != (language.replace(" ", "") + "Metricas.csv")]

for file in only_csv_files:
    path_file = join(path, file)
    projects.append(splitext(file)[0])

    with open(path_file, "r") as csv_file:
        file_reader = csv.reader(csv_file)
        cont = 0

        code_line_values.append(0)
        comment_line_values.append(0)
        for line in file_reader:
            if cont > 0:
                code_line_values[quant_projetos] += int(line[4])
                comment_line_values[quant_projetos] += int(line[3])
            cont += 1

    quant_projetos += 1

    remove(path_file)


with open(path + "/" + language.replace(" ", "") + "LinhasProjetos.csv", "a+") as csv_file:
    file_writer = csv.writer(csv_file)

    if stat(path + "/" + language.replace(" ", "") + "LinhasProjetos.csv").st_size == 0:
        file_writer.writerow(["Linguagem", "Projetos", "Linhas de Comentario", "Linhas de Codigo"])

    for index in range(len(projects)):
        file_writer.writerow([language, projects[index], comment_line_values[index], code_line_values[index]])
