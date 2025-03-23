import time
import os

from .gameobject import GameObjectManager
from .renderer import Renderer
from .display import Display
#from .ui import UIManager
from .prefs import Prefs
from .input_manager import Input
from .utils import reset_log, log


def initialize_components():
	if os.name == "nt":
		from colorama import just_fix_windows_console
		just_fix_windows_console()

	width, height = int(Prefs.get_param("width")), int(Prefs.get_param("height"))
	
	Display.initialize(width, height)
	GameObjectManager.initialize()
	#UIManager.initialize()
	Input.initialize()


def main_loop():
	"""The main logic loop of the engine that updates the system every tick"""
	tickrate = int(Prefs.get_param("tickrate"))
	ticktime = 1/tickrate

	while True:
		init_time = time.time()

		#UIManager.update()
		GameObjectManager.update()
		Renderer.update()
		Display.update()
		Input.update()

		dtime = time.time() - init_time
		if ticktime > dtime :
			time.sleep(ticktime - dtime)


def initialize_engine():
	"""Initialization of the system"""
	if os.name == "posix": os.system("stty -echo")
	
	reset_log()
	initialize_components()


if __name__ == "__main__":
	initialize_engine()

	main_loop()
