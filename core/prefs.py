from os import path


class Prefs:

    _params : dict[str: int] = dict()

    def set_params():
        file = open(path.join("prefs", "prefs.txt"), "r")
        lines = file.readlines()
        
        for line in lines:
            name, value = line.split(":")
            Prefs._params[name] = int(value)

    def get_param(param : str) -> int:
        """Returns the value of the parameter param"""
        return Prefs._params[param]