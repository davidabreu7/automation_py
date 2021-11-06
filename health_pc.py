#!/usr/bin/env python3
import shutil
import psutil

def disk_check():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free

def cpu_check():
    ps = psutil.cpu_percent(1)
    return ps

def temp_check():
    temp = psutil.sensors_temperatures()
    return temp
def print_health():

    print(temp_check())
    return f"O espaço em disco é: {disk_check():.2f}% \nA utilização da CPU é: {cpu_check():.2f}%\n"

if __name__ == "__main__":
    print(print_health())