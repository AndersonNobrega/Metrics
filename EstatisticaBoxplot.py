import matplotlib.pyplot as plt
import csv
from os import makedirs, stat

def ler_dados(file_name):
    ntc = []
    ncc = []
    nlc = []
    cont = 0

    with open(file_name, "r", encoding="ISO-8859-1") as csv_file:
        table = csv.reader(csv_file)
        for line in table:
            if cont > 0:
                ntc.append(float(line[6]))
                ncc.append(float(line[11]))
                nlc.append(float(line[16]))
            cont = 1

    return ntc, ncc, nlc


def save_file(file_name, label, results):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        if stat(file_name).st_size == 0:
            file_writer.writerow(["Metrica", "C#-PHP", "C#-Java", "C#-VisualBasic", "C#-C", "PHP-Java", 
                                "PHP-VisualBasic", "PHP-C", "Java-VisualBasic", "Java-C", "VisualBasic-C"])

        file_writer.writerow([label, "%.2f" % results[0], "%.2f" % results[1], "%.2f" % results[2], 
                            "%.2f" % results[3], "%.2f" % results[4], "%.2f" % results[5],
                            "%.2f" % results[6], "%.2f" % results[7], "%.2f" % results[8],
                            "%.2f" % results[9]])


def calcula_diff_percentual(data, label):
    fig = plt.figure(1, figsize=(9, 6))

    ax = fig.add_subplot(111)

    bp = ax.boxplot(data)

    boxes = []
    for box in bp["boxes"]:
        boxes.append([box.get_ydata()[0], box.get_ydata()[2]])
    
    ovs = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            temp = [boxes[i][0], boxes[i][1], boxes[j][0], boxes[j][1]]
            temp.sort()
            ovs.append(temp[-1] - temp[0]) 

    medians = []
    for medline in bp["medians"]:
        medians.append(medline.get_ydata()[0])

    bdm = []
    for i in range(len(medians)):
        for j in range(i+1, len(medians)):
            bdm.append(abs(medians[i] - medians[j]))

    diff = []
    for i in range(len(ovs)):
        diff.append((bdm[i] / ovs[i]) * 100)
    
    save_file("Linguagens/MetricasLinguagensBoxplot.csv", label, diff)

    plt.clf()


valores_csharp = ler_dados("C#/C#Metricas.csv")
valores_php = ler_dados("PHP/PHPMetricas.csv")
valores_java = ler_dados("Java/JavaMetricas.csv")
valores_vb = ler_dados("Visual Basic/VisualBasicMetricas.csv")
valores_c = ler_dados("C/CMetricas.csv")

try:
    makedirs("Linguagens/")
except FileExistsError:
    pass

ntc = [valores_csharp[0], valores_php[0], valores_java[0], valores_vb[0], valores_c[0]]
ncc = [valores_csharp[1], valores_php[1], valores_java[1], valores_vb[1], valores_c[1]]
nlc = [valores_csharp[2], valores_php[2], valores_java[2], valores_vb[2], valores_c[2]]

languages = ["C#", "PHP", "Java", "Visual Basic", "C"]

calcula_diff_percentual(ntc, "NTC")
calcula_diff_percentual(ncc, "NCC")
calcula_diff_percentual(nlc, "NLC")