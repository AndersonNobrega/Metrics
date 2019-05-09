import numpy as np
import matplotlib.pyplot as plt
import csv
from os import makedirs

def read_file(file_path):
    media = []
    mediana = []
    desvio = []
    linguagem = []
    cont = 0

    with open(file_path, "r", encoding="ISO-8859-1") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if cont > 0:
                linguagem.append(linha[0])
                media.append(float(linha[3]))
                mediana.append(float(linha[4]))
                desvio.append(float(linha[5]))
            cont = 1

        return linguagem, media, mediana, desvio


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', fontsize=7)


def plot_grafico(title, save_label, file_path):
    linguagem, media, mediana, desvio = read_file(file_path)

    N = len(linguagem)
    ind = np.arange(N)
    width = 0.2

    p1 = plt.bar(ind, media, width, color="silver", label="Média", zorder=3)
    p2 = plt.bar(ind+width, mediana, width, color="grey", label="Mediana", zorder=3)
    p3 = plt.bar(ind+width*2, desvio, width, color="black", label="Desvio Padrão", zorder=3)

    plt.ylabel("Porcentagem")
    plt.xlabel("Linguagens")
    plt.title(title)
    plt.xticks(ind+width, linguagem, rotation=0, fontsize=10)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='-', zorder=0)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.01), ncol=3, shadow=True, fontsize=6)

    autolabel(p1)
    autolabel(p2)
    autolabel(p3)

    plt.savefig("Graficos/Linguagens" + save_label + ".png", format='png', dpi=300)
    plt.clf()


try:
    makedirs("Graficos/")
except FileExistsError:
    pass


plot_grafico("NTCF/NTTP", "NTCF", "Linguagens/MetricasLinguagensNTCF.csv")
plot_grafico("NTC/NTTP", "NTC", "Linguagens/MetricasLinguagensNTC.csv")
plot_grafico("NCCF/NTCP", "NCCF", "Linguagens/MetricasLinguagensNCCF.csv")
plot_grafico("NCC/NTCP", "NCC", "Linguagens/MetricasLinguagensNCC.csv")
plot_grafico("NLCF/NTLP", "NLCF", "Linguagens/MetricasLinguagensNLCF.csv")
plot_grafico("NLC/NTLP", "NLC", "Linguagens/MetricasLinguagensNLC.csv")

#Gŕafico do Número de Tokens do Codigo Fonte por Range
plot_grafico("NTCF/NTTP em Projetos Pequenos", "ProjPeqNTCF", "Linguagens/ProjPeqMetricasLinguagensNTCF.csv")
plot_grafico("NTCF/NTTP em Projetos Médios", "ProjMedNTCF", "Linguagens/ProjMedMetricasLinguagensNTCF.csv")
plot_grafico("NTCF/NTTP em Projetos Grandes", "ProjGrdNTCF", "Linguagens/ProjGrdMetricasLinguagensNTCF.csv")
plot_grafico("NTCF/NTTP em Projetos Muito Grandes", "ProjMuitoGrdNTCF", "Linguagens/ProjMuitoGrdMetricasLinguagensNTCF.csv")

#Gŕafico do Número de Tokens dos Comentarios por Range
plot_grafico("NTC/NTTP em Projetos Pequenos", "ProjPeqNTC", "Linguagens/ProjPeqMetricasLinguagensNTC.csv")
plot_grafico("NTC/NTTP em Projetos Médios", "ProjMedNTC", "Linguagens/ProjMedMetricasLinguagensNTC.csv")
plot_grafico("NTC/NTTP em Projetos Grandes", "ProjGrdNTC", "Linguagens/ProjGrdMetricasLinguagensNTC.csv")
plot_grafico("NTC/NTTP em Projetos Muito Grandes", "ProjMuitoGrdNTC", "Linguagens/ProjMuitoGrdMetricasLinguagensNTC.csv")

#Gŕafico do Número de Caracteres do Codigo Fonte por Range
plot_grafico("NCCF/NTCP em Projetos Pequenos", "ProjPeqNCCF", "Linguagens/ProjPeqMetricasLinguagensNCCF.csv")
plot_grafico("NCCF/NTCP em Projetos Médios", "ProjMedNCCF", "Linguagens/ProjMedMetricasLinguagensNCCF.csv")
plot_grafico("NCCF/NTCP em Projetos Grandes", "ProjGrdNCCF", "Linguagens/ProjGrdMetricasLinguagensNCCF.csv")
plot_grafico("NCCF/NTCP em Projetos Muito Grandes", "ProjMuitoGrdNCCF", "Linguagens/ProjMuitoGrdMetricasLinguagensNCCF.csv")

#Gŕafico do Número de Caracteres dos Comentarios por Range
plot_grafico("NCC/NTCP em Projetos Pequenos", "ProjPeqNCC", "Linguagens/ProjPeqMetricasLinguagensNCC.csv")
plot_grafico("NCC/NTCP em Projetos Médios", "ProjMedNCC", "Linguagens/ProjMedMetricasLinguagensNCC.csv")
plot_grafico("NCC/NTCP em Projetos Grandes", "ProjGrdNCC", "Linguagens/ProjGrdMetricasLinguagensNCC.csv")
plot_grafico("NCC/NTCP em Projetos Muito Grandes", "ProjMuitoGrdNCC", "Linguagens/ProjMuitoGrdMetricasLinguagensNCC.csv")

#Gŕafico do Número de Linhas de Codigo Fonte por Range
plot_grafico("NLCF/NTLP em Projetos Pequenos", "ProjPeqNLCF", "Linguagens/ProjPeqMetricasLinguagensNLCF.csv")
plot_grafico("NLCF/NTLP em Projetos Médios", "ProjMedNLCF", "Linguagens/ProjMedMetricasLinguagensNLCF.csv")
plot_grafico("NLCF/NTLP em Projetos Grandes", "ProjGrdNLCF", "Linguagens/ProjGrdMetricasLinguagensNLCF.csv")
plot_grafico("NLCF/NTLP em Projetos Muito Grandes", "ProjMuitoGrdNLCF", "Linguagens/ProjMuitoGrdMetricasLinguagensNLCF.csv")

#Gŕafico do Número de Linhas de Comentarios por Range
plot_grafico("NLC/NTLP em Projetos Pequenos", "ProjPeqNLC", "Linguagens/ProjPeqMetricasLinguagensNLC.csv")
plot_grafico("NLC/NTLP em Projetos Médios", "ProjMedNLC", "Linguagens/ProjMedMetricasLinguagensNLC.csv")
plot_grafico("NLC/NTLP em Projetos Grandes", "ProjGrdNLC", "Linguagens/ProjGrdMetricasLinguagensNLC.csv")
plot_grafico("NLC/NTLP em Projetos Muito Grandes", "ProjMuitoGrdNLC", "Linguagens/ProjMuitoGrdMetricasLinguagensNLC.csv")