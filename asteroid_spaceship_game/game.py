TITLE = "Game"
WIDTH = 600
HEIGHT = 600
BG_COLOUR = (255, 255, 255)

import pgzero, pgzrun
import random

screen: pgzero.screen.Screen

x = 300
y = 300


class Ball:
    ANGLE = random.uniform(0.1, 5.0)
    VELOCITY = 1
    RADIUS = 30
    COLOUR = (0, 0, 0)

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.velocity = self.VELOCITY
        self.angle = self.ANGLE

    @property
    def x(self):
        return int(self._x)

    @property
    def y(self):
        return int(self._y)

    def move(self):
        if self._x > WIDTH - self.RADIUS or self._x < self.RADIUS:
            self.velocity = -self.velocity
            self.angle = -self.angle
        if self.y > HEIGHT - self.RADIUS or self.y < self.RADIUS:
            self.angle = -self.angle
        self._x += self.velocity
        self._y += self.velocity * self.angle


ball = Ball(x, y)


def update():
    ball.move()


def draw():
    screen.fill(BG_COLOUR)
    screen.draw.filled_circle((ball.x, ball.y), ball.RADIUS, ball.COLOUR)


pgzrun.go()
