import matplotlib.pyplot as plt
import csv
from os import makedirs


def ler_dados(arquivo):
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    cont = 0

    with open(arquivo, "r", encoding="ISO-8859-1") as arquivo:
        tabela = csv.reader(arquivo)
        for linha in tabela:
            if cont > 0:
                lista1.append(float(linha[5]))
                lista2.append(float(linha[6]))
                lista3.append(float(linha[10]))
                lista4.append(float(linha[11]))
                lista5.append(float(linha[15]))
                lista6.append(float(linha[16]))
            cont = 1

    return lista1, lista2, lista3, lista4, lista5, lista6

def plot_grafico(title, data, languages, label):
    fig = plt.figure(1, figsize=(9, 6))

    ax = fig.add_subplot(111)

    bp = ax.boxplot(data, zorder=3)

    ax.set_xticklabels(languages)
    ax.get_yaxis().tick_left()
    plt.xlabel("Linguagens")
    plt.title(title)
    plt.grid(axis="y", linestyle="-", zorder=0)
    fig.savefig("Graficos/Linguagens" + label + "Boxplot.png", bbox_inches="tight", dpi=300)
    plt.clf()

valores_csharp = ler_dados("C#/C#Metricas.csv")
valores_php = ler_dados("PHP/PHPMetricas.csv")
valores_java = ler_dados("Java/JavaMetricas.csv")
valores_vb = ler_dados("Visual Basic/VisualBasicMetricas.csv")
valores_c = ler_dados("C/CMetricas.csv")
valores_js = ler_dados("JavaScript/JavaScriptMetricas.csv")

try:
    makedirs("Linguagens/")
except FileExistsError:
    pass

ntcf = [valores_csharp[0], valores_php[0], valores_java[0], valores_vb[0], valores_c[0], valores_js[0]]
ntc = [valores_csharp[1], valores_php[1], valores_java[1], valores_vb[1], valores_c[1], valores_js[1]]
nccf = [valores_csharp[2], valores_php[2], valores_java[2], valores_vb[2], valores_c[2], valores_js[2]]
ncc = [valores_csharp[3], valores_php[3], valores_java[3], valores_vb[3], valores_c[3], valores_js[3]]
nlcf = [valores_csharp[4], valores_php[4], valores_java[4], valores_vb[4], valores_c[4], valores_js[4]]
nlc = [valores_csharp[5], valores_php[5], valores_java[5], valores_vb[5], valores_c[5], valores_js[5]]

languages = ["C#", "PHP", "Java", "Visual Basic", "C", "JavaScript"]

plot_grafico("NTCF/NTTP", ntcf, languages, "NTCF")
plot_grafico("NTC/NTTP", ntc, languages, "NTC")
plot_grafico("NCCF/NTCP", nccf, languages, "NCCF")
plot_grafico("NCC/NTCP", ncc, languages, "NCC")
plot_grafico("NLCF/NTLP", nlcf, languages, "NLCF")
plot_grafico("NLC/NTLP", nlc, languages, "NLC")