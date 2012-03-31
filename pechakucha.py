
# PechaKucha is a 20s long slide.
timeout = 20

class PechaKucha(Exception):
    pass

def pechakucha(message="So bored..."):
    raise PechaKucha(message)
