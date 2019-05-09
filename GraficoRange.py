import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn
import numpy as np
from sys import argv
from os import makedirs

total = []
language = argv[1]


def ler_dados(arquivo):
    lista1 = []
    lista2 = []
    lista3 = []
    cont = 0

    with open(arquivo, "r", encoding="ISO-8859-1") as arquivo:
        tabela = csv.reader(arquivo)
        for linha in tabela:
            if cont > 0:
                lista1.append(int(linha[3]))
                lista2.append(int(linha[2]))
                lista3.append(linha[1])
            cont = 1

    return lista1, lista2, lista3


def plot_grafico(index_min, index_max, label):
    plt.bar(np.arange(index_min, index_max+1), total[index_min:index_max+1], width=0.6, linewidth=0.55, edgecolor="black", zorder=3)
    plt.ylabel("Número de Linhas")
    plt.xlabel("Projetos")
    plt.title("Número Total de Linhas de Projetos " + label + " na Linguagem " + language, fontsize=8)
    plt.xticks(np.arange(index_min, index_max+1))
    plt.ticklabel_format(style="sci", axis="y", scilimits=(0,0))
    plt.margins(x=0)
    plt.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=False)
    plt.grid(axis='y', linestyle='-', zorder=0)
    plt.savefig("Graficos/" + language.replace(" ", "") + "BarGraphic" + label.replace(" ", "") + ".png", format='png', dpi=300)
    plt.clf()


valores_codigo, valores_comentarios, projeto = ler_dados(language + "/" + language.replace(" ", "") + "LinhasProjetos.csv")
for i in range(len(projeto)):
    total.append((valores_codigo[i] + valores_comentarios[i]))

total.sort()

try:
    makedirs("Graficos/")
except FileExistsError:
    pass

plot_grafico(0, 59, "Pequenos") #0, 59
plot_grafico(60, 119, "Medios") #60, 119
plot_grafico(120, 179, "Grandes") #120, 179
plot_grafico(180, 199, "Muito Grandes") # 180, 199
