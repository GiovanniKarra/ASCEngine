from os import system, remove, name
from sys import argv

system("pip install pynput")
if name == "nt": system("pip install colorama")

system("pip install -e .")

input("\nDONE\nThis file is going to be deleted\nPress ENTER to continue")

remove(argv[0])