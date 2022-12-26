from settings import *
from random import randint

class Cloud:
    def __init__(self, game):
        self.game = game
        self.image = CLOUD_IMAGE
        self.velocity = VELOCITY
        self.x0 = SCREEN_WIDTH
        self.x1 = SCREEN_WIDTH + SCREEN_WIDTH / 2
        self.y0 = randint(50, 250)
        self.y1 = randint(50, 250)

    def move(self):
        self.x0 -= self.velocity
        self.x1 -= self.velocity

        if self.x0 + self.image.get_width() < 0:
            self.x0 = SCREEN_WIDTH
            self.y0 = randint(50, 250)
        if self.x1 + self.image.get_width() < 0:
            self.x1 = SCREEN_WIDTH
            self.y1 = randint(50, 250)

    def update(self):
        self.game.screen.blit(self.image, (self.x0, self.y0))
        self.game.screen.blit(self.image, (self.x1, self.y1))
