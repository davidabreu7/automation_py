#!/usr/bin/env python3
import sys

print(sys.argv)

arg_total, arg1, arg2, arg3 = sys.argv

def read_args(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    for arg in arg_list:
        print(arg)

read_args(arg1,arg2,arg3)