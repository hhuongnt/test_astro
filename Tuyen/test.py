import pyglet
from pyglet import window
from pyglet import clock
from pyglet import font
from pyglet.window import key
from random import randint
# print random.randint(0, 5)

###############################################################################
class HyperSpace(window.Window):

    def __init__(self, *args, **kwargs):
        self.win = window.Window.__init__(self, *args, **kwargs)

        clock.schedule_interval(self.update, 1.0/30)  # update at 30Hz

        # setting text objects
        ft = font.load('Times New Roman', 40)
        self.fpstext = font.Text(ft, y=40)

        # load image
        self.background_image = pyglet.image.load("Resources/Space_background.jpg")
        self.background = Background(self.background_image)
        self.spaceship_animation = pyglet.image.load_animation("Resources/rocket_vertical.gif")
        self.spaceship = Spaceship(self.spaceship_animation, x=1400, y=1000)
        self.black_fire_ball_animation = pyglet.image.load_animation("Resources/black_fire_ball.gif")
        self.white_fire_ball_animation = pyglet.image.load_animation("Resources/white_fire_ball.gif")
        self.black_fire_ball = Fireball(self.black_fire_ball_animation, x=randint(0,600)*-1, y=randint(100,900))
        self.white_fire_ball = Fireball(self.white_fire_ball_animation, x=randint(0,600)*-1, y=randint(100,900))

    def update(self, dt):
        self.black_fire_ball.update()
        self.white_fire_ball.update()

    def on_draw(self):
        self.clear()
        clock.tick()
        self.background.draw()
        # showing fps
        self.fpstext.text = "fps: %d" % clock.get_fps()
        self.fpstext.draw()
        #  Draw objects
        self.spaceship.draw()
        self.black_fire_ball.draw()
        self.white_fire_ball.draw()

    # Event handlers
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.dispatch_event('on_close')

    def on_mouse_motion(self, x, y, dx, dy):
        if x < 1750:
            self.spaceship.x = x
        if y < 1000:
            self.spaceship.y = y


###############################################################################
class Spaceship(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        pyglet.sprite.Sprite.__init__(self, *args, **kwargs)


###############################################################################
class Fireball(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        pyglet.sprite.Sprite.__init__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pyglet.sprite.Sprite.__init__(self, *args, **kwargs)
        self.x_velocity = 10
        # self.y_velocity = 5

    def update(self):
        self.x += self.x_velocity
        # self.y -= self.y_velocity

###############################################################################
class Background(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        pyglet.sprite.Sprite.__init__(self, *args, **kwargs)

# Global variables
# window = pyglet.window.Window(fullscreen=True)
# window.set_mouse_visible(False)
# score = pyglet.text.Label("0", font_size=36, y=1000, x=1800, anchor_x = 'center', anchor_y = 'center')
# background = pyglet.image.load('Space_background.jpg')
# sprite_background = pyglet.sprite.Sprite(img=background)
# sprite_background.scale = 0.75
# spaceship = pyglet.image.load_animation('rocket_vertical.gif')
# sprite_spaceship = pyglet.sprite.Sprite(img=spaceship, x=1400,y=540)
# bfire_ball = pyglet.image.load_animation('black_fire_ball.gif')
# sprite_bfire_ball =  pyglet.sprite.Sprite(img=bfire_ball, x=randint(0,600)*-1, y=randint(100,900))
# wfire_ball = pyglet.image.load_animation('white_fire_ball.gif')
# sprite_wfire_ball =  pyglet.sprite.Sprite(img=wfire_ball, x=randint(0,600)*-1, y=randint(100,900))
#
#
#
# # Event callbacks
# @window.event
# def on_draw():
#     window.clear()
#     sprite_background.draw()
#     sprite_spaceship.draw()
#     sprite_bfire_ball.draw()
#     sprite_wfire_ball.draw()
#     score.draw()
#
# @window.event
# def on_mouse_motion(x, y, dx, dy):
#     sprite_spaceship.x, sprite_spaceship.y = x, y
#
#
# # Game loop (loop? Why loop?)
# def game_loop(_):
#     global sprite_spaceship, sprite_bfire_ball,sprite_wfire_ball, score
#     score.text = str(int(score.text) + 1)
#     sprite_bfire_ball.x += 10
#     sprite_wfire_ball.x += 5
#     if sprite_bfire_ball.x > 1920:
#         sprite_bfire_ball =  pyglet.sprite.Sprite(img=bfire_ball, x=randint(0, 600)*-1, y=randint(100,900))
#     if sprite_wfire_ball.x > 1920:
#         sprite_wfire_ball =  pyglet.sprite.Sprite(img=wfire_ball, x=randint(0, 600)*-1, y=randint(100,900))





# pyglet.clock.schedule(game_loop)
if __name__ == "__main__":
    win = HyperSpace(caption="HyperSpace", fullscreen=True)
    pyglet.app.run()
