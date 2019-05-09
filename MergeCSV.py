import csv
from sys import argv
from os import stat, remove

projects = {}
cont = 0
language = argv[1]

with open(language + "/" + language.replace(" ", "") + "Metrics.csv", "r") as csv_file:
        file_reader = csv.reader(csv_file)
        for line in file_reader:
            if cont > 0:
                language = line[0]
                projects[line[1]] = []
                for i in range(len(line)):
                    if i >= 2:
                        projects[line[1]].append(line[i])
            cont += 1

cont = 0

with open(language + "/" + language.replace(" ", "") + "LinhasProjetos.csv", "r") as csv_file:
    file_reader = csv.reader(csv_file)
    for line in file_reader:
        if cont > 0:
            line_code = int(line[3])
            line_comments = int(line[2])
            total = line_code + line_comments

            code_percentage = (line_code / total) * 100
            comment_percentage = (line_comments / total) * 100

            projects[line[1]].append(line_code)
            projects[line[1]].append(line_comments)
            projects[line[1]].append(total)
            projects[line[1]].append(code_percentage)
            projects[line[1]].append(comment_percentage)
        cont = 1

#remove("C#/C#Metrics.csv")
#remove("C#/C#LinhasProjetos.csv")

with open(language + "/" + language.replace(" ", "") + "Metricas.csv", "a+") as csv_file:
    file_writer = csv.writer(csv_file)

    if stat(language + "/" + language.replace(" ", "") + "Metricas.csv").st_size == 0:
        file_writer.writerow(["Linguagem", "Projeto", "Numero de Tokens de Codigo Fonte (Excluindo Tokens de Comentario)",
                            "Numero de Tokens apenas dos Comentarios", "Numero Total de Tokens do Projeto", "NTCF/NTTP (%)", 
                            "NTC/NTTP (%)", "Numero de Caracteres de Codigo Fonte (Excluindo Caracteres de Comentario)",
                            "Numero de Caracteres apenas dos Comentarios", "Numero Total de Carateres do Projeto", "NCCF/NTCP (%)",
                            "NCC/NTCP (%)", "Numero de Linhas de Codigo Fonte (Excluindo Linhas de Comentario)", 
                            "Numero de Linhas apenas do Comentarios", "Numero Total de Linhas do Projeto", "NLCF/NTLP (%)", "NLC/NTLP (%)"])

    for project in projects:
        file_writer.writerow([language, project, projects[project][0], projects[project][1], projects[project][2], projects[project][3], 
                            projects[project][4], projects[project][5], projects[project][6], projects[project][7], projects[project][8],
                            projects[project][9], projects[project][10], projects[project][11], projects[project][12], "%.2f" % projects[project][13], 
                            "%.2f" % projects[project][14]])
