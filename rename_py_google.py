#!/usr/bin/env python3
import sys
import subprocess as sub

with open(sys.argv[1], "r") as f:
    f_text = f.readlines()
    for line in f_text:
      new_line = line.strip()
      #print(new_line)
      new_line = new_line.replace("jane", "jdoe")
      sub.run(["mv",line.strip(),new_line])