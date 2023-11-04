from .renderer import Sprite, Renderer, TYPE_UI
from .gameobject import GameObject, GameObjectManager


class UIElement(GameObject):
    
    def __init__(self):
        self._x : int = 0
        self._y : int = 0
        self._sprite : Sprite = None
        self.tickcount : int = 0

        GameObjectManager.add_object(self)


    def destroy(self) -> None:
        GameObjectManager.remove_object(self)
        del self

    
    def set_sprite(self, sprite: Sprite) -> None:
        sprite.type = TYPE_UI
        super().set_sprite(sprite)



# class UIManager:

#     _uielements : list[GameObject]


#     @classmethod
#     def initialize(cls) -> None:
#         cls._uielements = []

    
#     @classmethod
#     def update(cls) -> None:
#         for element in cls._uielements:
#             element.update()
#             if (sprite := element.get_sprite()) is not None:
#                 x, y = element.get_position()
#                 Renderer.draw_sprite(sprite, (x, y))


#     @classmethod
#     def add_object(cls, object : GameObject) -> None:
#         cls._uielements.append(object)


#     @classmethod
#     def remove_object(cls, object : GameObject) -> None:
#         cls._uielements.remove(object)