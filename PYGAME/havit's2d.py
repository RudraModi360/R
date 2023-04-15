from ursina import *

app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d

player = PlatformerController2d(position=(15, 150, 0.01), scale_y=10, max_jumps=8)
player.walk_speed = 50
player.air_time = 0.5
bg = Entity(
    model="cube", texture="background.png", scale=(500, 250), position=(150, 100), z=2
)
bg = Entity(
    model="cube", texture="assets.png", scale=(500, 250), position=(100, 100), z=1
)


quad = load_model("quad", use_deepcopy=True)


level_parent = Entity(model=Mesh(vertices=[], uvs=[]), color=(244, 244, 244, 0.3))


def make_level(texture):
    [destroy(c) for c in level_parent.children]
    pos = []
    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x, y)

            # If it's black, it's solid, so we'll place a tile there.
            if col == color.black:
                level_parent.model.vertices += [
                    Vec3(*e) + Vec3(x + 0.5, y + 0.5, 0)
                    for e in quad.generated_vertices
                ]  # copy the quad model, but offset it with Vec3(x+.5,y+.5,0)
                level_parent.model.uvs += quad.uvs
                # Entity(parent=level_parent, position=(x,y), model='cube', origin=(-.5,-.5), color=color.gray, texture='white_cube', visible=True)
                if not collider:
                    collider = Entity(
                        parent=level_parent,
                        position=(x, y),
                        model="quad",
                        origin=(-0.5, -0.5),
                        collider="box",
                        visible=False,
                    )
                else:
                    # instead of creating a new collider per tile, stretch the previous collider right.
                    collider.scale_x += 1
                    pos.append(collider.position)
            else:
                collider = None

    # print('cordinates are:\n', pos)
    level_parent.model.generate()


make_level(load_texture("le_ver_1_collider"))  # generate the level

camera.orthographic = True
camera.position = (-100, -100)
camera.fov = 150
camera.add_script(SmoothFollow(target=player, offset=[0, 5, -30]))


player.traverse_target = level_parent
enemy = Entity(model="cube", collider="box", color=color.red, position=(16, 5, -0.1))


def update():
    if player.intersects(enemy).hit:
        print("die")
        player.position = player.start_position
    if player.y < 0:
        print("Game Over!!")
        quit()



input_handler.bind("right arrow", "d")
input_handler.bind("left arrow", "a")
input_handler.bind("up arrow", "space")
input_handler.bind("down arrow", "b")
input_handler.bind("gamepad dpad right", "d")
input_handler.bind("gamepad dpad left", "a")
input_handler.bind("gamepad a", "space")


app.run()
