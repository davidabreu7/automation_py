import csv
import os
dir_file = os.path.dirname(__file__)
filename = os.path.join(dir_file, "aux_files", "roteadores.csv")


def csv_reader(file):
    csv_list = []
    with open(file, encoding="utf-8-sig") as f:
        csv_file = csv.reader(f, delimiter=";")
        for row in csv_file:
            csv_list.append(row)
    return csv_list


def csv_dict_reader(file):
    csv_list_dict = []
    with open(file, encoding="utf-8-sig") as f:
        csv_dict = csv.DictReader(f, delimiter=";")
        for row in csv_dict:
            csv_list_dict.append(row)
    return csv_list_dict


def csv_line(file, cod):
    csv_list = csv_dict_reader(file)
    csv_dict = []
    for row in csv_list:
        if row["COD"] in cod:
            csv_dict.append(line)

    return csv_dict


for line in csv_line(filename, ["PR28", "MG27", "BA21"]):
    print(line)
