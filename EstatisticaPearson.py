import csv
from sys import argv
from os import makedirs, stat
import scipy.stats as stats

language = argv[1]

def read_file(path_file):
    values_ntc = []
    values_ncc = []
    values_nlc = []
    cont = 0

    with open(path_file, "r", encoding="ISO-8859-1") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if cont > 0:
                values_ntc.append(float(linha[6]))
                values_ncc.append(float(linha[11]))
                values_nlc.append(float(linha[16]))
            cont = 1

    return values_ntc, values_ncc, values_nlc


def retorna_resultados(ntc, ncc, nlc):
    a = stats.pearsonr(ntc, ncc)
    b = stats.pearsonr(ntc, nlc)
    c = stats.pearsonr(ncc, nlc)

    return [a[0], a[1], b[0], b[1], c[0], c[1]]


def save_file(file_name, language, results):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        if stat(file_name).st_size == 0:
            file_writer.writerow(["Linguagem", "NTC-NCC", "NTC-NCC:p-value", "NTC-NLC", 
                                "NTC-NLC:p-value", "NCC-NLC", "NCC-NLC:p-value"])

        file_writer.writerow([language, "%.6f" % results[0], "%g" % results[1], "%.6f" % results[2], 
                            "%g" % results[3], "%.6f" % results[4], "%g" % results[5]])


values_ntc, values_ncc, values_nlc = read_file(language + "/" + language.replace(" ", "") + "Metricas.csv")

try:
    makedirs("Linguagens/")
except FileExistsError:
    pass

save_file("Linguagens/MetricasPearsonLinguagens.csv", language, retorna_resultados(values_ntc, values_ncc, values_nlc))