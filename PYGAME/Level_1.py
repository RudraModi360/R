from ursina.scripts.noclip_mode import NoclipMode2d
import time

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
# player=Entity(texture='char.png')
window.color = color.black10

bg = Entity(model='quad', texture='bg2.png', scale=(45, 10, 1), y=3)
camera.orthographic = True
camera.fov = 20
ground = Entity(model='cube', color=(67, 30, 67, 0.3), z=-.1, y=-1,origin_y=.5, scale=(45, 10, 1), collider='box', ignore=True)
random.seed(4)
celling= Entity(model='cube', color=color.white33, origin_y=.3,scale=(8,1,1),y=2,x=10, collider='box')
ceiling = Entity(model='cube', color=color.white33,origin_y=.5, scale=(10, 1, 1), y=4, collider='box')

player = PlatformerController2d()
player.x = 1
player.texture = 'char.png'
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))


input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('down arrow', 'b')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

# test
player.add_script(NoclipMode2d())

app.run()
