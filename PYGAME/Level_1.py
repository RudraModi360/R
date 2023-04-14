# from ursina.scripts.noclip_mode import NoclipMode2d
# import time
# from ursina import *
# from ursina.prefabs.platformer_controller_2d import PlatformerController2d

# window.borderless = False
# app = Ursina()
# window.color = color.black10
# player = PlatformerController2d()
# player.x = 1
# player.texture = 'char.png'
# player.x = raycast(player.world_position, player.right).world_point[1] + .01
# player.bullet_renderer = Entity(model=Mesh(
#     mode='point', thickness=.2), texture='circle', color=color.yellow)
# # ec = EditorCamera(rotation_x=-20)


# def shoot():
#     player.bullet_renderer.model.vertices.append(player.position)


# shoot_cooldown = .1
# shoot_sequence = Sequence(Func(shoot), Wait(shoot_cooldown), loop=True)
# enemies=[]

# for i, bullet in enumerate(player.bullet_renderer.model.vertices):
#         player.bullet_renderer.model.vertices[i] += Vec3(0, time.dt * 10, 0)
#         for enemy in enemies:
#             if distance_2d(bullet, enemy) < .5:
#                 enemy.hp -= 1
#                 enemy.blink(color.white)
#                 if enemy.hp <= 0:
#                     enemies.remove(enemy)
#                     destroy(enemy)
#                     # todo: add explosion particles and sound effect
#                 player.bullet_renderer.model.vertices.remove(bullet)

#                 print('a')

# if len(player.bullet_renderer.model.vertices):
#         player.bullet_renderer.model.vertices = player.bullet_renderer.model.vertices[-100:]  # max bullets

#         player.bullet_renderer.model.generate()


# def input(key):
#     if key == 'space':
#         shoot_sequence.start()
#     if key == 'space up':
#         shoot_sequence.paused = True




# enemies = []
# enemy = Entity(model=Circle(3), texture='2.png', position=(0, 16), z=1, speed=1, hp=5)
# enemies.append(enemy)

# def enemy_update():
#     for e in enemies:
#         e.position += e.up * enemy.speed * time.dt



# enemy_handler = Entity(update=enemy_update)


# bg = Entity(model='quad', texture='bg2.png', scale=(45, 10, 1), y=3)
# duplicate(bg,x=40)
# ground = Entity(model='cube', color=(67, 30, 67, 0.3), z=-.1, y=-1,origin_y=.5, scale=(100, 10, 1), collider='box', ignore=True)
# camera.orthographic = True
# camera.fov = 20

# wall = Draggable(model='cube', color=color.white33, origin=(0,.5), scale=(5,10), x=10, y=.5, collider='box')

# celling= Entity(model='cube', color=color.white33, origin_y=.3,scale=(8,1,1),y=2,x=10, collider='box')
# ceiling = Entity(model='cube', color=color.white33,origin_y=.5, scale=(10, 1, 1), y=4, collider='box')
# level=Entity(model='cube',color=color.white50,origin_y=.5,y=4,x=20,scale=(3,1),collider='box')

# camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))

# input_handler.bind('right arrow', 'd')
# input_handler.bind('left arrow', 'a')
# input_handler.bind('up arrow', 'space')
# input_handler.bind('down arrow', 'b')
# input_handler.bind('gamepad dpad right', 'd')
# input_handler.bind('gamepad dpad left', 'a')
# input_handler.bind('gamepad a', 'space')

# player.add_script(NoclipMode2d())

# app.run()
from ursina.scripts.noclip_mode import NoclipMode2d
import time
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
window.color = color.black10
player = PlatformerController2d()
player.x = 1
player.texture = 'char.png'
player.x = raycast(player.world_position, player.right).world_point[1] + .01
player.bullet_renderer = Entity(model=Mesh(
    mode='point', thickness=.2), texture='circle', color=color.yellow)
player.bullet_renderer.position = player.position  # set the position of the bullet renderer to the player position
player.bullet_renderer.parent = scene  # add the bullet renderer to the scene
# ec = EditorCamera(rotation_x=-20)


def shoot():
    player.bullet_renderer.model.vertices.append(player.position)


shoot_cooldown = .1
shoot_sequence = Sequence(Func(shoot), Wait(shoot_cooldown), loop=True)


enemies = []
enemy = Entity(model=Circle(3), texture='2.png', position=(0, 16), z=1, speed=1, hp=5)
enemies.append(enemy)

def enemy_update():
    for e in enemies:
        e.position += e.up * enemy.speed * time.dt


def update():
    shoot_sequence.start()  # start the shoot sequence
    for i, bullet in enumerate(player.bullet_renderer.model.vertices):
        player.bullet_renderer.model.vertices[i] += Vec3(0, time.dt * 10, 0)
        for enemy in enemies:
            if distance_2d(bullet, enemy) < .5:
                enemy.hp -= 1
                enemy.blink(color.white)
                if enemy.hp <= 0:
                    enemies.remove(enemy)
                    destroy(enemy)
                    # todo: add explosion particles and sound effect
                player.bullet_renderer.model.vertices.remove(bullet)

                print('a')

    if len(player.bullet_renderer.model.vertices):
        player.bullet_renderer.model.vertices = player.bullet_renderer.model.vertices[-100:]  # max bullets
        player.bullet_renderer.model.generate()


enemy_handler = Entity(update=enemy_update)


bg = Entity(model='quad', texture='bg2.png', scale=(45, 10, 1), y=3)
duplicate(bg,x=40)
ground = Entity(model='cube', color=(67, 30, 67, 0.3), z=-.1, y=-1,origin_y=.5, scale=(100, 10, 1), collider='box', ignore=True)
camera.orthographic = True
camera.fov = 20

wall = Draggable(model='cube', color=color.white33, origin=(0,.5), scale=(5,10), x=10, y=.5, collider='box')

celling= Entity(model='cube', color=color.white33, origin_y=.3,scale=(8,1,1),y=2,x=10, collider='box')
ceiling = Entity(model='cube', color=color.white33,origin_y=.5, scale=(10, 1, 1), y=4, collider='box')
level=Entity(model='cube',color=color.white50,origin_y=.5,y=4,x=20,scale=(3,1),collider='box')

camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30], speed=4))

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('down arrow', 'b')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

player.add_script(NoclipMode2d())

app.run()
