import time

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
# player=Entity(texture='char.png')
window.color = color.black10

bg = Entity(model='quad',texture='bg2.png',scale=(18,5,1))
camera.orthographic = True
camera.fov = 20
ground = Entity(model='cube', texture='gr1.png',scale=(40,3,1), collider='box', ignore=True)


app.run()