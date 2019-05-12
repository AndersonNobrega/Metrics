from github import Github, GithubException
from time import time, sleep
from subprocess import call
from os import stat, remove
from os.path import expanduser
from sys import argv
from shutil import rmtree
import csv

home_path = expanduser("~")
language = argv[1]
path = home_path + "/" + language

github = Github("aca18348d0a6a4624afde2c6f1c017f1b687c733")

quant = 0
max_repo_quant = int(argv[2])
repositories_url = []
repositories_name = []
repositories_contributors_count = []
url_ant = ""
name_ant = ""

git_query = "stars:>=15 language:\"" + language + "\""

repositories = github.search_repositories(query=git_query)


def save_file(file_name, project_language, project_name, contributors_count, url):
    with open(file_name, "a+") as csv_file:
        file_writer = csv.writer(csv_file)

        if stat(file_name).st_size == 0:
            file_writer.writerow(["Linguagem", "Projeto", "Quantidade de Contribuidores", "URL"])

        file_writer.writerow([project_language, project_name, contributors_count, url])


def read_file(path_file):
    code_line_values = 0
    comment_line_values = 0

    with open(path_file, "r", encoding="ISO-8859-1") as csv_file:
        file_reader = csv.reader(csv_file)
        cont = 0

        for line in file_reader:
            if cont > 0:
                code_line_values += int(line[4])
                comment_line_values += int(line[3])
            cont += 1

    return code_line_values >= 200


for repo in repositories:
    repo_url = repo.git_url.lstrip("git")
    repo_name = repo.full_name
    repo_name = repo_name.replace("/", " | ")
    repo_url = "https" + repo_url

    try:
        repo_contributors_count = repo.get_contributors().totalCount
    except GithubException:
        repo_contributors_count = "N/A"

    if url_ant != repo_url and name_ant != repo_name:
        
        call(["git", "clone", "%s" % repo_url, "%s" % (language + "/" + repo_name)])

        call(["./CountLines2.sh", "%s" % language, "%s" % repo_name])

        try:
            if read_file(language + "/" + repo_name + ".csv"):
                repositories_url.append(repo_url)
                repositories_name.append(repo_name)
                repositories_contributors_count.append(repo_contributors_count)
                quant += 1
                call(["./ExtractionRunner.sh", "%s" % language])
            else:
                rmtree(language + "/" + repo_name, ignore_errors=True)
                remove(language + "/" + repo_name + ".csv")
        except FileNotFoundError:
            rmtree(language + "/" + repo_name, ignore_errors=True)
        

    rate = github.rate_limiting[0]
    if rate == 0:
        resettime = github.rate_limiting_resettime
        time_to_sleep = resettime - time()
        sleep(time_to_sleep)

    if quant >= max_repo_quant:     
        for i in range(len(repositories_name)):
            save_file(language + "/" + language.replace(" ", "") + "GitMetrics.csv", language, repositories_name[i], repositories_contributors_count[i],
                      repositories_url[i])
        break

    url_ant = repo_url
    name_ant = repo_name
