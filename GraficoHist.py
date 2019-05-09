import numpy as np
import csv
from sys import argv
from os import makedirs, stat
import matplotlib.pyplot as plt

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


def plot_grafico(path, language, values, label):
    plt.hist(values, zorder=3)
    plt.ylabel("Quantidade de Projetos")
    plt.xlabel(label)
    plt.title("Histograma da Linguagem " + language, fontsize=10)
    plt.grid(axis='y', linestyle='-', zorder=0)
    plt.savefig(path, format='png', dpi=300)
    plt.clf()


values_ntcf, values_ntc, values_nccf, values_ncc, values_nlcf, values_nlc = read_file(language + "/" + language.replace(" ", "") + "Metricas.csv")

try:
    makedirs("Graficos/")
except FileExistsError:
    pass

plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNTCF.png", language, values_ntcf, "NTCF/NTTP")
plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNTC.png", language, values_ntc, "NTCF/NTTP")
plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNCCF.png", language, values_nccf, "NCCF/NTCP")
plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNCC.png", language, values_ncc, "NCC/NTCP")
plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNLCF.png", language, values_nlcf, "NLCF/NTLP")
plot_grafico("Graficos/" + language.replace(" ", "") + "HistogramNLC.png", language, values_nlc, "NLC/NTLP")