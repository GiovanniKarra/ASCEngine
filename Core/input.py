from pynput.keyboard import Key, Listener


class Input:

    _pressed_buffer : set[Key] = set()
    _released_buffer : set[Key] = set()

    @classmethod
    def keypressed(cls, key : Key) -> bool:
        return key in cls._pressed_buffer
    
    @classmethod
    def keyreleased(cls, key : Key) -> bool:
        return key in cls._released_buffer

    @classmethod
    def initialize(cls):
        listener = Listener(on_press=cls._on_press, on_release=cls._on_release)
        listener.start()

    @classmethod
    def update(cls):
        cls._pressed_buffer = set()
        cls._released_buffer = set()

    @classmethod
    def _on_press(cls, key):
        try:
            cls._pressed_buffer.add(key)
        except AttributeError:
            pass

    @classmethod
    def _on_release(cls, key):
        cls._released_buffer.add(key)
