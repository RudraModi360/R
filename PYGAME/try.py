# from ursina import *

# app = Ursina()
# bg = Entity(model='quad', texture='assets\BG', scale=36, z=1)
# window.fullscreen = True
# player = Animation('assets\player', collider='box', y=5)
# fly = Entity(model='cube', texture='assets\\fly1', collider='box',
#              scale=2, x=20, y=-10)

# flies = []
# def newFly():
#   new = duplicate(fly,y=-5+(5124*time.dt)%15)
#   flies.append(new)
#   invoke(newFly, delay=1)


# newFly()
# camera.orthographic = True
# camera.fov = 20

# def update():
#   player.y += held_keys['w']*6*time.dt
#   player.y -= held_keys['s'] *6* time.dt
#   a = held_keys['w']*-20
#   b = held_keys['s'] *20
#   if a != 0:
#     player.rotation_z = a
#   else:
#     player.rotation_z = b
#   for fly in flies:
#     fly.x -= 4*time.dt
#     touch = fly.intersects()
#     if touch.hit:
#       flies.remove(fly)
#       destroy(fly)
#       destroy(touch.entity)
#   t = player.intersects()
#   if t.hit and t.entity.scale==2:
#     quit()


# def input(key):
#   if key == 'space':
#     e = Entity(y=player.y, x=player.x+1, model='cube', scale=1,
#       texture='assets\Bullet', collider='cube')
#     e.animate_x(30,duration=2,curve=curve.linear)
#     invoke(destroy, e, delay=2)

# app.run()
import time

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
player=Entity(texture='char.png')
window.color = color.green

bg = Entity(model='quad',texture='BGl1.jpg',scale=45,position=(0,18),z=1)
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