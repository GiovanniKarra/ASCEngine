from renderer import Sprite, Renderer

class GameObject:
    
    def __init__(self):
        self._x : int
        self._y : int
        self._sprite : Sprite = None

        GameObjectManager.add_object(self)


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

    
    def get_sprite(self) -> Sprite:
        return self._sprite



class GameObjectManager:

    _gameobjects : list[GameObject]


    @classmethod
    def initialize(cls) -> None:
        cls._gameobjects = []

    
    @classmethod
    def update(cls) -> None:
        for object in cls._gameobjects:
            object.update()
            if sprite := object.get_sprite() is not None:
                x, y = object.get_position()
                Renderer.draw_sprite(sprite, x, y)


    @classmethod
    def add_object(cls, object : GameObject) -> None:
        cls._gameobjects.append(object)


    @classmethod
    def remove_object(cls, object : GameObject) -> None:
        cls._gameobjects.remove(object)