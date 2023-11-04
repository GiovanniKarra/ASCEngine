import os
from os import path

name = input("Project name : ")
width = input("Width : ")
height = input("Height : ")
tickrate = input("Tickrate : ")

if not path.exists(path.join(path.curdir, "Projects")):
    os.mkdir("Projects")

main_dir = os.getcwd()

os.chdir("Projects")
os.mkdir(name)
os.chdir(name)

project_dir = os.getcwd()

os.mkdir("Prefs")
os.chdir("Prefs")

f = open("prefs.txt", "w")
f.write(f"width:{width}\nheight:{height}\ntickrate:{tickrate}")
f.close()

os.chdir(project_dir)

f = open("main.py", "w")
f.write("from Core import *\n\n\n"\
        "if __name__ == \"__main__\":\n"\
        "   initialize_components()\n\n"\
        "   # YOUR CODE\n\n"\
        "   main_loop()\n")

f.close()