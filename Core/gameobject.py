class GameObject:
    
    def __init__(self):
        self._x : int
        self._y : int

        GameObjectManager.send_object(self)


    def set_position(self, x : int, y : int):
        self.x = x
        self.y = y


    def get_position(self):
        return self.x, self.y


    def destroy(self):
        GameObjectManager.remove_object(self)
        del self



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