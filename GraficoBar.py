import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn
import numpy as np
from sys import argv
from os import makedirs
from scipy.stats import iqr

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
                lista1.append(float(linha[3]))
                lista2.append(float(linha[2]))
                lista3.append(linha[1])
            cont = 1

    return lista1, lista2, lista3


def plot_grafico(index_min, index_max, label):
    plt.bar(np.arange(index_min, index_max+1), total[index_min:index_max+1], width=0.6, linewidth=0.55, label=label, zorder=3)
    plt.ylabel("Número de Linhas")
    plt.xlabel("Projetos")
    plt.title("Número Total de Linhas de Projetos na Linguagem " + language, fontsize=10)
    plt.xticks(np.arange(index_min, index_max+1))
    plt.ticklabel_format(style="sci", axis="y", scilimits=(0,0))
    plt.margins(x=0)
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.grid(axis='y', linestyle='-', zorder=0)


valores_codigo, valores_comentarios, projeto = ler_dados(language + "/" + language.replace(" ", "") + "LinhasProjetos.csv")
for i in range(len(projeto)):
    total.append((valores_codigo[i] + valores_comentarios[i]))

total.sort()

try:
    makedirs("Graficos/")
except FileExistsError:
    pass

plot_grafico(0, 59, "Pequenos")
plot_grafico(60, 119, "Medios")
plot_grafico(120, 179, "Grandes")
plot_grafico(180, 199, "Muito Grandes")
plt.legend(loc="upper left", fontsize=8)
plt.savefig("Graficos/" + language.replace(" ", "") + "BarGraphic.png", format='png', dpi=300)
