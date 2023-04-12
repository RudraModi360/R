from ursina.scripts.noclip_mode import NoclipMode2d
import time
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.borderless = False
app = Ursina()
window.color = color.black10


bg = Entity(model='quad', texture='bg2.png', scale=(45, 10, 1), y=3)
duplicate(bg,x=40)
ground = Entity(model='cube', color=(67, 30, 67, 0.3), z=-.1, y=-1,origin_y=.5, scale=(100, 10, 1), collider='box', ignore=True)
camera.orthographic = True
camera.fov = 20
# ground = Entity(model='cube', color=(67, 30, 67, 0.3), z=-.1, y=-1,origin_y=.5, scale=(100, 10, 1), collider='box', ignore=True)
# random.seed(4)
# wall=Entity(model='cube',color=color.white33,origin)oh
# sprite_texture = load_texture('bg_remove.png')
# cropped_texture = Texture.subtexture(sprite_texture, ((0, 0), (26,48)),((25,2),(50,48)),((51,6),(78,47)),((79,5),(105,46)),((106,5),(132,47)),((134,6),(160,45)),((162,5),(185,46)) # Crop a 32x32 square from the top-left corner of the image
# sprite = Sprite(texture=cropped_texture)

#Sprite.look_at_2d(self="bg_remove.png",target="standing",axis=(100,194))
wall = Draggable(model='cube', color=color.white33, origin=(0,.5), scale=(5,10), x=10, y=.5, collider='box')

celling= Entity(model='cube', color=color.white33, origin_y=.3,scale=(8,1,1),y=2,x=10, collider='box')
ceiling = Entity(model='cube', color=color.white33,origin_y=.5, scale=(10, 1, 1), y=4, collider='box')
# level=Entity(model='cube',color=color.white50,scale=(3,1),collider='box')

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



player.add_script(NoclipMode2d())

app.run()
