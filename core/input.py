from pynput.keyboard import Key, Listener


class Input:

    _pressed_buffer : set[Key] = set()
    _released_buffer : set[Key] = set()

    @staticmethod
    def keypressed(key : Key) -> bool:
        return key in Input._pressed_buffer
    
    @staticmethod
    def keyreleased(key : Key) -> bool:
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
