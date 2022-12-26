from settings import *
from random import randint

class Ptero:
    def __init__(self, game):
        self.game = game
        self.imageCount = 0
        self.image = PTERO_IMAGES[self.imageCount]
        self.x = PTERO_INITIAL
        self.y = randint(50, 250)
        self.fly = False

    def move(self):
        self.x -= self.game.gameVelocity
        self.imageCount += 0.15

        if self.imageCount >= 2:
            self.imageCount = 0
        self.image = PTERO_IMAGES[int(self.imageCount)]

        if self.x + self.image.get_width() < 0:
            self.fly = False
            self.x = randint(2000, 5000)
            self.y = randint(50, 250)

    def collide(self):
        dinoMask = self.game.dino.getMask()
        pteroMask = pygame.mask.from_surface(self.image)

        distance = (self.x - self.game.dino.x, self.y - round(self.game.dino.y))
        point = dinoMask.overlap(pteroMask, distance)

        if point:
            return True
        else:
            return False

    def update(self):
        self.game.screen.blit(self.image, (self.x, self.y))
