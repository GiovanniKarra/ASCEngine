from setuptools import setup, find_packages
from os import name, system

system("pip install pynput")
if name == "nt": system("pip install colorama")

setup(name="ascengine",
      version="0.0.3",
      #packages=["pynput"])#+["colorama"]*int(name == "nt")))
      packages=find_packages())