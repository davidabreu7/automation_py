#!/usr/bin/env python3
import os
import datetime

def read_file(filename):
    dirname = os.path.dirname(__file__)  # pega a path do script que esta sendo executado (mesmo fora do virtual env)
    filename = os.path.join(dirname, "red_death.txt")  # usar os.path.join para criar uma path para qualquer OS
    # arquivo = os.path.abspath("red_death.txt") #porque o script executa DENTRO do virtual env ele ele não acha o arquivo fora do env
    file = open(filename)
    for line in file:
        print(line, end="")

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        file.write("")

    # Return the list of files in the new directory
    return os.listdir()

def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        file.write("")

    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = str(datetime.datetime.fromtimestamp(timestamp))
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(date[:10])


def main():
    print(create_python_script("program.py"))
    print(new_directory("PythonPrograms", "script.py"))
    print(file_date("newfile.txt"))    # Should be today's date in the format of yyyy-mm-dd


main()
