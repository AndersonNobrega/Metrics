import matplotlib.pyplot as plt
import csv
from os import makedirs, stat


def ler_dados(arquivo):
    lista1 = []
    lista2 = []
    lista3 = []
    cont = 0

    with open(arquivo, "r", encoding="ISO-8859-1") as arquivo:
        tabela = csv.reader(arquivo)
        for linha in tabela:
            if cont > 0:
                lista1.append(float(linha[6]))
                lista2.append(float(linha[11]))
                lista3.append(float(linha[16]))
            cont = 1

    return lista1, lista2, lista3


def save_file(file_name, languages, result):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        if stat(file_name).st_size == 0:
            file_writer.writerow(["Linguagems", "Diferenca Percentual"])

        file_writer.writerow([languages, "%.2f" % result])


def show_percentage_diff(boxplot, index1, index2):
    ovs = []
    ovs.append(boxplot["boxes"][index1].get_ydata()[0])
    ovs.append(boxplot["boxes"][index1].get_ydata()[2])
    ovs.append(boxplot["boxes"][index2].get_ydata()[0])
    ovs.append(boxplot["boxes"][index2].get_ydata()[2])
    ovs.sort()

    ovs_value = ovs[3] - ovs[0]
    dbm_value = abs(boxplot["medians"][index1].get_ydata()[0] - boxplot["medians"][index2].get_ydata()[0])

    return (dbm_value/ovs_value) * 100

def calculo_equivalencia(data, languages, label):
    fig = plt.figure(1, figsize=(9, 6))

    ax = fig.add_subplot(111)

    bp = ax.boxplot(data)

    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                save_file("Linguagens/BoxplotPercDifference" + label + ".csv", languages[i] + "-" + languages[j],
                        show_percentage_diff(bp, i, j))

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

ntc = [valores_csharp[0], valores_php[0], valores_java[0], valores_vb[0], valores_c[0], valores_js[0]]
ncc = [valores_csharp[1], valores_php[1], valores_java[1], valores_vb[1], valores_c[1], valores_js[1]]
nlc = [valores_csharp[2], valores_php[2], valores_java[2], valores_vb[2], valores_c[2], valores_js[2]]

languages = ["C#", "PHP", "Java", "Visual Basic", "C", "JavaScript"]

calculo_equivalencia(ntc, languages, "NTC")
calculo_equivalencia(ncc, languages, "NCC")
calculo_equivalencia(nlc, languages, "NLC")