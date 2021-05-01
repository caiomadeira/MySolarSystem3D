from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy as np
from planet import Planet


def update():
    global t
    t = t + 0.0020
    angle = np.pi * 40 / 180

    sun.rotation_y += 50 * time.dt

    radius_1 = 1
    mercury.x = np.cos(t) * radius_1
    mercury.z = np.sin(t) * radius_1
    mercury.rotation_y += 200 * time.dt

    radius_2 = 1.4
    venus.x = np.cos(t + angle) * radius_2
    venus.z = np.sin(t + angle) * radius_2
    venus.rotation_y += 200 * time.dt

    radius_3 = 1.8
    earth.x = np.cos(t + angle * 2) * radius_3
    earth.z = np.sin(t + angle * 2) * radius_3
    earth.rotation_y += 200 * time.dt

    radius_4 = 2.2
    mars.x = np.cos(t + angle * 3) * radius_4
    mars.z = np.sin(t + angle * 3) * radius_4
    mars.rotation_y += 200 * time.dt

    radius_5 = 2.6
    jupiter.x = np.cos(t + angle * 4) * radius_5
    jupiter.z = np.sin(t + angle * 4) * radius_5
    jupiter.rotation_y += 200 * time.dt

    radius_6 = 3
    saturn.x = np.cos(t + angle * 5) * radius_6
    saturn.z = np.sin(t + angle * 5) * radius_6
    saturn.rotation_y += 200 * time.dt

    radius_7 = 3.4
    uranus.x = np.cos(t + angle * 6) * radius_7
    uranus.z = np.sin(t + angle * 6) * radius_7
    uranus.rotation_y += 200 * time.dt

    radius_8 = 3.8
    neptune.x = np.cos(t + angle * 7) * radius_8
    neptune.z = np.sin(t + angle * 7) * radius_8
    neptune.rotation_y += 200 * time.dt

    radius_9 = 4
    pluto.x = np.cos(t + angle * 8) * radius_9
    pluto.z = np.sin(t + angle * 8) * radius_9
    pluto.rotation_y += 200 * time.dt


def input(key):
    if key == 'escape' or key == 'q':
        quit()
    if key == 'space':
        sun.scale *= 2
    elif key == 'tab':
        sun.scale /= 2


if __name__ == '__main__':
    app = Ursina()
    window.color = color.black

    sun = Entity(model='sphere', color=color.yellow, texture='brick', scale=1.5, position=Vec3(0, 0, 0), shader=lit_with_shadows_shader)
    mercury = Entity(model='sphere', color=color.gray, texture='brick', scale=0.2)
    venus = Entity(model='sphere', color=color.orange, texture='brick', scale=0.3)
    earth = Entity(model='sphere', color=color.blue, texture='brick', scale=0.4)
    mars = Entity(model='sphere', color=color.violet, texture='brick', scale=0.3)
    jupiter = Entity(model='sphere', color=color.yellow, texture='brick', scale=0.6)
    saturn = Entity(model='sphere', color=color.white, texture='brick', scale=0.5)
    uranus = Entity(model='sphere', color=color.cyan, texture='brick', scale=0.5)
    neptune = Entity(model='sphere', color=color.gold, texture='brick', scale=0.5)
    pluto = Entity(model='sphere', color=color.pink, texture='brick', scale=0.2)

    t = -np.pi
    pivot = sun
    PointLight(parent=pivot, y=2, z=0, shadows=True)

    EditorCamera()
    # observer = FirstPersonController()

    app.run()
