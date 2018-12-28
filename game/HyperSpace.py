import pyglet
from random import randint
# print random.randint(0, 5)

# Global variables
window = pyglet.window.Window(fullscreen=True)
window.set_mouse_visible(False)
score = pyglet.text.Label("0", font_size=36, y=1000, x=1800, anchor_x ='center', anchor_y ='center')
background = pyglet.image.load('Space_background.jpg')
sprite_background = pyglet.sprite.Sprite(img=background)
sprite_background.scale = 0.75
spaceship = pyglet.image.load_animation('rocket_vertical.gif')
sprite_spaceship = pyglet.sprite.Sprite(img=spaceship, x=1400,y=540)
bfire_ball = pyglet.image.load_animation('black_fire_ball.gif')
sprite_bfire_ball = pyglet.sprite.Sprite(img=bfire_ball, x=randint(0, 600)*-1, y=randint(100, 900))
wfire_ball = pyglet.image.load_animation('white_fire_ball.gif')
sprite_wfire_ball = pyglet.sprite.Sprite(img=wfire_ball, x=randint(0, 600)*-1, y=randint(100, 900))


# Event callbacks
@window.event
def on_draw():
    window.clear()
    sprite_background.draw()
    sprite_spaceship.draw()
    sprite_bfire_ball.draw()
    sprite_wfire_ball.draw()
    score.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    if x < 1750:
        sprite_spaceship.x = x
    if y < 1000:
        sprite_spaceship.y = y

# Game loop (loop? Why loop?)
def game_loop(_):
    global sprite_spaceship, sprite_bfire_ball, sprite_wfire_ball, score
    score.text = str(int(score.text) + 1)
    sprite_bfire_ball.x += 10
    sprite_wfire_ball.x += 5
    if sprite_bfire_ball.x > 1920:
        sprite_bfire_ball = pyglet.sprite.Sprite(img=bfire_ball, x=randint(0, 600)*-1, y=randint(100, 900))
    if sprite_wfire_ball.x > 1920:
        sprite_wfire_ball = pyglet.sprite.Sprite(img=wfire_ball, x=randint(0, 600)*-1, y=randint(100, 900))





pyglet.clock.schedule(game_loop)
pyglet.app.run()
