import pyglet
from random import randint
# print random.randint(0, 5)

# Global variables
window = pyglet.window.Window(fullscreen=True)
window.set_mouse_visible(False)
text_score = pyglet.text.Label("Your score :", font_size=30, y=1000, x=1600, anchor_x = 'center', anchor_y = 'center')
score = pyglet.text.Label("0", font_size=30, y=1000, x=1800, anchor_x = 'center', anchor_y = 'center')
background = pyglet.image.load('Space_background.jpg')
sprite_background = pyglet.sprite.Sprite(img=background)
sprite_background.scale = 0.75
spaceship = pyglet.image.load_animation('rocket_vertical.gif')
sprite_spaceship = pyglet.sprite.Sprite(img=spaceship, x=1400,y=540)
bfire_ball = pyglet.image.load_animation('black_fire_ball.gif')
sprite_bfire_ball =  pyglet.sprite.Sprite(img=bfire_ball, x=randint(0,600)*-1, y=randint(100,900))
wfire_ball = pyglet.image.load_animation('white_fire_ball.gif')
sprite_wfire_ball =  pyglet.sprite.Sprite(img=wfire_ball, x=randint(0,600)*-1, y=randint(100,900))

end_game = False
end_background = pyglet.image.load('Endgame_background.jpg')
sprite_end_background = pyglet.sprite.Sprite(img=end_background)


# Event callbacks
@window.event
def on_draw():
    pyglet.window.MouseCursor.draw(1600, 900)
    if end_game == False:
        window.clear()
        sprite_background.draw()
        sprite_spaceship.draw()
        sprite_bfire_ball.draw()
        sprite_wfire_ball.draw()
        text_score.draw()
        score.draw()
    else:
        window.clear()
        sprite_end_background.draw()



@window.event
def on_mouse_enter(x, y):
    sprite_spaceship.x = 1600
    sprite_spaceship/y = 900

def on_mouse_motion(x, y, dx, dy):
    sprite_spaceship.x, sprite_spaceship.y = x, y


# Game loop (loop? Why loop?)
def game_loop(_):
    global sprite_spaceship, sprite_bfire_ball,sprite_wfire_ball, score, end_game
    if end_game == False:
        score.text = str(int(score.text) + 1)
        sprite_bfire_ball.x += 10
        sprite_wfire_ball.x += 5
        if sprite_bfire_ball.x > 1920:
            sprite_bfire_ball =  pyglet.sprite.Sprite(img=bfire_ball, x=randint(0,600)*-1, y=randint(100,900))
        if sprite_wfire_ball.x > 1920:
            sprite_wfire_ball =  pyglet.sprite.Sprite(img=wfire_ball, x=randint(0,600)*-1, y=randint(100,900))
        if sprite_bfire_ball.x < sprite_spaceship.x + 170 and sprite_bfire_ball.x +231 > sprite_spaceship.x and sprite_bfire_ball.y < sprite_spaceship.y + 80 and sprite_bfire_ball.y + 90 > sprite_spaceship.y:
            end_game = True
        if sprite_wfire_ball.x < sprite_spaceship.x + 170 and sprite_wfire_ball.x +226 > sprite_spaceship.x and sprite_wfire_ball.y < sprite_spaceship.y + 80 and sprite_wfire_ball.y + 90 > sprite_spaceship.y:
            end_game = True


pyglet.clock.schedule(game_loop)
pyglet.app.run()
