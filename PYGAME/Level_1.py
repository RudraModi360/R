import time

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
# player=Entity(texture='char.png')
window.color = color.black10

bg = Entity(model='quad',texture='bg2.png',scale=45,position=(0,18),z=1)
camera.orthographic = True
camera.fov = 20
ground = Entity(model='cube', texture='gr1.png', z=-.1, y=-1, origin_y=.5, scale=(50,10,1), collider='box', ignore=True)
random.seed(4)
for i in range(5):
    Entity(model='cube', texture='gr1.png', collider='box', ignore=True, position=(random.randint(-10,20), random.randint(0,10) + i * 2), scale=(random.randint(1,20), random.randint(2,5), 10),z=i)
# ground = Entity(model='cube', color=color.white33, origin_y=.5, scale=(20, 10, 1), collider='box')
# wall = Entity(model='cube', color=color.azure, origin=(-.5,.5), scale=(5,10), x=10, y=.5, collider='box')
# ceiling = Entity(model='cube', color=color.white33, origin_y=.5, scale=(10, 1, 1), y=4, collider='box')

player = PlatformerController2d()
player.jump_height=10
player.x=1
player.texture='char.png'
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))



input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('down arrow','b')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

# test
from ursina.scripts.noclip_mode import NoclipMode2d
player.add_script(NoclipMode2d())

app.run()