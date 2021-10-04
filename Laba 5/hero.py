from gameunit import *

class Hero(Attacker):
    _attack = 50
    _experience = 0

    def __init__(self, name):
        self._name = name
        self._health = 100

