from .renderer import Sprite, Renderer
from typing import Callable

class GameObject:
    
    def __init__(self):
        self._x : int = 0
        self._y : int = 0
        self._sprite : Sprite = None
        self.tickcount : int = 0

        GameObjectManager.add_object(self)


    def update(self) -> None:
        self.tickcount += 1


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

    
    def get_sprite(self) -> Sprite:
        return self._sprite



class GameObjectManager:

    _gameobjects : list[GameObject]


    @staticmethod
    def initialize() -> None:
        GameObjectManager._gameobjects = []

    
    @staticmethod
    def update() -> None:
        for object in GameObjectManager._gameobjects:
            object.update()
            if (sprite := object.get_sprite()) is not None:
                x, y = object.get_position()
                Renderer.draw_sprite(sprite, (x, y))


    @staticmethod
    def add_object(object : GameObject) -> None:
        GameObjectManager._gameobjects.append(object)


    @staticmethod
    def remove_object(object : GameObject) -> None:
        GameObjectManager._gameobjects.remove(object)

    @staticmethod
    def get_objects(condition : Callable[[GameObject], tuple[GameObject]]):
        return tuple(filter(condition, GameObjectManager._gameobjects))