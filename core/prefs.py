from os import path


class Prefs:

    _params : dict[str: int | str | float] = dict()
    _accessed : bool = False

    @staticmethod
    def set_default_params():
        Prefs._accessed = True
        Prefs.set_param("width", 50)
        Prefs.set_param("height", 10)
        Prefs.set_param("tickrate", 30)

    @staticmethod
    def get_param(param : str) -> int | str | float:
        """Returns the value of the parameter param"""
        Prefs._accessed = True
        return Prefs._params[param]
    
    @staticmethod
    def set_param(param : str, value : int | str | float) -> None:
        """Sets the parameter param to value"""
        Prefs._accessed = True
        Prefs._params[param] = value

    @staticmethod
    def accessed() -> bool:
        return Prefs._accessed