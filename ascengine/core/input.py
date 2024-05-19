from pynput.keyboard import Key, Listener, KeyCode

from .utils import log


class Input:

	_pressed_buffer : set[Key | str] = set()
	_released_buffer : set[Key | str] = set()

	@staticmethod
	def keypressed(key : Key | str) -> bool:
		"""Returns True if key was pressed during the last tick, False otherwise"""
		if type(key) == str:
			key = KeyCode.from_char(key)
		return key in Input._pressed_buffer
	
	@staticmethod
	def keyreleased(key : Key | str) -> bool:
		"""Returns True if key was released during the last tick, False otherwise"""
		if type(key) == str:
			key = KeyCode.from_char(key)
		return key in Input._released_buffer

	@staticmethod
	def initialize():
		listener = Listener(on_press=Input._on_press, on_release=Input._on_release)
		listener.start()

	@staticmethod
	def update():
		Input._pressed_buffer = set()
		Input._released_buffer = set()

	@staticmethod
	def _on_press(key):
		try:
			Input._pressed_buffer.add(key)
		except AttributeError:
			pass

	@staticmethod
	def _on_release(key):
		Input._released_buffer.add(key)
