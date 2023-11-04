from typing import Callable

from .renderer import Sprite, Renderer


class GameObject:
    
    def __init__(self):
        self._x : int = 0
        self._y : int = 0
        self._sprite : Sprite = None
        self.tickcount : int = 0

        GameObjectManager.add_object(self)


    def update(self) -> None:
        """Method that's called once every tick"""
        self.tickcount += 1


    def set_position(self, x : int, y : int) -> None:
        """Set the objects position to x, y"""
        self.x = x
        self.y = y


    def get_position(self) -> (int, int):
        """Returns the object's position (x, y)"""
        return self.x, self.y


    def destroy(self) -> None:
        """Destroy the object"""
        GameObjectManager.remove_object(self)
        del self

    
    def set_sprite(self, sprite : Sprite) -> None:
        """Sets the object's sprite to sprite"""
        self._sprite = sprite

    
    def get_sprite(self) -> Sprite:
        """Returns the object's sprite"""
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
        """
        Returns a tuple of GameObject's that satisfy a condition
        Example : get_objects(lamda x : x.get_position() == (1, 2)) returns all GameObjects
        with coordinates (1, 2)
        """
        return tuple(filter(condition, GameObjectManager._gameobjects))