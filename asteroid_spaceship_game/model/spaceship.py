from pgzero.actor import Actor


class Fire(Actor):
    def __init__(self, keyboard, spaceship: Actor, relative_position: tuple):
        super().__init__("laser_yellow2.png")
        self.keyboard = keyboard
        self.spaceship = spaceship
        self.relative_position = relative_position
        self.x = spaceship.x + relative_position[0]
        self.y = spaceship.y + relative_position[1]
        self.visible = False

    def update(self):
        self.x = self.spaceship.x + self.relative_position[0]
        self.y = self.spaceship.y + self.relative_position[1]
        self.angle = 0

        if self.keyboard.left:
            self.x += 70
            self.y -= 40
            self.angle = 45
            self.visible = True
        elif self.keyboard.right:
            self.x -= 70
            self.y -= 40
            self.angle = -45
            self.visible = True
        elif self.keyboard.up:
            self.visible = True
        elif self.keyboard.down:
            self.visible = False
        else:
            self.visible = False

    def draw(self):
        if self.visible:
            super().draw()


class Spaceship(Actor):
    def __init__(self, keyboard, image, WIDTH, HEIGHT):
        super().__init__(image)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.left:
            self.x -= 5
            if self.x < 0:
                self.x = 0
            self.angle = 45
        elif self.keyboard.right:
            self.x += 5
            if self.x > self.WIDTH:
                self.x = self.WIDTH
            self.angle = -45
        elif self.keyboard.up:
            self.y -= 5
            if self.y < 0:
                self.y = 0
            self.angle = 0
        elif self.keyboard.down:
            self.y += 5
            if self.y > self.HEIGHT:
                self.y = self.HEIGHT
            self.angle = 0
        else:
            self.angle = 0
