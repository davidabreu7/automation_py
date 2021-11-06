import csv
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, "aux_files", "roteadores.csv")

def csv_reader(filename):
    csv_list = []
    with open(filename, encoding='utf-8-sig') as f:
        file = csv.reader(f, delimiter=";")
        for row in file:
            # print(row)
            csv_list.append(row)

    return csv_list

def csv_dict(filename):
    csv_list = []
    with open(filename, encoding='utf-8-sig') as f:
        csv_file = csv.DictReader(f, delimiter=";")
        for row in csv_file:
            csv_list.append(row)

    return csv_list

def csv_dict_line(*args):
    csv_list = csv_dict(filename)
    lines = []
    # print(args)
    for line in csv_list:
        # print(line)
        for code in args:
            if line["COD"] == code:
                lines.append(line)
    return lines

def csv_dict_col(*args):
    csv_list = csv_dict(filename)
    col_list = []
    for line in csv_list:
        # print(line[col])
        column = []
        for arg in args:
            column += [line[arg]]
        col_list += [column]

    return col_list

def main():
    # print(csv_reader(filename))
    # print(csv_dict(filename))
    # print(csv_dict_line("GO08", "SP26"))
    return_string = ""
    # for i in csv_dict_col("COD", "PROCURADORIA", "MODEM DE ACESSO"):
    #     cod, proc, modem = i
    #     return_string += f"{cod} {proc} {modem}\n"
    # print(return_string)
    # Different ways to test multiple
    # flags at once in Python


main()