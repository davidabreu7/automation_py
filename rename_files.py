##!/usr/bin/env python3
import os
import re
import subprocess
import sys

get_main_dir = os.path.dirname(__file__)
get_aux_dir = os.path.join(get_main_dir, "aux_files")
search_file = re.compile("([\w\-\s]*)(\.[a-z]*)")
file_dict = {}

for file in os.listdir(get_aux_dir):
    filename = re.search(search_file, file)
    if filename:
        file_dict[file] = [filename[1], filename[2]]

for line in file_dict:
    file_dict[line][0] += "-RENAME"
    subprocess.run(["mv", line, file_dict[line][0]], cwd=get_aux_dir)

