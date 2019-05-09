import nltk
from sys import argv
import csv
from os import stat, system, name
from os.path import expanduser
import logging

logging.basicConfig(filename="tool.log", level=logging.DEBUG)

symbols_list = ["&&", "->", ">=", "<=", "<<", ">>", "!="]
quotes_list = ["'", "\""]
visual_basic_tokens = ["End If", "End Sub", "End With", "End Select", "End Function", "End Property"]
home_path = expanduser("~")


def create_tokens(text):
    tokens = [nltk.word_tokenize(tokens) for tokens in text]

    return tokens


def treat_token_left(token):
    if token[0:3] == "/**":
        if len(token) != 3:
            return token[0:3] + "\n" + token[3:]
        return token
    elif token[0:2] == "/*":
        if len(token) != 2:
            return token[0:2] + "\n" + token[2:]
        return token
    elif token[0:3] == "///":
        if len(token) != 3:
            return token[0:3] + "\n" + token[3:]
        return token
    elif token[0:2] == "//":
        if len(token) != 2:
            return token[0:2] + "\n" + token[2:]
        return token
    return token


def treat_token_right(token):
    if token[-3:] == "**/":
        if len(token) != 3:
            return token[:-3] + "\n" + token[-3:]
        return token
    elif token[-2:] == "*/":
        if len(token) != 2:
            return token[:-2] + "\n" + token[-2:]
        return token
    return token


def read_file(file_path):
    with open(file_path, "r", encoding="ISO-8859-1") as file:
        tokens = []
        for line in file:
            tokens.append(line)

    return tokens


def comments_metrics(text):
    count_caracteres = 0
    count_tokens = 0

    for line in text:
        for token in line:
            token = treat_token_left(token)
            token = treat_token_right(token)
            token = token.split("\n")
            count_tokens += len(token)
            for element in token:
                count_caracteres += len(element)

    return count_tokens, count_caracteres


def code_metrics(text, language):
    count_caracteres = 0
    count_tokens = 0

    for line in text:
        line = line.rstrip("\n")
        if line != "" and not line.isspace():
            if language == "Visual Basic":
                if line in visual_basic_tokens:
                    count_caracteres += len(line) - 1
                    count_tokens += 2
                else:
                    count_caracteres += len(line)
                    count_tokens += 1
            else:
                count_caracteres += len(line)
                count_tokens += 1

    return count_tokens, count_caracteres


def save_file(file_name, lang, project, tokens_comments, char_comments, tokens_code, char_code):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        vocabulary = tokens_code + tokens_comments
        char_total = char_code + char_comments

        tcod_percentage = (tokens_code / vocabulary) * 100
        tcmn_percentage = (tokens_comments / vocabulary) * 100
        ccod_percentage = (char_code / char_total) * 100
        ccmn_percentage = (char_comments / char_total) * 100

        if stat(file_name).st_size == 0:
            file_writer.writerow(
                ["Linguagem", "Projeto", "Numero de Tokens de Codigo Fonte (Excluindo Tokens de Comentario)",
                 "Numero de Tokens apenas dos Comentarios",
                 "Numero Total de Tokens do Projeto", "NTCF/NTTP (%)", "NTC/NTTP (%)",
                 "Numero de Caracteres de Codigo Fonte (Excluindo Caracteres de Comentario)",
                 "Numero de Caracteres apenas dos Comentarios", "Numero Total de Carateres do Projeto", "NCCF/NTCP (%)",
                 "NCC/NTCP (%)"])

        logging.info([lang, project, tokens_code, tokens_comments, vocabulary, "%.2f" % tcod_percentage,
                      "%.2f" % tcmn_percentage, char_code, char_comments, char_total,
                      "%.2f" % ccod_percentage, "%.2f" % ccmn_percentage])

        file_writer.writerow([lang, project, tokens_code, tokens_comments, vocabulary, "%.2f" % tcod_percentage,
                              "%.2f" % tcmn_percentage, char_code, char_comments, char_total,
                              "%.2f" % ccod_percentage, "%.2f" % ccmn_percentage])


try:
    path = argv[1].split("/")
    projects = path[-1]
    language = path[-3]

    if language == "CSharp":
        language = "C#"
    elif language == "VisualBasic":
        language = "Visual Basic"
    elif language == "Php":
        language = "PHP"

    system("cls" if name == "nt" else "clear")
    print("Processando projeto: %s Linguagem: %s" %(projects, language))

    save_path = language
    file_tokens_comments = read_file(argv[1] + "_Comments_Tokens.txt")
    file_tokens_comments = create_tokens(file_tokens_comments)
    file_tokens_code = read_file(argv[1] + "_Code_Tokens.txt")

    count_tokens_comments, count_char_comments = comments_metrics(file_tokens_comments)
    count_tokens_code, count_char_code = code_metrics(file_tokens_code, language)

    save_file(save_path + "/" + language.replace(" ", "") + "Metrics.csv", language, projects, count_tokens_comments,
              count_char_comments,
              count_tokens_code, count_char_code)

    print("Processamento concluido.")
except:
    logging.exception("Error Occurred")
