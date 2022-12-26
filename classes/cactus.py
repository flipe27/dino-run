from settings import *
from random import randint

class Cactus:
    def __init__(self, game, index):
        self.game = game
        self.image = CACTUS_IMAGES[randint(0, 2)]
        self.index = index
        self.x = SCREEN_WIDTH + 200 if self.index == 0 else SCREEN_WIDTH + 200 + randint(400, 1000)
        self.y = GROUND_Y - self.image.get_height() + 50

    def move(self):
        self.x -= self.game.gameVelocity

    def collide(self):
        dinoMask = self.game.dino.getMask()
        cactusMask = pygame.mask.from_surface(self.image)

        distance = (self.x - self.game.dino.x, self.y - round(self.game.dino.y))
        point = dinoMask.overlap(cactusMask, distance)

        if point:
            return True
        else:
            return False

    def update(self):
        self.game.screen.blit(self.image, (self.x, self.y))
