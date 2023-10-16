from renderer import Sprite

class GameObject:
    
    def __init__(self):
        self._x : int
        self._y : int
        self._sprite : Sprite = None

        GameObjectManager.send_object(self)


    def update(self) -> None:
        pass


    def set_position(self, x : int, y : int) -> None:
        self.x = x
        self.y = y


    def get_position(self) -> (int, int):
        return self.x, self.y


    def destroy(self) -> None:
        GameObjectManager.remove_object(self)
        del self

    
    def set_sprite(self, sprite : Sprite) -> None:
        self._sprite = sprite



class GameObjectManager:

    _gameobjects : list[GameObject]


    @classmethod
    def initialize(cls):
        cls._gameobjects = []

    
    @classmethod
    def send_object(cls, object : GameObject):
        cls._gameobjects.append(object)


    @classmethod
    def remove_object(cls, object : GameObject):
        cls._gameobjects.remove(object)