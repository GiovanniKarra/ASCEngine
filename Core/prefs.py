class Prefs:

    _params : dict[str: int] = dict()

    def set_params():
        file = open("../Prefs/Prefs.txt", "r")
        lines = file.readlines()
        
        for line in lines:
            name, value = line.split(":")
            Prefs._params[name] = int(value)

    def get_param(param : str) -> int:
        return Prefs._params[param]