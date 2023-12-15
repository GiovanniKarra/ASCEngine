class Prefs:

    _params : dict[str: int | str | float] = {
        "width": 50,
        "height": 10,
        "tickrate": 30
    }

    @staticmethod
    def get_param(param : str) -> int | str | float:
        """Returns the value of the parameter param"""
        return Prefs._params[param]
    
    @staticmethod
    def set_param(param : str, value : int | str | float) -> None:
        """Sets the parameter param to value"""
        Prefs._params[param] = value
