from setuptools import setup, find_packages
from os import name

setup(name="ascengine",
      version="0.0.3",
      packages=find_packages(),
      install_requires=["pynput"]+["colorama"]*int(name == "nt"))