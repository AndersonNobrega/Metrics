import numpy as np
import csv
from sys import argv
from os import makedirs, stat

minimo = []
maximo = []
media = []
mediana = []
desvio = []
language = argv[1]

def read_file(path_file):
    values = []
    cont = 0

    with open(path_file, "r", encoding="ISO-8859-1") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if cont > 0:
                values.append([float(linha[5]), float(linha[6]), float(linha[10]), float(linha[11]), 
                                int(linha[14]), float(linha[15]), float(linha[16])])
            cont = 1

    return values


def retorna_resultados(valores):
    resultado_min = np.min(valores)
    resultado_max = np.max(valores)
    resultado_media = np.mean(valores)
    resultado_mediana = np.median(valores)
    resultado_desvio = np.std(valores)

    return resultado_min, resultado_max, resultado_media, resultado_mediana, resultado_desvio


def save_file(file_name, language, results):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        if stat(file_name).st_size == 0:
            file_writer.writerow(["Linguagem", "Minimo", "Maximo", "Media","Mediana", "Desvio Padrao"])

        file_writer.writerow([language, "%.2f" % results[0], "%.2f" % results[1], "%.2f" % results[2], 
                            "%.2f" % results[3], "%.2f" % results[4]])


values = read_file(language + "/" + language.replace(" ", "") + "Metricas.csv")
values.sort(key=lambda x: x[4])

try:
    makedirs("Linguagens/")
except FileExistsError:
    pass


#Número de Tokens do Codigo Fonte por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNTCF.csv", language, retorna_resultados([value[0] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNTCF.csv", language, retorna_resultados([value[0] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNTCF.csv", language, retorna_resultados([value[0] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNTCF.csv", language, retorna_resultados([value[0] for value in values[90:100]]))

#Número de Tokens dos Comentarios por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNTC.csv", language, retorna_resultados([value[1] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNTC.csv", language, retorna_resultados([value[1] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNTC.csv", language, retorna_resultados([value[1] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNTC.csv", language, retorna_resultados([value[1] for value in values[90:100]]))

#Número de Caracteres do Codigo Fonte por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNCCF.csv", language, retorna_resultados([value[2] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNCCF.csv", language, retorna_resultados([value[2] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNCCF.csv", language, retorna_resultados([value[2] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNCCF.csv", language, retorna_resultados([value[2] for value in values[90:100]]))

#Número de Caracteres dos Comentarios por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNCC.csv", language, retorna_resultados([value[3] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNCC.csv", language, retorna_resultados([value[3] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNCC.csv", language, retorna_resultados([value[3] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNCC.csv", language, retorna_resultados([value[3] for value in values[90:100]]))

#Número de Linhas de Codigo Fonte por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNLCF.csv", language, retorna_resultados([value[5] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNLCF.csv", language, retorna_resultados([value[5] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNLCF.csv", language, retorna_resultados([value[5] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNLCF.csv", language, retorna_resultados([value[5] for value in values[90:100]]))

#Número de Linhas de Comentarios por Range
save_file("Linguagens/ProjPeqMetricasLinguagensNLC.csv", language, retorna_resultados([value[6] for value in values[0:30]]))
save_file("Linguagens/ProjMedMetricasLinguagensNLC.csv", language, retorna_resultados([value[6] for value in values[30:60]]))
save_file("Linguagens/ProjGrdMetricasLinguagensNLC.csv", language, retorna_resultados([value[6] for value in values[60:90]]))
save_file("Linguagens/ProjMuitoGrdMetricasLinguagensNLC.csv", language, retorna_resultados([value[6] for value in values[90:100]]))