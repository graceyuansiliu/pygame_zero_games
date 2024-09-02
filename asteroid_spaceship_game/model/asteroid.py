# import random
# from pgzero import screen
# from pgzero.actor import Actor
#
#
# class Asteroid(Actor):
#     ANGLE = random.uniform(0.1, 5.0)
#     VELOCITY = 1
#     RADIUS = 30
#     COLOUR = (0, 0, 0)
#
#     def __init__(self, x, y, GAME_WIDTH, GAME_HEIGHT, image):
#         super().__init__(image)
#         self.x = x
#         self.y = y
#         self.velocity = self.VELOCITY
#         self.angle2 = self.ANGLE
#         self.GAME_WIDTH = GAME_WIDTH
#         self.GAME_HEIGHT = GAME_HEIGHT
#
#     def update(self):
#         self.angle += 2.5
#         if self.x > self.GAME_WIDTH - self.RADIUS or self.x < self.RADIUS:
#             self.velocity = -self.velocity
#             self.angle2 = -self.angle2
#         if self.y > self.GAME_HEIGHT - self.RADIUS or self.y < self.RADIUS:
#             self.angle2 = -self.angle2
#         self.x += self.velocity
#         self.y += self.velocity * self.angle2
#
#
# def draw():
#     screen.draw.text(f"Collisions: {State().collisions_number}", (10, 10), color="white")









import random
from pgzero.actor import Actor

GAME_WIDTH = 750
GAME_HEIGHT = 750


class Asteroid(Actor):
    def __init__(self, x, y):
        super().__init__("meteor_grey_big1.png")
        self.x = x
        self.y = y
        self.velocity = 3.5
        self.padding = 10
        self.k = random.uniform(0.1, 5.0)
        self.angle = 0

    def update(self):
        self.angle += 1
        if self.x > GAME_WIDTH - self.padding or self.x < self.padding:
            self.velocity = -self.velocity
            self.k = -self.k
        if self.y > GAME_HEIGHT - self.padding or self.y < self.padding:
            self.k = -self.k
        self.x += self.velocity
        self.y += self.velocity * self.k

