import random

import pgzero
import pgzrun

from model.asteroid import Asteroid
from model.spaceship import Spaceship, Fire


TITLE = "Asteroid Game :)"
GAME_WIDTH = 750
GAME_HEIGHT = 750
BG_COLOUR = (0, 50, 100)

screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard


class State:
    def __init__(self):
        self.collisions_number = 0

    def register_collision(self):
        self.collisions_number += 1


spaceship = Spaceship(keyboard, "ship_green_manned.png", GAME_WIDTH, GAME_HEIGHT)
asteroid = Asteroid(100, 100)
spaceship.x = GAME_WIDTH / 2
spaceship.y = GAME_HEIGHT / 2

fire = Fire(keyboard, spaceship, (0, 108))
# asteroid1 = Asteroid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), WIDTH, HEIGHT, "meteor_grey_big1.png")
# asteroid2 = Asteroid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), WIDTH, HEIGHT, "meteor_grey_big2.png")

sprites = [spaceship, asteroid, fire]
state = State()


def update():
    for sprite in sprites:
        sprite.update()
    if spaceship.colliderect(asteroid):
        state.register_collision()


def draw():
    screen.fill(BG_COLOUR)
    for sprite in sprites:
        sprite.draw()
    screen.draw.text(f"Collisions: {state.collisions_number}", (10, 10), color="white")


pgzrun.go()
