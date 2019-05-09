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
    values_ntcf = []
    values_ntc = []
    values_nccf = []
    values_ncc = []
    values_nlcf = []
    values_nlc = []
    cont = 0

    with open(path_file, "r", encoding="ISO-8859-1") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if cont > 0:
                values_ntcf.append(float(linha[5]))
                values_ntc.append(float(linha[6]))
                values_nccf.append(float(linha[10]))
                values_ncc.append(float(linha[11]))
                values_nlcf.append(float(linha[15]))
                values_nlc.append(float(linha[16]))
            cont = 1

    return values_ntcf, values_ntc, values_nccf, values_ncc, values_nlcf, values_nlc


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


values_ntcf, values_ntc, values_nccf, values_ncc, values_nlcf, values_nlc = read_file(language + "/" + language.replace(" ", "") + "Metricas.csv")

try:
    makedirs("Linguagens/")
except FileExistsError:
    pass

save_file("Linguagens/MetricasLinguagensNTCF.csv", language, retorna_resultados(values_ntcf))
save_file("Linguagens/MetricasLinguagensNTC.csv", language, retorna_resultados(values_ntc))
save_file("Linguagens/MetricasLinguagensNCCF.csv", language, retorna_resultados(values_nccf))
save_file("Linguagens/MetricasLinguagensNCC.csv", language, retorna_resultados(values_ncc))
save_file("Linguagens/MetricasLinguagensNLCF.csv", language, retorna_resultados(values_nlcf))
save_file("Linguagens/MetricasLinguagensNLC.csv", language, retorna_resultados(values_nlc))