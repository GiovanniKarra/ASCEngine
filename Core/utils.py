import os

os.system(f"echo \"\" > ../log.txt")

def log(message : str):
    os.system(f"echo \"{message}\" >> ../log.txt")