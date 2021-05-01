from ursina import *
import random

class Planet:
    def __init__(self):
        randS = random.randint(3, 24)
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        a = random.randint(164, 255)

        self.ent = Entity(model='sphere', scale=randS, color=color.rgb(r,g,b, a), texture='brick')

planets = []
planets_qtd = 9
for p in range(planets_qtd):
    baby = Planet()
    baby.ent.z = -80
    planets.append(baby)