from ascengine.core import *

if __name__ == "__main__":
    # Manual parameter setting
    # (optional, if you remove this the default parameters are set)
    Prefs.set_param("width",    50)
    Prefs.set_param("height",   10)
    Prefs.set_param("tickrate", 30)

    initialize_engine()

    # Setup your objects
    # (that are preferably defined in other files)

    main_loop()