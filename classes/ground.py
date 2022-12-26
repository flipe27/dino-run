from settings import *

class Ground:
    def __init__(self, game, y):
        self.game = game
        self.image = GROUND_IMAGE
        self.width = self.image.get_width()
        self.y = y
        self.x0 = 0
        self.x1 = self.width

    def move(self):
        self.x0 -= self.game.gameVelocity
        self.x1 -= self.game.gameVelocity

        if self.x0 + self.width < 0:
            self.x0 = self.x1 + self.width
        if self.x1 + self.width < 0:
            self.x1 = self.x0 + self.width

    def update(self):
        self.game.screen.blit(self.image, (self.x0, self.y))
        self.game.screen.blit(self.image, (self.x1, self.y))
