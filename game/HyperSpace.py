import pyglet
from random import randint

# Global variables
window = pyglet.window.Window(fullscreen=True)
window.set_mouse_visible(False)
score = pyglet.text.Label("0", font_size=36, y=1000, x=1800, anchor_x ='center', anchor_y ='center')
background = pyglet.image.load('res/Space_background.jpg')
sprite_background = pyglet.sprite.Sprite(img=background)
sprite_background.scale = 0.75
spaceship = pyglet.image.load_animation('res/rocket_vertical.gif')
sprite_spaceship = pyglet.sprite.Sprite(img=spaceship, x=1400,y=540)
bfire_ball = pyglet.image.load_animation('res/black_fire_ball.gif')
wfire_ball = pyglet.image.load_animation('res/white_fire_ball.gif')
alien1 = pyglet.image.load_animation('res/alien1.gif')
alien2 = pyglet.image.load_animation('res/alien2.gif')
alien3 = pyglet.image.load_animation('res/alien3.gif')
# end game variables
end_game = False
end_background = pyglet.image.load('res/Endgame_background.jpg')
sprite_end_background = pyglet.sprite.Sprite(img=end_background)
explosion = pyglet.image.load_animation('res/explosion.gif')
explosion_time = 0
end_game_astronaut = pyglet.image.load_animation('res/Astronauts_dead.gif')
sprite_end_game_astronaut=pyglet.sprite.Sprite(img=end_game_astronaut,x=0,y=300)
#  media variables
player = pyglet.media.Player()
source = pyglet.media.load('music/HyperSpaceSound.wav')
player.queue(source)
player.eos_action = 'loop'
#  highscore variables
f = open('HS_File', 'r')
hscore = f.read()
hscore = hscore.rstrip()
f.close()
old_hscore = pyglet.text.Label('HIGHSCORE : ' + hscore, font_size=36, y=1000, x=100, anchor_y ='center')
logo_new_hscore = pyglet.text.Label('NEW HIGHSCORE', font_size=50, y=window.height//2, x=window.width//2, anchor_x='center', anchor_y='center')
logo_nice_try = pyglet.text.Label('BETTER LUCK NEXT TIME', font_size=50, y=window.height//2, x=window.width//2, anchor_x='center', anchor_y='center')
new_hscore = pyglet.text.Label(score.text, font_size=40, y=window.height//2 - 80 , x=window.width//2, anchor_x='center', anchor_y='center')
class Object(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = randint(5, 15)
    def update(self):
        self.x += self.velocity_x
        self.check_bound()
    def check_bound(self):
        max_x = window.width + 226/2
        if self.x > max_x:
            self.x = randint(0, 1000)*-1
            self.y = randint(0, 1000)
            self.velocity_x = randint(15, 50)


"""Class Object"""


def random_objects(num_objects, object):
    objects = []
    for i in range(num_objects):
        obj_x = -800
        obj_y = randint(0, 1000)
        new_object = Object(object)
        # new_object = pyglet.sprite.Sprite(img=object,
        #                             x=object_x, y=object_y)
        new_object.x = obj_x
        new_object.y = obj_y
        objects.append(new_object)
    return objects


"""Return list of object images"""

#  Global variables
black_fire_balls = random_objects(3, bfire_ball)
white_fire_balls = random_objects(3, wfire_ball)
aliens1 = random_objects(1, alien1)
aliens2 = random_objects(1, alien2)
aliens3 = random_objects(1, alien3)


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


"""Move objects"""


def draw_obj(objects):
    for i in objects:
        i.draw()


"""Draw objects"""


def hit_object(objects):
    global sprite_explosion, end_game, score, aliens1, aliens2, aliens3, event
    s = sprite_spaceship
    for i in objects:
        if objects == black_fire_balls or objects == white_fire_balls:
            if i.x + 50 < s.x + 150 and i.x +210 > s.x and i.y + 30 < s.y + 70 and i.y + 80 > s.y:
                end_game = True
                sprite_explosion = pyglet.sprite.Sprite(img=explosion, x=s.x+20, y=s.y-40 )
                sprite_explosion.scale =0.5
        else:
            if i.x  < s.x + 170 and i.x +190 > s.x and i.y < s.y + 90 and i.y + 190 > s.y:
                score.text = str(int(score.text) + 1000)
                i.x = randint(0, 1000)*-1
                i.y = randint(0, 1000)
                i.velocity_x = randint(15, 50)


"""Event when collapse"""

# Event callbacks
@window.event
def on_draw():
    global explosion_time
    if end_game == False:
        window.clear()
        player.play()
        old_hscore.draw()
        sprite_background.draw()
        sprite_spaceship.draw()
        old_hscore.draw()
        draw_obj(black_fire_balls)
        draw_obj(white_fire_balls)
        draw_obj(aliens1)
        draw_obj(aliens2)
        draw_obj(aliens3)
        score.draw()
    else:
        if explosion_time < 150:
            sprite_background.draw()
            sprite_spaceship.draw()
            sprite_explosion.draw()
            old_hscore.draw()
            score.draw()
        else:
            window.clear()
            sprite_end_background.draw()
            sprite_end_game_astronaut.draw()
            if int(score.text) > int(hscore):
                new_hscore.text = score.text
                logo_new_hscore.draw()
                new_hscore.draw()
                f = open('HS_File', 'w')
                f.write(score.text)
                f.close()

            else:
                logo_nice_try.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    global end_game
    if end_game == False:
        if x < 1750:
            sprite_spaceship.x = x
        if y < 1000:
            sprite_spaceship.y = y

# Game loop (loop? Why loop?)
def game_loop(_):
    global score, explosion_time
    if end_game == False:
        score.text = str(int(score.text) + 1)
        hit_object(black_fire_balls)
        hit_object(white_fire_balls)
        hit_object(aliens1)
        hit_object(aliens2)
        hit_object(aliens3)
    else:
        explosion_time += 1
        if explosion_time > 150:
            sprite_end_game_astronaut.x += 5

pyglet.clock.schedule_interval(update, 1/300.0)
pyglet.clock.schedule(game_loop)
pyglet.app.run()
