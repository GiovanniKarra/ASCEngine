from core import *

class Joyeux(GameObject):
    def __init__(self):
        super().__init__()
        sprite : Sprite = Sprite.create_sprite_from_string(colored("JOYEUX",
                                                                   COLOR.BOLD))
        self.set_sprite(sprite)
        self.set_position(10, -50)

    def update(self) -> None:
        super().update()

        x, y = self.get_position()

        if y < 20:
            self.set_position(x, y+1)
        else:
            sprite : Sprite = Sprite.create_sprite_from_string(colored("JOYEUX",
                                                            COLOR.BOLD, COLOR.UNDERLINE))
            self.set_sprite(sprite)


class Anniversaire(GameObject):
    def __init__(self):
        super().__init__()
        sprite : Sprite = Sprite.create_sprite_from_string(colored("ANNIVERSAIRE",
                                                                   38, 5, 206, COLOR.BOLD))
        self.set_sprite(sprite)
        self.set_position(17, -100)

    def update(self) -> None:
        super().update()

        x, y = self.get_position()

        if y < 20:
            self.set_position(x, y+1)
        else:
            sprite : Sprite = Sprite.create_sprite_from_string(colored("ANNIVERSAIRE",
                                                            38, 5, 206, COLOR.BOLD, COLOR.UNDERLINE))
            self.set_sprite(sprite)


class Letter(GameObject):
    def __init__(self, letter, id):
        super().__init__()
        sprite : Sprite = Sprite.create_sprite_from_string(colored(letter,
                                                                   id+90, COLOR.BOLD))
        self.set_sprite(sprite)
        self.set_position(200 + 10*id, 30)
        self.id = id
        self.phase = 0

    def update(self) -> None:
        super().update()

        x, y = self.get_position()
        log((x,y))
        match self.phase:
            case 0:
                if x > 5:
                    self.set_position(x-1, y)
                else:
                    self.phase += 1
            case 1:
                if y > 5:
                    self.set_position(x, y-1)
                else:
                    self.phase += 1
            case 2:
                if x < 40:
                    self.set_position(x+1, y)
                else:
                    self.phase += 1
            case 3:
                if y < 21:
                    self.set_position(x, y+1)
                else:
                    self.phase += 1
            case 4:
                if x > 10+self.id:
                    self.set_position(x-1, y)
                else:
                    self.phase += 1


if __name__ == "__main__":
    Prefs.set_param("width", 60)
    Prefs.set_param("height", 40)
    Prefs.set_param("tickrate", 30)
    
    initialize_engine()

    j = Joyeux()
    a = Anniversaire()

    mot = "FLORIANE"

    for i in range(len(mot)):
        Letter(mot[i], i+1)

    main_loop()
