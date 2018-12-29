import pyglet
from random import randint
window = pyglet.window.Window(fullscreen = True)
background = pyglet.image.load('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/Space_background.jpg')
sprite_background = pyglet.sprite.Sprite(img=background)
black_fire_ball = pyglet.image.load_animation('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/black_fire_ball.gif')
white_fire_ball = pyglet.image.load_animation('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/white_fire_ball.gif')
alien1 = pyglet.image.load_animation('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/alien1.gif')
alien2 = pyglet.image.load_animation('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/alien2.gif')
alien3 = pyglet.image.load_animation('/tmp/guest-kx3svv/test_astro/Tuyen/Resources/alien3.gif')
sprite_background.scale = 0.75


class Object(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 200
    def update(self):
        self.x += self.velocity_x
        self.check_bound()
    def check_bound(self):
        min_x = -226/2
        max_x = window.width + 226/2
        if self.x < min_x or self.x > max_x:
            self.x = randint(0, window.width/3)



def random_objects(num_objects, object):
    objects = []
    for i in range(num_objects):
        obj_x = randint(0, window.width/3)
        obj_y = randint(0, window.height)
        new_object = Object(object)
        # new_object = pyglet.sprite.Sprite(img=object,
        #                             x=object_x, y=object_y)
        new_object.x = obj_x
        new_object.y = obj_y
        objects.append(new_object)
    return objects


def update(x):
        for i in black_fire_balls:
            i.update()
        for i in white_fire_balls:
            i.update()
        for i in aliens1:
            i.update()
        for i in aliens2:
            i.update()
        for i in aliens3:
            i.update()


def draw_obj(objects):
    for i in objects:
        i.draw()


black_fire_balls = random_objects(3, black_fire_ball)
white_fire_balls = random_objects(3, white_fire_ball)
aliens1 = random_objects(1, alien1)
aliens2 = random_objects(1, alien2)
aliens3 = random_objects(1, alien3)
# def update(random_objects, dt):
#     object.velocity_x, object.velocity_y = 0.0, 0.0
#     for object in random_objects:
#         object.x += object.velocity_x * dt


@window.event
def on_draw():
    window.clear()
    sprite_background.draw()
    draw_obj(black_fire_balls)
    draw_obj(white_fire_balls)
    draw_obj(aliens1)
    draw_obj(aliens2)
    draw_obj(aliens3)


# def run(objects):
#     for i in objects:
#         i.x += 10


# def game_loop(_):

    # run(black_fire_balls)
    # run(white_fire_balls)
    # run(aliens1)
    # run(aliens2)
    # run(aliens3)


# pyglet.clock.schedule(game_loop)
pyglet.clock.schedule_interval(update, 1/300.0)
pyglet.app.run()
