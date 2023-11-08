from os import system, remove
from sys import argv

system("pip install pynput")
system("pip install consoledraw")
system("pip install termcolor")

system("pip install -e .")

input("\nDONE\nThis file is going to be deleted\nPress ENTER to continue")

remove(argv[0])