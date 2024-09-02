import pgzero
import pgzrun

from model.spaceship import Spaceship, Fire

TITLE = "Game"
GAME_WIDTH = 750
GAME_HEIGHT = 750
BG_COLOUR = (0, 50, 100)

screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard


spaceship = Spaceship(keyboard, "ship_green_manned.png", WIDTH, HEIGHT)
spaceship.x = WIDTH / 2
spaceship.y = HEIGHT / 2

fire = Fire(keyboard, spaceship, (0, 108))


def update():
    fire.update()
    spaceship.update()


def draw():
    screen.fill(BG_COLOUR)
    fire.draw()
    spaceship.draw()


pgzrun.go()
