class Prefs:

    _params : dict[str, str] = {
        "width":    "50",
        "height":   "10",
        "tickrate": "30"
    }

    @staticmethod
    def get_param(param : str) -> str:
        """Returns the value of the parameter param"""
        return Prefs._params[param]
    
    @staticmethod
    def set_param(param : str, value : str) -> None:
        """Sets the parameter param to value"""
        Prefs._params[param] = value
